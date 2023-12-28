import os
import sys
import time
import random


print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_1.py

# ch11_1.py
def greeting( ):
    """我的第一個Python函數設計"""
    print("Python歡迎你")
    print("祝福學習順利")
    print("謝謝")

# 以下的程式碼也可稱主程式
greeting( )
greeting( )
greeting( )
greeting( )
greeting( )


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_2.py

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
print("Python歡迎你")
print("祝福學習順利")
print("謝謝")
print("Python歡迎你")
print("祝福學習順利")
print("謝謝")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_3.py

# ch11_3.py
def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi,", name, "Good Morning!")
greeting('Nelson')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_3_1.py

# ch11_3_1.py
def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi, " + name + " Good Morning!")
greeting('Nelson')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_4.py

# ch11_4.py
def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi, " + name + " Good Morning!")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_5.py

# ch11_5.py
def subtract(x1, x2):
    """ 減法設計 """
    result = x1 - x2
    print(result)               # 輸出減法結果
print("本程式會執行 a - b 的運算")     
a = int(input("a = "))
b = int(input("b = "))
print("a - b = ", end="")       # 輸出a-b字串,接下來輸出不跳行
subtract(a, b)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_6.py

# ch11_6.py
def interest(interest_type, subject):
    """ 顯示興趣和主題 """
    print("我的興趣是 " + interest_type )
    print("在 " + interest_type + " 中, 最喜歡的是 " + subject)
    print( )

interest('旅遊', '敦煌')
interest('程式設計', 'Python')




    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_7.py

# ch11_7.py
def interest(interest_type, subject):
    """ 顯示興趣和主題 """
    print("我的興趣是 " + interest_type )
    print("在 " + interest_type + " 中, 最喜歡的是 " + subject)
    print( )

interest(interest_type = '旅遊', subject = '敦煌')  # 位置正確
interest(subject = '敦煌', interest_type = '旅遊')  # 位置更動




    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_8.py

# ch11_8.py
def interest(interest_type, subject = '敦煌'):
    """ 顯示興趣和主題 """
    print("我的興趣是 " + interest_type )
    print("在 " + interest_type + " 中, 最喜歡的是 " + subject)
    print( )

interest('旅遊')                                     # 傳遞一個參數
interest(interest_type = '旅遊')                     # 傳遞一個參數
interest('旅遊', '張家界')                           # 傳遞二個參數
interest(interest_type = '旅遊', subject = '張家界') # 傳遞二個參數
interest(subject = '張家界', interest_type = '旅遊') # 傳遞二個參數
interest('閱讀', '旅遊類')                # 傳遞二個參數,不同的主題




    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_9.py

# ch11_9.py
def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi, ", name, " Good Morning!")
ret_value = greeting('Nelson')
print("greeting( )傳回值 = ", ret_value)
print(ret_value, " 的 type  = ", type(ret_value))




print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_10.py

# ch11_10.py
def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi, ", name, " Good Morning!")
    return                      # Python將自動回傳None
ret_value = greeting('Nelson')
print("greeting( )傳回值 = ", ret_value)
print(ret_value, " 的 type  = ", type(ret_value))




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_11.py

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

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_12.py

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

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_13.py

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

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_14.py

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

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_15.py

# ch11_15.py
def guest_info(firstname, lastname, gender, middlename = ''):
    """ 整合客戶名字資料 """
    if gender == "M":
        welcome = lastname + middlename + firstname + '先生歡迎你'
    else:
        welcome = lastname + middlename + firstname + '小姐歡迎妳'
    return welcome

info1 = guest_info('濤', '劉', 'M')
info2 = guest_info('雨', '洪', 'F', '冰')
print(info1)
print(info2)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_16.py

# ch11_16.py
def build_vip(id, name):
    """ 建立VIP資訊 """
    vip_dict = {'VIP_ID':id, 'Name':name}
    return vip_dict

member = build_vip('101', 'Nelson')
print(member)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_17.py

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

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_18.py

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

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_19.py

# ch11_19
def product_msg(customers):
    str1 = '親愛的: '
    str2 = '本公司將在2020年12月20日北京舉行產品發表會'
    str3 = '總經理:深石敬上'
    for customer in customers:
        msg = str1 + customer + '\n' + str2 + '\n' + str3
        print(msg, '\n')

members = ['Damon', 'Peter', 'Mary']
product_msg(members)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_20.py

# ch11_20.py
def kitchen(unserved, served):
    """ 將未服務的餐點轉為已經服務 """
    print("廚房處理顧客所點的餐點")
    while unserved:
        current_meal = unserved.pop( )
        # 模擬出餐點過程
        print("菜單: ", current_meal)
        # 將已出餐點轉入已經服務串列
        served.append(current_meal)

def show_unserved_meal(unserved):
    """ 顯示尚未服務的餐點 """
    print("=== 下列是尚未服務的餐點 ===")
    if not unserved:
        print("*** 沒有餐點 ***", "\n")
    for unserved_meal in unserved:
        print(unserved_meal)
        
def show_served_meal(served):
    """ 顯示已經服務的餐點 """
    print("=== 下列是已經服務的餐點 ===")
    if not served:
        print("*** 沒有餐點 ***", "\n")
    for served_meal in served:
        print(served_meal)

unserved = ['大麥克', '勁辣雞腿堡', '麥克雞塊']   # 所點餐點
served = []                                       # 已服務餐點

# 列出餐廳處理前的點餐內容
show_unserved_meal(unserved)                      # 列出未服務餐點
show_served_meal(served)                          # 列出已服務餐點

# 餐廳服務過程
kitchen(unserved, served)                         # 餐廳處理過程
print("\n", "=== 廚房處理結束 ===", "\n")

# 列出餐廳處理後的點餐內容
show_unserved_meal(unserved)                      # 列出未服務餐點
show_served_meal(served)                          # 列出已服務餐點


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_21.py

# ch11_21.py
def kitchen(unserved, served):
    """ 將未服務的餐點轉為已經服務 """
    print("廚房處理顧客所點的餐點")
    while unserved:
        current_meal = unserved.pop( )
        # 模擬出餐點過程
        print("菜單: ", current_meal)
        # 將已出餐點轉入已經服務串列
        served.append(current_meal)

def show_unserved_meal(unserved):
    """ 顯示尚未服務的餐點 """
    print("=== 下列是尚未服務的餐點 ===")
    if not unserved:
        print("*** 沒有餐點 ***", "\n")
    for unserved_meal in unserved:
        print(unserved_meal)
        
def show_served_meal(served):
    """ 顯示已經服務的餐點 """
    print("=== 下列是已經服務的餐點 ===")
    if not served:
        print("*** 沒有餐點 ***", "\n")
    for served_meal in served:
        print(served_meal)

order_list = ['大麥克', '勁辣雞腿堡', '麥克雞塊']   # 所點餐點
served_list = []                                    # 已服務餐點

# 列出餐廳處理前的點餐內容
show_unserved_meal(order_list)                      # 列出未服務餐點
show_served_meal(served_list)                       # 列出已服務餐點

# 餐廳服務過程
kitchen(order_list, served_list)                    # 餐廳處理過程
print("\n", "=== 廚房處理結束 ===", "\n")

# 列出餐廳處理後的點餐內容
show_unserved_meal(order_list)                      # 列出未服務餐點
show_served_meal(served_list)                       # 列出已服務餐點


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_22.py

# ch11_22.py
def kitchen(unserved, served):
    """ 將所點的餐點轉為已經服務 """
    print("廚房處理顧客所點的餐點")
    while unserved:
        current_meal = unserved.pop( )
        # 模擬出餐點過程
        print("菜單: ", current_meal)
        # 將已出餐點轉入已經服務串列
        served.append(current_meal)

def show_order_meal(unserved):
    """ 顯示所點的餐點 """
    print("=== 下列是所點的餐點 ===")
    if not unserved:
        print("*** 沒有餐點 ***", "\n")
    for unserved_meal in unserved:
        print(unserved_meal)
        
def show_served_meal(served):
    """ 顯示已經服務的餐點 """
    print("=== 下列是已經服務的餐點 ===")
    if not served:
        print("*** 沒有餐點 ***", "\n")
    for served_meal in served:
        print(served_meal)

order_list = ['大麥克', '勁辣雞腿堡', '麥克雞塊']   # 所點餐點
served_list = []                                    # 已服務餐點

# 列出餐廳處理前的點餐內容
show_order_meal(order_list)                         # 列出所點的餐點
show_served_meal(served_list)                       # 列出已服務餐點

# 餐廳服務過程
kitchen(order_list[:], served_list)                 # 餐廳處理過程
print("\n", "=== 廚房處理結束 ===", "\n")

# 列出餐廳處理後的點餐內容
show_order_meal(order_list)                         # 列出所點的餐點
show_served_meal(served_list)                       # 列出已服務餐點


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_23.py

# ch11_23.py
def make_icecream(*toppings):
    # 列出製作冰淇淋的配料
    print("這個冰淇淋所加配料如下")
    for topping in toppings:
        print("--- ", topping)

make_icecream('草莓醬')
make_icecream('草莓醬', '葡萄乾', '巧克力碎片')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_24.py

# ch11_24.py
def make_icecream(icecream_type, *toppings):
    # 列出製作冰淇淋的配料
    print("這個 ", icecream_type, " 冰淇淋所加配料如下")
    for topping in toppings:
        print("--- ", topping)

make_icecream('香草', '草莓醬')
make_icecream('芒果', '草莓醬', '葡萄乾', '巧克力碎片')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_25.py

# ch11_25.py
def build_dict(name, age, **players):
    # 建立NBA球員的字典資料
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

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_26.py

# ch11_26.py
def factorial(n):
    # 計算n的階乘, n 必須是正整數
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))

value = 3
print(value, " 的階乘結果是 = ", factorial(value))
value = 5
print(value, " 的階乘結果是 = ", factorial(value))


    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_27.py

# ch11_27.py
def printmsg( ):
    # 函數本身沒有定義變數, 只有執行列印全域變數功能
    print("函數列印: ", msg)    # 列印全域變數

msg = 'Global Variable'         # 設定全域變數
print("主程式列印: ", msg)      # 列印全域變數
printmsg( )                     # 呼叫函數



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_28.py

# ch11_28.py
def printmsg( ):
    # 函數本身有定義變數, 將執行列印區域變數功能
    msg = 'Local Variable'      # 設定區域變數
    print("函數列印: ", msg)    # 列印區域變數

msg = 'Global Variable'         # 這是全域變數
print("主程式列印: ", msg)      # 列印全域變數
printmsg( )                     # 呼叫函數



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_29.py

# ch11_29.py
def defmsg( ):
    msg = 'pringmsg variable'

def printmsg( ):
    print(msg)      # 列印defmsg( )函數定義的區域變數

printmsg( )         # 呼叫printmsg( )




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_30.py

# ch11_30.py
def defmsg( ):
    msg = 'pringmsg variable'

print(msg)         # 主程式列印區域變數產生錯誤




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_30_1.py

# ch11_30_1.py
def printmsg():
    print("列印全域變數: ", msg)
    msg = "Java"        # 嘗試更改全域變數造成錯誤
    print("更改後: ", msg)
msg = "Python"
printmsg()




   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_30_2.py

# ch11_30_2.py
def printmsg():
    global msg
    msg = "Java"        # 更改全域變數
    print("更改後: ", msg)
msg = "Python"
print("更改前: ", msg)
printmsg()




   


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_31.py

# ch11_31.py
# 定義lambda函數
square = lambda x: x ** 2

# 輸出平方值
print(square(10))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_32.py

# ch11_32.py
# 使用一般函數
def square(x):
    value = x ** 2
    return value

# 輸出平方值
print(square(10))




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_33.py

# ch11_33.py
# 定義lambda函數
product = lambda x, y: x * y

# 輸出相乘結果
print(product(5, 10))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_34.py

# ch11_34.py
def oddfn(x):
    return x if (x % 2 == 1) else None

mylist = [5, 10, 15, 20, 25, 30]
filter_object = filter(oddfn, mylist)     # 傳回filter object

# 輸出奇數串列
print("奇數串列: ",[item for item in filter_object])





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_35.py

# ch11_35.py
def oddfn(x):
    return x if (x % 2 == 1) else None

mylist = [5, 10, 15, 20, 25, 30]
filter_object = filter(oddfn, mylist)     # 傳回filter object
oddlist = [item for item in filter_object]
# 輸出奇數串列
print("奇數串列: ",oddlist)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_36.py

# ch11_36.py
mylist = [5, 10, 15, 20, 25, 30]

oddlist = list(filter(lambda x: (x % 2 == 1), mylist))

# 輸出奇數串列
print("奇數串列: ",oddlist)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_37.py

# ch11_37.py
mylist = [5, 10, 15, 20, 25, 30]

squarelist = list(map(lambda x: x ** 2, mylist))

# 輸出串列元素的平方值
print("串列的平方值: ",squarelist)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_38.py

# ch11_38.py
def fun(arg):
    pass


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch11\ch11_39.py

# ch11_39.py
def fun(arg):
    pass

print("列出fun的type類型   :      ", type(fun))
print("列出lambda的type類型:      ", type(lambda x:x))
print("列出內建函數abs的type類型: ", type(abs))



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
