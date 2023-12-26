# ch23_6.py
import requests

url = 'http://mcut.edu.tw/file_not_existed' # 不存在的內容
try:
    htmlfile = requests.get(url)
    htmlfile.raise_for_status()             # 異常處理
    print("下載成功")
except Exception as err:                    # err是系統內建的錯誤訊息
    print(f"網頁下載失敗: {err}")
print("程式繼續執行 ... ")



