# ch9_6.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
key = input("請輸入鍵(key) = ")
if key in fruits:
    print(f"{key}已經在字典了")
else:
    value = input("請輸入值(value) = ")
    fruits[key] = value
    print("新的fruits字典內容 = ", fruits)


