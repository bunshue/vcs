from twilio.rest import Client

sid = '您的 ACCOUNT SID'
token = '您的 AUTH　TOKEN'
us_phone = '您的美國手機號碼'
tw_phone = '+您的台灣手機號碼'


def send_sms(text, sid, token, us_phone, tw_phone):
    client = Client(sid, token)    # 建立 Client 物件
    sms = client.messages.create(from_=us_phone,
                                 to=tw_phone,
                                 body=text)
    print('簡訊發送時間: ', sms.date_created)


#-----↓↓發送簡訊↓↓-----#
send_sms('注意！！家中有人闖入！！', sid, token, us_phone, tw_phone)    # 送出簡訊
