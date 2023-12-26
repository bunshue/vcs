# ch6_52.py
fruits = ['apple', 'banana', 'watermelon']
fruit = input("請輸入水果 = ")
if fruit in fruits:
    print("這個水果已經有了")
else:
    fruits.append(fruit)
    print("謝謝提醒已經加入水果清單: ", fruits)

