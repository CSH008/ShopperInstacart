import datetime
import json
import time
import uuid
import requests

track_kvinit_url = "https://kvinit-prod.api.kochava.com/track/kvinit"
track_json_url = "https://control.kochava.com/track/json"
logs_logdna_url = "https://logs.logdna.com/logs/ingest"

header_batches = json.load(open("header_batches.json"))


def kochava_int():
    now_date = datetime.datetime.now()
    header = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G955F Build/JLS36C)"
    }
    data = {
        "action": "init",
        "kochava_app_id": "koshopper-android-ob4ml",
        "kochava_device_id": "KA3601572446239tf2b369de8daf4f7b9b8b6921be73ab60",
        "sdk_protocol": "12",
        "sdk_version": "AndroidTracker 3.6.0",
        "nt_id": "67e14-26-58c9a58f-5cfa-4870-93f2-50337586e338",
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
    header = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G955F Build/JLS36C)"
    }
    data = \
        [
            {
                "action": "session",
                "kochava_app_id": "koshopper-android-ob4ml",
                "kochava_device_id": "KA3601572446239tf2b369de8daf4f7b9b8b6921be73ab60",
                "sdk_protocol": "12",
                "sdk_version": "AndroidTracker 3.6.0",
                "nt_id": "67e14-26-9bca0140-7361-4c17-9f2d-70a362ba6497",
                "data": {
                    "screen_brightness": 0.4,
                    "device_orientation": "portrait",
                    "volume": 1,
                    "carrier_name": "T-Mobile",
                    "device": "SM-G955F-samsung",
                    "disp_h": 960,
                    "disp_w": 540,
                    "app_version": "Shopper 415605",
                    "app_short_string": "4.156.5-p",
                    "os_version": "Android 5.1.1",
                    "screen_dpi": 160,
                    "manufacturer": "samsung",
                    "product_name": "SM-G955F",
                    "architecture": "i686",
                    "battery_status": "charging",
                    "battery_level": 80,
                    "signal_bars": 0,
                    "locale": "en-US",
                    "timezone": "America\/Bogota",
                    "ui_mode": "Normal",
                    "notifications_enabled": True,
                    "network_conn_type": "wifi",
                    "ssid": "x8628e347a153323548",
                    "bssid": "28:E3:47:A1:53:32",
                    "network_metered": False,
                    "usertime": int(time.time()),
                    "uptime": 0,
                    "state_active": True,
                    "state": "resume"
                },
                "send_date": "2019-11-25T02:35:17.614Z"
            },
            {
                "action": "event",
                "kochava_app_id": "koshopper-android-ob4ml",
                "kochava_device_id": "KA3601572446239tf2b369de8daf4f7b9b8b6921be73ab60",
                "sdk_protocol": "12",
                "sdk_version": "AndroidTracker 3.6.0",
                "nt_id": "67e14-26-b1df433e-2568-4eab-84b0-a2892a2741e2",
                "data": {
                    "event_name": "app_launch",
                    "event_data": {

                    },
                    "screen_brightness": 0.4,
                    "device_orientation": "portrait",
                    "volume": 1,
                    "carrier_name": "T-Mobile",
                    "device": "SM-G955F-samsung",
                    "disp_h": 960,
                    "disp_w": 540,
                    "app_version": "Shopper 415605",
                    "app_short_string": "4.156.5-p",
                    "os_version": "Android 5.1.1",
                    "screen_dpi": 160,
                    "manufacturer": "samsung",
                    "product_name": "SM-G955F",
                    "architecture": "i686",
                    "battery_status": "charging",
                    "battery_level": 80,
                    "signal_bars": 0,
                    "locale": "en-US",
                    "timezone": "America\/Bogota",
                    "ui_mode": "Normal",
                    "notifications_enabled": True,
                    "network_conn_type": "wifi",
                    "ssid": "x8628e347a153323548",
                    "bssid": "28:E3:47:A1:53:32",
                    "network_metered": False,
                    "usertime": int(time.time()),
                    "uptime": 4.326,
                    "state_active": True
                },
                "send_date": str(now_date)
            }
        ]
    response = requests.post(track_json_url, headers=header, json=data)
    if response.status_code == 200:
        print('Track Json Success!')
        print(response.text)
    else:
        print("%d: %s" % (response.status_code, response.reason))
