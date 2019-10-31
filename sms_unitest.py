from send_sms import *

batch_str = '{"suggested_warehouse_location":{"id":3409,"city":"Miami","name":"Publix #529 - Shoppes at Lago Mar","state":"FL","active":true,"street":"15750 S.W. 72nd St","latitude":25.698059,"zip_code":"33193","longitude":-80.447772,"inventory_area_id":1655,"payment_cards_available":false},"warehouse":{"id":57,"name":"Publix","logo_url":"https://d2lnr5mha7bycj.cloudfront.net/warehouse/logo/57/29520839-7042-45a0-af82-54f973b4abe5.png"},"earnings":{"tip":"$18.42","distance":"7.0 miles","estimate":"$25.21","peak_boost":false,"heavy_batch":false,"batch_payment":"$6.79","peak_boost_amount":"","batch_payment_floors":{"delivery":"$7","rx_delivery":"","delivery_only":"$5","drive_and_pick":""}}}'
b = json.loads(batch_str)
send_sms("+14047236476", b)
