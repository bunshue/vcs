import os
import sys
import time
import random


print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_1.py

# ch10_1.py
langs = {'Python', 'C', 'Java'}
print("列印集合 = ", langs)
print("列印類別 = ", type(langs))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_2.py

# ch10_2.py
langs = {'Python', 'C', 'Java', 'Python', 'C'}
print(langs)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_3.py

# ch10_3.py
# 集合由整數所組成
integer_set = {1, 2, 3, 4, 5}
print(integer_set)
# 集合由不同資料型態所組成
mixed_set = {1, 'Python', (2, 5, 10)}
print(mixed_set)
# 集合的元素是不可變的所以程式第6行所設定的元組元素改成
# 第10行串列的寫法將會產生錯誤
# mixed_set = { 1, 'Python', [2, 5, 10]}

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_4.py

# ch10_4.py
x = {}                      # 這是建立空字典非空集合
print("列印     = ", x)
print("列印類別 = ", type(x))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_5.py

# ch10_5.py
empty_dict = {}                      # 這是建立空字典
print("列印類別 = ", type(empty_dict))
empty_set = set()                    # 這是建立空集合
print("列印類別 = ", type(empty_set))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_6.py

# ch10_6.py
x = set('DeepStone mean Deep Learning')
print(x)
print(type(x))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_7.py

# ch10_7.py
# 表達方式1
fruits = ['apple', 'orange', 'apple', 'banana', 'orange']
x = set(fruits)
print(x)
# 表達方式2
y = set(['apple', 'orange', 'apple', 'banana', 'orange'])
print(y)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_8.py

# ch10_8.py
cities = set(('Beijing', 'Tokyo', 'Beijing', 'Taipei', 'Tokyo'))
print(cities)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_9.py

# ch10_9.py
fruits1 = ['apple', 'orange', 'apple', 'banana', 'orange']
x = set(fruits1)                # 將串列轉成集合
fruits2 = list(x)               # 將集合轉成串列
print("原先串列資料fruits1 = ", fruits1)
print("新的串列資料fruits2 = ", fruits2)







print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_10.py

# ch10_10.py 
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
both = math & physics
print("同時參加數學與物理夏令營的成員 ",both)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_11.py

# ch10_11.py
A = {1, 2, 3, 4, 5}         # 定義集合A
B = {3, 4, 5, 6, 7}         # 定義集合B
# 將intersection( )應用在A集合
AB = A.intersection(B)      # A和B的交集
print("A和B的交集是 ", AB)
# 將intersection( )應用在B集合
BA = B.intersection(A)      # B和A的交集
print("B和A的交集是 ", BA)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_12.py

# ch10_12.py 
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
allmember = math | physics
print("同時參加數學與物理夏令營的成員 ",allmember)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_13.py

# ch10_13.py
A = {1, 2, 3, 4, 5}             # 定義集合A
B = {3, 4, 5, 6, 7}             # 定義集合B
# 將union( )應用在A集合
AorB = A.union(B)               # A和B的聯集
print("A和B的聯集是 ", AorB)    
# 將union( )應用在B集合
BorA = B.union(A)               # B和A的聯集
print("B和A的聯集是 ", BorA)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_14.py

# ch10_14.py 
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
math_only = math - physics
print("參加數學夏令營同時沒有參加物理夏令營的成員 ",math_only)
physics_only = physics - math
print("參加數學夏令營同時沒有參加物理夏令營的成員 ",physics_only)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_15.py

# ch10_15.py
A = {1, 2, 3, 4, 5}             # 定義集合A
B = {3, 4, 5, 6, 7}             # 定義集合B
# 將difference( )應用在A集合
A_B = A.difference(B)           # A-B的差集
print("A-B的差集是 ", A_B)    
# 將difference( )應用在B集合
B_A = B.difference(A)           # B-A的差集
print("B-A的差集是 ", B_A)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_16.py

# ch10_16.py 
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
math_sydi_physics = math ^ physics
print("沒有同時參加數學和物理夏令營的成員 ",math_sydi_physics)






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_17.py

# ch10_17.py
A = {1, 2, 3, 4, 5}                     # 定義集合A
B = {3, 4, 5, 6, 7}                     # 定義集合B
# 將symmetric_difference( )應用在A集合
A_sydi_B = A.symmetric_difference(B)    # A和B的對稱差集
print("A和B的對稱差集是 ", A_sydi_B)    
# 將symmetric_difference( )應用在B集合
B_sydi_A = B.symmetric_difference(A)    # B和A的對稱差集
print("B和A的對稱差集是 ", B_sydi_A)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_18.py

# ch10_18.py
A = {1, 2, 3, 4, 5}                     # 定義集合A
B = {3, 4, 5, 6, 7}                     # 定義集合B
C = {1, 2, 3, 4, 5}                     # 定義集合C
# 列出A與B集合是否相等                              
print("A與B集合相等", A == B)
# 列出A與C集合是否相等                             
print("A與C集合相等", A == C)
          



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_19.py

# ch10_19.py
A = {1, 2, 3, 4, 5}                     # 定義集合A
B = {3, 4, 5, 6, 7}                     # 定義集合B
C = {1, 2, 3, 4, 5}                     # 定義集合C
# 列出A與B集合是否相等                             
print("A與B集合不相等", A != B)
# 列出A與C集合是否不相等                              
print("A與C集合不相等", A != C)          



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_20.py

# ch10_20.py
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


          



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch10\ch10_21.py

# ch10_21.py
# 方法1
fruits = set("orange")
print("字元a是不屬於fruits集合?", 'a' not in fruits)
print("字元d是不屬於fruits集合?", 'd' not in fruits)
# 方法2
cars = {"Nissan", "Toyota", "Ford"}
boolean = "Ford" not in cars
print("Ford not in cars", boolean)
boolean = "Audi" not in cars
print("Audi not in cars", boolean)


          



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
