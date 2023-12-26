# ex14_4.py

fn = 'ch14_20.txt'          # 設定欲開啟的檔案
with open(fn) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
    obj_list = file_Obj.readlines()  # 每次讀一行

str_Obj = ''                # 先設為空字串
for line in obj_list:       # 將各行字串存入 
    str_Obj += line.rstrip()

print(str_Obj)              # 列印檔案字串






    
