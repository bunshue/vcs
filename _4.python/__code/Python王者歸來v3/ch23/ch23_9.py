# ch23_9.py
import requests

url = 'http://www.tenlong.com.tw'                    # 天瓏書局網址
try:
    htmlfile = requests.get(url)
    print("下載成功")
except Exception as err:                                
    print(f"網頁下載失敗: {err}")
# 儲存網頁內容
fn = 'out23_9.txt'
with open(fn, 'wb') as file_Obj:                     # 以二進位儲存
    for diskStorage in htmlfile.iter_content(10240): # Response物件處理
        size = file_Obj.write(diskStorage)           # Response物件寫入
        print(size)                                  # 列出每次寫入大小
    print(f"以 {fn} 儲存網頁HTML檔案成功")

