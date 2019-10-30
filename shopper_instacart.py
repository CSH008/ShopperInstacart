import json
import datetime
import uuid
from decimal import Decimal
from re import sub
from time import sleep

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

Token_url = 'https://shopper-api.instacart.com/oauth/token.json'
RegisteringDevice_url = 'https://shopper-api.instacart.com/shopper_devices.json'
Location_url = 'https://locations-api.instacart.com/locations.json'
Batches_url = 'https://shopper-api.instacart.com/driver/virtual_batches'

settings = json.load(open("settings.json"))
header_batches = json.load(open("header_batches.json"))


def login():
    expires = 0
    access_token = 'Basic QmFzaWMgTW1Nek5ETXdOR1F4WldFNFlUaGxOVFkyTWpabE1HRmpPRGt6T1dWaU5EZzJZekE0WVRsbE5EQmtNR0V4TVROaE9UVm1OelpsWXpFNU5qQTVOMkUwTnpwak0yVXhaREkzWVRVMk9ESmhOakUwWTJVNE5qQm1Zak0yT0ROallqbGhObU00WkRkbVpUQmxOVEU1Wm1NeFpHSmxNall5TW1GbFkyVXlZMkUyTmpVNA=='
    # 1. Auth login to get Token
    data_for_token = [
        ('client_id', settings['CLIENT_ID']),
        ('client_secret', settings['CLIENT_SECRET']),
        ('grant_type', 'password'),
        ('kochava_device_id', settings['KOCHAVA_DEVICE_ID']),
        ('password', settings['PASSWORD']),
        ('scope', 'driver'),
        ('username', settings['PHONE'])
    ]
    print("1. Post " + Token_url)
    response = requests.post(Token_url, data=data_for_token)
    if response.status_code == 200:
        print('Token Success!')
        print(response.text)
        response_token_json = json.loads(response.text)
        if 'access_token' in response_token_json:
            access_token = "Bearer " + response_token_json['access_token']
        if 'expires_in' in response_token_json:
            expires = response_token_json['expires_in']
    else:
        print("%d: %s" % (response.status_code, response.reason))

    print(access_token)
    header_batches['Authorization'] = access_token
    header_batches['X-Request-ID'] = str(uuid.uuid4())
    # 2. Registering Device
    data_for_register_device = [
        ('device_token', settings['DEVICE_TOKEN']),
        ('device_type', 'android')
    ]
    print("2. Post "+RegisteringDevice_url)
    response = requests.post(RegisteringDevice_url, headers=header_batches, data=data_for_register_device)
    if response.status_code == 200:
        print('Register Device Success!')
        print(response.text)
    else:
        print("%d: %s" % (response.status_code, response.reason))

    # 3. Getting Location info

    now_date = datetime.datetime.now()
    sixteen_hours_from_now = now_date + datetime.timedelta(hours=16)
    data_for_location = [
        ('accuracy', 3.9),
        ('direction', 0.0),
        ('is_considered_mock', False),
        ('is_mock', False),
        ('latitude', settings['LOCATION_LATITUDE']),
        ('longitude', settings['LOCATION_LONGITUDE']),
        ('measured_at', str(now_date)),
        ('speed', 0.0),
        ('track_location_response', True),
        ('true_measured_at', str(sixteen_hours_from_now))
    ]

    print("3 Post "+Location_url)
    response = requests.post(Location_url, headers=header_batches, data=data_for_location)
    if response.status_code == 200:
        print('Location Success!')
        print(response.text)
        # response_json = json.loads(response.text)
    else:
        print("%d: %s" % (response.status_code, response.reason))
    return expires


def accept_batch(batch_uuid):
    print("5 Post " + Batches_url+"/"+batch_uuid+"/accept?batch_id_only=true")
    response_accept = requests.post(Batches_url+"/"+batch_uuid+"/accept?batch_id_only=true", headers=header_batches)
    if response_accept.status_code == 200:
        print('Batches Accept Success!')
        print(response_accept.text)
        batches_accept_file = open('batches.txt', 'a')
        batches_accept_file.write(str(datetime.datetime.now()) + " " + batch_uuid + " is accepted\n")
        batches_accept_file.close()
    else:
        print("%d: %s" % (response_accept.status_code, response_accept.reason))


expires_in = login()
header_batches['If-None-Match'] = 'W/"1d8f80f5473d4e400a8aaba4978839ca"'
i = 0
now = datetime.datetime.now()
# print
# for x in header_batches:
#    print("%s: %s" % (x, header_batches[x]))
while True:
    try:
        print("4 Get "+Batches_url)
        response_batches = requests.get(Batches_url, headers=header_batches)
        if response_batches.status_code == 200:
            print('Batches Success!')
            print(response_batches.text)
            try:
                batches_file = open('batches.txt', 'a')
                batches_file.write(str(datetime.datetime.now())+" "+response_batches.text+"\n")
                batches_file.close()
                response_json = json.loads(response_batches.text)
                virtual_batches = response_json['data']['virtual_batches']
                for batch in virtual_batches:
                    price = Decimal(sub(r'[^\d.]', '', batch['earnings']['batch_payment']))
                    if price > settings['MINIMUM_PRICE']:
                        if 'uuid' in batch:
                            accept_batch(batch['uuid'])
            except:
                print("no json")
        else:
            print("%d: %s" % (response_batches.status_code, response_batches.reason))

        later = datetime.datetime.now()
        difference_seconds = (later - now).total_seconds()
        if (settings['REQUEST_PAUSE_TIME'] != 0) and (settings['REQUEST_PAUSE_TIME'] < difference_seconds):
            break
        if (expires_in != 0) and (expires_in < difference_seconds*1000):
            login()
    except:
        login()
