import datetime
import http.client

sms_send_url = "https://api.sms.to/v1/sms/send"


def send_sms(phone, batch):

    print("send sms " + phone)
    now = datetime.datetime.now()
    my_date = datetime.datetime.strptime(str(now.hour) + ":" + str(now.minute), "%H:%M")
    message = "You have accepted a new batch, at " + my_date.strftime("%I:%M %p") + " located in " + \
              batch['warehouse']['name'] + " of " + batch['suggested_warehouse_location']['name'] + " paid for " + batch['earnings']['batch_payment']
    conn = http.client.HTTPSConnection("api.sms.to")
    payload = "{\"body\": \"" + message + "\",\"to\": \"" + phone + "\",\"sender_id\": \"SMS.to\",\"callback_url\": \"https://your-website.com/handle-notification\"}"
    print(payload)

    headers = {
        'Authorization': "Bearer OwQuiPLDlJxmrGUPhWrATWRhN425o3yK",
        'Content-Type': "application/json",
        'Accept': "application/json"
    }
    print("SMS Sending Post " + sms_send_url)
    conn.request("POST", "/v1/sms/send", payload, headers)

    response = conn.getresponse()
    if response.status_code == 200:
        print('Sending sms Success!')
        data = response.read()
        print(data.decode("utf-8"))
    else:
        print("%d: %s" % (response.status, response.reason))



