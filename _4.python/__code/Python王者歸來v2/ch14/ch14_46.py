# ch14_46.py

fn = 'utf14_45.txt'                     # 設定欲開啟的檔案
file_Obj =  open(fn, encoding='utf-8')  # 用encoding='utf-8'開啟檔案
data = file_Obj.read()                  # 讀取檔案到變數data
file_Obj.close()                        # 關閉檔案物件
print(data)                             # 輸出變數data相當於輸出檔案




    
