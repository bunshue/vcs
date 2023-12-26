# ch14_16.py
fn = 'data14_15.txt'        # 設定欲開啟的檔案
with open(fn, 'r', encoding='cp950') as fObj:    
    mylist = fObj.readlines()

for line in mylist:
    print(line)             # 列印串列





