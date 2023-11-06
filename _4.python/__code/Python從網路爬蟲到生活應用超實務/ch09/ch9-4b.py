import requests 
from bs4 import BeautifulSoup

url = "https://www.msn.com/zh-tw/weather/today/台北,台灣/we-city?iso=TW"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
span = soup.find('span', class_="current")
temp = span.text
summary = span.get("aria-label")

def telegram_bot_sendText(msg):
    token = "<API權杖>"
    chat_id = "<聊天室識別碼>"
    url = "https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}"
    r = requests.post(url.format(token,chat_id,msg))  
    return r.json()

telegram_bot_sendText(temp +"/" + summary)


