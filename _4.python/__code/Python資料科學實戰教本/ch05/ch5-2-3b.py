import re
import requests
from bs4 import BeautifulSoup

url = "http://www.google.com.tw"
path = "logo.png"
r = requests.get(url)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
tag_img = soup.find("img")
# 取出Logo圖片的正規運算式
match = re.search(r"(/[^/#?]+)+\.(?:jpg|gif|png)", str(tag_img))
print(match.group())
url = url + str(match.group())
response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(path, 'wb') as fp:
        for chunk in response:
            fp.write(chunk)
    print("圖檔logo.png已經下載")        
else:
    print("錯誤! HTTP請求失敗...")


