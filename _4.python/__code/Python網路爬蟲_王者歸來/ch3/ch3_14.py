# ch3_14.py
import requests

url = 'http://www.deepmind.com.tw'                     # 網址
try:
    htmlfile = requests.get(url)
    print("下載成功")
except Exception as err:                                # err是系統自訂的錯誤訊息
    print("網頁下載失敗: %s" % err)
# 儲存網頁內容
fn = 'out3_14.txt'
with open(fn, 'wb') as file_Obj:                        # 以二進位儲存
    for diskStorage in htmlfile.iter_content(40960):    # Response物件處理
        size = file_Obj.write(diskStorage)              # Response物件寫入
        print(size)                                     # 列出每次寫入大小
    print("以 %s 儲存網頁HTML檔案成功" % fn)

