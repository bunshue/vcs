# encoding:UTF-8
import requests
import json

url = "https://www.oxxostudio.tw/json/pageList.json"
r = requests.get(url)
j = json.loads(r.text)  # 轉換成 json 格式
print(j)
