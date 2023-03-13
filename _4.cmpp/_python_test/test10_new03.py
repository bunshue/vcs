# Python 新進測試 03




def pick(x):
    fruits = ['Apple', 'Banana', 'Orange', 'Tomato', 'Pine Apple', 'Berry']
    return fruits[x]

alist = [1, 4, 2, 5, 0, 3, 4, 4, 2]
choices = map(pick, alist)
for choice in choices:
    print(choice)






while True:
    try:
        age = int(input("What is your age?"))
        break
    except:
        print("Please enter a number")

if age < 15:
    print("You are too young")


import os, sys
try:
    os.remove('hello.txt')
except Exception as e:
    print(e)
    e_type, e_value, e_tb = sys.exc_info()
    print("種類：{}\n訊息：{}\n資訊：{}".format(e_type, e_value, e_tb))




