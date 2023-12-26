# ch23_3.py
import requests

url = 'http://www.mcut.edu.tw'
htmlfile = requests.get(url)
print(f"回傳資料型態 : {type(htmlfile)}")
if htmlfile.status_code == requests.codes.ok:
    print("取得網頁內容成功")
    print("網頁內容大小 = ", len(htmlfile.text))
else:
    print("取得網頁內容失敗")





