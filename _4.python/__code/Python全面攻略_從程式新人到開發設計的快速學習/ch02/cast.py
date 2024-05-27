i1 = int(3.64)      # 浮點數轉型為整數3,再指定給變數i1
i2 = round(3.64)    # 浮點數四捨五入後轉型為整數4,再指定給變數i2
f = float(100)      # 整數轉型為浮點數100.0,再指定給變數f
print(i1, i2, f)    # 顯示 3 100.0
s = str(12.3)       # 數值轉型為字串'12.3',再指定給變數s
print(s, type(s))   # 顯示 12.3 <class 'str'>
b = bool('123')     # 非0數值資料轉型為布林資料True,再指定給變數b
print(b, type(b))   # 顯示 True <class 'bool'>