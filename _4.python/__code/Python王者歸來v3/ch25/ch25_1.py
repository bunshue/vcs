# ch25_1.py
from twilio.rest import Client

# 你從twilio.com申請的帳號
accountSid='AC6fdc3efffd15cabcdee8b361e9d4e67'
# 你從twilio.com獲得的圖騰
authToken='9a6dfab51a342a480e7cf9c1f88d3e638'

client = Client(accountSid, authToken)
message = client.messages.create (
            from_ = "+12512548607",         # 這是twilio.com給你的號碼
            to = "+886952000000",           # 這是收簡訊方的號碼
            body = "Python王者歸來" )       # 發送的訊息



