# encoding:UTF-8

import csv
import requests
import json

url = "https://www.oxxostudio.tw/json/pageList.json"
r = requests.get(url)
j = json.loads(r.text)  # 轉成 json 格式

# 轉換成文字寫入，因為中文會變成編碼，所以後方要加上 ensure_ascii=False
# 此處不使用，因為發現出來變成純文字格式，非 json
jj = json.dumps(j[0], ensure_ascii=False)

with open('demo/a15.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for i in j:
        writer.writerow([i['tag'], i['title'], i['site'], i['date']])
        # writer.writerows([[0, 1, 3], [1, 2, 3], [2, 3, 4]])
    print('寫入完成！')
