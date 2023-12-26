# ch23_4.py
import requests

url = 'http://www.mcut.edu.tw'
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    print("取得網頁內容成功")
else:
    print("取得網頁內容失敗")


