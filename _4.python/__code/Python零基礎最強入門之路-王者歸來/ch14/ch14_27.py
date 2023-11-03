# ch14_27.py
fn = 'out14_27.txt'
x = 100

with open(fn, 'w') as file_Obj:
    file_Obj.write(x)               # 直接輸出數值x產生錯誤

