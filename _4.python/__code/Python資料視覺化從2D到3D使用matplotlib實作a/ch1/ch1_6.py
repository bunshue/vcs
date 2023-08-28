# ch1_6.py
import numpy as np

x1 = np.random.randint(10, 20)
print("回傳值是10(含)至20(不含)的單一隨機數")
print(x1)
print("-"*70)
print("回傳一維陣列10個元素, 值是1(含)至5(不含)的隨機數")
x2 = np.random.randint(1, 5, 10)
print(x2)
print("-"*70)
print("回傳單3*5陣列, 值是0(含)至10(不含)的隨機數")
x3 = np.random.randint(10, size=(3, 5))     
print(x3)














 
