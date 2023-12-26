# ch14_27.py
fn = 'out14_27.txt'
x = 100

with open(fn, 'w') as file_Obj:
    file_Obj.write(str(x))      # 使用str(x)輸出

