# ch14_21.py

fn = 'ch14_20.txt'          # 設定欲開啟的檔案
with open(fn) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
    obj_list = file_Obj.readlines()  # 一次讀取全部txt,內部是每次讀一行

for line in obj_list:
    print(line.rstrip())    # 列印串列






    
