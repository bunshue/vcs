import sys

print('------------------------------------------------------------')	#60個

empty_dict = {}                      # 這是建立空字典
print("列印類別 = ", type(empty_dict))
empty_set = set()                    # 這是建立空集合
print("列印類別 = ", type(empty_set))

print('------------------------------------------------------------')	#60個

x = set('DeepStone mean Deep Learning')
print(x)
print(type(x))

print('------------------------------------------------------------')	#60個

fruits1 = ['apple', 'orange', 'apple', 'banana', 'orange']
x = set(fruits1)                # 將串列轉成集合
fruits2 = list(x)               # 將集合轉成串列
print("原先串列資料fruits1 = ", fruits1)
print("新的串列資料fruits2 = ", fruits2)

print('------------------------------------------------------------')	#60個

# 方法1
fruits = set("orange")
print("字元a是屬於fruits集合?", 'a' in fruits)
print("字元d是屬於fruits集合?", 'd' in fruits)
# 方法2
cars = {"Nissan", "Toyota", "Ford"}
boolean = "Ford" in cars
print("Ford in cars", boolean)
boolean = "Audi" in cars
print("Audi in cars", boolean)

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('字典範例')
cocktail = {
    'Blue Hawaiian':{'Rum','Sweet Wine','Cream','Pineapple Juice','Lemon Juice'},
    'Ginger Mojito':{'Rum','Ginger','Mint Leaves','Lime Juice','Ginger Soda'},
    'New Yorker':{'Whiskey','Red Wine','Lemon Juice','Sugar Syrup'},
    }
print(type(cocktail))

# 列出含有Lemon Juice的酒
print("含有Lemon Juice的酒 : ")
for name, formulas in cocktail.items():
    if 'Lemon Juice' in formulas:
        print(name)
# 列出含有Rum但是沒有薑的酒
print("含有Rum但是沒有薑的酒 : ")
for name, formulas in cocktail.items():
    if 'Rum' in formulas and not ('Ginger' in formulas):
        print(name)

print('------------------------------------------------------------')	#60個


