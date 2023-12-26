# ch23_11.py
import requests

url = 'https://opendata.epa.gov.tw/data/contents'       # 網址
try:
    htmlfile = requests.get(url)
    print("下載成功")
except Exception as err:                                # err是系統自訂的錯誤訊息
    print(f"網頁下載失敗: {err}")
# 儲存網頁內容
fn = 'out23_11.txt'
with open(fn, 'wb') as file_Obj:                        # 以二進位儲存
    for diskStorage in htmlfile.iter_content(10240):    # Response物件處理
        size = file_Obj.write(diskStorage)              # Response物件寫入
        print(size)                                     # 列出每次寫入大小
    print(f"以 {fn} 儲存網頁HTML檔案成功")

