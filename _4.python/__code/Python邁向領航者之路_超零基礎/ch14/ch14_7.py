# ch14_7.py

fn = 'data14_7.txt'         # 設定欲開啟的檔案
with open(fn) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
    obj_list = file_Obj.readlines()  # 每次讀一行

print(obj_list)             # 列印串列






    
