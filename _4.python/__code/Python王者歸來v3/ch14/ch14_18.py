# ch14_18.py
fn = 'data14_18.txt'            # 設定欲開啟的檔案
chunk = 100
msg = ''
with open(fn, 'r', encoding='utf-8') as fObj: 
    while True:
        txt = fObj.read(chunk)  # 一次讀取chunk數量
        if not txt:
            break
        msg += txt
print(msg)







