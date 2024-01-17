# ch14_36.py

fn = 'data14_35.txt'                             # 欲開啟的檔案
with open(fn, encoding='utf-8-sig') as file_Obj: # utf-8-sig
    obj_list = file_Obj.readlines()              # 每次讀一列

print(obj_list)                                  # 列印串列






    
