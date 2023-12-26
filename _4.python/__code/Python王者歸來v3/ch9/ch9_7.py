# ch9_7.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print("水果字典:", fruits)
fruit = input("請輸入要刪除的水果 : ")
if fruit in fruits:
    del fruits[fruit]
    print("新水果字典:", fruits)
else:
    print(f"{fruit} 不在水果字典內")

   
