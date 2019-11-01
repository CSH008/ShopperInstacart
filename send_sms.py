import datetime
import json

import requests

sms_auth_url = "https://auth.sms.to/oauth/token"
sms_send_url = "https://api.sms.to/sms/send"


def send_sms(phone, batch):
    header_sms = {
        # "Accept": "application/json"
    }
    print("send sms " + phone)
    now = datetime.datetime.now()
    my_date = datetime.datetime.strptime(str(now.hour) + ":" + str(now.minute), "%H:%M")
    message = "You have accepted a new batch, at " + my_date.strftime("%I:%M %p") + " located in " + \
              batch['warehouse']['name'] + " of " + batch['suggested_warehouse_location']['name'] + " paid for " + batch['earnings']['batch_payment']
    print(message)
    # data_for_auth = [
    #     ('client_id', '234'),
    #     ('secret', 'Kn5TtQMMGx0BYU3ECctXG6m7l2BKmirq9FZ8YLbi')
    # ]
    # access_token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2F1dGgtYXBpLnRlc3Qvb2F1dGgvdG9rZW4iLCJpYXQiOjE1NjY4Mzc1OTYsImV4cCI6MTU2NzQ0MjM5NiwibmJmIjoxNTY2ODM3NTk2LCJqdGkiOiI5RlhnbkRCSkgxaFh6NzB1Iiwic3ViIjo4MTkzLCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.U6NqFpbo1QQ4NP9F-xWDZJT5FG8cSN-ySkZgQsiG2kI"
    # print("SMS AUTH Post " + sms_auth_url)
    # try:
    #     response = requests.post(sms_auth_url, data=data_for_auth)
    #     if response.status_code == 200:
    #         print('SMS Token Success!')
    #         print(response.text)
    #         response_token_json = json.loads(response.text)
    #         if 'jwt' in response_token_json:
    #             access_token = "Bearer " + response_token_json['jwt']
    #     else:
    #         print("%d: %s" % (response.status_code, response.reason))
    #         return
    # except:
    #     return

    # print("sms token " + access_token)
    header_sms['Content-Type'] = 'application/json'
    header_sms['Authorization'] = 'Bearer OwQuiPLDlJxmrGUPhWrATWRhN425o3yK'
    data_for_sending_sms = [
        ('message', message),
        ('to', phone),
        ('sender_id', 'SMS.to'),
        ('callback_url', 'https://sms.to/callback/handler')
    ]
    print("SMS Sending Post " + sms_send_url)
    response = requests.post(sms_send_url, headers=header_sms, data=data_for_sending_sms)
    if response.status_code == 200:
        print('Sending sms Success!')
        print(response.text)
    else:
        print("%d: %s" % (response.status_code, response.reason))
