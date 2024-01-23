import requests

url = "https://www.shoeisha.co.jp/rss/book/index.xml"
r = requests.get(url)                   #取得URL的資料
r.encoding = r.apparent_encoding        #自動辨識字元編碼
print(r.text)