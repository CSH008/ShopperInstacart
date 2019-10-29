import json
import datetime
import uuid

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

Token_url = 'https://shopper-api.instacart.com/oauth/token.json'
Location_url = 'https://locations-api.instacart.com/locations.json'
Batches_url = 'https://shopper-api.instacart.com/driver/virtual_batches'
#/driver/virtual_batches
# Auth login to get Token
header = {
}

data_for_token = [
    ('client_id', '2c34304d1ea8a8e56626e0ac8939eb486c08a9e40d0a113a95f76ec196097a47'),
    ('client_secret', 'c3e1d27a5682a614ce860fb3683cb9a6c8d7fe0e519fc1dbe2622aece2ca6658'),
    ('grant_type', 'password'),
    ('kochava_device_id', 'KA3601571807197t2f0e32f059644f2ba020cf82441d62a4'),
    ('password', 'Vanegonza87$'),
    ('scope', 'driver'),
    ('username', '+14047236476')
]

TOKEN = 'Basic QmFzaWMgTW1Nek5ETXdOR1F4WldFNFlUaGxOVFkyTWpabE1HRmpPRGt6T1dWaU5EZzJZekE0WVRsbE5EQmtNR0V4TVROaE9UVm1OelpsWXpFNU5qQTVOMkUwTnpwak0yVXhaREkzWVRVMk9ESmhOakUwWTJVNE5qQm1Zak0yT0ROallqbGhObU00WkRkbVpUQmxOVEU1Wm1NeFpHSmxNall5TW1GbFkyVXlZMkUyTmpVNA=='

print("post "+Token_url)
response = requests.post(Token_url, data=data_for_token)
if response.status_code == 200:
    print('Token Success!')
    print(response.text)
    response_json = json.loads(response.text)
    if 'access_token' in response_json:
        TOKEN = "Bearer "+response_json['access_token']
else:
    print("%d: %s" % (response.status_code, response.reason))
print(TOKEN)

# Getting Location info
header['Authorization'] = TOKEN
header_batches = {
    "Authorization": TOKEN,
    "Accept": "application/json",
    "Accept": "application/json;version=3",
    "x-client-identifier": "Android",
    "x-client-os": "android",
    "x-client-version": "4.150.6",
    "User-Agent": "Instacart Shopper 4.150.6 (store), (Android 7.1.2) (SM-G935F)",
    "Device-Info": "{\"device_id\":\"b1be8a49b9ac8d25\",\"brand\":\"samsung\",\"model\":\"SM-G935F\",\"api_level\":25,\"os_version\":\"7.1.2\",\"properties\":{\"google_play_services_status\":true,\"has_autofocus\":true,\"camera_res\":720}}",
    "Device-Data": "SM-G935F",
    "X-Request-ID": str(uuid.uuid4()),
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}
data_for_location = json.load(open("location.json"))
# print
# for x in header_batches:
#    print("%s: %s" % (x, header_batches[x]))

now_date = datetime.datetime.now()
data_for_token = [
    ('accuracy', data_for_location['accuracy']),
    ('direction', data_for_location['direction']),
    ('is_considered_mock', data_for_location['is_considered_mock']),
    ('is_mock', data_for_location['is_mock']),
    ('latitude', data_for_location['latitude']),
    ('longitude', data_for_location['longitude']),
    ('measured_at', now_date),
    ('speed', data_for_location['speed']),
    ('track_location_response', data_for_location['track_location_response']),
    ('true_measured_at', now_date),
]

print("post "+Location_url)
response = requests.post(Location_url, headers=header, data=data_for_location)
if response.status_code == 200:
    print('Location Success!')
    print(response.text)
    # response_json = json.loads(response.text)
else:
    print("%d: %s" % (response.status_code, response.reason))


def accept_batch(batch_uuid):
    print("accept - "+batch_uuid)
    response1 = requests.post(Batches_url+"/"+batch_uuid+"/accept?batch_id_only=true", headers=header)
    if response1.status_code == 200:
        print('Batches Accept Success!')
        print(response1.text)
    else:
        print("%d: %s" % (response.status_code, response.reason))


i = 1
while True:
    print(i)
    i += 1
    print("Get "+Batches_url)
    response = requests.get(Batches_url, headers=header_batches)
    if response.status_code == 200:
        print('Batches Success!')
        print(response.text)
        try:
            response_json = json.loads(response.text)
            # if 'uuid' in response_json:
            #     accept_batch(response_json['uuid'])
        except ValueError as e:
            print("no json")
    else:
        print("%d: %s" % (response.status_code, response.reason))
