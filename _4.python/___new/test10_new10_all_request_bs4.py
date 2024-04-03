"""
相關抽出

request

bs4

"""

import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




""" wait long
print("requests 1")
import requests

r = requests.get("https://tw.yahoo.com/")
print(r.text)

print("------------------------------------------------------------")  # 60個

print("requests 2")
import requests

base_url = "https://zipcloud.ibsnet.co.jp/api/search"

query_parameter = "?zipcode="

zipcode = "1600021"

request_url = base_url + query_parameter + zipcode

request_url

requests.get(request_url).json()


# 有這樣的 API 啊，網址是：https://zipcloud.ibsnet.co.jp/doc/api，請幫我寫出來

print("------------------------------------------------------------")  # 60個

print("requests 3")
import requests

# 郵遞區號
zipcode = "1000001"

# API 端點
api_endpoint = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"

# 進行查詢
response = requests.get(api_endpoint)

# 檢查回應狀態
if response.status_code == 200:
    # 解析回應內容
    data = response.json()

    # 驗證 API 回應狀態
    if data['status'] == 200:
        # 取出第一筆地址資訊
        address_info = data['results'][0]

        # 印出完整郵遞區域
        print(f"{address_info['address1']} {address_info['address2']} {address_info['address3']}")
    else:
        print("API 回應錯誤，訊息：", data['message'])
else:
    print("API 查詢失敗，狀態碼：", response.status_code)


"""
print("------------------------------------------------------------")  # 60個

""" fail
import requests

# 郵遞區號
zipcode = "100-0001"

# API 端點
api_endpoint = "http://your_api_endpoint"

# 你的 API 金鑰
api_key = "your_api_key"

# 設定查詢參數
params = {
    'apikey': api_key,
    'zipcode': zipcode,
}

# 進行查詢
response = requests.get(api_endpoint, params=params)

# 檢查回應狀態
if response.status_code == 200:
    # 解析回應內容
    data = response.json()

    # 印出郵遞區域
    print(data['area'])
else:
    print("API 查詢失敗，狀態碼：", response.status_code)
"""

print("------------------------------------------------------------")  # 60個

"""
print("requests 4")
import requests
api_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
response = requests.get(api_url)
response_dict = response.json()

response_dict.keys()
response_dict["total"]

get_object_url = (
    "https://collectionapi.metmuseum.org/public/collection/v1/objects/435864"
)

object_response = requests.get(get_object_url)

object_response.json()["objectURL"]

object_response.json()["title"]

object_response.json()["primaryImageSmall"]
"""

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

html_str = "<p>Hello World!</p>"
soup = BeautifulSoup(html_str, "lxml")
print(soup)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

soup = BeautifulSoup("<html> Lollipop </html>", "html.parser")

print("------------------------------------------------------------")  # 60個

import requests

from bs4 import BeautifulSoup

html_data = requests.get("http://tw.yahoo.com")

soup = BeautifulSoup(html_data.text, "html.parser")

print(soup.title)

print("------------------------------------------------------------")  # 60個

import requests

from bs4 import BeautifulSoup

game_ranking_html = requests.get(
    "https://www.kamatari.org/blog/2021/best-games-of-2021/"
)

soup = BeautifulSoup(game_ranking_html.text, "html.parser")

for game in soup.findAll("h2"):
    print(game.text)

print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup

game_ranking_html = requests.get(
    "https://www.kamatari.org/blog/2021/best-games-of-2021/"
)
soup = BeautifulSoup(game_ranking_html.text, "html.parser")
for game in soup.findAll("h2"):
    print(game.text)



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
