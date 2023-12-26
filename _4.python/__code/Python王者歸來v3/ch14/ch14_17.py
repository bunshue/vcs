# ch14_17.py
fn = 'data14_17.txt'         # 設定欲開啟的檔案
with open(fn, 'r', encoding='cp950') as fObj:
    print(f"指針位置 {fObj.tell()}")    
    txt1 = fObj.read(3)
    print(f"{txt1}, 指針位置 {fObj.tell()}")
    txt2 = fObj.read(3)
    print(f"{txt2}, 指針位置 {fObj.tell()}")
    txt3 = fObj.read(3)
    print(f"{txt3}, 指針位置 {fObj.tell()}")  





