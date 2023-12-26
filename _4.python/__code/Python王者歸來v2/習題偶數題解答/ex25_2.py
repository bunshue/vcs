# ex25_2.py
from twilio.rest import Client

# 你從twilio.com申請的帳號
accountSid='AC308f91e9dc748a01538feb9d74ed993a'
# 你從twilio.com獲得的圖騰
authToken='f513161b63f71720f62118e4d33ca8ac'

client = Client(accountSid, authToken)
message = client.messages.create (
            from_ = "+15052070000",         # 這是twilio.com給你的號碼
            to = "+886952xxxxxx",           # 填上老師的號碼
            body = "感謝老師,我們學會了Python" )   # 發送的訊息



