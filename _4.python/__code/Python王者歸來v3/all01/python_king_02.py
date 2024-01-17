# ch10_1.py
empty_dict = {}                      # 這是建立空字典
print("列印類別 = ", type(empty_dict))
empty_set = set()                    # 這是建立空集合
print("列印類別 = ", type(empty_set))




#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_10.py

# ch10_10.py 
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
print("列印參加數學夏令營的成員")
for name in math:
    print(name)







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_11.py

# ch10_11.py
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

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_12.py

# ch10_12.py
cities = { 'Taipei', 'Beijing', 'Tokyo'}
# 增加一般元素
cities.add('Chicago')
print('cities集合內容 ', cities)
# 增加已有元素並觀察執行結果
cities.add('Beijing')
print('cities集合內容 ', cities)
# 增加元組元素並觀察執行結果
tup = (1, 2, 3)
cities.add(tup)
print('cities集合內容 ', cities)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_13.py

# ch10_13.py
# 賦值
numset = {1, 2, 3}
deep_numset = numset
deep_numset.add(10)
print("賦值 - 觀察numset        ", numset)
print("賦值 - 觀察deep_numset   ", deep_numset)

# 淺拷貝shallow copy
shallow_numset = numset.copy( )
shallow_numset.add(100)
print("拷貝 - 觀察numset        ", numset)
print("拷貝 - 觀察shallow_numset", shallow_numset)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_14.py

# ch10_14.py
countries = {'Japan', 'China', 'France'}
print("刪除前的countries集合 ", countries)
country = input("請輸入國家 : ")
if country in countries:    
    countries.remove('Japan')
    print("刪除後的countries集合 ", countries)
else:
    print(f"{country} 不存在")


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_15.py

# ch10_15.py
animals = {'dog', 'cat', 'bird'}
print("刪除前的animals集合    ", animals)
# 欲刪除元素有在集合內
animals.discard('cat')        
print("刪除後的animals集合    ", animals)
# 欲刪除元素沒有在集合內 
animals.discard('pig')
print("刪除後的animals集合    ", animals)
# 列印傳回值
print("刪除資料存在的傳回值   ", animals.discard('dog'))
print("刪除資料不存在的傳回值 ", animals.discard('pig'))



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_16.py

# ch10_16.py
animals = {'dog', 'cat', 'bird'}
print("刪除前的animals集合 ", animals)
ret_element = animals.pop( )        
print("刪除後的animals集合 ", animals)
print("所刪除的元素是      ", ret_element)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_17.py

# ch10_17.py
states = {'Mississippi', 'Idaho', 'Florida'}
print("刪除前的states集合    ", states)
states.clear( )
print("刪除後的states集合    ", states)

# 測試刪除空集合
empty_set = set( )
print("刪除前的empty_set集合 ", empty_set)
states.clear( )
print("刪除後的empty_set集合 ", empty_set)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_18.py

# ch10_18.py
A = {'a', 'b', 'c'}
B = {'c', 'd', 'e'}
C = {'h', 'k', 'p'}
# 測試A和B集合
boolean = A.isdisjoint(B)       # 有共同的元素'c'
print("有共同的元素傳回值是   ", boolean)

# 測試A和C集合
boolean = A.isdisjoint(C)       # 沒有共同的元素
print("沒有共同的元素傳回值是 ", boolean)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_19.py

# ch10_19.py
A = {'a', 'b', 'c'}
B = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'k'}
C = {'k', 'm', 'n'}
# 測試A和B集合
boolean = A.issubset(B)         # 所有A的元素皆是B的元素
print("A集合是B集合的子集合傳回值是 ", boolean)

# 測試C和B集合
boolean = C.issubset(B)         # 有共同的元素k
print("C集合是B集合的子集合傳回值是 ", boolean)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_2.py

# ch10_2.py
fruits1 = ['apple', 'orange', 'apple', 'banana', 'orange']
x = set(fruits1)                # 將串列轉成集合
fruits2 = list(x)               # 將集合轉成串列
print("原先串列資料fruits1 = ", fruits1)
print("新的串列資料fruits2 = ", fruits2)







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_20.py

# ch10_20.py
A = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'k'}
B = {'a', 'b', 'c'}
C = {'k', 'm', 'n'}
# 測試A和B集合
boolean = A.issuperset(B)           # 測試
print("A集合是B集合的父集合傳回值是 ", boolean)

# 測試A和C集合
boolean = A.issuperset(C)           # 測試
print("A集合是C集合的父集合傳回值是 ", boolean)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_21.py

# ch10_21.py
cars1 = {'Audi', 'Ford', 'Toyota'}
cars2 = {'Nissan', 'Toyota'}
print("執行update( )前列出cars1和cars2內容")
print("cars1 = ", cars1)
print("cars2 = ", cars2)
cars1.update(cars2)
print("執行update( )後列出cars1和cars2內容")
print("cars1 = ", cars1)
print("cars2 = ", cars2)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_22.py

# ch10_22.py
# 創建一個集合
myset = {5, 3, 8, 1, 2}

print(f"集合元素數量   : {len(myset)}")
print(f"集合元素最大值 : {max(myset)}")
print(f"集合元素最小值 : {min(myset)}")
print(f"集合元素總和   : {sum(myset)}")

# 使用 sorted() 函數對集合進行排序
sorted_list = sorted(myset)
print(f"小到大排序 : {sorted_list}")         # 輸出: [1, 2, 3, 5, 8]
sorted_list_desc = sorted(myset, reverse=True)
print(f"大到小排序 : {sorted_list_desc}")    # 輸出: [8, 5, 3, 2, 1]



    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_23.py

# ch10_23.py
X = frozenset([1, 3, 5])
Y = frozenset([5, 7, 9])
print(X)
print(Y)
print("交集  = ", X & Y)
print("聯集  = ", X | Y)
A = X & Y
print("交集A = ", A)
A = X.intersection(Y)
print("交集A = ", A)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_24.py

# ch10_24.py
# students是學生名單集合
students = {'Peter', 'Norton', 'Kevin', 'Mary', 'John',     
            'Ford', 'Nelson', 'Damon', 'Ivan', 'Tom'
           }

Math = {'Peter', 'Kevin', 'Damon'}          # 數學夏令營參加人員
Physics = {'Nelson', 'Damon', 'Tom' }       # 物理夏令營參加人員

MorP = Math | Physics
print("有 %d 人參加數學或物理夏令營名單  : " % len(MorP), MorP )
unAttend = students - MorP
print("沒有參加任何夏令營有 %d 人名單是 : " % len(unAttend), unAttend)













print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_25.py

# ch10_25.py
A = {n for n in range(1,100,2)}
print(type(A))
print(A)













print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_26.py

# ch10_26.py
A = {n for n in range(1,100,2) if n % 11 == 0}
print(type(A))
print(A)












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_27.py

# ch10_27.py
word = 'deepmind'
alphabetCount = {alphabet:word.count(alphabet) for alphabet in set(word)}
print(alphabetCount)












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_28.py

# ch10_28.py
cocktail = {
    'Blue Hawaiian':{'Rum','Sweet Wine','Cream','Pineapple Juice','Lemon Juice'},
    'Ginger Mojito':{'Rum','Ginger','Mint Leaves','Lime Juice','Ginger Soda'},
    'New Yorker':{'Whiskey','Red Wine','Lemon Juice','Sugar Syrup'},
    'Bloody Mary':{'Vodka','Lemon Juice','Tomato Juice','Tabasco','little Sale'}
    }
# 列出含有Vodka的酒
print("含有Vodka的酒 : ")
for name, formulas in cocktail.items():
    if 'Vodka' in formulas:
        print(name)
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
# 列出含有Lemon Juice但是沒有Cream或是Tabasco的酒
print("含有Lemon Juice但是沒有Cream或是Tabasco的酒 : ")
for name, formulas in cocktail.items():
    if 'Lemon Juice' in formulas and not formulas & {'Cream', 'Tabasco'}:
        print(name)






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_29.py

# ch10_29.py
# 供應商 A 和 B 的產品列表
supplier_a_products = {"apple", "banana", "cherry", "date", "elderberry"}
supplier_b_products = {"banana", "cherry", "fig", "grape"}

# 找到共同產品
common_products = supplier_a_products.intersection(supplier_b_products)
print(f"共同產品 : {common_products}")

# 找到只由供應商 A 提供的獨特產品
unique_to_a = supplier_a_products - supplier_b_products
print(f"供應商 A 的獨特產品 : {unique_to_a}")

# 找到只由供應商 B 提供的獨特產品
unique_to_b = supplier_b_products - supplier_a_products
print(f"供應商 B 的獨特產品 : {unique_to_b}")

# 所有提供的產品
all_products = supplier_a_products.union(supplier_b_products)
print(f"所有產品 : {all_products}")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_3.py

# ch10_3.py 
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
both1 = math & physics
print("同時參加數學與物理夏令營的成員 ",both1)
both2 = math.intersection(physics)
print("同時參加數學與物理夏令營的成員 ",both2)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_30.py

# ch10_30.py
# 定義飛行路線
routes = {
    frozenset({"Los Angeles", "New York"}): {"距離": 2451, "時間": "5h 15m"},
    frozenset({"New York", "Chicago"}): {"距離": 713, "時間": "2h 5m"},
    frozenset({"Chicago", "Los Angeles"}): {"距離": 1744, "時間": "4h 5m"},
    frozenset({"New York", "San Francisco"}): {"距離": 2572, "時間": "5h 30m"}
}

def get_route_info(city1, city2):
    # 使用 frozenset 確保無論城市的順序如何，都可以正確查詢路線
    route = frozenset({city1, city2})
    if route in routes:
        info = routes[route]
        print(f"距離 : {info['距離']:5d} miles, 時間 : {info['時間']}")
    else:
        print(f"No route found between {city1} and {city2}")

# 查詢路線資訊
get_route_info("New York", "Los Angeles")
get_route_info("Los Angeles", "New York")
get_route_info("New York", "Chicago")
get_route_info("San Francisco", "New York")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_4.py

# ch10_4.py 
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
allmember1 = math | physics
print("參加數學或物理夏令營的成員 ",allmember1)
allmember2 = math.union(physics)
print("參加數學或物理夏令營的成員 ",allmember2)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_5.py

# ch10_5.py 
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
math_only1 = math - physics
print("參加數學夏令營同時沒有參加物理夏令營的成員 ",math_only1)
math_only2 = math.difference(physics)
print("參加數學夏令營同時沒有參加物理夏令營的成員 ",math_only2)
physics_only1 = physics - math
print("參加物理夏令營同時沒有參加數學夏令營的成員 ",physics_only1)
physics_only2 = physics.difference(math)
print("參加物理夏令營同時沒有參加數學夏令營的成員 ",physics_only2)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_6.py

# ch10_6.py 
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
math_sydi_physics1 = math ^ physics
print("沒有同時參加數學和物理夏令營的成員 ",math_sydi_physics1)
math_sydi_physics2 = math.symmetric_difference(physics)
print("沒有同時參加數學和物理夏令營的成員 ",math_sydi_physics2)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_7.py

# ch10_7.py
A = {1, 2, 3, 4, 5}                     # 定義集合A
B = {3, 4, 5, 6, 7}                     # 定義集合B
C = {1, 2, 3, 4, 5}                     # 定義集合C
# 列出A與B集合是否相等                              
print("A與B集合相等", A == B)
# 列出A與C集合是否相等                             
print("A與C集合相等", A == C)
          



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_8.py

# ch10_8.py
A = {1, 2, 3, 4, 5}                     # 定義集合A
B = {3, 4, 5, 6, 7}                     # 定義集合B
C = {1, 2, 3, 4, 5}                     # 定義集合C
# 列出A與B集合是否相等                             
print("A與B集合不相等", A != B)
# 列出A與C集合是否不相等                              
print("A與C集合不相等", A != C)          



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch10\ch10_9.py

# ch10_9.py
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



#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_1.py

# ch11_1.py
def greeting():
    """我的第一個Python函數設計"""
    print("Python歡迎你")
    print("祝福學習順利")
    print("謝謝")

# 以下的程式碼也可稱主程式
greeting()
greeting()
greeting()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_10.py

# ch11_10.py
def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi, ", name, " Good Morning!")
    return      # Python自動回傳 None
ret_value = greeting('Nelson')
print(f"greeting()傳回值 = {ret_value}")
print(f"{ret_value} 的 type  = {type(ret_value)}")




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_11.py

# ch11_11.py
def subtract(x1, x2):
    """ 減法設計 """
    result = x1 - x2
    return result                   # 回傳減法結果
print("本程式會執行 a - b 的運算")     
a = int(input("a = "))
b = int(input("b = "))
print("a - b = ", subtract(a, b))   # 輸出a-b字串和結果



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_12.py

# ch11_12.py
def subtract(x1, x2):
    """ 減法設計 """
    return x1 - x2                     # 回傳減法結果
def addition(x1, x2):
    """ 加法設計 """
    return x1 + x2                     # 回傳加法結果

# 使用者輸入
print("請輸入運算")
print("1:加法")
print("2:減法")
op = int(input("輸入1/2: "))
a = int(input("a = "))
b = int(input("b = "))

# 程式運算
if op == 1:
    print("a + b = ", addition(a, b))   # 輸出a-b字串和結果
elif op == 2:
    print("a - b = ", subtract(a, b))   # 輸出a-b字串和結果
else:
    print("運算方法輸入錯誤")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_13.py

# ch11_13.py
def mutifunction(x1, x2):
    """ 加, 減, 乘, 除四則運算 """
    addresult = x1 + x2
    subresult = x1 - x2
    mulresult = x1 * x2
    divresult = x1 / x2
    return addresult, subresult, mulresult, divresult

x1 = x2 = 10
add, sub, mul, div = mutifunction(x1, x2)
print("加法結果 = ", add)
print("減法結果 = ", sub)
print("乘法結果 = ", mul)
print("除法結果 = ", div)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_13_1.py

# ch11_13_1.py
def mutifunction(x1, x2):
    """ 加, 減, 乘, 除四則運算 """
    addresult = x1 + x2
    subresult = x1 - x2
    mulresult = x1 * x2
    divresult = x1 / x2
    return addresult, subresult, mulresult, divresult

x1 = x2 = 10
ans = mutifunction(x1, x2)
print("資料型態 : ", type(ans))
print("加法結果 = ", ans[0])
print("減法結果 = ", ans[1])
print("乘法結果 = ", ans[2])
print("除法結果 = ", ans[3])







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_14.py

# ch11_14.py
def guest_info(firstname, middlename, lastname, gender):
    """ 整合客戶名字資料 """
    if gender == "M":
        welcome = lastname + middlename + firstname + '先生歡迎你'
    else:
        welcome = lastname + middlename + firstname + '小姐歡迎妳'
    return welcome

info1 = guest_info('宇', '星', '洪', 'M')
info2 = guest_info('雨', '冰', '洪', 'F')
print(info1)
print(info2)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_15.py

# ch11_15.py
def guest_info(firstname, lastname, gender, middlename = ''):
    """ 整合客戶名字資料 """
    if gender == "M":
        welcome = f"{lastname}{middlename}{firstname}先生歡迎你"
    else:
        welcome = f"{lastname}{middlename}{firstname}小姐歡迎妳"
    return welcome

info1 = guest_info('濤', '劉', 'M')
info2 = guest_info('雨', '洪', 'F', '冰')
print(info1)
print(info2)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_16.py

# ch11_16.py
def build_vip(id, name):
    """ 建立VIP資訊 """
    vip_dict = {'VIP_ID':id, 'Name':name}
    return vip_dict

member = build_vip('101', 'Nelson')
print(member)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_17.py

# ch11_17.py
def build_vip(id, name, tel = ''):
    """ 建立VIP資訊 """
    vip_dict = {'VIP_ID':id, 'Name':name}
    if tel:
        vip_dict['Tel'] = tel
    return vip_dict

member1 = build_vip('101', 'Nelson')
member2 = build_vip('102', 'Henry', '0952222333')
print(member1)
print(member2)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_18.py

# ch11_18.py
def build_vip(id, name, tel = ''):
    """ 建立VIP資訊 """
    vip_dict = {'VIP_ID':id, 'Name':name}
    if tel:
        vip_dict['Tel'] = tel
    return vip_dict

while True:
    print("建立VIP資訊系統")
    idnum = input("請輸入ID: ")
    name = input("請輸入姓名: ")    
    tel = input("請輸入電話號碼: ")        # 如果直接按Enter可不建立此欄位
    member = build_vip(idnum, name, tel)   # 建立字典
    print(member, '\n')
    repeat = input("是否繼續(y/n)? 輸入非y字元可結束系統: ")
    if repeat != 'y':
        break

print("歡迎下次再使用")


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_19.py

# ch11_19.py
def product_msg(customers):
    str1 = '親愛的: '
    str2 = '本公司將在2023年12月20日夏威夷舉行產品發表會'
    str3 = '總經理:深智公司敬上'
    for customer in customers:
        msg = str1 + customer + '\n' + str2 + '\n' + str3
        print(msg, '\n')

members = ['Damon', 'Peter', 'Mary']
product_msg(members)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_19_1.py

# ch11_19_1.py
def mydata(n):
    print("副程式 id(n) = : ", id(n), "\t", n)
    n = 5
    print("副程式 id(n) = : ", id(n), "\t", n)

x = 1
print("主程式 id(x) = : ", id(x), "\t", x)
mydata(x)
print("主程式 id(x) = : ", id(x), "\t", x)









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_19_2.py

# ch11_19_2.py
def mydata(n):
    print(f"函  數 id(n) = :  {id(n)} \t {n}")
    n[0] = 5
    print(f"函  數 id(n) = :  {id(n)} \t {n}")

x = [1, 2]
print("主程式 id(x) = : ", id(x), "\t", x)
mydata(x)
print("主程式 id(x) = : ", id(x), "\t", x)









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_2.py

# ch11_2.py
print("Python歡迎你")
print("祝福學習順利")
print("謝謝")
print("Python歡迎你")
print("祝福學習順利")
print("謝謝")
print("Python歡迎你")
print("祝福學習順利")
print("謝謝")




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_20.py

# ch11_20.py
def kitchen(unserved, served):
    """ 將未服務的餐點轉為已經服務 """
    print("\n廚房處理顧客所點的餐點")
    while unserved:
        current_meal = unserved.pop( )
        # 模擬出餐點過程
        print(f"菜單: {current_meal}")
        # 將已出餐點轉入已經服務串列
        served.append(current_meal)
    print()

def show_unserved_meal(unserved):
    """ 顯示尚未服務的餐點 """
    print("=== 下列是尚未服務的餐點 ===")
    if not unserved:
        print("*** 沒有餐點 ***")
    for unserved_meal in unserved:
        print(unserved_meal)
        
def show_served_meal(served):
    """ 顯示已經服務的餐點 """
    print("=== 下列是已經服務的餐點 ===")
    if not served:
        print("*** 沒有餐點 ***")
    for served_meal in served:
        print(served_meal)

unserved = ['大麥克', '可樂', '麥克雞塊']   # 所點餐點
served = []                               # 已服務餐點
# 列出餐廳處理前的點餐內容
show_unserved_meal(unserved)              # 列出未服務餐點
show_served_meal(served)                  # 列出已服務餐點
# 餐廳服務過程
kitchen(unserved, served)                 # 餐廳處理過程
# 列出餐廳處理後的點餐內容
show_unserved_meal(unserved)              # 列出未服務餐點
show_served_meal(served)                  # 列出已服務餐點


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_21.py

# ch11_21.py
def kitchen(unserved, served):
    """ 將未服務的餐點轉為已經服務 """
    print("\n廚房處理顧客所點的餐點")
    while unserved:
        current_meal = unserved.pop( )
        # 模擬出餐點過程
        print(f"菜單: {current_meal}")
        # 將已出餐點轉入已經服務串列
        served.append(current_meal)
    print()

def show_unserved_meal(unserved):
    """ 顯示尚未服務的餐點 """
    print("=== 下列是尚未服務的餐點 ===")
    if not unserved:
        print("*** 沒有餐點 ***")
    for unserved_meal in unserved:
        print(unserved_meal)
        
def show_served_meal(served):
    """ 顯示已經服務的餐點 """
    print("=== 下列是已經服務的餐點 ===")
    if not served:
        print("*** 沒有餐點 ***")
    for served_meal in served:
        print(served_meal)

order_list = ['大麥克', '可樂', '麥克雞塊']  # 所點餐點
served_list = []                           # 已服務餐點
# 列出餐廳處理前的點餐內容
show_unserved_meal(order_list)             # 列出未服務餐點
show_served_meal(served_list)              # 列出已服務餐點
# 餐廳服務過程
kitchen(order_list, served_list)           # 餐廳處理過程
# 列出餐廳處理後的點餐內容
show_unserved_meal(order_list)             # 列出未服務餐點
show_served_meal(served_list)              # 列出已服務餐點


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_22.py

# ch11_22.py
def kitchen(unserved, served):
    """ 將未服務的餐點轉為已經服務 """
    print("\n廚房處理顧客所點的餐點")
    while unserved:
        current_meal = unserved.pop( )
        # 模擬出餐點過程
        print(f"菜單: {current_meal}")
        # 將已出餐點轉入已經服務串列
        served.append(current_meal)
    print()

def show_order_meal(unserved):
    """ 顯示所點的餐點 """
    print("=== 下列是所點的餐點 ===")
    if not unserved:
        print("*** 沒有餐點 ***")
    for unserved_meal in unserved:
        print(unserved_meal)
        
def show_served_meal(served):
    """ 顯示已經服務的餐點 """
    print("=== 下列是已經服務的餐點 ===")
    if not served:
        print("*** 沒有餐點 ***")
    for served_meal in served:
        print(served_meal)

order_list = ['大麥克', '可樂', '麥克雞塊']  # 所點餐點
served_list = []                           # 已服務餐點
# 列出餐廳處理前的點餐內容
show_order_meal(order_list)                # 列出所點的餐點
show_served_meal(served_list)              # 列出已服務餐點
# 餐廳服務過程
kitchen(order_list[:], served_list)        # 餐廳處理過程
# 列出餐廳處理後的點餐內容
show_order_meal(order_list)                # 列出所點的餐點
show_served_meal(served_list)              # 列出已服務餐點


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_23.py

# ch11_23.py
def make_icecream(*toppings):
    """ 列出製作冰淇淋的配料 """
    print("這個冰淇淋所加配料如下")
    for topping in toppings:
        print("--- ", topping)

make_icecream('草莓醬')
make_icecream('草莓醬', '葡萄乾', '巧克力碎片')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_23_1.py

# ch11_23_1.py
def make_icecream(*toppings):
    """ 列出製作冰淇淋的配料 """
    print("這個冰淇淋所加配料如下")
    for topping in toppings:
        print("--- ", topping)
    print(type(toppings))
    print(toppings)

make_icecream('草莓醬')
make_icecream('草莓醬', '葡萄乾', '巧克力碎片')





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_23_2.py

# ch11_23_2.py
def make_icecream(*toppings):
    """ 列出製作冰淇淋的配料 """
    print("這個冰淇淋所加配料如下")
    for topping in toppings:
        print("--- ", topping)

make_icecream()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_24.py

# ch11_24.py
def make_icecream(icecream_type, *toppings):
    """ 列出製作冰淇淋的配料 """
    print("這個 ", icecream_type, " 冰淇淋所加配料如下")
    for topping in toppings:
        print("--- ", topping)

make_icecream('香草', '草莓醬')
make_icecream('芒果', '草莓醬', '葡萄乾', '巧克力碎片')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_25.py

# ch11_25.py
def build_dict(name, age, **players):
    """ 建立NBA球員的字典資料 """
    info = {}           # 建立空字典
    info['Name'] = name
    info['Age'] = age
    for key, value in players.items( ):
        info[key] = value
    return info         # 回傳所建的字典

player_dict = build_dict('James', '32',
                         City = 'Cleveland',
                         State = 'Ohio')

print(player_dict)      # 列印所建字典



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_25_1.py

# ch11_25_1.py
def total(data):
    return sum(data)

x = (1,5,10)
myList = [min, max, sum, total]
for f in myList:
    print(f)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_25_10.py

# ch11_25_10.py
def factorial(n):
    """ 計算n的階乘, n 必須是正整數 """
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact    

value = 3
print(f"{value} 的階乘結果是 = {factorial(value)}")
value = 5
print(f"{value} 的階乘結果是 = {factorial(value)}")


    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_25_2.py

# ch11_25_2.py
def total(data):
    return sum(data)

x = (1,5,10)
myList = [min, max, sum, total]
for f in myList:
    print(f, f(x))



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_25_3.py

# ch11_25_3.py
def add(x, y):
    return x+y

def mul(x, y):
    return x*y

def running(func, arg1, arg2):
    return func(arg1, arg2)
    
result1 = running(add, 5, 10)       # add函數當作參數
print(result1)
result2 = running(mul, 5, 10)       # mul函數當作參數
print(result2)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_25_4.py

# ch11_25_4.py
def mysum(*args):
    return sum(args)

def run_with_multiple_args(func, *args):
    return func(*args)

print(run_with_multiple_args(mysum,1,2,3,4,5))
print(run_with_multiple_args(mysum,6,7,8,9))








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_25_5.py

# ch11_25_5.py
def dist(x1,y1,x2,y2):          # 計算2點之距離函數
    def mySqrt(z):              # 計算開根號值
        return z ** 0.5
    dx = (x1 - x2) ** 2
    dy = (y1 - y2) ** 2
    return mySqrt(dx+dy)

print(dist(0,0,1,1))







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_25_5a.py

# ch11_25_5a.py
def outer():                   
    def inner(n):
        print('inner running')
        return sum(range(n))
    return inner

f = outer()         # outer()傳回inner位址
print(f)            # 列印inner記憶體
print(f(5))         # 實際執行的是inner()

y = outer()
print(y)
print(y(10))
















print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_25_5b.py

# ch11_25_5b.py
def create_multiplier(multiplier):
    def multiplier_function(number):
        return number * multiplier

    return multiplier_function

# 建立一個將數字乘以2的函數
double_function = create_multiplier(2)

result = double_function(5)     # 返回值是 10
print(result)                   # 輸出: 10

# 建立一個將數字乘以3的函數
triple_function = create_multiplier(3)

result = triple_function(5)     # 返回值是 15
print(result)                   # 輸出: 15



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_25_5c.py

# ch11_25_5c.py
def outer():
    b = 10                  # inner所使用的變數值
    def inner(x):
        return 5 * x + b    # 引用第3列的b
    return inner

b = 2
f = outer()
print(f(b))






















print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_25_5d.py

# ch11_25_5d.py
def outer(a, b):
    ''' a 和 b 將是inner()的環境變數 '''
    def inner(x):
        return a * x + b    
    return inner

f1 = outer(1, 2)
f2 = outer(3, 4)
print(f1(1), f2(3))























print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_25_5e.py

# ch11_25_5e.py
def lazy_evaluation(expression):
    def evaluate():
        print(f'評估 : {expression}')
        return eval(expression)
    return evaluate

lazy_sum = lazy_evaluation('1 + 2 + 3 + 4')     # 這裡不會立即計算總和

result = lazy_sum()                             # 這裡將計算並返回總和
print(result)                               


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_25_5f.py

# ch11_25_5f.py
def counter(start=0):
    count = [start]
    def increment():
        count[0] += 1
        return count[0]
    return increment

count_from_5 = counter(5)
print(count_from_5())       # 輸出: 6
print(count_from_5())       # 輸出: 7



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_25_5g.py

# ch11_25_5g.py
def event_handler(event):
    def register_handler(handler_function):
        print(f"Handling {event} with {handler_function.__name__}")
        handler_function(event)
    return register_handler

def on_click(event):
    print(f"Clicked: {event}")

def on_hover(event):
    print(f"Hovered: {event}")

# 創建事件處理器
click_handler = event_handler("Click Event")
hover_handler = event_handler("Hover Event")

# 註冊和觸發事件
click_handler(on_click)
hover_handler(on_hover)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_25_6.py

# ch11_25_6.py
import time
def recur(i):
    print(i, end='\t')
    time.sleep(1)       # 休息 1 秒
    return recur(i-1)

recur(5)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_25_7.py

# ch11_25_7.py
import time
def recur(i):
    print(i, end='\t')
    time.sleep(1)           # 休息 1 秒
    if (i <= 1):            # 結束條件
        return 0
    else:
        return recur(i-1)   # 每次呼叫讓自己減 1

recur(5)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_25_8.py

# ch11_25_8.py
def recur(i):    
    if (i < 1):            # 結束條件
        return 0
    else:
        recur(i-1)         # 每次呼叫讓自己減 1
    print(i, end='\t')
    
recur(5)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_25_9.py

# ch11_25_9.py
def sum(n):    
    if (n <= 1):                # 結束條件
        return 1
    else:
        return n + sum(n-1)     
    
print(f"total(5) = {sum(5)}")


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_26.py

# ch11_26.py
def factorial(n):
    """ 計算n的階乘, n 必須是正整數 """
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))

value = 3
print(f"{value} 的階乘結果是 = {factorial(value)}")
value = 5
print(f"{value} 的階乘結果是 = {factorial(value)}")


    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_27.py

# ch11_27.py
def printmsg( ):
    """ 函數本身沒有定義變數, 只有執行列印全域變數功能 """
    print("函數列印: ", msg)    # 列印全域變數

msg = 'Global Variable'         # 設定全域變數
print("主程式列印: ", msg)      # 列印全域變數
printmsg( )                     # 呼叫函數



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_28.py

# ch11_28.py
def printmsg( ):
    """ 函數本身有定義變數, 將執行列印區域變數功能 """
    msg = 'Local Variable'      # 設定區域變數
    print("函數列印: ", msg)    # 列印區域變數

msg = 'Global Variable'         # 這是全域變數
print("主程式列印: ", msg)      # 列印全域變數
printmsg( )                     # 呼叫函數



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_29.py

# ch11_29.py
def printmsg():
    global msg
    msg = "Java"        # 更改全域變數
    print(f"函數列印  :更改後: {msg}")
msg = "Python"
print(f"主程式列印:更改前: {msg}")
printmsg()
print(f"主程式列印:更改後: {msg}")



   


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_3.py

# ch11_3.py
def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi,", name, "Good Morning!")
greeting('Nelson')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_3_1.py

# ch11_3_1.py
def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi, " + name + " Good Morning!")
greeting('Nelson')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_30.py

# ch11_30.py
def printlocal():
    lang = "Java"
    print(f"語言 : {lang}")
    print(f"區域變數 : {locals()}")
msg = "Python"
printlocal()
print(f"語言 : {msg}")
print(f"全域變數 : {globals()}")








   


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_31.py

# ch11_31.py
# 使用一般函數
def square(x):
    value = x ** 2
    return value

# 輸出平方值
print(square(10))




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_32.py

# ch11_32.py
# 定義lambda函數
square = lambda x: x ** 2

# 輸出平方值
print(square(10))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_33.py

# ch11_33.py
# 定義lambda函數
product = lambda x, y: x * y

# 輸出相乘結果
print(product(5, 10))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_33_1.py

# ch11_33_1.py
def func(b):
    return lambda x : 2 * x + b 

linear  = func(5)       # 5將傳給lambda的 b
print(linear(10))       # 10是lambda的 x










print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_33_2.py

# ch11_33_2.py
def func(b):
    return lambda x : 2 * x + b 

linear  = func(5)       # 5將傳給lambda的 b
print(linear(10))       # 10是lambda的 x

linear2 = func(3)
print(linear2(10))













print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_33_3.py

# ch11_33_3.py
def mycar(cars,func):
    for car in cars:
        print(func(car))
def wdcar(carbrand):
    return "My dream car is " + carbrand.title()
    
dreamcars = ['porsche','rolls royce','maserati']
mycar(dreamcars, wdcar)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_33_4.py

# ch11_33_4.py
def mycar(cars,func):
    for car in cars:
        print(func(car))
    
dreamcars = ['porsche','rolls royce','maserati']
mycar(dreamcars, lambda carbrand:"My dream car is " + carbrand.title())


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_34.py

# ch11_34.py
def oddfn(x):
    return x if (x % 2 == 1) else None

mylist = [5, 10, 15, 20, 25, 30]
filter_object = filter(oddfn, mylist)     # 傳回filter object

# 輸出奇數串列
print("奇數串列: ",[item for item in filter_object])





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_35.py

# ch11_35.py
def oddfn(x):
    return x if (x % 2 == 1) else None

mylist = [5, 10, 15, 20, 25, 30]
filter_object = filter(oddfn, mylist)     # 傳回filter object
oddlist = [item for item in filter_object]
# 輸出奇數串列
print("奇數串列: ",oddlist)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_36.py

# ch11_36.py
mylist = [5, 10, 15, 20, 25, 30]

oddlist = list(filter(lambda x: (x % 2 == 1), mylist))

# 輸出奇數串列
print("奇數串列: ",oddlist)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_37.py

# ch11_37.py
mylist = [5, 10, 15, 20, 25, 30]

squarelist = list(map(lambda x: x ** 2, mylist))

# 輸出串列元素的平方值
print("串列的平方值: ",squarelist)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_37_1.py

# ch11_37_1.py
from functools import reduce
def strToInt(s):
    def func(x, y):
        return 10*x+y
    def charToNum(s):
        print("s = ", type(s), s)
        mydict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        n = mydict[s]
        print("n = ", type(n), n)
        return n
    return reduce(func,map(charToNum,s))

string = '5487'
x = strToInt(string) + 10
print("x = ", x)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_37_10.py

# ch11_37_10.py
things = {'iWatch手錶':(15000, 0.1),    # 定義商品
          'Asus  筆電':(35000, 0.7),
          'iPhone手機':(38000, 0.3),
          'Acer  筆電':(40000, 0.8),          
          'Go Pro攝影':(12000, 0.1),
         }

# 商品依價值排序
th = sorted(things.items(), key=lambda item:item[1][1])   
print('所有商品依價值排序如下')
print('商品', '        商品價格 ',  ' 商品重量')
for i in range(len(th)):
    print(f"{th[i][0]:8s}{th[i][1][0]:10d}{th[i][1][1]:10.2f}")





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_37_2.py

# ch11_37_2.py
from functools import reduce
def strToInt(s):
    def func(x, y):
        return 10*x+y
    def charToNum(s):
        print("s = ", type(s), s)
        n = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
        print("n = ", type(n), n)
        return n
    return reduce(func,map(charToNum,s))

string = '5487'
x = strToInt(string) + 10
print("x = ", x)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_37_3.py

# ch11_37_3.py
from functools import reduce
def strToInt(s):
    def func(x, y):
        return 10*x+y
    def charToNum(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(func,map(charToNum,s))

string = '5487'
x = strToInt(string) + 10
print("x = ", x)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_37_4.py

# ch11_37_4.py
from functools import reduce
def strToInt(s):
    def charToNum(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(lambda x,y:10*x+y, map(charToNum,s))

string = '5487'
x = strToInt(string) + 10
print("x = ", x)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_37_5.py

# ch11_37_5.py
str_len = lambda x:len(x)
strs = ['abc', 'ab', 'abcde']
strs.sort(key = str_len)
print(strs)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_37_6.py

# ch11_37_6.py
strs = ['abc', 'ab', 'abcde']
strs.sort(key = lambda x:len(x))
print(strs)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_37_7.py

# ch11_37_7.py
sc = [['John', 80],['Tom', 90], ['Kevin', 77]]
sc.sort(key = lambda x:x[1])
print(sc)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_37_8.py

# ch11_37_8.py
sc = [['John', 80],['Tom', 90], ['Kevin', 77]]
newsc = sorted(sc, key = lambda x:x[1])
print(newsc)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_37_9.py

# ch11_37_9.py
sc = {'John':80, 'Tom':90, 'Kevin':77}
newsc1 = sorted(sc.items(), key = lambda x:x[0])  # 依照key排序
print("依照人名排序")
print(newsc1)

newsc2 = sorted(sc.items(), key = lambda x:x[1])  # 依照value排序
print("依照分數排序")
print(newsc2)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_38.py

# ch11_38.py
def fun(arg):
    pass


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_39.py

# ch11_39.py
def fun(arg):
    pass

print("列出fun的type類型   :      ", type(fun))
print("列出lambda的type類型:      ", type(lambda x:x))
print("列出內建函數abs的type類型: ", type(abs))



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_39_1.py

# ch11_39_1.py
def myRange(start=0, stop=100, step=1):
    n = start
    while n < stop:
        yield n
        n += step

print(type(myRange))
for x in myRange(0,5):
    print(x)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_39_1a.py

# ch11_39_1a.py
# 創建一個簡單的串列
my_list = [1, 3, 5]

# 建立串列的迭代器
my_iterator = iter(my_list)

# 使用 next() 函數遍歷迭代器並列印元素
print(next(my_iterator))  
print(next(my_iterator))  
print(next(my_iterator))  



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_39_1b.py

# ch11_39_1b.py
my_list = [1, 3, 5]

for item in my_list:
    print(item)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_39_1c.py

# ch11_39_1c.py
def iter_data():
    x = 10
    yield x
    x = x * x
    yield x
    x = 2 * x
    yield x

myiter = iter_data()    # 建立迭代器
print(next(myiter))
print(next(myiter))
print(next(myiter))






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_39_1d.py

# ch11_39_1d.py
def iter_data():
    x = 10
    yield x
    x = x * x
    yield x
    x = 2 * x
    yield x

myiter = iter_data()    # 建立迭代器
for data in myiter:
    print(data)






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_39_1e.py

# ch11_39_1e.py
def list_square(n):
    mylist = []
    for data in range(1, n+1):
        mylist.append(data ** 2)
    return mylist

print(list_square(5))








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_39_1f.py

# ch11_39_1f.py
def iter_square(n):
    for data in range(1, n+1):
        yield data ** 2
    
myiter = iter_square(5)     # 建立迭代器
for data in myiter:
    print(data)








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_39_1g.py

# ch11_39_1g.py
list_square = [n ** 2 for n in range(1, 6)]
print(list_square)








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_39_1h.py

# ch11_39_1h.py
list_square = (n ** 2 for n in range(1, 6))
for data in list_square:
    print(data)








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_39_1i.py

# ch11_39_1i.py
def myRange(start=0, stop=100, step=1):
    n = start
    while n < stop:
        yield n
        n += step

print(type(myRange))
for x in myRange(0,5):
    print(x)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_39_1j.py

# ch11_39_1j.py
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# 呼叫生成器函數，建立迭代器
fib = fibonacci(10)

# for 迴圈遍歷迭代器，輸出前 10 個 Fib 數
for num in fib:
    print(num, end='  ')



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_39_2.py

# ch11_39_2.py
def upper(func):                # 裝飾器
    def newFunc(args):
        oldresult = func(args)
        newresult = oldresult.upper()
        print('函數名稱 : ', func.__name__)
        print('函數參數 : ', args)
        return newresult
    return newFunc

def greeting(string):           # 問候函數
    return string

mygreeting = upper(greeting)    # 手動裝飾器
print(mygreeting('Hello! iPhone'))








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_39_3.py

# ch11_39_3.py
def upper(func):                # 裝飾器
    def newFunc(args):
        oldresult = func(args)
        newresult = oldresult.upper()
        print('函數名稱 : ', func.__name__)
        print('函數參數 : ', args)
        return newresult
    return newFunc
@upper                          # 設定裝飾器
def greeting(string):           # 問候函數
    return string

print(greeting('Hello! iPhone'))








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_39_4.py

# ch11_39_4.py
def errcheck(func):             # 裝飾器
    def newFunc(*args):
        if args[1] != 0:
            result = func(*args)
        else:
            result = "除數不可為0"
        print('函數名稱 : ', func.__name__)
        print('函數參數 : ', args)
        print('執行結果 : ', result)
        return result
    return newFunc
@errcheck                       # 設定裝飾器
def mydiv(x, y):                # 函數
    return x/y 

print(mydiv(6,2))
print(mydiv(6,0))






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_39_5.py

# ch11_39_5.py
def upper(func):                # 大寫裝飾器
    def newFunc(args):
        oldresult = func(args)
        newresult = oldresult.upper()
        return newresult
    return newFunc
def bold(func):                 # 加粗體字串裝飾器
    def wrapper(args):
        return 'bold' + func(args) + 'bold'
    return wrapper

@bold                           # 設定加粗體字串裝飾器
@upper                          # 設定大寫裝飾器
def greeting(string):           # 問候函數
    return string

print(greeting('Hello! iPhone'))








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_39_6.py

# ch11_39_6.py
def upper(func):                # 裝飾器
    def newFunc(args):
        oldresult = func(args)
        newresult = oldresult.upper()
        return newresult
    return newFunc
def bold(func):
    def wrapper(args):
        return 'bold' + func(args) + 'bold'
    return wrapper

@upper                          # 設定大寫裝飾器
@bold                           # 設定加粗體字串大寫裝飾器
def greeting(string):           # 問候函數
    return string

print(greeting('Hello! iPhone'))








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_4.py

# ch11_4.py
def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi, " + name + " Good Morning!")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_40.py

# ch11_40.py
def modifySong(songStr):            # 將歌曲的標點符號用空字元取代       
    for ch in songStr:
        if ch in ".,?":
            songStr = songStr.replace(ch,'')
    return songStr                  # 傳回取代結果

def wordCount(songCount):
    global mydict
    songList = songCount.split()    # 將歌曲字串轉成串列
    print("以下是歌曲串列")
    print(songList)
    mydict = {wd:songList.count(wd) for wd in set(songList)}

data = """Are you sleeping, are you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong."""

mydict = {}                         # 空字典未來儲存單字計數結果
print("以下是將歌曲大寫字母全部改成小寫同時將標點符號用空字元取代")
song = modifySong(data.lower())
print(song)

wordCount(song)                     # 執行歌曲單字計數
print("以下是最後執行結果")
print(mydict)                       # 列印字典









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_41.py

# ch11_41.py
def isPrime(num):
    """ 測試num是否質數 """
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

num = int(input("請輸入大於1的整數做質數測試 = "))
if isPrime(num):                   
    print(f"{num} 是質數")
else:                                   
    print(f"{num} 不是質數")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_41_1.py

# ch11_41_1.py
import math
def isPrime(num):
    """ 測試num是否質數 """
    for n in range(2, int(math.sqrt(num))+1):
        if num % n == 0:
            return False
    return True

num = int(input("請輸入大於1的整數做質數測試 = "))
if isPrime(num):                   
    print(f"{num} 是質數")
else:                                   
    print(f"{num} 不是質數")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_42.py

# ch11_42.py
def gcd(n1, n2):
    g = 1                               # 最初化最大公約數
    n = 2                               # 從2開始檢測
    while n <= n1 and n <= n2:
        if n1 % n == 0 and n2 % n == 0:
            g = n                       # 新最大公約數
        n += 1
    return g

n1, n2 = eval(input("請輸入2個整數值 : "))
print("最大公約數是 : ", gcd(n1,n2))



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_43.py

# ch11_43.py
def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a

a, b = eval(input("請輸入2個整數值 : "))
print("最大公約數是 : ", gcd(a, b))






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_44.py

# ch11_44.py
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

a, b = eval(input("請輸入2個整數值 : "))
print("最大公約數是 : ", gcd(a, b))






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_45.py

# ch11_45.py

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

a, b = eval(input("請輸入2個整數值 : "))
print("最大公約數是 : ", gcd(a, b))
print("最小公倍數是 : ", lcm(a, b))





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_46.py

# ch11_46.py
def create_multiplier(multiplier):
    def multiplier_function(number):
        return number * multiplier

    return multiplier_function

# 建立一個將數字乘以2的函數
double_function = create_multiplier(2)

# 使用返回的函數
result = double_function(5)             # 返回值是 10
print(result)                           # 輸出: 10

# 建立一個將數字乘以3的函數
triple_function = create_multiplier(3)

# 使用返回的函數
result = triple_function(5)             # 返回值是 15
print(result)                           # 輸出: 15



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_47.py

# ch11_47.py
def event_handler(event):
    def register_handler(handler_function):
        print(f"處理(Handling) {event} with {handler_function.__name__}")
        handler_function(event)
    return register_handler

def on_click(event):                # 按一下
    print(f"按一下 : {event}")

def on_hover(event):                # 懸停留
    print(f"懸停留 : {event}")

# 創建事件處理器
click_handler = event_handler("按一下事件")
hover_handler = event_handler("懸停留事件")

# 註冊和觸發事件
click_handler(on_click)
hover_handler(on_hover)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_48.py

# ch11_48.py
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()    # 獲取函數開始執行的時間
        result = func(*args, **kwargs)      # 調用原始函數
        end_time = time.perf_counter()      # 獲取函數結束執行的時間
        duration = end_time - start_time    # 計算函數執行時間
        print(f'{func.__name__} 執行需 : {duration:.7f} 秒')
        return result
    return wrapper

@timing_decorator
def slow_function(duration):
    time.sleep(duration)                    # 使函數暫停指定的秒數

# 調用裝飾器函數
slow_function(3)            # 輸出 slow_function 執行需 : 3.000xxxx 秒



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_5.py

# ch11_5.py
def subtract(x1, x2):
    """ 減法設計 """
    result = x1 - x2
    print(result)               # 輸出減法結果
print("本程式會執行 a - b 的運算")     
a = eval(input("a = "))
b = eval(input("b = "))
print("a - b = ", end="")       # 輸出a-b字串,接下來輸出不跳列
subtract(a, b)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_6.py

# ch11_6.py
def interest(interest_type, subject):
    """ 顯示興趣和主題 """
    print("我的興趣是 " + interest_type )
    print("在 " + interest_type + " 中, 最喜歡的是 " + subject)
    print()

interest('旅遊', '敦煌')
interest('程式設計', 'Python')




    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_7.py

# ch11_7.py
def interest(interest_type, subject):
    """ 顯示興趣和主題 """
    print(f"我的興趣是 {interest_type}")
    print(f"在 {interest_type} 中, 最喜歡的是 {subject}")
    print()

interest(interest_type='旅遊', subject='敦煌')  # 位置正確
interest(subject='敦煌', interest_type='旅遊')  # 位置更動




    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_8.py

# ch11_8.py
def interest(interest_type, subject = '敦煌'):
    """ 顯示興趣和主題 """
    print(f"我的興趣是 {interest_type}")
    print(f"在 {interest_type}  中, 最喜歡的是 {subject}")
    print()

interest('旅遊')                                 # 傳遞一個參數
interest(interest_type='旅遊')                   # 傳遞一個參數
interest('旅遊', '張家界')                       # 傳遞二個參數
interest(interest_type='旅遊', subject='張家界') # 傳遞二個參數
interest(subject='張家界', interest_type='旅遊') # 傳遞二個參數
interest('閱讀', '旅遊類')            # 傳遞二個參數,不同的主題




    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch11\ch11_9.py

# ch11_9.py
def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi, ", name, " Good Morning!")
    
ret_value = greeting('Nelson')
print(f"greeting()傳回值 = {ret_value}")
print(f"{ret_value} 的 type  = {type(ret_value)}")




print("------------------------------------------------------------")  # 60個




#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_1.py

# ch12_1.py
class Banks():
    ''' 定義銀行類別 '''
    bankname = 'Taipei Bank'        # 定義屬性
    def motto(self):                # 定義方法
        return "以客為尊"





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_10.py

# ch12_10.py
class Banks():
    ''' 定義銀行類別 '''

    def __init__(self, uname):              # 初始化方法
        self.__name = uname                 # 設定私有存款者名字
        self.__balance = 0                  # 設定私有開戶金額是0
        self.__bankname = "Taipei Bank"     # 設定私有銀行名稱
        self.__rate = 30                    # 預設美金與台幣換匯比例
        self.__service_charge = 0.01        # 換匯的服務費

    def save_money(self, money):            # 設計存款方法
        self.__balance += money             # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.__balance -= money             # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)

    def usa_to_taiwan(self, usa_d):         # 美金兌換台幣方法
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self,usa_d):             # 計算換匯這是私有方法
        return int(usa_d * self.__rate * (1 - self.__service_charge))

class Shilin_Banks(Banks):
    # 定義士林分行
    pass
       
hungbank = Shilin_Banks('hung')             # 定義物件hungbank
hungbank.save_money(500)
hungbank.get_balance()












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_10_1.py

# ch12_10_1.py
class Father():
    def __init__(self):
        self.__address = '台北市羅斯福路'
    def getaddr(self):
        return self.__address

class Son(Father):
    pass

hung = Father()
ivan = Son()
print('父類別 : ',hung.getaddr())
print('子類別 : ',ivan.getaddr())








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_11.py

# ch12_11.py
class Banks():
    # 定義銀行類別

    def __init__(self, uname):              # 初始化方法
        self.__name = uname                 # 設定私有存款者名字
        self.__balance = 0                  # 設定私有開戶金額是0
        self.__bankname = "Taipei Bank"     # 設定私有銀行名稱
        self.__rate = 30                    # 預設美金與台幣換匯比例
        self.__service_charge = 0.01        # 換匯的服務費

    def save_money(self, money):            # 設計存款方法
        self.__balance += money             # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.__balance -= money             # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)

    def usa_to_taiwan(self, usa_d):         # 美金兌換台幣方法
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self,usa_d):             # 計算換匯這是私有方法
        return int(usa_d * self.__rate * (1 - self.__service_charge))

    def bank_title(self):                   # 獲得銀行名稱
        return self.__bankname

class Shilin_Banks(Banks):
    # 定義士林分行
    pass

hungbank = Shilin_Banks('hung')             # 定義物件hungbank
print("我的存款銀行是: ", hungbank.bank_title())














print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_11_1.py

# ch12_11_1.py
class Person():
    def __init__(self,name):
        self.name = name
class LawerPerson(Person):
    def __init__(self,name):
        self.name = name + "律師"

hung = Person("洪錦魁")
lawer = LawerPerson("洪錦魁")
print(hung.name)
print(lawer.name)

















print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_12.py

# ch12_12.py
class Banks():
    ''' 定義銀行類別 '''

    def __init__(self, uname):              # 初始化方法
        self.__name = uname                 # 設定私有存款者名字
        self.__balance = 0                  # 設定私有開戶金額是0
        self.bankname = "Taipei Bank"       # 設定公有銀行名稱
        self.__rate = 30                    # 預設美金與台幣換匯比例
        self.__service_charge = 0.01        # 換匯的服務費

    def save_money(self, money):            # 設計存款方法
        self.__balance += money             # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.__balance -= money             # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)

    def usa_to_taiwan(self, usa_d):         # 美金兌換台幣方法
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self,usa_d):             # 計算換匯這是私有方法
        return int(usa_d * self.__rate * (1 - self.__service_charge))

    def bank_title(self):                   # 獲得銀行名稱
        return self.bankname

class Shilin_Banks(Banks):
    # 定義士林分行
    def __init__(self, uname):
        self.bankname = "Taipei Bank - Shilin Branch"  # 定義分行名稱

jamesbank = Banks('James')                      # 定義Banks類別物件
print("James's banks = ", jamesbank.bankname)   # 列印銀行名稱
hungbank = Shilin_Banks('Hung')                 # 定義Shilin_Banks類別物件
print("Hung's banks  = ", hungbank.bankname)    # 列印銀行名稱















print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_12_1.py

# ch12_12_1.py
class Person():
    def job(self):
        print("我是老師")
    
class LawerPerson(Person):
    def job(self):
        print("我是律師")

hung = Person()
ivan = LawerPerson()
hung.job()
ivan.job()



















print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_13.py

# ch12_13.py
class Banks():
    ''' 定義銀行類別 '''

    def __init__(self, uname):              # 初始化方法
        self.__name = uname                 # 設定私有存款者名字
        self.__balance = 0                  # 設定私有開戶金額是0
        self.__bankname = "Taipei Bank"     # 設定私有銀行名稱
        self.__rate = 30                    # 預設美金與台幣換匯比例
        self.__service_charge = 0.01        # 換匯的服務費

    def save_money(self, money):            # 設計存款方法
        self.__balance += money             # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.__balance -= money             # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)

    def usa_to_taiwan(self, usa_d):         # 美金兌換台幣方法
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self,usa_d):             # 計算換匯這是私有方法
        return int(usa_d * self.__rate * (1 - self.__service_charge))

    def bank_title(self):                   # 獲得銀行名稱
        return self.__bankname

class Shilin_Banks(Banks):
    # 定義士林分行
    def __init__(self, uname):
        self.bankname = "Taipei Bank - Shilin Branch"  # 定義分行名稱
    def bank_title(self):                   # 獲得銀行名稱
        return self.bankname

jamesbank = Banks('James')                  # 定義Banks類別物件
print("James's banks = ", jamesbank.bank_title())  # 列印銀行名稱
hungbank = Shilin_Banks('Hung')             # 定義Shilin_Banks類別物件
print("Hung's banks  = ", hungbank.bank_title())   # 列印銀行名稱















print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_14.py

# ch12_14.py
class Animals():
    """Animals類別, 這是基底類別 """
    def __init__(self, animal_name, animal_age ):
        self.name = animal_name # 紀錄動物名稱
        self.age = animal_age   # 紀錄動物年齡

    def run(self):              # 輸出動物 is running
        print(self.name.title(), " is running")

class Dogs(Animals):
    """Dogs類別, 這是Animal的衍生類別 """
    def __init__(self, dog_name, dog_age):
        super().__init__('My pet ' + dog_name.title(), dog_age)

mycat = Animals('lucy', 5)      # 建立Animals物件以及測試
print(mycat.name.title(), ' is ', mycat.age, " years old.")
mycat.run()

mydog = Dogs('lily', 6)         # 建立Dogs物件以及測試
print(mydog.name.title(), ' is ', mydog.age, " years old.")
mydog.run()
        
        

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_14_1.py

# ch12_14_1.py
class Animals():
    """Animals類別, 這是基底類別 """
    def __init__(self, animal_name, animal_age ):
        self.name = animal_name # 紀錄動物名稱
        self.age = animal_age   # 紀錄動物年齡

    def run(self):              # 輸出動物 is running
        print(self.name.title(), " is running")

class Dogs(Animals):
    """Dogs類別, 這是Animal的衍生類別 """
    def __init__(self, dog_name, dog_age):
        super().__init__('My pet ' + dog_name.title(), dog_age)
    def sleeping(self):
        print("My pet", "is sleeping")

mycat = Animals('lucy', 5)      # 建立Animals物件以及測試
print(mycat.name.title(), ' is ', mycat.age, " years old.")
mycat.run()

mydog = Dogs('lily', 6)         # 建立Dogs物件以及測試
print(mydog.name.title(), ' is ', mydog.age, " years old.")
mydog.run()
mydog.sleeping()


        
        

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_15.py

# ch12_15
class Grandfather():
    """ 定義祖父的資產 """
    def __init__(self):
        self.grandfathermoney = 10000
    def get_info1(self):
        print("Grandfather's information")

class Father(Grandfather):      # 父類別是Grandfather
    """ 定義父親的資產 """
    def __init__(self):
        self.fathermoney = 8000
        super().__init__()
    def get_info2(self):
        print("Father's information")

class Ivan(Father):             # 父類別是Father
    """ 定義Ivan的資產 """
    def __init__(self):
        self.ivanmoney = 3000
        super().__init__()
    def get_info3(self):
        print("Ivan's information")
    def get_money(self):        # 取得資產明細
        print("\nIvan資產: ", self.ivanmoney,
              "\n父親資產: ", self.fathermoney,
              "\n祖父資產: ", self.grandfathermoney)

ivan = Ivan()
ivan.get_info3()                # 從Ivan中獲得
ivan.get_info2()                # 流程 Ivan -> Father
ivan.get_info1()                # 流程 Ivan -> Father -> Grandtather
ivan.get_money()                # 取得資產明細


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_16.py

# ch12_16.py
class Father():
    """ 定義父親的資產 """
    def __init__(self):
        self.fathermoney = 10000
   
class Ira(Father):                                  # 父類別是Father
    """ 定義Ira的資產 """
    def __init__(self):
        self.iramoney = 8000
        super().__init__()
   
class Ivan(Father):                                 # 父類別是Father
    """ 定義Ivan的資產 """
    def __init__(self):
        self.ivanmoney = 3000
        super().__init__()   
    def get_money(self):                            # 取得資產明細
        print("Ivan資產: ", self.ivanmoney,
              "\n父親資產: ", self.fathermoney,
              "\nIra資產 : ", Ira().iramoney)       # 注意寫法

ivan = Ivan()
ivan.get_money()                                    # 取得資產明細


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_16_1.py

# ch12_16_1.py
class Person():
    def interest(self):
        print("Smiling is my interest")

hung = Person()
hung.interest()




        
        

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_17.py

# ch12_17.py
class Animals():
    """Animals類別, 這是基底類別 """
    def __init__(self, animal_name):
        self.name = animal_name         # 紀錄動物名稱
    def which(self):                    # 回傳動物名稱
        return 'My pet ' + self.name.title()
    def action(self):                   # 動物的行為
        return ' sleeping'

class Dogs(Animals):
    """Dogs類別, 這是Animal的衍生類別 """
    def __init__(self, dog_name):       # 紀錄動物名稱
        super().__init__(dog_name.title())
    def action(self):                   # 動物的行為
        return ' running in the street'

class Monkeys():
    """猴子類別, 這是其他類別 """
    def __init__(self, monkey_name):    # 紀錄動物名稱
        self.name = 'My monkey ' + monkey_name.title()
    def which(self):                    # 回傳動物名稱
        return self.name
    def action(self):                   # 動物的行為
        return ' running in the forest'
    
def doing(obj):                         # 列出動物的行為
    print(obj.which(), "is", obj.action())
    
my_cat = Animals('lucy')                # Animals物件
doing(my_cat)
my_dog = Dogs('gimi')                   # Dogs物件
doing(my_dog)
my_monkey = Monkeys('taylor')           # Monkeys物件
doing(my_monkey)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_18.py

# ch12_18.py
class Grandfather():
    """ 定義祖父類別 """
    def action1(self):
        print("Grandfather")
        
class Father(Grandfather):
    """ 定義父親類別 """
    def action2(self):      # 定義action2()
        print("Father")

class Uncle(Grandfather):
    """ 定義叔父類別 """
    def action2(self):      # 定義action2()
        print("Uncle")

class Ivan(Father, Uncle):
    """ 定義Ivan類別 """
    def action3(self):
        print("Ivan")

ivan = Ivan()
ivan.action3()              # 順序 Ivan
ivan.action2()              # 順序 Ivan -> Father
ivan.action1()              # 順序 Ivan -> Father -> Grandfather




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_19.py

# ch12_19.py
class Grandfather():
    """ 定義祖父類別 """
    def action1(self):
        print("Grandfather")
        
class Father(Grandfather):
    """ 定義父親類別 """
    def action3(self):      # 定義action3()
        print("Father")

class Uncle(Grandfather):
    """ 定義叔父類別 """
    def action2(self):      # 定義action2()
        print("Uncle")

class Ivan(Father, Uncle):
    """ 定義Ivan類別 """
    def action4(self):
        print("Ivan")

ivan = Ivan()
ivan.action4()              # 順序 Ivan
ivan.action3()              # 順序 Ivan -> Father
ivan.action2()              # 順序 Ivan -> Father -> Uncle
ivan.action1()              # 順序 Ivan -> Father -> Uncle -> Grandfather




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_19_1.py

# ch12_19_1.py
class A():
    def __init__(self):
        print('class A')

class B():
    def __init__(self):
        print('class B')

class C(A,B):
    def __init__(self):
        super().__init__()  
        print('class C')

x = C()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_19_2.py

# ch12_19_2.py
class A():
    def __init__(self):
        super().__init__()
        print('class A')

class B():
    def __init__(self):
        super().__init__()
        print('class B')

class C(A,B):
    def __init__(self):
        super().__init__()  
        print('class C')

x = C()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_2.py

# ch12_2.py
class Banks():
    ''' 定義銀行類別 '''
    bankname = 'Taipei Bank'    # 定義屬性
    def motto(self):            # 定義方法
        return "以客為尊"

userbank = Banks()              # 定義物件userbank
print("目前服務銀行是 ", userbank.bankname)
print("銀行服務理念是 ", userbank.motto())



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_20.py

# ch12_20.py
class Grandfather():
    """ 定義祖父類別 """
    pass
        
class Father(Grandfather):
    """ 定義父親類別 """
    pass

class Ivan(Father):
    """ 定義Ivan類別 """
    def fn(self):
        pass

grandfather = Grandfather()
father = Father()
ivan = Ivan()
print("grandfather物件類型: ", type(grandfather))
print("father物件類型     : ", type(father))
print("ivan物件類型       : ", type(ivan))
print("ivan物件fn方法類型 : ", type(ivan.fn))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_21.py

# ch12_21.py
class Grandfather():
    """ 定義祖父類別 """
    pass
        
class Father(Grandfather):
    """ 定義父親類別 """
    pass

class Ivan(Father):
    """ 定義Ivan類別 """
    def fn(self):
        pass

grandfa = Grandfather()
father = Father()
ivan = Ivan()
print("ivan屬於Ivan類別: ", isinstance(ivan, Ivan))
print("ivan屬於Father類別: ", isinstance(ivan, Father))
print("ivan屬於GrandFather類別: ", isinstance(ivan, Grandfather))
print("father屬於Ivan類別: ", isinstance(father, Ivan))
print("father屬於Father類別: ", isinstance(father, Father))
print("father屬於Grandfather類別: ", isinstance(father, Grandfather))
print("grandfa屬於Ivan類別: ", isinstance(grandfa, Ivan))
print("grandfa屬於Father類別: ", isinstance(grandfa, Father))
print("grandfa屬於Grandfather類別: ", isinstance(grandfa, Grandfather))



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_22.py

# ch12_22.py
def getMax(x, y):
    '''文件字串實例
建議x, y是整數
這個函數將傳回較大值'''
    if int(x) > int(y):
        return x
    else:
        return y

print(getMax(2, 3))         # 列印較大值
print(getMax.__doc__)       # 列印文件字串docstring


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_23.py

# ch12_23.py
class Myclass:
    '''文件字串實例
Myclass類別的應用'''
    def __init__(self, x):
        self.x = x
    def printMe(self):
        '''文字檔字串實例
Myclass類別內printMe方法的應用'''
        print("Hi", self.x)

data = Myclass(100)
data.printMe()
print(data.__doc__)             # 列印Myclass文件字串docstring
print(data.printMe.__doc__)     # 列印printMe文件字串docstring


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_24.py

# ch12_24.py
print('ch12_24.py module name = ', __name__)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_25.py

# ch12_25.py
def myFun():
    print("__name__ == __main__")
if __name__ == '__main__':
    myFun()






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_26.py

# ch12_26.py
import ch12_24


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_27.py

# ch12_27.py
import ch12_25




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_28.py

# ch12_28.py
class Name:
    def __init__(self, name):
        self.name = name

a = Name('Hung')
print(a)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_29.py

# ch12_29.py
class Name:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"{self.name}"

a = Name('Hung')
print(a)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_3.py

# ch12_3.py
class Banks():
    ''' 定義銀行類別 '''
    bankname = 'Taipei Bank'                # 定義屬性
    def __init__(self, uname, money):       # 初始化方法
        self.name = uname                   # 設定存款者名字
        self.balance = money                # 設定所存的錢

    def get_balance(self):                  # 獲得存款餘額
        return self.balance

hungbank = Banks('hung', 100)               # 定義物件hungbank
print(hungbank.name.title(), " 存款餘額是 ", hungbank.get_balance())






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_30.py

# ch12_30.py
class Name:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"{self.name}"
    __repr__ = __str__

a = Name('Hung')
print(a)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_31.py

# ch12_31.py
class Fib():                                        
    def __init__(self, max):                      
        self.max = max

    def __iter__(self):                           
        self.a = 0
        self.b = 1
        return self

    def __next__(self):                           
        fib = self.a
        if fib > self.max:
            raise StopIteration                   
        self.a, self.b = self.b, self.a + self.b
        return fib
for i in Fib(100):
    print(i)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_32.py

# ch12_32.py
class City():
    def __init__(self, name):
        self.name = name
    def equals(self, city2):
        return self.name.upper() == city2.name.upper()

one = City("Taipei")
two = City("taipei")
three = City("myhome")
print(one.equals(two))
print(one.equals(three))





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_33.py

# ch12_33.py
class City():
    def __init__(self, name):
        self.name = name
    def __eq__(self, city2):
        return self.name.upper() == city2.name.upper()

one = City("Taipei")
two = City("taipei")
three = City("myhome")
print(one == two)
print(one == three)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_34.py

# ch12_34.py
class Geometric():
    def __init__(self):
        self.color = "Green"
class Circle(Geometric):
    def __init__(self,radius):
        super().__init__()
        self.PI = 3.14159
        self.radius = radius
    def getRadius(self):
        return self.radius
    def setRadius(self,radius):
        self.radius = radius
    def getDiameter(self):
        return self.radius * 2
    def getPerimeter(self):
        return self.radius * 2 * self.PI
    def getArea(self):
        return self.PI * (self.radius ** 2)
    def getColor(self):
        return color

A = Circle(5)
print("圓形的顏色 : ", A.color)
print("圓形的半徑 : ", A.getRadius())
print("圓形的直徑 : ", A.getDiameter())
print("圓形的圓周 : ", A.getPerimeter())
print("圓形的面積 : ", A.getArea())
A.setRadius(10)
print("圓形的直徑 : ", A.getDiameter())





                       

    












        
        

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_35.py

# ch12_35.py
# 定義 Inventory 類別來管理商品庫存
class Inventory:
    # 初始化方法，建立一個空的商品字典
    def __init__(self):
        self.items = {}         # 商品字典，鍵是商品名，值是商品數量

    # 庫存中添加商品,如果商品存在則更新其數量；如果不存在則添加到字典中 
    def add_item(self, item, quantity):
        self.items[item] = self.items.get(item, 0) + quantity

    # 庫存中移除商品
    def remove_item(self, item, quantity):
        # 檢查商品是否存在且數量充足，然後從庫存中移除指定數量的商品
        if item in self.items and self.items[item] >= quantity:
            self.items[item] -= quantity
            # 如果商品數量為0，從字典中移除該商品
            if self.items[item] == 0:
                del self.items[item]

# 使用 Inventory 類別來管理庫存
inventory = Inventory()                 # 建立 Inventory 物件
inventory.add_item('apple', 10)         # 向庫存中添加10個蘋果
inventory.remove_item('apple', 3)       # 從庫存中移除3個蘋果

# 查看庫存的目前狀態
print(inventory.items)                  # 輸出：{'apple': 7}





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_36.py

# ch12_36.py
# 定義 Vehicle 類別來表示車輛
class Vehicle:
    # 初始化方法，設置車輛的製造商、型號和生產年份
    def __init__(self, make, model, year):
        self.make = make                    # 車輛的製造商
        self.model = model                  # 車輛的型號
        self.year = year                    # 車輛的生產年份

    # 方法回傳車輛的基本資料
    def get_info(self):
        # 回傳格式化的車輛資料字串
        return f'{self.year} {self.make} {self.model}'

# 使用 Vehicle 類別來建立車輛物件並獲取車輛資料
car = Vehicle('Lexus', 'ES 300h', 2025)     # 建立一個 Vehicle 對象
info = car.get_info()                       # get_info方法獲取車輛資料
print(info)                                 # 輸出：'2025 ES 300h'




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_37.py

# ch12_37.py
# 定義 StudentManager 類別來管理學生資料
class StudentManager:
    # 初始化方法, 建立一個空的學生字典
    def __init__(self):
        self.students = {}          # 學生字典,鍵是學生ID,值是學生名字

    # 方法用於添加新學生到字典中
    def add_student(self, id, name):
        self.students[id] = name    # 添加學生

    # 移除指定ID的學生, 檢查學生ID是否存在，如果存在則移除
    def remove_student(self, id):
        if id in self.students:
            del self.students[id]

# 使用 StudentManager 類別來管理學生
manager = StudentManager()          # 建立 StudentManager 物件
manager.add_student(1, 'Hung')      # 添加學生 Hung
manager.remove_student(1)           # 移除學生ID為 1 的學生

# 用 print(manager.students) 來查看學生字典的當前狀態
print(manager.students)             # 輸出：{}



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_4.py

# ch12_4.py
class Banks():
    ''' 定義銀行類別 '''
    bankname = 'Taipei Bank'                # 定義屬性
    def __init__(self, uname, money):       # 初始化方法
        self.name = uname                   # 設定存款者名字
        self.balance = money                # 設定所存的錢

    def save_money(self, money):            # 設計存款方法
        self.balance += money               # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.balance -= money               # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.name.title(), " 目前餘額: ", self.balance)

hungbank = Banks('hung', 100)               # 定義物件hungbank
hungbank.get_balance()                      # 獲得存款餘額                
hungbank.save_money(300)                    # 存款300元
hungbank.get_balance()                      # 獲得存款餘額
hungbank.withdraw_money(200)                # 提款200元
hungbank.get_balance()                      # 獲得存款餘額






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_5.py

# ch12_5.py
class Banks():
    ''' 定義銀行類別 '''
    bankname = 'Taipei Bank'                # 定義屬性
    def __init__(self, uname, money):       # 初始化方法
        self.name = uname                   # 設定存款者名字
        self.balance = money                # 設定所存的錢

    def save_money(self, money):            # 設計存款方法
        self.balance += money               # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.balance -= money               # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.name.title(), " 目前餘額: ", self.balance)

hungbank = Banks('hung', 100)               # 定義物件hungbank
johnbank = Banks('john', 300)               # 定義物件johnbank
hungbank.get_balance()                      # 獲得hung存款餘額                
johnbank.get_balance()                      # 獲得john存款餘額
hungbank.save_money(100)                    # hung存款100
johnbank.withdraw_money(150)                # john提款150
hungbank.get_balance()                      # 獲得hung存款餘額                
johnbank.get_balance()                      # 獲得john存款餘額









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_6.py

# ch12_6.py
class Banks():
    ''' 定義銀行類別 '''

    def __init__(self, uname):              # 初始化方法
        self.name = uname                   # 設定存款者名字
        self.balance = 0                    # 設定開戶金額是0
        self.bankname = "Taipei Bank"       # 設定銀行名稱

    def save_money(self, money):            # 設計存款方法
        self.balance += money               # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.balance -= money               # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.name.title(), " 目前餘額: ", self.balance)

hungbank = Banks('hung')                    # 定義物件hungbank
print("目前開戶銀行 ", hungbank.bankname)   # 列出目前開戶銀行
hungbank.get_balance()                      # 獲得hung存款餘額                
hungbank.save_money(100)                    # hung存款100
hungbank.get_balance()                      # 獲得hung存款餘額                










print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_7.py

# ch12_7.py
class Banks():
    ''' 定義銀行類別 '''

    def __init__(self, uname):              # 初始化方法
        self.name = uname                   # 設定存款者名字
        self.balance = 0                    # 設定開戶金額是0
        self.bankname = "Taipei Bank"       # 設定銀行名稱

    def save_money(self, money):            # 設計存款方法
        self.balance += money               # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.balance -= money               # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.name.title(), " 目前餘額: ", self.balance)

hungbank = Banks('hung')                    # 定義物件hungbank
hungbank.get_balance()
hungbank.balance = 10000                    # 類別外直接竄改存款餘額
hungbank.get_balance()












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_8.py

# ch12_8.py
class Banks():
    ''' 定義銀行類別 '''

    def __init__(self, uname):              # 初始化方法
        self.__name = uname                 # 設定私有存款者名字
        self.__balance = 0                  # 設定私有開戶金額是0
        self.__bankname = "Taipei Bank"     # 設定私有銀行名稱

    def save_money(self, money):            # 設計存款方法
        self.__balance += money             # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.__balance -= money             # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)

hungbank = Banks('hung')                    # 定義物件hungbank
hungbank.get_balance()
hungbank.__balance = 10000                  # 類別外直接竄改存款餘額
hungbank.get_balance()












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_9.py

# ch12_9.py
class Banks():
    ''' 定義銀行類別 '''

    def __init__(self, uname):              # 初始化方法
        self.__name = uname                 # 設定私有存款者名字
        self.__balance = 0                  # 設定私有開戶金額是0
        self.__bankname = "Taipei Bank"     # 設定私有銀行名稱
        self.__rate = 30                    # 預設美金與台幣換匯比例
        self.__service_charge = 0.01        # 換匯的服務費

    def save_money(self, money):            # 設計存款方法
        self.__balance += money             # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.__balance -= money             # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)

    def usa_to_taiwan(self, usa_d):         # 美金兌換台幣方法
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self,usa_d):             # 計算換匯這是私有方法
        return int(usa_d * self.__rate * (1 - self.__service_charge))
        
hungbank = Banks('hung')                    # 定義物件hungbank
usdallor = 50
print(usdallor, " 美金可以兌換 ", hungbank.usa_to_taiwan(usdallor), " 台幣") 












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_9_1.py

# ch12_9_1.py
class Score():
    def __init__(self, score):
        self.score = score

stu = Score(50)
print(stu.score)
stu.score = 100             
print(stu.score)





        
        

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_9_2.py

# ch12_9_2.py
class Score():
    def __init__(self, score):
        self.__score = score
    def getscore(self):
        print("inside the getscore")
        return self.__score
    def setscore(self, score):
        print("inside the setscore")
        self.__score = score

stu = Score(0)
print(stu.getscore())
stu.setscore(80)            
print(stu.getscore())





        
        

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_9_3.py

# ch12_9_3.py
class Score():
    def __init__(self, score):
        self.__score = score
    def getscore(self):
        print("inside the getscore")
        return self.__score
    def setscore(self, score):
        print("inside the setscore")
        self.__score = score
    sc = property(getscore, setscore)   # Python 風格     
    
stu = Score(0)
print(stu.sc)
stu.sc = 80
print(stu.sc)







        
        

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_9_4.py

# ch12_9_4.py
class Score():
    def __init__(self, score):
        self.__score = score
    @property
    def sc(self):
        print("inside the getscore")
        return self.__score
    @sc.setter
    def sc(self, score):
        print("inside the setscore")
        self.__score = score    
    
stu = Score(0)
print(stu.sc)
stu.sc = 80
print(stu.sc)







        
        

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_9_5.py

# ch12_9_5.py
class Square():
    def __init__(self, sideLen):
        self.__sideLen = sideLen
    @property
    def area(self):
        return self.__sideLen ** 2
    
obj = Square(10)
print(obj.area)









        
        

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_9_6.py

# ch12_9_6.py
class Counter():
    counter = 0                             # 類別屬性,可由類別本身調用
    def __init__(self):
        Counter.counter += 1                # 更新指標
    @classmethod
    def show_counter(cls):                  # 類別方法,可由類別本身調用
        print("class method")
        print("counter = ", cls.counter)    # 也可使用Counter.counter調用
        print("counter = ", Counter.counter)
        
one = Counter()
two = Counter()
three = Counter()
Counter.show_counter()












        
        

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_9_7.py

# ch12_9_7.py
class Pizza():
    @staticmethod
    def demo():
        print("I like Pizza")

Pizza.demo()



    











        
        

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch12\ch12_9_8.py

# ch12_9_8.py
class Father():
    def hometown(self):
        print('我住在台北')

class Son(Father):
    pass

hung = Father()
ivan = Son()
hung.hometown()
ivan.hometown()





print("------------------------------------------------------------")  # 60個



#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_1.py

# ch15_1.py
def division(x, y):
    return x / y

print(division(10, 2))      # 列出10/2
print(division(5, 0))       # 列出5/0
print(division(6, 3))       # 列出6/3




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_10.py

# ch15_10.py
def wordsNum(fn):
    """適用英文文件, 輸入文章的檔案名稱,可以計算此文章的字數"""
    try:
        with open(fn) as file_Obj:  # 用預設"r"傳回檔案
            data = file_Obj.read()  # 讀取檔案到變數data
    except Exception:
        print(f"Exception找不到 {fn} 檔案")
    else:
        wordList = data.split()     # 將文章轉成串列
        print(f"{fn} 文章的字數是 {len(wordList)}")   # 文章字數

files = ['data1.txt', 'data2.txt', 'data3.txt']       # 檔案串列
for file in files:
    wordsNum(file)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_11.py

# ch15_11.py
def division(x, y):
    try:                        # try - except指令
        return x / y
    except ZeroDivisionError:   # 除數為0使用
        print("除數為0發生")
    except TypeError:           # 資料型別錯誤
        print("使用字元做除法運算異常")

print(division(10, 2))          # 列出10/2
print(division(5, 0))           # 列出5/0
print(division('a', 'b'))       # 列出'a' / 'b'
print(division(6, 3))           # 列出6/3






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_12.py

# ch15_12.py
def division(x, y):
    try:                        # try - except指令
        return x / y
    except (ZeroDivisionError, TypeError):   # 2個異常
        print("除數為0發生 或 使用字元做除法運算異常")

print(division(10, 2))          # 列出10/2
print(division(5, 0))           # 列出5/0
print(division('a', 'b'))       # 列出'a' / 'b'
print(division(6, 3))           # 列出6/3






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_13.py

# ch15_13.py
def division(x, y):
    try:                        # try - except指令
        return x / y
    except (ZeroDivisionError, TypeError) as e:   # 2個異常
        print(e)

print(division(10, 2))          # 列出10/2
print(division(5, 0))           # 列出5/0
print(division('a', 'b'))       # 列出'a' / 'b'
print(division(6, 3))           # 列出6/3






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_14.py

# ch15_14.py
def division(x, y):
    try:                        # try - except指令
        return x / y
    except:                     # 捕捉所有異常
        print("異常發生")

print(division(10, 2))          # 列出10/2
print(division(5, 0))           # 列出5/0
print(division('a', 'b'))       # 列出'a' / 'b'
print(division(6, 3))           # 列出6/3






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_15.py

# ch15_15.py
def passWord(pwd):
    """檢查密碼長度必須是5到8個字元"""
    pwdlen = len(pwd)                       # 密碼長度
    if pwdlen < 5:                          # 密碼長度不足            
        raise Exception('密碼長度不足')
    if pwdlen > 8:                          # 密碼長度太長
        raise Exception('密碼長度太長')
    print('密碼長度正確')

for pwd in ('aaabbbccc', 'aaa', 'aaabbb'):  # 測試系列密碼值
    try:
        passWord(pwd)
    except Exception as err:
        print("密碼長度檢查異常發生: ", str(err))



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_16.py

# ch15_16.py
import traceback                            # 導入taceback

def passWord(pwd):
    """檢查密碼長度必須是5到8個字元"""
    pwdlen = len(pwd)                       # 密碼長度
    if pwdlen < 5:                          # 密碼長度不足            
        raise Exception('密碼長度不足')
    if pwdlen > 8:                          # 密碼長度太長
        raise Exception('密碼長度太長')
    print('密碼長度正確')

for pwd in ('aaabbbccc', 'aaa', 'aaabbb'):  # 測試系列密碼值
    try:
        passWord(pwd)
    except Exception as err:
        errlog = open('errch15_16.txt', 'a')   # 開啟錯誤檔案
        errlog.write(traceback.format_exc())   # 寫入錯誤檔案
        errlog.close()                         # 關閉錯誤檔案
        print("將Traceback寫入錯誤檔案errch15_16.txt完成")
        print("密碼長度檢查異常發生: ", str(err))



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_17.py

# ch15_17.py
import traceback

def division(x, y):
    try:                        # try - except指令
        return x / y
    except:                     # 捕捉所有異常
        errlog = open('errch15_17.txt', 'a')   # 開啟錯誤檔案
        errlog.write(traceback.format_exc())   # 寫入錯誤檔案
        errlog.close()                         # 關閉錯誤檔案
        print("將Traceback寫入錯誤檔案errch15_17.txt完成")
        print("異常發生")

print(division(10, 2))          # 列出10/2
print(division(5, 0))           # 列出5/0
print(division('a', 'b'))       # 列出'a' / 'b'
print(division(6, 3))           # 列出6/3






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_18.py

# ch15_18.py
def division(x, y):
    try:                             # try - except指令
        return x / y
    except:                          # 捕捉所有異常
        print("異常發生")
    finally:                         # 離開函數前先執行此程式碼
        print("階段任務完成")

print(division(10, 2),"\n")          # 列出10/2
print(division(5, 0),"\n")           # 列出5/0
print(division('a', 'b'),"\n")       # 列出'a' / 'b'
print(division(6, 3),"\n")           # 列出6/3






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_19.py

# ch15_19.py
class Banks():
    # 定義銀行類別
    title = 'Taipei Bank'                   # 定義屬性
    def __init__(self, uname, money):       # 初始化方法
        self.name = uname                   # 設定存款者名字
        self.balance = money                # 設定所存的錢

    def save_money(self, money):            # 設計存款方法
        self.balance += money               # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.balance -= money               # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.name.title(), " 目前餘額: ", self.balance)

hungbank = Banks('hung', 100)               # 定義物件hungbank
hungbank.get_balance()                      # 獲得存款餘額                
hungbank.save_money(-300)                   # 存款-300元
hungbank.get_balance()                      # 獲得存款餘額
hungbank.withdraw_money(700)                # 提款700元
hungbank.get_balance()                      # 獲得存款餘額






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_2.py

# ch15_2.py
def division(x, y):
    try:                        # try - except指令
        return x / y
    except ZeroDivisionError:   # 除數為0時執行
        print("除數不可為0")

print(division(10, 2))          # 列出10/2
print(division(5, 0))           # 列出5/0
print(division(6, 3))           # 列出6/3






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_2_1.py

# ch15_2_1.py
def division(x, y):
    try:                        # try - except指令
        return x / y
    except ZeroDivisionError:   # 除數為0時執行
        print("除數不可為0")

print(division(10, 2))          # 列出10/2
print(division('a', 'b'))       # 列出'a' / 'b'
print(division(6, 3))           # 列出6/3






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_20.py

# ch15_20.py
class Banks():
    # 定義銀行類別
    title = 'Taipei Bank'                   # 定義屬性
    def __init__(self, uname, money):       # 初始化方法
        self.name = uname                   # 設定存款者名字
        self.balance = money                # 設定所存的錢

    def save_money(self, money):            # 設計存款方法
        assert money > 0, '存款money必需大於0'
        self.balance += money               # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        assert money > 0, '提款money必需大於0'
        assert money <= self.balance, '存款金額不足'
        self.balance -= money               # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.name.title(), " 目前餘額: ", self.balance)

hungbank = Banks('hung', 100)               # 定義物件hungbank
hungbank.get_balance()                      # 獲得存款餘額                
hungbank.save_money(300)                    # 存款300元
hungbank.get_balance()                      # 獲得存款餘額
hungbank.save_money(-300)                   # 存款-300元
hungbank.get_balance()                      # 獲得存款餘額





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_21.py

# ch15_21.py
class Banks():
    # 定義銀行類別
    title = 'Taipei Bank'                   # 定義屬性
    def __init__(self, uname, money):       # 初始化方法
        self.name = uname                   # 設定存款者名字
        self.balance = money                # 設定所存的錢

    def save_money(self, money):            # 設計存款方法
        assert money > 0, '存款money必需大於0'
        self.balance += money               # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        assert money > 0, '提款money必需大於0'
        assert money <= self.balance, '存款金額不足'
        self.balance -= money               # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.name.title(), " 目前餘額: ", self.balance)

hungbank = Banks('hung', 100)               # 定義物件hungbank
hungbank.get_balance()                      # 獲得存款餘額                
hungbank.save_money(300)                    # 存款300元
hungbank.get_balance()                      # 獲得存款餘額
hungbank.withdraw_money(700)                # 提款700元
hungbank.get_balance()                      # 獲得存款餘額





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_22.py

# ch15_22.py
import logging

logging.basicConfig(level=logging.DEBUG)    # 等級是DEBUG
logging.debug('logging message, DEBUG')
logging.info('logging message, INFO')
logging.warning('logging message, WARNING')
logging.error('logging message, ERROR')
logging.critical('logging message, CRITICAL')



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_23.py

# ch15_23.py
import logging

logging.basicConfig(level=logging.WARNING)    # 等級是WARNING
logging.debug('logging message, DEBUG')
logging.info('logging message, INFO')
logging.warning('logging message, WARNING')
logging.error('logging message, ERROR')
logging.critical('logging message, CRITICAL')



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_24.py

# ch15_24.py
import logging

logging.basicConfig(level=logging.DEBUG, format='')
logging.debug('logging message, DEBUG')
logging.info('logging message, INFO')
logging.warning('logging message, WARNING')
logging.error('logging message, ERROR')
logging.critical('logging message, CRITICAL')



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_25.py

# ch15_25.py
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s')
logging.debug('logging message, DEBUG')
logging.info('logging message, INFO')
logging.warning('logging message, WARNING')
logging.error('logging message, ERROR')
logging.critical('logging message, CRITICAL')



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_26.py

# ch15_26.py
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s : %(message)s')
logging.debug('logging message, DEBUG')
logging.info('logging message, INFO')
logging.warning('logging message, WARNING')
logging.error('logging message, ERROR')
logging.critical('logging message, CRITICAL')



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_27.py

# ch15_27.py
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s : %(message)s')
logging.debug('logging message.')
logging.info('logging message.')
logging.warning('logging message')
logging.error('logging message')
logging.critical('logging message')



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_28.py

# ch15_28.py
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s : %(message)s')
logging.debug("程式開始")
for i in range(5):
    logging.debug(f"目前索引 {i}")
logging.debug("程式結束")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_29.py

# ch15_29.py
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s : %(message)s')
logging.debug("程式開始")

def factorial(n):
    logging.debug(f"factorial {n} 計算開始")
    ans = 1
    for i in range(n + 1):
        ans *= i
        logging.debug('i = ' + str(i) + ', ans = ' + str(ans))
    logging.debug(f"factorial {n} 計算結束")
    return ans

num = 5
print(f"factorial({num}) = {factorial(num)}")
logging.debug("程式結束")





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_3.py

# ch15_3.py
def division(x, y):
    try:                        # try - except指令
        ans =  x / y
    except ZeroDivisionError:   # 除數為0時執行
        print("除數不可為0")
    else:
        return ans              # 傳回正確的執行結果

print(division(10, 2))          # 列出10/2
print(division(5, 0))           # 列出5/0
print(division(6, 3))           # 列出6/3






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_30.py

# ch15_30.py
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s : %(message)s')
logging.debug('程式開始')

def factorial(n):
    logging.debug(f"factorial {n} 計算開始")
    ans = 1
    for i in range(1, n + 1):
        ans *= i
        logging.debug('i = ' + str(i) + ', ans = ' + str(ans))
    logging.debug(f"factorial {n} 計算結束")
    return ans

num = 5
print(f"factorial({num}) = {factorial(num)}")
logging.debug('程式結束')





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_31.py

# ch15_31.py
import logging

logging.basicConfig(filename='out15_31.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s : %(message)s')
logging.debug('程式開始')

def factorial(n):
    logging.debug(f"factorial {n} 計算開始")
    ans = 1
    for i in range(1, n + 1):
        ans *= i
        logging.debug('i = ' + str(i) + ', ans = ' + str(ans))
    logging.debug(f"factorial {n} 計算結束")
    return ans

num = 5
print(f"factorial({num}) = {factorial(num)}")
logging.debug("程式結束")





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_32.py

# ch15_32.py
import logging

logging.basicConfig(level=logging.CRITICAL,
                    format='%(asctime)s - %(levelname)s : %(message)s')
logging.debug('程式開始')

def factorial(n):
    logging.debug(f"factorial {n} 計算開始")
    ans = 1
    for i in range(1, n + 1):
        ans *= i
        logging.debug('i = ' + str(i) + ', ans = ' + str(ans))
    logging.debug(f"factorial {n} 計算結束")
    return ans

num = 5
print(f"factorial({num}) = {factorial(num)}")
logging.debug("程式結束")





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_33.py

# ch15_33.py
import logging
logging.disable(logging.CRITICAL)       # 停用所有logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s : %(message)s')
logging.debug('程式開始')

def factorial(n):
    logging.debug('factorial %s 計算開始' % n)
    ans = 1
    for i in range(1, n + 1):
        ans *= i
        logging.debug('i = ' + str(i) + ', ans = ' + str(ans))
    logging.debug('factorial %s 計算結束' % n)
    return ans

num = 5
print("factorial(%d) = %d" % (num, factorial(num)))
logging.debug('程式結束')





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_34.py

# ch15_34.py
import sqlite3

try:
    # 嘗試連接到資料庫
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    # 嘗試執行查詢，可能會引發異常
    cursor.execute('SELECT * FROM non_existent_table')
except sqlite3.Error as e:
    # 捕獲並處理 SQLite 特定的異常
    print(f"Database error: {e}")
except Exception as e:
    # 捕獲並處理其他所有異常
    print(f"Exception occurred: {e}")
finally:
    # 確保資料庫連接被關閉
    conn.close()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_35.py

# ch15_35.py
try:
    # 嘗試打開一個不存在的檔案
    with open('non_existent_file.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    # 如果文件不存在, 捕獲異常
    print("The file was not found")
except IOError:
    # 處理 I/O 錯誤, 例如:讀取錯誤
    print("An I/O error occurred")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_36.py

# ch15_36.py
import requests

try:
    # 嘗試發出網絡請求
    response = requests.get('http://example.com')
    # 如果請求返回了錯誤響應, 會引發 HTTPError
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    # 處理 HTTP 錯誤
    print(f"HTTP Error: {e}")
except requests.exceptions.ConnectionError as e:
    # 處理連接錯誤
    print(f"Connection Error: {e}")
except requests.exceptions.Timeout as e:
    # 處理請求超時錯誤
    print(f"Timeout Error: {e}")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_37.py

# ch15_37.py
user_input = input("Please enter a number: ")

try:
    # 嘗試將使用者輸入轉換為整數
    val = int(user_input)
    print(f"Valid number entered: {val}")
except ValueError:
    # 如果輸入不能轉換為整數，處理 ValueError
    print("That's not a number!")




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_4.py

# ch15_4.py

fn = 'data15_4.txt'             # 設定欲開啟的檔案
try:
    with open(fn) as file_Obj:  # 預設mode=r開啟檔案
        data = file_Obj.read()  # 讀取檔案到變數data
except FileNotFoundError:
    print(f"找不到 {fn} 檔案")
else:
    print(data)                 # 輸出變數data







    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_5.py

# ch15_5.py

fn = 'data15_5.txt'             # 設定欲開啟的檔案
try:
    with open(fn) as file_Obj:  # 用預設mode=r開啟檔案
        data = file_Obj.read()  # 讀取檔案到變數data
except FileNotFoundError:
    print("找不到 %s 檔案" % fn)
else:
    print(data)                 # 輸出變數data







    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_6.py

# ch15_6.py

fn = 'data15_6.txt'             # 設定欲開啟的檔案
try:
    with open(fn) as file_Obj:  # 用預設mode=r開啟檔案
        data = file_Obj.read()  # 讀取檔案到變數data
except FileNotFoundError:
    print(f"找不到 {fn} 檔案")
else:
    wordList = data.split()     # 將文章轉成串列
    print(f"{fn} 文章的字數是 {len(wordList)}")    # 列印文章字數






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_7.py

# ch15_7.py
def wordsNum(fn):
    """適用英文文件, 輸入文章的檔案名稱,可以計算此文章的字數"""
    try:
        with open(fn) as file_Obj:  # 用預設mode=r開啟檔案
            data = file_Obj.read()  # 讀取檔案到變數data
    except FileNotFoundError:
        print(f"找不到 {fn} 檔案")
    else:
        wordList = data.split()     # 將文章轉成串列
        print(f"{fn} 文章的字數是 {len(wordList)}")   # 文章字數

file = 'data15_6.txt'               # 設定欲開啟的檔案
wordsNum(file)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_8.py

# ch15_8.py
def wordsNum(fn):
    """適用英文文件, 輸入文章的檔案名稱,可以計算此文章的字數"""
    try:
        with open(fn) as file_Obj:  # 用預設mode=r開啟檔案
            data = file_Obj.read()  # 讀取檔案到變數data
    except FileNotFoundError:
        print(f"找不到 {fn} 檔案")
    else:
        wordList = data.split()     # 將文章轉成串列
        print(f"{fn} 文章的字數是 {len(wordList)}")   # 文章字數

files = ['data1.txt', 'data2.txt', 'data3.txt']       # 檔案串列
for file in files:
    wordsNum(file)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch15\ch15_9.py

# ch15_9.py
def division(x, y):
    try:                        # try - except指令
        return x / y
    except Exception:           # 通用錯誤使用
        print("通用錯誤發生")

print(division(10, 2))          # 列出10/2
print(division(5, 0))           # 列出5/0
print(division('a', 'b'))       # 列出'a' / 'b'
print(division(6, 3))           # 列出6/3






print("------------------------------------------------------------")  # 60個



#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_1.py

# ch16_1.py
def taiwanPhoneNum(string):
    """檢查是否有含手機聯絡資訊的台灣手機號碼格式"""
    if len(string) != 12:       # 如果長度不是12
        return False            # 傳回非手機號碼格式
    
    for i in range(0, 4):       # 如果前4個字出現非數字字元
        if string[i].isdecimal() == False:
            return False        # 傳回非手機號碼格式
        
    if string[4] != '-':        # 如果不是'-'字元
        return False            # 傳回非手機號碼格式
   
    for i in range(5, 8):       # 如果中間3個字出現非數字字元
        if string[i].isdecimal() == False:
            return False        # 傳回非手機號碼格

    if string[8] != '-':        # 如果不是'-'字元
        return False            # 傳回非手機號碼格式

    for i in range(9, 12):      # 如果最後3個字出現非數字字元
        if string[i].isdecimal() == False:
            return False        # 傳回非手機號碼格
    return True                 # 通過以上測試

print("I love Ming-Chi: 是台灣手機號碼", taiwanPhoneNum('I love Ming-Chi'))
print("0932-999-199:    是台灣手機號碼", taiwanPhoneNum('0932-999-199'))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_10.py

# ch16_10.py
import re

msg = 'John and Tom will attend my party tonight. John is my best friend.'
pattern = 'John|Tom'                # 搜尋John和Tom
txt = re.findall(pattern, msg)      # 傳回搜尋結果
print(txt)
pattern = 'Mary|Tom'                # 搜尋Mary和Tom
txt = re.findall(pattern, msg)      # 傳回搜尋結果
print(txt)






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_11.py

# ch16_11.py
import re

msg = 'john and TOM will attend my party tonight. JOHN is my best friend.'
pattern = 'John|Tom'                        # 搜尋John和Tom
txt = re.findall(pattern, msg, re.I)        # 傳回搜尋忽略大小寫的結果
print(txt)
pattern = 'Mary|tom'                        # 搜尋Mary和tom
txt = re.findall(pattern, msg, re.I)        # 傳回搜尋忽略大小寫的結果
print(txt)






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_12.py

# ch16_12.py
import re

def searchStr(pattern, msg):
    txt = re.search(pattern, msg)
    if txt == None:         # 搜尋失敗
        print("搜尋失敗 ",txt)
    else:                   # 搜尋成功
        print("搜尋成功 ",txt.group())

msg1 = 'son'
msg2 = 'sonson'
msg3 = 'sonsonson'
msg4 = 'sonsonsonson'
msg5 = 'sonsonsonsonson'
pattern = '(son){3,5}'
searchStr(pattern,msg1)
searchStr(pattern,msg2)
searchStr(pattern,msg3)
searchStr(pattern,msg4)
searchStr(pattern,msg5)


    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_13.py

# ch16_13.py
import re

def searchStr(pattern, msg):
    txt = re.search(pattern, msg)
    if txt == None:         # 搜尋失敗
        print("搜尋失敗 ",txt)
    else:                   # 搜尋成功
        print("搜尋成功 ",txt.group())

msg = 'sonsonsonsonson'
pattern = '(son){3,5}'
searchStr(pattern,msg)


    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_14.py

# ch16_14.py
import re

def searchStr(pattern, msg):
    txt = re.search(pattern, msg)
    if txt == None:         # 搜尋失敗
        print("搜尋失敗 ",txt)
    else:                   # 搜尋成功
        print("搜尋成功 ",txt.group())

msg = 'sonsonsonsonson'
pattern = '(son){3,5}?'     # 非貪婪模式
searchStr(pattern,msg)


    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_15.py

# ch16_15.py
import re
# 測試1將字串從句子分離
msg = 'John, Johnson, Johnnason and Johnnathan will attend my party tonight.'
pattern = '\w+'                    # 不限長度的單字
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試2將John開始的字串分離
msg = 'John, Johnson, Johnnason and Johnnathan will attend my party tonight.'
pattern = 'John\w*'                # John開頭的單字
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_16.py

# ch16_16.py
import re

msg = '1 cat, 2 dogs, 3 pigs, 4 swans'
pattern = '\d+\s\w+'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_17.py

# ch16_17.py
import re
# 測試1搜尋[aeiouAEIOU]字元
msg = 'John, Johnson, Johnnason and Johnnathan will attend my party tonight.'
pattern = '[aeiouAEIOU]'           
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試2搜尋[2-5.]字元
msg = '1. cat, 2. dogs, 3. pigs, 4. swans'
pattern = '[2-5.]'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_18.py

# ch16_18.py
import re
# 測試1搜尋不在[aeiouAEIOU]的字元
msg = 'John, Johnson, Johnnason and Johnnathan will attend my party tonight.'
pattern = '[^aeiouAEIOU]'           
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試2搜尋不在[2-5.]的字元
msg = '1. cat, 2. dogs, 3. pigs, 4. swans'
pattern = '[^2-5.]'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_19.py

# ch16_19.py
import re
# 測試1搜尋John字串在最前面
msg = 'John will attend my party tonight.'
pattern = '^John'           
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試2搜尋John字串不是在最前面
msg = 'My best friend is John'
pattern = '^John'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_2.py

# ch16_2.py
def taiwanPhoneNum(string):
    """檢查是否有含手機聯絡資訊的台灣手機號碼格式"""
    if len(string) != 12:       # 如果長度不是12
        return False            # 傳回非手機號碼格式
    
    for i in range(0, 4):       # 如果前4個字出現非數字字元
        if string[i].isdecimal() == False:
            return False        # 傳回非手機號碼格式
        
    if string[4] != '-':        # 如果不是'-'字元
        return False            # 傳回非手機號碼格式
   
    for i in range(5, 8):       # 如果中間3個字出現非數字字元
        if string[i].isdecimal() == False:
            return False        # 傳回非手機號碼格

    if string[8] != '-':        # 如果不是'-'字元
        return False            # 傳回非手機號碼格式

    for i in range(9, 12):      # 如果最後3個字出現非數字字元
        if string[i].isdecimal() == False:
            return False        # 傳回非手機號碼格
    return True                 # 通過以上測試

def parseString(string):
    """解析字串是否含有電話號碼"""
    notFoundSignal = True       # 註記沒有找到電話號碼為True
    for i in range(len(string)):  # 用迴圈逐步抽取12個字元做測試
        msg = string[i:i+12]
        if taiwanPhoneNum(msg):
            print(f"電話號碼是: {msg}")
            notFoundSignal = False        
    if notFoundSignal:          # 如果沒有找到電話號碼則列印
        print(f"{string} 字串不含電話號碼")

msg1 = 'Please call my secretary using 0930-919-919 or 0952-001-001'
msg2 = '請明天17:30和我一起參加明志科大教師節晚餐'
msg3 = '請明天17:30和我一起參加明志科大教師節晚餐, 可用0933-080-080聯絡我'
parseString(msg1)
parseString(msg2)
parseString(msg3)






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_20.py

# ch16_20.py
import re
# 測試1搜尋最後字元是非英文字母數字和底線字元
msg = 'John will attend my party 28 tonight.'
pattern = '\W$'           
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試2搜尋最後字元是非英文字母數字和底線字元
msg = 'I am 28'
pattern = '\W$'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試3搜尋最後字元是數字
msg = 'I am 28'
pattern = '\d$'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試4搜尋最後字元是數字
msg = 'I am 28 year old.'
pattern = '\d$'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_21.py

# ch16_21.py
import re
# 測試1搜尋開始到結尾皆是數字的字串
msg = '09282028222'
pattern = '^\d+$'           
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試2搜尋開始到結尾皆是數字的字串
msg = '0928tuyr990'
pattern = '^\d+$'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_22.py

# ch16_22.py
import re
msg = 'cat hat sat at matter flat'
pattern = '.at'           
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_23.py

# ch16_23.py
import re

msg = 'Name: Jiin-Kwei Hung Address: 8F, Nan-Jing E. Rd, Taipei'
pattern = 'Name: (.*) Address: (.*)'
txt = re.search(pattern,msg)      # 傳回搜尋結果
Name, Address = txt.groups()
print("Name:    ", Name)
print("Address: ", Address)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_24.py

# ch16_24.py
import re
#測試1搜尋除了換列字元以外字元
msg = 'Name: Jiin-Kwei Hung \nAddress: 8F, Nan-Jing E. Rd, Taipei'
pattern = '.*'
txt = re.search(pattern,msg)           # 傳回搜尋不含換列字元結果
print("測試1輸出: ", txt.group())
#測試2搜尋包括換列字元
msg = 'Name: Jiin-Kwei Hung \nAddress: 8F, Nan-Jing E. Rd, Taipei'
pattern = '.*'
txt = re.search(pattern,msg,re.DOTALL) # 傳回搜尋含換列字元結果
print("測試2輸出: ", txt.group())




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_25.py

# ch16_25.py
import re
#測試1搜尋使用re.match()
msg = 'John will attend my party tonight.'  # John是第一個字串
pattern = 'John'
txt = re.match(pattern,msg)                 # 傳回搜尋結果
if txt != None:
    print("測試1輸出: ", txt.group())
else:
    print("測試1搜尋失敗")
#測試2搜尋使用re.match()
msg = 'My best friend is John.'             # John不是第一個字串
txt = re.match(pattern,msg,re.DOTALL)       # 傳回搜尋結果
if txt != None:
    print("測試2輸出: ", txt.group())
else:
    print("測試2搜尋失敗")







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_26.py

# ch16_26.py
import re
#測試1搜尋使用re.match()
msg = 'John will attend my party tonight.'  
pattern = 'John'
txt = re.match(pattern,msg)                 # re.match()
if txt != None:
    print("使用re.match()輸出MatchObject物件:  ", txt)
else:
    print("測試1搜尋失敗")
#測試1搜尋使用re.search()
txt = re.search(pattern,msg)                # re.search()
if txt != None:
    print("使用re.search()輸出MatchObject物件: ", txt)
else:
    print("測試1搜尋失敗")







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_27.py

# ch16_27.py
import re
#測試1搜尋使用re.match()
msg = 'John will attend my party tonight.'  
pattern = 'John'
txt = re.match(pattern,msg)                 # re.match()
if txt != None:
    print("搜尋成功字串的起始索引位置 :  ", txt.start())
    print("搜尋成功字串的結束索引位置 :  ", txt.end())
    print("搜尋成功字串的結束索引位置 :  ", txt.span())
#測試2搜尋使用re.search()
msg = 'My best friend is John.'  
txt = re.search(pattern,msg)                # re.search()
if txt != None:
    print("搜尋成功字串的起始索引位置 :  ", txt.start())
    print("搜尋成功字串的結束索引位置 :  ", txt.end())
    print("搜尋成功字串的結束索引位置 :  ", txt.span())









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_28.py

# ch16_28.py
import re
#測試1取代使用re.sub()結果成功
msg = 'Eli Nan will attend my party tonight. My best friend is Eli Nan'  
pattern = 'Eli Nan'                 # 欲搜尋字串        
newstr = 'Kevin Thomson'            # 新字串
txt = re.sub(pattern,newstr,msg)    # 如果找到則取代
if txt != msg:                      # 如果txt與msg內容不同表示取代成功
    print("取代成功: ", txt)        # 列出成功取代結果
else:
    print("取代失敗: ", txt)        # 列出失敗取代結果
#測試2取代使用re.sub()結果失敗  
pattern = 'Eli Thomson'             # 欲搜尋字串        
txt = re.sub(pattern,newstr,msg)    # 如果找到則取代           
if txt != msg:                      # 如果txt與msg內容不同表示取代成功
    print("取代成功: ", txt)        # 列出成功取代結果
else:
    print("取代失敗: ", txt)        # 列出失敗取代結果




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_29.py

# ch16_29.py
import re
# 使用隱藏文字執行取代
msg = 'CIA Mark told CIA Linda that secret USB had given to CIA Peter.'
pattern = r'CIA (\w)\w*'            # 欲搜尋CIA + 空一格後的名字        
newstr = r'\1***'                   # 新字串使用隱藏文字
txt = re.sub(pattern,newstr,msg)    # 執行取代
print("取代成功: ", txt)            # 列出取代結果



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_3.py

# ch16_3.py
import re

msg1 = 'Please call my secretary using 0930-919-919 or 0952-001-001'
msg2 = '請明天17:30和我一起參加明志科大教師節晚餐'
msg3 = '請明天17:30和我一起參加明志科大教師節晚餐, 可用0933-080-080聯絡我'

def parseString(string):
    """解析字串是否含有電話號碼"""
    pattern = r'\d\d\d\d-\d\d\d-\d\d\d'
    phoneNum = re.search(pattern, string)
    if phoneNum != None:        # 如果phoneNum不是None表示取得號碼
        print(f"電話號碼是: {phoneNum.group()}")
    else:
        print(f"{string} 字串不含電話號碼")

parseString(msg1)
parseString(msg2)
parseString(msg3)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_30.py

# ch16_30.py
import re

msg = '''02-88223349,
        (02)-26669999,
        02-29998888 ext 123,
        1234567899999,
        02 33887766 ext. 1234,
        02 33887799 ext. 12345,
        12345,
        123'''
pattern = r'''(
    (\d{2}|\(\d{2}\))?              # 區域號碼
    (\s|-)?                         # 區域號碼與電話號碼的分隔符號
    \d{8}                           # 電話號碼
    (\s*(ext|ext.)\s*\d{2,4})?      # 2-4位數的分機號碼
    )'''
phoneNum = re.findall(pattern, msg, re.VERBOSE)     # 傳回搜尋結果
print("以下是符合的電話號碼")
for num in phoneNum:
    print(num[0])





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_31.py

# ch16_31.py
import re

msg = '''02-88223349,
        (02)-26669999,
        02-29998888 ext 123,
        1234567899999,
        02 33887766 ext. 1234,
        02 33887799 ext. 12345,
        12345,
        123'''
pattern = r'''(
    (\d{2}|\(\d{2}\))?              # 區域號碼
    (\s|-)?                         # 區域號碼與電話號碼的分隔符號
    \b\d{8}\b                       # 電話號碼
    (\s*(ext|ext.)\s*\d{2,4}\b)?    # 2-4位數的分機號碼
    )'''
phoneNum = re.findall(pattern, msg, re.VERBOSE)     # 傳回搜尋結果
print("以下是符合的電話號碼")
for num in phoneNum:
    print(num[0])





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_32.py

# ch16_32.py
import re

msg = '''txt@deepwisdom.comyyy.twkkk,
         ser@deepmind.com.tw,
         aaa@gmail.comcomkk,
         kkk@gmail.com,
         abc@aa,
         abcdefg'''
pattern = r'''(
    [a-zA-Z0-9_.]+                  # 使用者帳號
    @                               # @符號
    [a-zA-Z0-9-.]+                  # 主機域名domain
    [\.]                            # .符號
    [a-zA-Z]{2,4}\b                 # 可能是com或edu或其它
    ([\.])?                         # .符號, 也可能無特別是美國
    ([a-zA-Z]{2,4}\b)?              # 國別
    )'''
eMail = re.findall(pattern, msg, re.VERBOSE)     # 傳回搜尋結果
print("以下是符合的電子郵件地址")
for mail in eMail:
    print(mail[0])




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_33.py

# ch16_33.py
import re                   

# 定義一個函數用於重命名檔案串列
def rename_files(files):
    # 定義正則表達式模式匹配檔案名的一部分
    # (\w+)   匹配一個或多個單詞字元(字母、數字或底線)
    # (\d{4}) 匹配四位數字 (代表年份)
    # (\d{2}) 匹配兩位數字 (代表月份)
    pattern = r"(\w+)_(\d{4})_(\d{2})"
    for file in files:                              # 遍歷檔案串列
        # 使用 sub() 函數替換匹配的名稱
        # \1, \2, \3 分別對應第一、第二、第三個捕獲組匹配的內容
        # 這裡將 底線( _ ) 替換為 ( - )
        new_name = re.sub(pattern, r"\1-\2-\3", file)
        print(f"Old : {file},   New: {new_name}")   # 輸出舊和新檔名

# 檔案名稱串列
files = [
    "report_2023_04.pdf",
    "report_2023_05.pdf",
    "summary_2023_04.docx"
]

rename_files(files)  # 呼叫函數, 傳入檔案名稱串列

# 輸出
# Old: report_2023_04.pdf,  New: report-2023-04.pdf
# Old: report_2023_05.pdf,  New: report-2023-05.pdf
# Old: summary_2023_04.docx,  New: summary-2023-04.docx






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_34.py

# ch16_34.py
import re

def validate_and_format_credit_card(number):
    # 定義Visa信用卡號碼的正則表達式, Visa卡號以4開頭, 並有16位數字
    pattern = r"^(?:4[0-9]{12}(?:[0-9]{3})?)$"  

    # 使用match方法檢查提供的卡號是否符合正則表達式模式。
    match = re.match(pattern, number)
    if match:
        # 如果匹配成功，使用findall方法分組每四位數字
        # 然後用join方法將這些組用 "-" 連接成一個格式化的字串
        formatted = "-".join(re.findall(r"....", number))
        return True, formatted  # 返回一個元組和驗證成功格式化的卡號
    return False, None          # 如果匹配不成功, 返回False和None

# 測試卡號
card_number = "4111111111111111"
is_valid, formatted = validate_and_format_credit_card(card_number)
print(is_valid, formatted)      # 輸出結果應該為True和格式化後的卡號







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_35.py

# ch16_35.py
import re

def clean_text(text):
    # 刪除不可列印字元和特殊符號, 只保留字母、數字和空格
    pattern = r"[^\w\s]"
    cleaned_text = re.sub(pattern, "", text)
    return cleaned_text

dirty_data = "Name: John Doe; Age: 30; %Salary: $5000"
print(clean_text(dirty_data))
# 輸出: Name John Doe Age 30 Salary 5000



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_4.py

# ch16_4.py
import re

msg1 = 'Please call my secretary using 0930-919-919 or 0952-001-001'
msg2 = '請明天17:30和我一起參加明志科大教師節晚餐'
msg3 = '請明天17:30和我一起參加明志科大教師節晚餐, 可用0933-080-080聯絡我'

def parseString(string):
    """解析字串是否含有電話號碼"""
    pattern = r'\d\d\d\d-\d\d\d-\d\d\d'
    phoneNum = re.findall(pattern, string)
    if phoneNum != None:        # 如果phoneNum不是None表示取得號碼
        print(f"電話號碼是: {phoneNum}")
    else:
        print(f"{string} 字串不含電話號碼")

parseString(msg1)
parseString(msg2)
parseString(msg3)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_5.py

# ch16_5.py
import re

msg1 = 'Please call my secretary using 0930-919-919 or 0952-001-001'
msg2 = '請明天17:30和我一起參加明志科大教師節晚餐'
msg3 = '請明天17:30和我一起參加明志科大教師節晚餐, 可用0933-080-080聯絡我'

def parseString(string):
    """解析字串是否含有電話號碼"""
    pattern = r'\d{4}-\d{3}-\d{3}'
    phoneNum = re.findall(pattern, string)   # 用串列傳回搜尋結果
    print(f"電話號碼是: {phoneNum}")         # 串列方式顯示電話號碼

parseString(msg1)
parseString(msg2)
parseString(msg3)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_6.py

# ch16_6.py
import re

msg = 'Please call my secretary using 02-26669999'
pattern = r'(\d{2})-(\d{8})'
phoneNum = re.search(pattern, msg)           # 傳回搜尋結果

print(f"完整號碼是: {phoneNum.group()}")     # 顯示完整號碼
print(f"完整號碼是: {phoneNum.group(0)}")    # 顯示完整號碼
print(f"區域號碼是: {phoneNum.group(1)}")    # 顯示區域號碼
print(f"電話號碼是: {phoneNum.group(2)}")    # 顯示電話號碼




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_7.py

# ch16_7.py
import re

msg = 'Please call my secretary using 02-26669999 or 02-11112222'
pattern = r'(\d{2})-(\d{8})'
phoneNum = re.findall(pattern, msg)           # 傳回搜尋結果
print(phoneNum)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_8.py

# ch16_8.py
import re

msg = 'Please call my secretary using 02-26669999'
pattern = r'(\d{2})-(\d{8})'
phoneNum = re.search(pattern, msg)      # 傳回搜尋結果
areaNum, localNum = phoneNum.groups()   # 留意是groups()
print(f"區域號碼是: {areaNum}")         # 顯示區域號碼
print(f"電話號碼是: {localNum}")        # 顯示電話號碼




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_9.py

# ch16_9.py
import re

msg = 'Please call my secretary using (02)-26669999'
pattern = r'(\(\d{2}\))-(\d{8})'
phoneNum = re.search(pattern, msg)       # 傳回搜尋結果
areaNum, localNum = phoneNum.groups()    # 留意是groups()
print(f"區域號碼是: {areaNum}")          # 顯示區域號碼
print(f"電話號碼是: {localNum}")         # 顯示電話號碼




print("------------------------------------------------------------")  # 60個


