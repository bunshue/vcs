import requests 
 
token = "<API權杖>"
chat_id = "<聊天室識別碼>"

def telegram_bot_sendText(msg):
    url = "https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}"
    r = requests.post(url.format(token,chat_id,msg))  
    return r.json()

test = telegram_bot_sendText("大家好!")
print(test)

