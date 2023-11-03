# ch14_16.py

fn = 'ch14_15.txt'          # 設定欲開啟的檔案
with open(fn) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
    data = file_Obj.read()  # 讀取檔案到變數data
    print(data)             # 輸出變數data相當於輸出檔案




    
