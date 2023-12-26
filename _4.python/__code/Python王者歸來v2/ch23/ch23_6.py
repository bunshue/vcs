# ch23_6.py
import requests

url = 'http://www.mcut.edu.tw'
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    print("取得網頁內容成功")
    print(htmlfile.text)            # 列印網頁內容
else:
    print("取得網頁內容失敗")



