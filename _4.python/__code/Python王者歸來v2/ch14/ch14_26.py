# ch14_26.py
fn = 'out14_26.txt'
x = 100

with open(fn, 'w') as file_Obj:
    file_Obj.write(x)               # 直接輸出數值x產生錯誤

