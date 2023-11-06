import requests 
from bs4 import BeautifulSoup

url = "https://fchart.github.io/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
tags = soup("a")
tag = tags[12]
print("URL網址: ", tag.get("href", None))
print("標籤內容: ", tag.text)
print("target屬性: ", tag["target"])
tags = soup("img")
tag = tags[1]
print("圖片網址: ", tag.get("src", None))
print("alt屬性: ", tag["alt"])
print("屬性: ", tag.attrs)


