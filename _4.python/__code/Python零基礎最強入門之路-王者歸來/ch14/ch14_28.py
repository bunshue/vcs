# ch14_28.py
fn = 'out14_28.txt'
x = 100

with open(fn, 'w') as file_Obj:
    file_Obj.write(str(x))      # 使用str(x)輸出

