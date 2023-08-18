# ch13_8.py
import numpy as np

# 建立 1 個 0-4(含) 的整數隨機數
x = np.random.randint(5)
print(x)

# 建立 3 個 0-9(含) 的整數隨機數 
x = np.random.randint(10,size=3)
print(x)
    
# 建立 3x2 個0-9(含) 的整數隨機數
x = np.random.randint(0, 10, size=(3,2))
print(x)
    





