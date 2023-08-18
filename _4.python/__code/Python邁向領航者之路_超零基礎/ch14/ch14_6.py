# ch14_6.py

fn = 'data14_2.txt'          # 設定欲開啟的檔案
with open(fn) as file_Obj:   # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
    for line in file_Obj:    # 逐行讀取檔案到變數line
        print(line.rstrip()) # 輸出變數line相當於輸出一行,同時刪除末端字元






    
