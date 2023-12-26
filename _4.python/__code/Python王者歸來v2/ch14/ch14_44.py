# ch14_44.py

fn = 'ansi14_44.txt'                    # 設定欲開啟的檔案
file_Obj =  open(fn, encoding='cp950')  # 用預設encoding='cp950'開啟檔案
data = file_Obj.read()                  # 讀取檔案到變數data
file_Obj.close()                        # 關閉檔案物件
print(data)                             # 輸出變數data相當於輸出檔案




    
