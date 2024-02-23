# encoding:UTF-8
import requests
import json

url = "https://www.oxxostudio.tw/json/pageList.json"
r = requests.get(url)
j = json.loads(r.text)  # 轉成 json 格式
print(j[0])

# 轉換成文字寫入，因為中文會變成編碼，所以後方要加上 ensure_ascii=False
jj = json.dumps(j[0], ensure_ascii=False)
print(jj)

with open('demo/a06.txt', 'a+') as f:
    f.write(jj)
