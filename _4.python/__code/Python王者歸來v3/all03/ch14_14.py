# ch14_14.py
fn = 'data14_10.txt'        # 設定欲開啟的檔案
with open(fn, 'r', encoding='cp950') as fObj:    
    txt1 = fObj.readline()
    print(txt1)             # 輸出txt1
    txt2 = fObj.readline()
    print(txt2)             # 輸出txt2







