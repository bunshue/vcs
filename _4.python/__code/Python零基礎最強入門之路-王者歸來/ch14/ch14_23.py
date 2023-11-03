# ch14_23.py

fn = 'ch14_20.txt'              # 設定欲開啟的檔案
with open(fn) as file_Obj:      # 傳回檔案物件file_Obj
    data = file_Obj.read()      # 讀取檔案到變數data
    new_data = data.replace('工專', '科大') # 新變數儲存
    print(new_data.rstrip())    # 輸出檔案




    
