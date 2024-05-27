s1 = '100'				# 文數字字串
s2 = '3.14' 				# 文數字字串
i1 = int(s1)				# 文數字'100'轉型為整數100,指定給i1變數
f1 = float(s2) 	# 文數字'3.14'轉型為浮點數3.14,指定給f1變數
print(i1, f1)				# 顯示 100 3.14
print(type(i1), type(f1))  # 顯示 <class 'int'> <class 'float'>
i2 = int(float(s2)) # 文數字'3.14'先轉型為浮點數3.14,再轉型為變數3
f2 = float(s1) 	 # 文數字'100'轉型為浮點數100.0,指定給f2變數
print(i2, f2)				 # 顯示 3 100.0
print(type(i2), type(f2))  # 顯示 <class 'int'> <class 'float'>
n1 = eval(s1)         # 文數字'100'轉型為整數100,指定給n1變數
n2 = eval(s2) 			 # 文數字'3.14'轉型為浮點數3.14,指定給n2變數
print(n1, n2)				 # 顯示 100 3.14
print(type(n1), type(n2)) # 顯示 <class 'int'> <class 'float'>
