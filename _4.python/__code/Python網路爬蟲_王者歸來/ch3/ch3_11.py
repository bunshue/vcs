# ch3_11.py
import requests

url = 'http://www.gzaxxc.com/file_not_existed'  # 錯誤的網址
try:
    htmlfile = requests.get(url)
    print("下載成功")
except Exception as err:                        # err是系統自訂的錯誤訊息
    print("網頁下載失敗: %s" % err)
print("程式結束")

