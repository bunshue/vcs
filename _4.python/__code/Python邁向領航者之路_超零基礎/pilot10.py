import sys

print('------------------------------------------------------------')	#60個

langs = {'Python', 'C', 'Java'}
print("列印類別 = ", type(langs))
print("列印集合 = ", langs)

print('------------------------------------------------------------')	#60個

langs = {'Python', 'C', 'Java', 'Python', 'C'}
print("列印集合 = ", langs)

print('------------------------------------------------------------')	#60個

# 集合由整數所組成
integer_set = {1, 2, 3, 4, 5}
print(integer_set)

# 集合由不同資料型態所組成
mixed_set = {1, 'Python', (2, 5, 10)}
print(mixed_set)

# 集合的元素是不可變的所以程式第6行所設定的元組元素改成
# 第10行串列的寫法將會產生錯誤
# mixed_set = { 1, 'Python', [2, 5, 10]}

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

math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
both = math & physics
print("同時參加數學與物理夏令營的成員 ",both)

print('------------------------------------------------------------')	#60個

math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
allmember = math | physics
print("參加數學或物理夏令營的成員 ",allmember)

print('------------------------------------------------------------')	#60個

math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
math_only = math - physics
print("參加數學夏令營同時沒有參加物理夏令營的成員 ",math_only)
physics_only = physics - math
print("參加物理夏令營同時沒有參加數學夏令營的成員 ",physics_only)

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

math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
print("列印參加數學夏令營的成員")
for name in math:
    print(name)

print('------------------------------------------------------------')	#60個

# students是學生名單集合
students = {'Peter', 'Norton', 'Kevin', 'Mary', 'John',     
            'Ford', 'Nelson', 'Damon', 'Ivan', 'Tom'
           }

Math = {'Peter', 'Kevin', 'Damon'}          # 數學夏令營參加人員
Physics = {'Nelson', 'Damon', 'Tom' }       # 物理夏令營參加人員

MandP = Math | Physics
print("有 %d 人參加數學和物理夏令營名單  : " % len(MandP), MandP )
unAttend = students - MandP
print("沒有參加任何夏令營有 %d 人名單是 : " % len(unAttend), unAttend)

print('------------------------------------------------------------')	#60個

cocktail = {
    'Blue Hawaiian':{'Rum','Sweet Wine','Cream','Pineapple Juice','Lemon Juice'},
    'Ginger Mojito':{'Rum','Ginger','Mint Leaves','Lime Juice','Ginger Soda'},
    'New Yorker':{'Whiskey','Red Wine','Lemon Juice','Sugar Syrup'},
    }
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


