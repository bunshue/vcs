import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

        
print("------------------------------------------------------------")  # 60個

print('亂數不重複 範圍 個數')
num = random.sample(range(1, 20), 10)

print(type(num))
print(num)
print('排序')

num.sort()
print(num)

print("------------------------------------------------------------")  # 60個

print('測試不定引數的函式')

#定義函式
def funtionTest(*number):
    print('你傳入了', len(number), '個引數')
    outcome = 1
    for item in number:
        outcome *= item
    return outcome

#呼叫函式
print('呼叫函式並傳入 1 個引數 :', funtionTest(7))
print('呼叫函式並傳入 2 個引數 :', funtionTest(12, 3))
print('呼叫函式並傳入 4 個引數 :', funtionTest(3, 5, 9, 14))

print("------------------------------------------------------------")  # 60個

print('print語法')

for x in range(1, 10):
    for y in range(1, 10):
        print("{0}*{1}={2: ^2}".format(y, x, x * y), end=" ")
    print()



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
