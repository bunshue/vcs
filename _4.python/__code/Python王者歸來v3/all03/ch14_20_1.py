# ch14_20_1.py
fn = 'out14_20_1.txt'
x = 100

with open(fn, 'w') as file_Obj:
    file_Obj.write(str(x))      # 使用str(x)輸出

