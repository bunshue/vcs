# ch25_1.py
from twilio.rest import Client

# 你從twilio.com申請的帳號
accountSid='AC308f91e9dc748a59538feb9d74ed993a'
# 你從twilio.com獲得的圖騰
authToken='f513161b63f71720f64118e4d33ca8ac'

client = Client(accountSid, authToken)
message = client.messages.create (
            from_ = "+15052070000",         # 這是twilio.com給你的號碼
            to = "+886952xxxxxx",           # 這是收簡訊方的號碼
            body = "Python王者歸來" )        # 發送的訊息



