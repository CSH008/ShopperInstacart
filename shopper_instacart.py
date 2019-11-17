import json
import os
import time
import uuid
from decimal import Decimal
from re import sub
from send_sms import *


import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


Token_url = 'https://shopper-api.instacart.com/oauth/token.json'
RegisteringDevice_url = 'https://shopper-api.instacart.com/shopper_devices.json'
Batches_json_url = 'https://shopper-api.instacart.com/driver/batches.json?filters%5Bactive%5D=true'
Needs_location_url = 'https://locations-api.instacart.com/locations/needs_location.json'
Location_url = 'https://locations-api.instacart.com/locations.json'
Batches_url = 'https://shopper-api.instacart.com/driver/virtual_batches'

settings = json.load(open("settings.json"))
header_batches = json.load(open("header_batches.json"))
header = json.load(open("header.json"))
proxies = {}
if settings['USE_PRX'] == True:
    proxies = {
        'http': 'http://'+settings['USER_PRX']+':'+settings['PASSWORD_PRX']+'@'+settings['IP_PRX']+':'+settings['PORT_PRX'],
        'https': 'http://'+settings['USER_PRX']+':'+settings['PASSWORD_PRX']+'@'+settings['IP_PRX']+':'+settings['PORT_PRX']
    }
    print(requests.get("http://lumtest.com/myip.json", proxies=proxies).text)



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
    # header['Accept'] = 'application/json'
    # header['X-Request-ID'] = str(uuid.uuid4())
    response = requests.post(Token_url, headers=header, data=data_for_token, proxies=proxies)
    # response = requests.post(Token_url, headers=header, data=data_for_token)
    # response = requests.post(Token_url, headers=header, data=data_for_token)
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
    response = requests.post(RegisteringDevice_url, headers=header_batches, data=data_for_register_device, proxies=proxies)
    if response.status_code == 200:
        print('Register Device Success!')
        print(response.text)
    else:
        print("%d: %s" % (response.status_code, response.reason))

    # # "https://shopper-api.instacart.com/me.json"
    # response = requests.get("https://shopper-api.instacart.com/me.json", headers=header_batches, proxies=proxies)
    # if response.status_code == 200:
    #     print('me.json Success!')
    #     print(response.text)
    # else:
    #     print("%d: %s" % (response.status_code, response.reason))
    # # "https://shopper-api.instacart.com/we"
    # response = requests.get("https://shopper-api.instacart.com/we", headers=header_batches, proxies=proxies)
    # if response.status_code == 200:
    #     print('we Success!')
    #     print(response.text)
    # else:
    #     print("%d: %s" % (response.status_code, response.reason))
    # # "https://shopper-api.instacart.com/driver/completed_orientations.json"
    # response = requests.get("https://shopper-api.instacart.com/driver/completed_orientations.json", headers=header_batches, proxies=proxies)
    # if response.status_code == 200:
    #     print('completed_orientations Success!')
    #     print(response.text)
    # else:
    #     print("%d: %s" % (response.status_code, response.reason))
    # # "https://shopper-api.instacart.com/driver/navigation_menu.json"
    # response = requests.get("https://shopper-api.instacart.com/driver/navigation_menu.json", headers=header_batches, proxies=proxies)
    # if response.status_code == 200:
    #     print('navigation_menu Success!')
    #     print(response.text)
    # else:
    #     print("%d: %s" % (response.status_code, response.reason))
    # # "https://shopper-api.instacart.com/communications.json"
    # response = requests.get("https://shopper-api.instacart.com/communications.json", headers=header_batches, proxies=proxies)
    # if response.status_code == 200:
    #     print('communications Success!')
    #     print(response.text)
    # else:
    #     print("%d: %s" % (response.status_code, response.reason))
    # # "https://shopper-api.instacart.com/driver/dashboard.json"
    # response = requests.get("https://shopper-api.instacart.com/driver/dashboard.json", headers=header_batches, proxies=proxies)
    # if response.status_code == 200:
    #     print('dashboard Success!')
    #     print(response.text)
    # else:
    #     print("%d: %s" % (response.status_code, response.reason))

    header_batches['If-None-Match'] = 'W/"e8053e2e8d58ca76d5961370db3a879d"'
    response = requests.get(Batches_json_url, headers=header_batches, proxies=proxies)
    if response.status_code == 200:
        print('Batches json Success!')
        print(response.text)
    else:
        print("%d: %s" % (response.status_code, response.reason))

    header_batches['If-None-Match'] = 'W/"89379b3a31c4bf6089f457389eda8b06"'
    response = requests.get(Needs_location_url, headers=header_batches, proxies=proxies)
    if response.status_code == 200:
        print('Needs location Success!')
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
    response = requests.post(Location_url, headers=header_batches, data=data_for_location, proxies=proxies)
    if response.status_code == 200:
        print('Location Success!')
        print(response.text)
        # response_json = json.loads(response.text)
    else:
        print("%d: %s" % (response.status_code, response.reason))
    return expires


def location():
    header_batches['If-None-Match'] = 'W/"89379b3a31c4bf6089f457389eda8b06"'
    response = requests.get(Needs_location_url, headers=header_batches, proxies=proxies)
    if response.status_code == 200:
        print('Needs location Success!')
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

    print("3 Post " + Location_url)
    response = requests.post(Location_url, headers=header_batches, data=data_for_location, proxies=proxies)
    if response.status_code == 200:
        print('Location Success!')
        print(response.text)
        # response_json = json.loads(response.text)
    else:
        print("%d: %s" % (response.status_code, response.reason))


def accept_batch(batch_uuid, batch_accept):
    print("5 Post " + Batches_url+"/"+batch_uuid+"/accept?batch_id_only=true")
    response_accept = requests.post(Batches_url+"/"+batch_uuid+"/accept?batch_id_only=true", headers=header_batches, proxies=proxies)
    if response_accept.status_code == 200:
        print('Batches Accept Success!')
        print(response_accept.text)

        now1 = datetime.datetime.now()
        my_date = datetime.datetime.strptime(str(now1.hour) + ":" + str(now1.minute), "%H:%M")
        msg = now1.strftime('%d/%m/%y') + " - " + my_date.strftime("%I:%M %p") + " - Batch paid for " + batch_accept['earnings']['estimate'] + ",at " + batch_accept['warehouse']['name'] + " located in " + batch_accept['suggested_warehouse_location']['name'] + "\n"
        batches_accept_file = open('batches_accepted.txt', 'a')
        batches_accept_file.write(msg)
        batches_accept_file.close()
        try:
            send_sms(settings['PHONE'], batch_accept)
        except:
            print("send sms exception")
    else:
        print("%d: %s" % (response_accept.status_code, response_accept.reason))


expires_in = login()
expires_in = expires_in - 2000

i = 0
flag = True
now = datetime.datetime.now()
# print
# for x in header_batches:
#    print("%s: %s" % (x, header_batches[x]))
while True:
    try:
        settings = json.load(open("./settings.json"))
        # print("4 Get " + Batches_url + " " + str(datetime.datetime.now()))
        print("4 Get " + Batches_url)
        header_batches['If-None-Match'] = 'W/"1d8f80f5473d4e400a8aaba4978839ca"'
        response_batches = requests.get(Batches_url, headers=header_batches, proxies=proxies)
        print(response_batches.elapsed.total_seconds())

        if response_batches.status_code == 200:
            try:
                response_json = json.loads(response_batches.text)
                virtual_batches = response_json['data']['virtual_batches']
                if len(virtual_batches) > 0:
                    print('Batches Success!')
                    print(response_batches.text)
                    # batches_file = open('batches.txt', 'a')
                    # batches_file.write(str(datetime.datetime.now()) + " " + response_batches.text + "\n")
                    # batches_file.close()
                    for batch in virtual_batches:
                        batch_type = batch['batch_type']
                        zone_id = batch['zone_id']
                        if (settings['DELIVERY_ONLY'] is False) or ((settings['DELIVERY_ONLY'] is True) and (batch_type == 'delivery_only')):
                            if settings['ZONE'] == zone_id:
                                price = Decimal(sub(r'[^\d.]', '', batch['earnings']['estimate']))
                                if price > settings['MINIMUM_PRICE']:
                                    if 'uuid' in batch:
                                        accept_batch(batch['uuid'], batch)
                else:
                    # login()
                    continue
            except:
                print("no json")
        else:
            print("%d: %s" % (response_batches.status_code, response_batches.reason))
            # if someone login by apk, close script
            if response_batches.status_code == 401:
                if settings['AUTO_LOGIN'] == True:
                    login()
                    continue
                else:
                    break

        later = datetime.datetime.now()
        difference_seconds = (later - now).total_seconds()
        if settings['REQUEST_STOP'] == True:
             break
        # if token is expired, then relogin
        if (expires_in != 0) and (expires_in < difference_seconds*1000):
            login()
        time.sleep(settings['REQUEST_PAUSE_TIME'])

        if difference_seconds > 3000:
            login()
    except:
        login()
