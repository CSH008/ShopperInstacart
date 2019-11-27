import datetime
import json
import time
import uuid
import requests

track_kvinit_url = "https://kvinit-prod.api.kochava.com/track/kvinit"
track_json_url = "https://control.kochava.com/track/json"
logs_logdna_url = "https://logs.logdna.com/logs/ingest"

settings = json.load(open("settings.json"))
header_batches = json.load(open("header_batches.json"))


def kochava_init():
    now_date = datetime.datetime.now()
    header = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G955F Build/JLS36C)"
    }
    data = {
        "action": "init",
        "kochava_app_id": "koshopper-android-ob4ml",
        "kochava_device_id": settings['KOCHAVA_DEVICE_ID'],
        "sdk_protocol": "12",
        "sdk_version": "AndroidTracker 3.6.0",
        "nt_id": settings['NT_ID'],
        "data": {
            "platform": "android",
            "package": "com.instacart.shopper",
            "locale": "en-US",
            "timezone": "America\/Bogota",
            "usertime": int(time.time()),
            "uptime": 0.657
        },
        "sdk_build_date": "2019-02-15T23:38:06Z",
        "send_date": str(now_date)
    }
    print("1. Post " + track_kvinit_url)
    response = requests.post(track_kvinit_url, headers=header, json=data)
    if response.status_code == 200:
        print('Kvinit Success!')
        print(response.text)
    else:
        print("%d: %s" % (response.status_code, response.reason))

    header_batches['Authorization'] = 'Basic QmFzaWMgTW1Nek5ETXdOR1F4WldFNFlUaGxOVFkyTWpabE1HRmpPRGt6T1dWaU5EZzJZekE0WVRsbE5EQmtNR0V4TVROaE9UVm1OelpsWXpFNU5qQTVOMkUwTnpwak0yVXhaREkzWVRVMk9ESmhOakUwWTJVNE5qQm1Zak0yT0ROallqbGhObU00WkRkbVpUQmxOVEU1Wm1NeFpHSmxNall5TW1GbFkyVXlZMkUyTmpVNA=='
    header_batches['X-Request-ID'] = str(uuid.uuid4())
    header_batches['If-None-Match'] = 'W/"f6b7885ddaff43a9385db72518e23a6d"'
    # "https://shopper-api.instacart.com/me.json"
    print("2. Get https://shopper-api.instacart.com/me.json")
    response = requests.get("https://shopper-api.instacart.com/me.json", headers=header_batches)
    if response.status_code == 200:
        print('me.json Success!')
        print(response.text)
    else:
        print("%d: %s" % (response.status_code, response.reason))

    header_batches['X-Request-ID'] = str(uuid.uuid4())
    header_batches['If-None-Match'] = 'W/"52f157b9bef05fbcd144c6760a763a54"'
    # "https://shopper-api.instacart.com/we"
    print("3. Get https://shopper-api.instacart.com/we")
    response = requests.get("https://shopper-api.instacart.com/we", headers=header_batches)
    if response.status_code == 200:
        print('we Success!')
        print(response.text)
    else:
        print("%d: %s" % (response.status_code, response.reason))

    print("4. Post " + track_json_url)
    now_date = datetime.datetime.now()
    header = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G955F Build/JLS36C)"
    }
    data = json.load(open("kv_track.json"))
    data[0]['kochava_device_id'] = settings['KOCHAVA_DEVICE_ID']
    data[0]['nt_id'] = settings['NT_ID']
    data[0]['data']['usertime'] = int(time.time())
    data[0]['send_date'] = str(now_date)
    now_date = datetime.datetime.now()
    data[1]['kochava_device_id'] = settings['KOCHAVA_DEVICE_ID']
    data[1]['nt_id'] = settings['NT_ID']
    data[1]['data']['usertime'] = int(time.time() + 4)
    data[1]['send_date'] = str(now_date)
    response = requests.post(track_json_url, headers=header, json=data)
    if response.status_code == 200:
        print('Track Json Success!')
        print(response.text)
    else:
        print("%d: %s" % (response.status_code, response.reason))

    # log_url = logs_logdna_url + "?hostname=driver-7356125&now=" + str(time.time() * 1000)
    # print("5. Post " + log_url)
    # header = {
    #     "Authorization": "Basic YzFlZWI1MjllZmNiNjQ2NDc4Zjg1NWVjZjMwNTI0NmY=",
    #     "Connection": "Keep-Alive",
    #     "Accept-Encoding": "gzip",
    #     "User-Agent": "okhttp/4.2.2"
    # }
    # data = \
    #     {
    #         "lines": [
    #             {
    #                 "app": "instashopper-android",
    #                 "env": "Production",
    #                 "timestamp": time.time() * 1000,
    #                 "level": "debug",
    #                 "meta": {
    #                     "app_version": "4.156.5",
    #                     "demo_mode": False,
    #                     "tag": "ISApplication",
    #                     "driver_id": 7356125,
    #                     "impersonate_driver_id": "null"
    #                 },
    #                 "line": "--- onCreate"
    #             },
    #             {
    #                 "app": "instashopper-android",
    #                 "env": "Production",
    #                 "timestamp": (time.time()+4) * 1000,
    #                 "level": "debug",
    #                 "meta": {
    #                     "app_version": "4.156.5",
    #                     "demo_mode": False,
    #                     "tag": "ISSplashActivity",
    #                     "driver_id": 7356125,
    #                     "impersonate_driver_id": "null"
    #                 },
    #                 "line": "--- onCreate [ savedInstanceState: null] com.instacart.instashopper.v2.auth.ISSplashActivity @ 2328bb05,task id 3,[intent: {profile = 0}]"
    #             }
    #         ]
    #     }
    #
    # response = requests.post(log_url, headers=header, json=data)
    # if response.status_code == 200:
    #     print('Logdna Success!')
    #     print(response.text)
    # else:
    #     print("%d: %s" % (response.status_code, response.reason))
