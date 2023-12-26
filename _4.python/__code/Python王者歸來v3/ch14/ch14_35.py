# ch14_35.py

fn = 'data14_35.txt'                            # 設定欲開啟的檔案
with open(fn, encoding='utf-8') as file_Obj:    # 開啟utf-8檔案
    obj_list = file_Obj.readlines()             # 每次讀一列

print(obj_list)                                 # 列印串列






    
