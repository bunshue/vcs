"""
準備清除
#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch8\ch8_9.py

# ch8_9.py


準備撈出

class bank  class Banks():

def

import traceback




"""

import sys

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

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

math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
both1 = math & physics
print("同時參加數學與物理夏令營的成員 ",both1)
both2 = math.intersection(physics)
print("同時參加數學與物理夏令營的成員 ",both2)

print("------------------------------------------------------------")  # 60個

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

A = {1, 2, 3, 4, 5}                     # 定義集合A
B = {3, 4, 5, 6, 7}                     # 定義集合B
C = {1, 2, 3, 4, 5}                     # 定義集合C
# 列出A與B集合是否相等                              
print("A與B集合相等", A == B)
# 列出A與C集合是否相等                             
print("A與C集合相等", A == C)

print("------------------------------------------------------------")  # 60個

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

def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi, ", name, " Good Morning!")
    return      # Python自動回傳 None
ret_value = greeting('Nelson')
print(f"greeting()傳回值 = {ret_value}")
print(f"{ret_value} 的 type  = {type(ret_value)}")

print("------------------------------------------------------------")  # 60個

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

def build_vip(id, name):
    """ 建立VIP資訊 """
    vip_dict = {'VIP_ID':id, 'Name':name}
    return vip_dict

member = build_vip('101', 'Nelson')
print(member)

print("------------------------------------------------------------")  # 60個

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

def mydata(n):
    print("副程式 id(n) = : ", id(n), "\t", n)
    n = 5
    print("副程式 id(n) = : ", id(n), "\t", n)

x = 1
print("主程式 id(x) = : ", id(x), "\t", x)
mydata(x)
print("主程式 id(x) = : ", id(x), "\t", x)

print("------------------------------------------------------------")  # 60個

def mydata(n):
    print(f"函  數 id(n) = :  {id(n)} \t {n}")
    n[0] = 5
    print(f"函  數 id(n) = :  {id(n)} \t {n}")

x = [1, 2]
print("主程式 id(x) = : ", id(x), "\t", x)
mydata(x)
print("主程式 id(x) = : ", id(x), "\t", x)

print("------------------------------------------------------------")  # 60個

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

def function_with_args(*args):
    """ 不定長度參數的函數 """
    #print(type(args))
    #print(args)
    print("使用的參數如下 : ", end = "")
    for arg in args:
        print(arg, end = " ")
    print()

help(function_with_args)
function_with_args()
function_with_args('AAA')
function_with_args('AAA', 'BBB')
function_with_args('AAA', 'BBB', 'CCC')
function_with_args('AAA', 'BBB', 'CCC', 'DDD')
function_with_args('AAA', 'BBB', 'CCC', 'DDD', 'EEE')
function_with_args('AAA', 'BBB', 'CCC', 'DDD', 'EEE', 'FFF')
function_with_args('AAA', 'BBB', 'CCC', 'DDD', 'EEE', 'FFF', 'GGG')

print("------------------------------------------------------------")  # 60個

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

def total(data):
    return sum(data)

x = (1,5,10)
myList = [min, max, sum, total]
for f in myList:
    print(f)

print("------------------------------------------------------------")  # 60個

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

"""
def total(data):
    return sum(data)

x = (1,5,10)
myList = [min, max, sum, total]
for f in myList:
    print(f, f(x))
"""

print("------------------------------------------------------------")  # 60個

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

def mysum(*args):
    return sum(args)

def run_with_multiple_args(func, *args):
    return func(*args)

print(run_with_multiple_args(mysum,1,2,3,4,5))
print(run_with_multiple_args(mysum,6,7,8,9))

print("------------------------------------------------------------")  # 60個

def dist(x1,y1,x2,y2):          # 計算2點之距離函數
    def mySqrt(z):              # 計算開根號值
        return z ** 0.5
    dx = (x1 - x2) ** 2
    dy = (y1 - y2) ** 2
    return mySqrt(dx+dy)

print(dist(0,0,1,1))

print("------------------------------------------------------------")  # 60個

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

def outer():
    b = 10                  # inner所使用的變數值
    def inner(x):
        return 5 * x + b    # 引用第3列的b
    return inner

b = 2
f = outer()
print(f(b))

print("------------------------------------------------------------")  # 60個

def outer(a, b):
    # a 和 b 將是inner()的環境變數
    def inner(x):
        return a * x + b    
    return inner

f1 = outer(1, 2)
f2 = outer(3, 4)
print(f1(1), f2(3))

print("------------------------------------------------------------")  # 60個

def lazy_evaluation(expression):
    def evaluate():
        print(f'評估 : {expression}')
        return eval(expression)
    return evaluate

lazy_sum = lazy_evaluation('1 + 2 + 3 + 4')     # 這裡不會立即計算總和

result = lazy_sum()                             # 這裡將計算並返回總和
print(result)                               

print("------------------------------------------------------------")  # 60個

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

def printmsg( ):
    """ 函數本身沒有定義變數, 只有執行列印全域變數功能 """
    print("函數列印: ", msg)    # 列印全域變數

msg = 'Global Variable'         # 設定全域變數
print("主程式列印: ", msg)      # 列印全域變數
printmsg( )                     # 呼叫函數

print("------------------------------------------------------------")  # 60個

def printmsg( ):
    """ 函數本身有定義變數, 將執行列印區域變數功能 """
    msg = 'Local Variable'      # 設定區域變數
    print("函數列印: ", msg)    # 列印區域變數

msg = 'Global Variable'         # 這是全域變數
print("主程式列印: ", msg)      # 列印全域變數
printmsg( )                     # 呼叫函數

print("------------------------------------------------------------")  # 60個

def printmsg():
    global msg
    msg = "Java"        # 更改全域變數
    print(f"函數列印  :更改後: {msg}")
msg = "Python"
print(f"主程式列印:更改前: {msg}")
printmsg()
print(f"主程式列印:更改後: {msg}")

print("------------------------------------------------------------")  # 60個

def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi,", name, "Good Morning!")
greeting('Nelson')

print("------------------------------------------------------------")  # 60個

def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi, " + name + " Good Morning!")
greeting('Nelson')

print("------------------------------------------------------------")  # 60個

def printlocal():
    lang = "Java"
    print(f"語言 : {lang}")
    print(f"區域變數 : {locals()}")
msg = "Python"
printlocal()
print(f"語言 : {msg}")
print(f"全域變數 : {globals()}")

print("------------------------------------------------------------")  # 60個

# 使用一般函數
def square(x):
    value = x ** 2
    return value

# 輸出平方值
print(square(10))

print("------------------------------------------------------------")  # 60個

# 定義lambda函數
square = lambda x: x ** 2

# 輸出平方值
print(square(10))

print("------------------------------------------------------------")  # 60個

# 定義lambda函數
product = lambda x, y: x * y

# 輸出相乘結果
print(product(5, 10))

print("------------------------------------------------------------")  # 60個

def func(b):
    return lambda x : 2 * x + b 

linear  = func(5)       # 5將傳給lambda的 b
print(linear(10))       # 10是lambda的 x

print("------------------------------------------------------------")  # 60個

def func(b):
    return lambda x : 2 * x + b 

linear  = func(5)       # 5將傳給lambda的 b
print(linear(10))       # 10是lambda的 x

linear2 = func(3)
print(linear2(10))

print("------------------------------------------------------------")  # 60個

def mycar(cars,func):
    for car in cars:
        print(func(car))
def wdcar(carbrand):
    return "My dream car is " + carbrand.title()
    
dreamcars = ['porsche','rolls royce','maserati']
mycar(dreamcars, wdcar)

print("------------------------------------------------------------")  # 60個

def mycar(cars,func):
    for car in cars:
        print(func(car))
    
dreamcars = ['porsche','rolls royce','maserati']
mycar(dreamcars, lambda carbrand:"My dream car is " + carbrand.title())

print("------------------------------------------------------------")  # 60個

def oddfn(x):
    return x if (x % 2 == 1) else None

mylist = [5, 10, 15, 20, 25, 30]
filter_object = filter(oddfn, mylist)     # 傳回filter object

# 輸出奇數串列
print("奇數串列: ",[item for item in filter_object])

print("------------------------------------------------------------")  # 60個

def oddfn(x):
    return x if (x % 2 == 1) else None

mylist = [5, 10, 15, 20, 25, 30]
filter_object = filter(oddfn, mylist)     # 傳回filter object
oddlist = [item for item in filter_object]
# 輸出奇數串列
print("奇數串列: ",oddlist)

print("------------------------------------------------------------")  # 60個

mylist = [5, 10, 15, 20, 25, 30]

oddlist = list(filter(lambda x: (x % 2 == 1), mylist))

# 輸出奇數串列
print("奇數串列: ",oddlist)

print("------------------------------------------------------------")  # 60個

mylist = [5, 10, 15, 20, 25, 30]

squarelist = list(map(lambda x: x ** 2, mylist))

# 輸出串列元素的平方值
print("串列的平方值: ",squarelist)

print("------------------------------------------------------------")  # 60個

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

from functools import reduce
def strToInt(s):
    def charToNum(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(lambda x,y:10*x+y, map(charToNum,s))

string = '5487'
x = strToInt(string) + 10
print("x = ", x)

print("------------------------------------------------------------")  # 60個

str_len = lambda x:len(x)
strs = ['abc', 'ab', 'abcde']
strs.sort(key = str_len)
print(strs)

print("------------------------------------------------------------")  # 60個

strs = ['abc', 'ab', 'abcde']
strs.sort(key = lambda x:len(x))
print(strs)

print("------------------------------------------------------------")  # 60個

sc = [['John', 80],['Tom', 90], ['Kevin', 77]]
sc.sort(key = lambda x:x[1])
print(sc)

print("------------------------------------------------------------")  # 60個

sc = [['John', 80],['Tom', 90], ['Kevin', 77]]
newsc = sorted(sc, key = lambda x:x[1])
print(newsc)

print("------------------------------------------------------------")  # 60個

sc = {'John':80, 'Tom':90, 'Kevin':77}
newsc1 = sorted(sc.items(), key = lambda x:x[0])  # 依照key排序
print("依照人名排序")
print(newsc1)

newsc2 = sorted(sc.items(), key = lambda x:x[1])  # 依照value排序
print("依照分數排序")
print(newsc2)

print("------------------------------------------------------------")  # 60個

def fun(arg):
    pass

print("列出fun的type類型   :      ", type(fun))
print("列出lambda的type類型:      ", type(lambda x:x))
print("列出內建函數abs的type類型: ", type(abs))

print("------------------------------------------------------------")  # 60個

def myRange(start=0, stop=100, step=1):
    n = start
    while n < stop:
        yield n
        n += step

print(type(myRange))
for x in myRange(0,5):
    print(x)

print("------------------------------------------------------------")  # 60個

# 創建一個簡單的串列
my_list = [1, 3, 5]

# 建立串列的迭代器
my_iterator = iter(my_list)

# 使用 next() 函數遍歷迭代器並列印元素
print(next(my_iterator))  
print(next(my_iterator))  
print(next(my_iterator))  

print("------------------------------------------------------------")  # 60個

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

def list_square(n):
    mylist = []
    for data in range(1, n+1):
        mylist.append(data ** 2)
    return mylist

print(list_square(5))

print("------------------------------------------------------------")  # 60個

def iter_square(n):
    for data in range(1, n+1):
        yield data ** 2
    
myiter = iter_square(5)     # 建立迭代器
for data in myiter:
    print(data)

print("------------------------------------------------------------")  # 60個

list_square = [n ** 2 for n in range(1, 6)]
print(list_square)

print("------------------------------------------------------------")  # 60個

list_square = (n ** 2 for n in range(1, 6))
for data in list_square:
    print(data)

print("------------------------------------------------------------")  # 60個

def myRange(start=0, stop=100, step=1):
    n = start
    while n < stop:
        yield n
        n += step

print(type(myRange))
for x in myRange(0,5):
    print(x)

print("------------------------------------------------------------")  # 60個

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

def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi, " + name + " Good Morning!")

print("------------------------------------------------------------")  # 60個

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

def gcd(n1, n2):
    g = 1                               # 最初化最大公約數
    n = 2                               # 從2開始檢測
    while n <= n1 and n <= n2:
        if n1 % n == 0 and n2 % n == 0:
            g = n                       # 新最大公約數
        n += 1
    return g

n1, n2 = 1233, 2477
print("最大公約數是 : ", gcd(n1,n2))

print("------------------------------------------------------------")  # 60個

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a

a, b = 1233,2477
print("最大公約數是 : ", gcd(a, b))

print("------------------------------------------------------------")  # 60個

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

a, b = 1233,2477
print("最大公約數是 : ", gcd(a, b))

print("------------------------------------------------------------")  # 60個

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

a, b = 1233,2477
print("最大公約數是 : ", gcd(a, b))
print("最小公倍數是 : ", lcm(a, b))

print("------------------------------------------------------------")  # 60個

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

def interest(interest_type, subject):
    """ 顯示興趣和主題 """
    print("我的興趣是 " + interest_type )
    print("在 " + interest_type + " 中, 最喜歡的是 " + subject)
    print()

interest('旅遊', '敦煌')
interest('程式設計', 'Python')

print("------------------------------------------------------------")  # 60個

def interest(interest_type, subject):
    """ 顯示興趣和主題 """
    print(f"我的興趣是 {interest_type}")
    print(f"在 {interest_type} 中, 最喜歡的是 {subject}")
    print()

interest(interest_type='旅遊', subject='敦煌')  # 位置正確
interest(subject='敦煌', interest_type='旅遊')  # 位置更動

print("------------------------------------------------------------")  # 60個

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

def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi, ", name, " Good Morning!")
    
ret_value = greeting('Nelson')
print(f"greeting()傳回值 = {ret_value}")
print(f"{ret_value} 的 type  = {type(ret_value)}")

print("------------------------------------------------------------")  # 60個

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

class Person():
    def interest(self):
        print("Smiling is my interest")

hung = Person()
hung.interest()

print("------------------------------------------------------------")  # 60個

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

def getMax(x, y):
    """文件字串實例
建議x, y是整數
這個函數將傳回較大值"""
    if int(x) > int(y):
        return x
    else:
        return y

print(getMax(2, 3))         # 列印較大值
print(getMax.__doc__)       # 列印文件字串docstring

print("------------------------------------------------------------")  # 60個

class Myclass:
    """文件字串實例
Myclass類別的應用"""
    def __init__(self, x):
        self.x = x
    def printMe(self):
        """文字檔字串實例
Myclass類別內printMe方法的應用"""
        print("Hi", self.x)

data = Myclass(100)
data.printMe()
print(data.__doc__)             # 列印Myclass文件字串docstring
print(data.printMe.__doc__)     # 列印printMe文件字串docstring

print("------------------------------------------------------------")  # 60個

print('ch12_24.py module name = ', __name__)

print("------------------------------------------------------------")  # 60個

def myFun():
    print("__name__ == __main__")

myFun()

print("------------------------------------------------------------")  # 60個

class Name:
    def __init__(self, name):
        self.name = name

a = Name('Hung')
print(a)

print("------------------------------------------------------------")  # 60個

class Name:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"{self.name}"

a = Name('Hung')
print(a)

print("------------------------------------------------------------")  # 60個

class Name:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"{self.name}"
    __repr__ = __str__

a = Name('Hung')
print(a)

print("------------------------------------------------------------")  # 60個

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

class Score():
    def __init__(self, score):
        self.score = score

stu = Score(50)
print(stu.score)
stu.score = 100             
print(stu.score)

print("------------------------------------------------------------")  # 60個

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

class Square():
    def __init__(self, sideLen):
        self.__sideLen = sideLen
    @property
    def area(self):
        return self.__sideLen ** 2
    
obj = Square(10)
print(obj.area)

print("------------------------------------------------------------")  # 60個

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

fn = 'data15_4.txt'             # 設定欲開啟的檔案
try:
    with open(fn) as file_Obj:  # 預設mode=r開啟檔案
        data = file_Obj.read()  # 讀取檔案到變數data
except FileNotFoundError:
    print(f"找不到 {fn} 檔案")
else:
    print(data)                 # 輸出變數data
   

print("------------------------------------------------------------")  # 60個

fn = 'data15_5.txt'             # 設定欲開啟的檔案
try:
    with open(fn) as file_Obj:  # 用預設mode=r開啟檔案
        data = file_Obj.read()  # 讀取檔案到變數data
except FileNotFoundError:
    print("找不到 %s 檔案" % fn)
else:
    print(data)                 # 輸出變數data

print("------------------------------------------------------------")  # 60個

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

import sys

print("------------------------------------------------------------")  # 60個

x1 = 1
x2 = 11
x3 = 111
x4 = 1111
print("x= ", str(x1).rjust(4))
print("x= ", str(x2).rjust(4))
print("x= ", str(x3).rjust(4))
print("x= ", str(x4).rjust(4))

print("------------------------------------------------------------")  # 60個

x1 = 1
x2 = 11
x3 = 111
x4 = 1111
print("x= ", str(x1).rjust(4), end="\r", flush=True)
print("x= ", str(x2).rjust(4), end="\r", flush=True)
print("x= ", str(x3).rjust(4), end="\r", flush=True)
print("x= ", str(x4).rjust(4), end="\r", flush=True)

print("------------------------------------------------------------")  # 60個

""" error
from twilio.rest import Client

# 你從twilio.com申請的帳號
accountSid='AC6fdc3efffd15cabcdee8b361e9d4e67'
# 你從twilio.com獲得的圖騰
authToken='9a6dfab51a342a480e7cf9c1f88d3e638'

client = Client(accountSid, authToken)
message = client.messages.create (
            from_ = "+12512548607",         # 這是twilio.com給你的號碼
            to = "+886952000000",           # 這是收簡訊方的號碼
            body = "Python王者歸來" )       # 發送的訊息
"""
print("------------------------------------------------------------")  # 60個

""" input
import sys
print("請輸入字串, 輸入完按Enter = ", end = "")
msg = sys.stdin.readline()
print(msg)

print("------------------------------------------------------------")  # 60個

import sys
print("請輸入字串, 輸入完按Enter = ", end = "")
msg = sys.stdin.readline(8)         # 讀8個字
print(msg)
"""

print("------------------------------------------------------------")  # 60個

import sys
sys.stdout.write("I like Python")

print("------------------------------------------------------------")  # 60個

import sys
for dirpath in sys.path:
    print(dirpath)

print("------------------------------------------------------------")  # 60個

import sys
print("命令列參數 : ", sys.argv)

print("------------------------------------------------------------")  # 60個

import sys

from pprint import pprint
print("使用print")
print(sys.path)
print("使用pprint")
pprint(sys.path)

print("------------------------------------------------------------")  # 60個

import string

def encrypt(text, encryDict):           # 加密文件
    cipher = []
    for i in text:                      # 執行每個字元加密
        v = encryDict[i]                # 加密
        cipher.append(v)                # 加密結果
    return ''.join(cipher)              # 將串列轉成字串
    
abc = string.printable[:-5]             # 取消不可列印字元
subText = abc[-3:] + abc[:-3]           # 加密字串
encry_dict = dict(zip(subText, abc))    # 建立字典
print("列印編碼字典\n", encry_dict)     # 列印字典

msg = 'If the implementation is easy to explain, it may be a good idea.'
ciphertext = encrypt(msg, encry_dict)

print("原始字串 ", msg)
print("加密字串 ", ciphertext)

print("------------------------------------------------------------")  # 60個

import sys
def wordsNum(filename):
    """適用英文文件, 輸入文章的檔案名稱,可以計算此文章的字數"""
    try:
        with open(filename) as file_Obj:  # 用預設"r"傳回檔案物件file_Obj
            data = file_Obj.read()  # 讀取檔案到變數data
    except FileNotFoundError:
        print("找不到 %s 檔案" % filename)
    else:
        wordList = data.split()     # 將文章轉成串列
        print(filename, " 文章的字數是 ", len(wordList))    # 列印文章字數

"""
files = []
for i in range(5):
    filename = input("請輸入檔案名稱 : ")
    files.append(filename)
    
for file in files:
    wordsNum(file)
"""

print("------------------------------------------------------------")  # 60個

def wordsNum(filename):
    """適用英文文件, 輸入文章的檔案名稱,可以計算此文章的字數"""
    try:
        with open(filename) as file_Obj:  # 用預設"r"傳回檔案物件file_Obj
            data = file_Obj.read()  # 讀取檔案到變數data
    except FileNotFoundError:
        print("找不到 %s 檔案" % filename)
    else:
        wordList = data.split()     # 將文章轉成串列
        print(filename, " 文章的字數是 ", len(wordList))    # 列印文章字數
        return len(wordList)

def lenWord(filename):
    """檢查檔案長度必須是10到35個字元"""
    wdlen = wordsNum(filename)                              # 檔案長度
    if wdlen < 10:                                    # 檔案長度不足            
        raise Exception('檔案長度不足')
    if wdlen > 35:                                    # 檔案長度太長
        raise Exception('檔案長度太長')
    print('檔案長度正確')

for file in ("data/d1.txt","data/d2.txt","data/d3.txt","data/d4.txt","data/d5.txt"):  # 測試系列檔案
    try:
        lenWord(file)
    except Exception as err:
        print("檔案長度檢查異常發生: ", str(err))

print("------------------------------------------------------------")  # 60個

import re

msg = """txt@deepwisdom.comyyy.twkkk,
         ser@deepmind.com.tw,
         hung@gmail.com
         aaa@gmail.comcomkk,
         kkk@gmail.com,
         abc@aa,
         service@deepwidsom.com
         mymail@yahoo.com
         de1988@kkk
         abcdefg"""
pattern = r"""(
    [a-zA-Z0-9_.]+                  # 使用者帳號
    @                               # @符號
    [a-zA-Z0-9-.]+                  # 主機域名domain
    [\.]                            # .符號
    [a-zA-Z]{2,4}\b                 # 可能是com或edu或其它
    ([\.])?                         # .符號, 也可能無特別是美國
    ([a-zA-Z]{2,4}\b)?              # 國別
    )"""
eMail = re.findall(pattern, msg, re.VERBOSE)     # 傳回搜尋結果
for mail in eMail:
    print(mail[0])

print("------------------------------------------------------------")  # 60個

import webbrowser

address = "花蓮市中正路"
webbrowser.open('http://www.google.com.tw/maps/place/' + address)

print("------------------------------------------------------------")  # 60個

import bs4, requests
"""
url = 'http://www.taiwanlottery.com.tw'
html = requests.get(url)

objSoup = bs4.BeautifulSoup(html.text, 'lxml')      # 建立BeautifulSoup物件

dataTag = objSoup.select('.contents_box02')         # 尋找class是contents_box02
        
# 找尋開出順序與大小順序的球
balls = dataTag[2].find_all('div', {'class':'ball_tx ball_yellow'})
print("開出順序 : ", end='')
for i in range(6):                                  # 前6球是開出順序
    print(balls[i].text, end='   ')

print("\n大小順序 : ", end='')
for i in range(6,len(balls)):                       # 第7球以後是大小順序
    print(balls[i].text, end='   ')

# 找出第二區的紅球                   
redball = dataTag[2].find_all('div', {'class':'ball_red'})
print("\n特別號   :", redball[0].text)

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
import time

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
url = 'https://www.wikipedia.org/'
browser.get(url)                    # 網頁下載至瀏覽器

txtBox = browser.find_element_by_id('searchInput')
txtBox.send_keys('Artificial Intelligence')          # 輸入表單資料
time.sleep(5)                       # 暫停5秒
txtBox.submit()                     # 送出表單

print("------------------------------------------------------------")  # 60個

from twilio.rest import Client

# 你從twilio.com申請的帳號
accountSid='AC308f91e9dc748a01538feb9d74ed993a'
# 你從twilio.com獲得的圖騰
authToken='f513161b63f71720f62118e4d33ca8ac'

client = Client(accountSid, authToken)
message = client.messages.create (
            from_ = "+15052070000",         # 這是twilio.com給你的號碼
            to = "+886952xxxxxx",           # 填上老師的號碼
            body = "感謝老師,我們學會了Python" )   # 發送的訊息

print("------------------------------------------------------------")  # 60個

import smtplib
from email.mime.text import MIMEText

from_addr = 'cshung1961@gmail.com'              # 設定發信帳號
pwd = input('請輸入 %s 的密碼 : ' % from_addr)  # 要求輸入發信帳號密碼
to_addr_list = ['cshung@deepwisdom.com.tw', 'jiinkwei@me.com']   # 設定收件人

with open('ex26_2.txt', 'rb') as filename:         # 讀取檔案內容
    mailContent = filename.read()
msg = MIMEText(mailContent, 'base64', 'utf-8')
msg['Content-Type'] = 'application/octet-stream'
msg['Content-Disposition'] = 'attachment; filename="ex26_2.txt"'
msg['Subject'] = '傳送Python學習心得附加檔案'
msg['From'] = '學生'
msg['To'] = 'cshung@deepwisdom.com.tw'
msg['Cc'] = 'jiinkwei@me.com'

mySMTP = smtplib.SMTP('smtp.gmail.com', 587)    # 執行連線
mySMTP.ehlo()                                   # 啟動對話
mySMTP.starttls()                               # 執行TLS加密               
mySMTP.login(from_addr, pwd)                    # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg.as_string())  # 執行發送信件
if status == {}:                                # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()                                   # 結束連線


print("------------------------------------------------------------")  # 60個
"""



print("------------------------------------------------------------")  # 60個

code1 = '洪'
print('洪')
print(hex(ord(code1)))     # 輸出字元'洪'的Unicode(16進位)碼值
code2 = '錦'
print('錦')
print(hex(ord(code2)))     # 輸出字元'錦'的Unicode(16進位)碼值
code3 = '魁'
print('魁')
print(hex(ord(code3)))     # 輸出字元'魁'的Unicode(16進位)碼值


print("------------------------------------------------------------")  # 60個

print(" 姓名    國文    英文    總分    平均")
print("%3s  %4d    %4d    %4d     %3.1f" % ("洪冰儒", 98, 90, 188, 188/2))
print("%3s  %4d    %4d    %4d     %3.1f" % ("洪雨星", 96, 95, 191, 191/2))
print("%3s  %4d    %4d    %4d     %3.1f" % ("洪冰雨", 92, 88, 180, 180/2))
print("%3s  %4d    %4d    %4d     %3.1f" % ("洪星宇", 93, 97, 190, 190/2))

print("------------------------------------------------------------")  # 60個

wd = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
print("下列是Python之禪內文")
print(wd)
print("以分行符號將Python 之禪的行資料變成串列元素")
songlist = wd.split('\n')
print(songlist)

print("------------------------------------------------------------")  # 60個

abc = 'abcdefghijklmnopqrstuvwxyz'
front5 = abc[:5]
end21 = abc[5:]
subText = end21 + front5
print("abc     = ", abc)
print("subText = ", subText)

print("------------------------------------------------------------")  # 60個

cities = ['Taipei','Beijing','Tokyo','Chicago','Nanjing']
print(cities)
cities.append('London')
print(cities)
cities.insert(3,'Xian')
print(cities)
cities.remove('Tokyo')
print(cities)

print("------------------------------------------------------------")  # 60個

sc = [['洪錦魁', 80, 95, 88, 0, 0],
      ['洪冰儒', 98, 97, 96, 0, 0],
      ['洪雨星', 91, 93, 95, 0, 0],
      ['洪冰雨', 92, 94, 90, 0, 0],
      ['洪星宇', 92, 97, 90, 0, 0],
     ]      
sc[0][4] = sum(sc[0][1:4])
sc[1][4] = sum(sc[1][1:4])
sc[2][4] = sum(sc[2][1:4])
sc[3][4] = sum(sc[3][1:4])
sc[4][4] = sum(sc[4][1:4])
sc[0][5] = round((sc[0][4] / 3), 1)
sc[1][5] = round((sc[1][4] / 3), 1)
sc[2][5] = round((sc[2][4] / 3), 1)
sc[3][5] = round((sc[3][4] / 3), 1) 
sc[4][5] = round((sc[4][4] / 3), 1) 
print(sc[0])   
print(sc[1])
print(sc[2])
print(sc[3])
print(sc[4])

print("------------------------------------------------------------")  # 60個

#網址
site = 'https://www.grenade.tw/blog/how-to-use-the-python-financial-analysis-visualization-module-mplfinance/'
if site.startswith("http://") or site.startswith("https://"):
    print("網址格式正確")
else:
    print("網址格式錯誤")

print("------------------------------------------------------------")  # 60個

n = 10
for i in range(1,n):
    for j in range(1,n-i+1):
        print(j, end='')
    print()

print("------------------------------------------------------------")  # 60個

fruits1 = ['蘋果', '香蕉', '西瓜', '水蜜桃', '百香果']
fruits2 = ['香蕉', '芭樂', '西瓜']
print("目前fruits2串列 : ", fruits2)
for fruit in fruits2[:]:
    if fruit in fruits1:
        fruits2.remove(fruit)
        print(f"刪除 {fruit}")
print("最後fruits2串列 : ", fruits2)

print("------------------------------------------------------------")  # 60個

title = "9 * 9 Multiplication Table"
print("%s" % title.center(40))
for i in range(1,10):
    print(f"{i:4d}", end='')
print()                                 # 跳列輸出
for i in range(40):
    print("=", end='')                  # 列印分隔符號
print()                                 # 跳列輸出
for i in range(1, 10):
    print(i, '|', end='')
    for j in range(1, 10):
        print(f"{i*j:4d}", end='')      # 列印乘法值
    print()                             # 跳列輸出

print("------------------------------------------------------------")  # 60個

names = ['洪錦魁','洪冰儒','東霞','大成']
lastname = []
for name in names:
    if name.startswith('洪'):    # 是否姓氏洪開頭
        lastname.append(name)    # 加入串列
print(lastname)

print("------------------------------------------------------------")  # 60個

sc = [[1, '洪錦魁', 80, 95, 88, 0, 0, 0],
      [2, '洪冰儒', 98, 97, 96, 0, 0, 0],
      [3, '洪雨星', 91, 93, 95, 0, 0, 0],
      [4, '洪冰雨', 92, 94, 90, 0, 0, 0],
      [5, '洪星宇', 92, 97, 90, 0, 0, 0],
     ]
# 計算總分與平均
print("原始成績單")
for i in range(len(sc)):
    print(sc[i])
    sc[i][5] = sum(sc[i][2:5])              # 填入總分
    sc[i][6] = round((sc[i][5] / 3), 1)     # 填入平均
sc.sort(key=lambda x:x[5],reverse=True)     # 依據總分高往低排序
# 以下填入名次
for i in range(len(sc)):                    # 填入名次
    sc[i][7] = i + 1
# 以下修正相同成績應該有相同名次
for i in range((len(sc)-1)):
    if sc[i][5] == sc[i+1][5]:              # 如果成績相同
        sc[i+1][7] = sc[i][7]               # 名次應該相同
# 以下依座號排序
sc.sort(key=lambda x:x[0])                  # 依據座號排序
print("最後成績單")
for i in range(len(sc)):
    print(sc[i])

print("------------------------------------------------------------")  # 60個

weight = 50              
increase = 1.2
n = 5
for i in range(int(n)):
    weight += increase
    print(f"第 {i+1} 年體重 : {weight:4.1f}")

print("------------------------------------------------------------")  # 60個

fahrenheit = [32, 77, 104]
celsius = [(x - 32) * 5 / 9 for x in fahrenheit]
print(celsius)

print("------------------------------------------------------------")  # 60個

n1 = [1,2,3,4,5]
n2 = [1,2,3,4,5]
result = [[x, y] for x in n1 for y in n2]
print(result)

print("------------------------------------------------------------")  # 60個

bookclub = ['John','Peter','Curry','Mike','Kevin']
print("讀書會成員")
for people in bookclub:
    print(people)
bookclub[0] = 'Johnnason'
for people in bookclub:
    print(people)

print("------------------------------------------------------------")  # 60個

tp = (1,2,3,4,5,2,3,1,4)
lst = list(tp)
newlst = []
for i in lst:
    if i not in newlst:
        newlst.append(i)
newtp = tuple(newlst)
print("新的元組內容 : ", newtp)    

print("------------------------------------------------------------")  # 60個

weatherH = (30, 28, 29, 31, 33, 35, 32)
weatherL = (20, 21, 19, 22, 23, 24, 20)
print(f"過去一周的最高溫度 {max(weatherH)}")
print(f"過去一周的最低溫度 {min(weatherH)}")

print("過去一周的平均溫度")     
for i in range(len(weatherH)):
    print(f"{((weatherH[i]+weatherL[i])/2):3.1f}  ", end="")

print("------------------------------------------------------------")  # 60個

abc = 'abcdefghijklmnopqrstuvwxyz'
encry_dict = {}
front3 = abc[:3]
end23 = abc[3:]
subText = end23 + front3
encry_dict = dict(zip(subText, abc))    # 建立字典
print("列印編碼字典\n", encry_dict)     # 列印字典

msgTest = 'python'                      # 測試字串
cipher = []
for i in msgTest:                       # 執行每個字元加密
    v = encry_dict[i]                   # 加密
    cipher.append(v)                    # 加密結果
ciphertext = ''.join(cipher)            # 將串列轉成字串

print("原始字串 ", msgTest)
print("加密字串 ", ciphertext)

print("------------------------------------------------------------")  # 60個

season = {'Spring':'春季',
          'Summer':'夏季',
          'Fall':'秋季',
          'Winter':'冬季'}

wd = "Spring"
if wd in season:
    print(wd, " 中文字義是 : ", season[wd])
else:
    print("查無此單字")

print("------------------------------------------------------------")  # 60個

month = {'一月':'January','二月':'February','三月':'March',
         '四月':'April', '五月':'May','六月':'June',
         '七月':'July','八月':'August','九月':'September',
         '十月':'October','十一月':'November','十二月':'December'
        }
         
key = "三月"
if key in month:
    print(month[key])
else:
    print('輸入錯誤')

print("------------------------------------------------------------")  # 60個

noodles = {'牛肉麵':100, '肉絲麵':80, '陽春麵':60,
           '大滷麵':90, '麻醬麵':70}
print(noodles)
for noodle, price in sorted(noodles.items(), key=lambda item:item[1]):
    print(noodle,":",price)

print("------------------------------------------------------------")  # 60個

armys = []                      # 建立小兵空串列
# 建立50個小兵
for soldier_number in range(50):
    soldier = {'tag':'red', 'score':3, 'speed':'slow'}
    armys.append(soldier)
# 列印前3個小兵
print("前3名小兵資料")
for soldier in armys[:3]:
    print(soldier)
# 更改編號36到38的小兵
for soldier in armys[35:38]:
    if soldier['tag'] == 'red':
        soldier['tag'] = 'blue'
        soldier['score'] = 5
        soldier['speed'] = 'medium'
# 列印編號35到40的小兵
print("列印編號35到40小兵資料")
for soldier in armys[34:40]:
    print(soldier)
# 更改編號47到49的小兵
for soldier in armys[47:50]:
    if soldier['tag'] == 'red':
        soldier['tag'] = 'green'
        soldier['score'] = 10
        soldier['speed'] = 'fast'
# 列印編號47到49的小兵
print("列印編號47到49小兵資料")
for soldier in armys[47:50]:
    print(soldier)   

print("------------------------------------------------------------")  # 60個

song = """Are you sleeping, are you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong."""

# 以下是將歌曲大寫字母全部改成小寫
songLower = song.lower()            # 歌曲改為小寫

# 將歌曲的標點符號用空字元取代
for ch in songLower:                
        if ch in ".,?":
            songLower = songLower.replace(ch,'')

# 將歌曲字串轉成串列
songList = songLower.split()        

# 將歌曲串列處理成字典
dict = {wd:songList.count(wd) for wd in songList}
   
maxCount = max(dict.values())       # 出現最多次數
for key, count in dict.items():
    if count == maxCount:
        print(f"字串 {key} 出現最多次共出現 {count} 次")

print("------------------------------------------------------------")  # 60個

A = []
for i in range(1,100,2):
    A.append(i)
B = []
for i in range(0,101,5):
    B.append(i)
aSet = set(A)                   # 將串列A轉成集合aSet
bSet = set(B)                   # 將串列B轉成集合bSet

unionAB = aSet | bSet
print("聯集 : ", unionAB)
interAB = aSet & bSet
print("交集 : ", interAB)
A_B = aSet - bSet
print("A-B差集 : ", A_B)
B_A = bSet - aSet
print("B-A差集 : ", B_A)

print("------------------------------------------------------------")  # 60個

A = []
for i in range(1,100,2):
    A.append(i)

num = 2
B = []
primeNum = 0
while num < 100:
    if num == 2:                                # 2是質數所以直接輸出
        B.append(num)
        primeNum += 1
    else:
        for n in range(2, num):                 # 用2 .. num-1當除數測試
            if num % n == 0:                    # 如果整除則不是質數
                break                           # 離開迴圈
        else:                                   # 否則是質數
            primeNum += 1
            B.append(num)
    num += 1

aSet = set(A)                                   # 將串列A轉成集合aSet
bSet = set(B)                                   # 將串列B轉成集合bSet

unionAB = aSet | bSet
print("聯集 : ", unionAB)
interAB = aSet & bSet
print("交集 : ", interAB)
A_B = aSet - bSet
print("A-B差集 : ", A_B)
B_A = bSet - aSet
print("B-A差集 : ", B_A)
AsdB = aSet ^ bSet
print("AB對稱差集 : ", AsdB)

print("------------------------------------------------------------")  # 60個

aSet = {i for i in range(1,100,2)}
bSet = {i for i in range(0,101,5)}

unionAB = aSet | bSet
print("聯集 : ", unionAB)
interAB = aSet & bSet
print("交集 : ", interAB)
A_B = aSet - bSet
print("A-B差集 : ", A_B)
B_A = bSet - aSet
print("B-A差集 : ", B_A)

print("------------------------------------------------------------")  # 60個

def mysum(nLst):
    if nLst == []:
        return 0
    return nLst[0] + mysum(nLst[1:])

data = [5, 7, 9, 15, 21, 6]
print(f'mysum = {mysum(data)}')

print("------------------------------------------------------------")  # 60個

def fun(n):
    if n == 1:
        return 1.0 / 2
    else:
        return fun(n - 1) + (n * 1.0) / (n + 1)

n = 100
for i in range(1, n + 1):
    print(f"{i} = {fun(i):5.3f}")           

print("------------------------------------------------------------")  # 60個

mylist = [5, 10, 15, 20, 25, 30]

evenlist = list(filter(lambda x: (x % 2 == 0), mylist))

# 輸出偶數串列
print("偶數串列: ",evenlist)

print("------------------------------------------------------------")  # 60個

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
def italic(func):               # 加斜體字串裝飾器
    def wrapper(args):
        return 'italic' + func(args) + 'italic'
    return wrapper
@italic
@bold                           # 設定加粗體字串裝飾器
@upper                          # 設定大寫裝飾器
def greeting(string):           # 問候函數
    return string

print(greeting('Hello! iPhone'))

print("------------------------------------------------------------")  # 60個

def factorial(n):
    """ 計算n的階乘, n 必須是正整數 """
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))

#輸入城市的個數
N = 10
times = 10000000000000          # 電腦每秒可處理數列數目
day_secs = 60 * 60 * 24         # 一天秒數
year_secs = 365 * day_secs      # 一年秒數
combinations = factorial(N)     # 組合方式
years = combinations / (times * year_secs)
print(f"城市個數 {N}, 路徑組合數 = {combinations}")
print(f"需要 {years} 年才可以獲得結果")

print("------------------------------------------------------------")  # 60個

def guest_info(firstname, middlename, lastname, gender):
    """ 整合客戶名字資料 """
    if gender == "M":
        welcome = 'Mr. ' + firstname + middlename + lastname + 'Welcome'
    else:
        welcome = 'Miss ' + firstname + middlename + lastname + 'Welcome'
    return welcome

info1 = guest_info('Ivan ', 'Carl ', 'Hung ', 'M')
info2 = guest_info('Mary ', 'Ice ', 'Hung ', 'F')
print(info1)
print(info2)

print("------------------------------------------------------------")  # 60個

def pi(n):
    p = 0
    for i in range(1,n+1, 1):
        p += 4 *((-1)**(i+1)/(2*i-1))
    return p

print("  i      PI ")
print("================")
for i in range(1, 10000, 1000):
    print("%5d   %7.5f" % (i, pi(i)))

print("------------------------------------------------------------")  # 60個

class Myschool():
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def msg(self):
        print("Hi!" + self.name.title() + "你的成績是" + str(self.score) + "分")

A = Myschool("kevin",80)
A.msg()

print("------------------------------------------------------------")  # 60個

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

class Birds(Animals):
    """Birds類別, 這是Animal的衍生類別 """
    def __init__(self, bird_name, bird_age):
        super().__init__('My pet ' + bird_name.title(), bird_age)
    def run(self):
        print(self.name.title(), "is flying")

mycat = Animals('lucy', 5)      # 建立Animals物件以及測試
print(mycat.name.title(), ' is ', mycat.age, " years old.")
mycat.run()

mydog = Dogs('lily', 6)         # 建立Dogs物件以及測試
print(mydog.name.title(), ' is ', mydog.age, " years old.")
mydog.run()
        
mybird = Birds('Cici', 8)       # 建立Birds物件以及測試
print(mybird.name.title(), ' is ', mybird.age, " years old.")
mybird.run()      

print("------------------------------------------------------------")  # 60個

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

class Aunt(Grandfather):
    """ 定義阿姨類別 """
    def action2(self):      # 定義action2()
        print("Aunt")
        
class Ivan(Father, Uncle, Aunt):
    """ 定義Ivan類別 """
    def action3(self):
        print("Ivan")

ivan = Ivan()
ivan.action3()              # 順序 Ivan
ivan.action2()              # 順序 Ivan -> Father
ivan.action1()              # 順序 Ivan -> Father -> Grandfather

print("------------------------------------------------------------")  # 60個

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

class Aunt(Grandfather):
    """ 定義阿姨類別 """
    def action2(self):      # 定義action2()
        print("Aunt")
        
class Ivan(Father, Uncle, Aunt):
    """ 定義Ivan類別 """
    def action3(self):
        print("Ivan")

ivan = Ivan()
ivan.action3()              # 順序 Ivan
ivan.action2()              # 順序 Ivan -> Father
ivan.action1()              # 順序 Ivan -> Father -> Grandfather

print("------------------------------------------------------------")  # 60個

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

class Aunt(Grandfather):
    """ 定義阿姨類別 """
    def action2(self):      # 定義action2()
        print("Aunt")
        
class Ivan(Uncle, Aunt, Father):
    """ 定義Ivan類別 """
    def action3(self):
        print("Ivan")

ivan = Ivan()
ivan.action3()              # 順序 Ivan
ivan.action2()              # 順序 Ivan -> Father
ivan.action1()              # 順序 Ivan -> Father -> Grandfather

print("------------------------------------------------------------")  # 60個

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

class Aunt(Grandfather):
    """ 定義阿姨類別 """
    def action2(self):      # 定義action2()
        print("Aunt")
        
class Ivan(Aunt, Father, Uncle):
    """ 定義Ivan類別 """
    def action3(self):
        print("Ivan")

ivan = Ivan()
ivan.action3()              # 順序 Ivan
ivan.action2()              # 順序 Ivan -> Father
ivan.action1()              # 順序 Ivan -> Father -> Grandfather

print("------------------------------------------------------------")  # 60個

import sys

print("目前Python版本是:     ", sys.version)
print("目前Python版本是:     ", sys.version_info)
print("目前Python平台是:     ", sys.platform)
print("目前Python視窗版本是: ", sys.getwindowsversion())
print("目前Python可執行檔路徑", sys.executable)

print("------------------------------------------------------------")  # 60個

""" 很多
secretcode = '112299'                                   # 設定密碼
codeNotFound = True                                     # 尚未找到密碼為True
for i1 in range(0, 10):                                 # 第一位數
    if codeNotFound:            # 檢查是否找到沒有找到才會往下執行
        for i2 in range(0, 10):                         # 第二位數
            if codeNotFound:    # 檢查是否找到沒有找到才會往下執行
                for i3 in range(0, 10):                 # 第三位數
                    if codeNotFound:
                        for i4 in range(0, 10):
                            if codeNotFound:
                                for i5 in range(0, 10):
                                    if codeNotFound:
                                        for i6 in range(0, 10):
                                            code = str(i1)+str(i2)+str(i3)+str(i4)+str(i5)+str(i6) # 組成密碼
                                            if code == secretcode:              # 比對密碼
                                                print('Bingo!', code)
                                                codeNotFound = False            # 註明已經比對成功
                                                break
                                            else:
                                                print(code)                     # 列印無效碼
"""
print("------------------------------------------------------------")  # 60個

import threading, time

def wakeUp(mytime,note,job):
    print(job," 開始")
    starttime = int(time.time())
    while int(time.time()) - starttime < mytime:
        pass
    print(note)
    print(job," 結束")
    
print("程式階段1")
threadObj1 = threading.Thread(target=wakeUp,
                args=[30,'買機票去北京','threadJob1'])
threadObj1.start()              # threadObj1執行緒開始工作
time.sleep(1)                   # 主執行緒休息1秒

threadObj2 = threading.Thread(target=wakeUp,
                args=[60,'送花給女友', 'threadJob2'])
threadObj2.start()              # threadObj1執行緒開始工作
time.sleep(1)                   # 主執行緒休息1秒

print("程式階段2,正常工作")

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


