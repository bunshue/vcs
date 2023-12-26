# ch14_10.py
fn = 'data14_10.txt'    # 設定欲開啟的檔案
fObj = open(fn, 'r', encoding='cp950')    
data = fObj.read()      # 讀取檔案到變數data
fObj.close()            # 關閉檔案物件
print(data)             # 輸出變數data相當於輸出檔案




