# ch7_18_2.py
fruits = ['蘋果', '香蕉', '西瓜']
print("目前fruits串列 : ", fruits)

for fruit in fruits[:]:
    fruits.remove(fruit)
    print(f"刪除 {fruit}")
    print("目前fruits串列 : ", fruits)







