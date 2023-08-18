# ch13_13.py
import numpy as np

fruits = ["Apple", "Orange", "Grapes", "Banana", "Mango"]
fruit1 = np.random.choice(fruits,3)
print("隨機挑選 3 種水果")
print(fruit1)

fruit2 = np.random.choice(fruits,5)
print("隨機挑選 5 種水果 -- 可以重複")
print(fruit2)
    
fruit3 = np.random.choice(fruits,5,replace=False)
print("隨機挑選 5 種水果 -- 不可以重複")
print(fruit3)




