

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch1\ch1_2.py

# ch1_2.py
print('Hello! Python')   # 列印字串


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch1\ch1_3.py

'''
程式實例ch1_3.py
作者:洪錦魁
使用三個單引號當作註解
'''
print("Hello! Python")   


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch1\ch1_3_1.py

"""
程式實例ch1_3_1.py
作者:洪錦魁
使用三個雙引號當作註解
"""
print("Hello! Python")   



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch1\ch1_4.py

"""
程式實例ch1_4.py
作者:洪錦魁
使用三個雙引號當作註解
"""
print("Hello! Python")   



print("------------------------------------------------------------")  # 60個



#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch2\ch2_1.py

# ch2_1.py
hourly_salary = 150
annual_salary = hourly_salary * 8 * 300
monthly_fee = 9000
annual_fee = monthly_fee * 12
annual_savings = annual_salary - annual_fee
print(annual_savings)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch2\ch2_10.py

# ch2_10.py
import inspect

# 輸出內建函數名
builtin_functions = [name for name, obj in inspect.getmembers(__builtins__) if inspect.isbuiltin(obj)]
for function_name in builtin_functions:
    print(function_name)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch2\ch2_2.py

# ch2_2.py
hourly_salary = 150                             # 設定時薪
annual_salary = hourly_salary * 8 * 300         # 計算年薪
monthly_fee = 9000                              # 設定每月花費
annual_fee = monthly_fee * 12                   # 計算每年花費
annual_savings = annual_salary - annual_fee     # 計算每年儲存金額
print(annual_savings)                           # 列出每年儲存金額



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch2\ch2_3.py

# ch2_3.py
a = b = c = 10
x = a + b + c + 12
print(x)
# 續行方法1
y = a +\
    b +\
    c +\
    12
print(y)
# 續行方法2
z = ( a +     # 此處可以加上註解  
      b +
      c +
      12 )
print(z)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch2\ch2_4.py

# ch2_4.py
a = b = c = 10
x = a + b + c + 12
print(x)
# 續行方法1     # PEP 8風格
y = a \
    + b \
    + c \
    + 12
print(y)
# 續行方法2     # PEP 8風格
z = ( a         # 此處可以加上註解  
      + b 
      + c 
      + 12 )
print(z)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch2\ch2_5.py

# ch2_5.py
money = 50000 * (1 + 0.015) ** 5
print("本金和是")
print(money)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch2\ch2_6.py

# ch2_6.py
car = 1000000 * (1 - 0.15) ** 3
print("車輛殘值是")
print(car)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch2\ch2_7.py

# ch2_7.py
PI = 3.14159
r = 5
print("圓面積:單位是平方公分")
area = PI * r * r
print(area)
circumference = 2 * PI * r
print("圓周長:單位是公分")
print(circumference)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch2\ch2_8.py

# ch2_8.py
import math

r = 5
print("圓面積:單位是平方公分") 		
area = math.pi * r * r
print(area)
circumference = 2 * math.pi * r
print("圓周長:單位是公分")
print(circumference)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch2\ch2_9.py

# ch2_9.py
# 輸出內建函數名
builtin_functions = dir(__builtins__)
for function_name in builtin_functions:
    print(function_name)




print("------------------------------------------------------------")  # 60個



#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch3\ch3_1.py

# ch3_1.py
x = 10
print(x)
print(type(x))      # 加法前列出x資料型態
x = x + 5.5
print(x)
print(type(x))      # 加法後列出x資料型態



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch3\ch3_10.py

# ch3_10.py
str1 = '''Silicon Stone Education is an unbiased organization
concentrated on bridging the gap ... '''
print(str1)                     # 字串內有分列符號
str2 = '''Silicon Stone Education is an unbiased organization \
concentrated on bridging the gap ... '''
print(str2)                     # 字串內沒有分列符號
str3 = "Silicon Stone Education is an unbiased organization " \
       "concentrated on bridging the gap ... "
print(str3)                     # 使用\符號
str4 = ("Silicon Stone Education is an unbiased organization "
        "concentrated on bridging the gap ... ")
print(str4)                     # 使用小括號


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch3\ch3_11.py

# ch3_11.py
#以下輸出使用單引號設定的字串，需使用\'
str1 = 'I can\'t stop loving you.'
print(str1)
#以下輸出使用雙引號設定的字串，不需使用\'
str2 = "I can't stop loving you."
print(str2)
#以下輸出有\t和\n字元
str3 = "I \tcan't stop \nloving you."
print(str3)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch3\ch3_12.py

# ch3_12.py
num1 = 222
num2 = 333
num3 = num1 + num2
print("這是數值相加")
print(num3)
str1 = str(num1) + str(num2)
print("強制轉換為字串相加")
print(str1)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch3\ch3_13.py

# ch3_13.py
x1 = "22"
x2 = "33"
x3 = x1 + x2
print("type(x3) = ", type(x3))
print("x3 = ", x3)             # 列印字串相加
x4 = int(x1) + int(x2)
print("type(x4) = ", type(x4))
print("x4 = ", x4)             # 列印整數相加
x5 = '1100'
print("2進位  '1100' = ", int(x5,2))
print("8進位  '22'   = ", int(x1,8))
print("16進位 '22'   = ", int(x1,16))
print("16進位 '5A'   = ", int('5A',16))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch3\ch3_14.py

# ch3_14.py
x1 = "A"
x2 = x1 * 10
print(x2)             # 列印字串乘以整數
x3 = "ABC"
x4 = x3 * 5
print(x4)             # 列印字串乘以整數


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch3\ch3_15.py

# ch3_15.py
str1 = "洪錦魁著作"
str2 = "機器學習基礎微積分王者歸來"
str3 = "Python程式語言王者歸來"
str4 = str1 + "\n" + str2 + "\n" + str3
print(str4)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch3\ch3_16.py

# ch3_16.py
str1 = "Hello!\nPython"
print("不含r字元的輸出")
print(str1)
str2 = r"Hello!\nPython"
print("含r字元的輸出")
print(str2)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch3\ch3_17.py

# ch3_17.py
x1 = 97
x2 = chr(x1)      
print(x2)               # 輸出數值97的字元
x3 = ord(x2)
print(x3)               # 輸出字元x3的Unicode(10進位)碼值
x4 = '魁'
print(hex(ord(x4)))     # 輸出字元'魁'的Unicode(16進位)碼值


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch3\ch3_18.py

# ch3_18.py
dist = 384400                   # 地球到月亮距離
speed = 1225                    # 馬赫速度每小時1225公里
total_hours = dist // speed     # 計算小時數
days = total_hours // 24        # 商 = 計算天數
hours = total_hours % 24        # 餘數 = 計算小時數
print("總共需要天數")
print(days)
print("小時數")
print(hours)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch3\ch3_18_1.py

# ch3_18_1.py
dist = 384400                           # 地球到月亮距離
speed = 1225                            # 馬赫速度每小時1225公里
total_hours = dist // speed             # 計算小時數
days, hours = divmod(total_hours, 24)   # 商和餘數
print("總共需要天數")
print(days)
print("小時數")
print(hours)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch3\ch3_19.py

# ch3_19.py
x1 = 1
y1 = 8
x2 = 3
y2 = 10
dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
print("2點的距離是")
print(dist)








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch3\ch3_2.py

# ch3_2.py
print('2 進位整數運算')
x = 0b1101          # 這是2進位整數
print(x)            # 列出10進位的結果
y = 13              # 這是10進位整數
print(bin(y))       # 列出轉換成2進位的結果
print('8 進位整數運算')
x = 0o57            # 這是8進位整數
print(x)            # 列出10進位的結果
y = 47              # 這是10進位整數
print(oct(y))       # 列出轉換成8進位的結果
print('16 進位整數運算')
x = 0x5D            # 這是16進位整數
print(x)            # 列出10進位的結果
y = 93              # 這是10進位整數
print(hex(y))       # 列出轉換成16進位的結果


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch3\ch3_3.py

# ch3_3.py
x = 10.5
print(x)
print(type(x))      # 加法前列出x資料型態
y = int(x) + 5
print(y)
print(type(y))      # 加法後列出y資料型態



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch3\ch3_4.py

# ch3_4.py
x = 10
print(x)
print(type(x))      # 加法前列出x資料型態
y = float(x) + 10
print(y)
print(type(y))      # 加法後列出y資料型態



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch3\ch3_5.py

# ch3_5.py
x = -10
print("以下輸出abs( )函數的應用")
print('x = ', x)                        # 輸出x變數
print('abs(-10) = ', abs(x))            # 輸出abs(x)
x = 5
y = 3
print("以下輸出pow( )函數的應用")
print('pow(5,3) = ', pow(x, y))         # 輸出pow(x,y)
x = 47.5
print("以下輸出round(x)函數的應用")
print('x = ', x)                        # 輸出x變數
print('round(47.5) = ', round(x))       # 輸出round(x)
x = 48.5
print('x = ', x)                        # 輸出x變數
print('round(48.5) = ', round(x))       # 輸出round(x)
x = 49.5
print('x = ', x)                        # 輸出x變數
print('round(49.5) = ', round(x))       # 輸出round(x)
print("以下輸出round(x,n)函數的應用")
x = 2.15
print('x = ', x)            # 輸出x變數
print('round(2.15,1) = ', round(x,1))   # 輸出round(x,1)
x = 2.25
print('x = ', x)                        # 輸出x變數
print('round(2.25,1) = ', round(x,1))   # 輸出round(x,1)
x = 2.151
print('x = ', x)                        # 輸出x變數
print('round(2.151,1) = ', round(x,1))  # 輸出round(x,1)
x = 2.251
print('x = ', x)                        # 輸出x變數
print('round(2.251,1) = ', round(x,1))  # 輸出round(x,1)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch3\ch3_6.py

# ch3_6.py
x = True
print(x)            # 列出 x 資料
print(int(x))       # 列出強制轉換 int(x)
print(type(x))      # 列出 x 資料型態
y = False
print(y)            # 列出 y 資料
print(int(y))       # 列出強制轉換 int(y)
print(type(y))      # 列出 y 資料型態



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch3\ch3_7.py

# ch3_7.py
xt = True
x = 1 + xt
print(x)
print(type(x))      # 列出x資料型態

yt = False
y = 1 + yt
print(y)
print(type(y))      # 列出y資料型態



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch3\ch3_8.py

# ch3_8.py
x = "Deepwisdom means deepen your wisdom"   # 雙引號設定字串
print(x)
print(type(x))                              # 列出x字串資料型態
y = '深智數位 - Deepen your wisdom'         # 單引號設定字串
print(y)
print(type(y))                              # 列出y字串資料型態



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch3\ch3_9.py

# ch3_9.py
num1 = 222
num2 = 333
num3 = num1 + num2
print("以下是數值相加")
print(num3)
numstr1 = "222"
numstr2 = "333"
numstr3 = numstr1 + numstr2
print("以下是由數值組成的字串相加")
print(numstr3)
numstr4 = numstr1 + " " + numstr2
print("以下是由數值組成的字串相加，同時中間加上一空格")
print(numstr4)
str1 = "Deepmind "
str2 = "Deepen your mind"
str3 = str1 + str2
print("以下是一般字串相加")
print(str3)


print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_1.py

# ch4_1.py
str1 = '明志科技大學'
str2 = '明志工專'
print(str1, str2, sep=" $$$ ")  # 以 $$$ 值位置分隔資料輸出

print(str1, str2, sep="\t")     # 以Tab鍵值位置分隔資料輸出



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_10.py

# ch4_10.py
x = 12345678
print("/%10.1e/" % x)
print("/%10.2E/" % x)
print("/%-10.2E/" % x)
print("/%+10.2E/" % x)
print("="*60)
string = "abcdefg"
print("/%10.3s/" % string)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_11.py

# ch4_11.py
score = 90
name = "洪錦魁"
count = 1
print("{}你的第 {} 次物理考試成績是 {}".format(name, count, score))




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_12.py

# ch4_12.py
score = 90
name = "洪錦魁"
count = 1
string = "{}你的第 {} 次物理考試成績是 {}"
print(string.format(name, count, score))




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_13.py

# ch4_13.py
score = 90
name = "洪錦魁"
count = 1
# 以下鼓勵使用
print("{0}你的第 {1} 次物理考試成績是 {2}".format(name,count,score))

# 以下語法對但不鼓勵使用
print("{2}你的第 {1} 次物理考試成績是 {0}".format(score,count,name))



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_14.py

# ch4_14.py
print("{n}你的第 {c} 次物理考試成績是 {s}".format(n="洪錦魁",c=1,s=90))



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_15.py

# ch4_15.py
r = 5
PI = 3.14159
area = PI * r ** 2
print("/半徑{0:3d}圓面積是{1:10.2f}/".format(r,area))






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_16.py

# ch4_16.py
r = 5
PI = 3.14159
area = PI * r ** 2
print("/半徑{0:3d}圓面積是{1:10.2f}/".format(r,area))
print("/半徑{0:>3d}圓面積是{1:>10.2f}/".format(r,area))
print("/半徑{0:<3d}圓面積是{1:<10.2f}/".format(r,area))
print("/半徑{0:^3d}圓面積是{1:^10.2f}/".format(r,area))





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_17.py

# ch4_17.py
title = "南極旅遊講座"
print("/{0:*^20s}/".format(title))







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_18.py

# ch4_18.py
url = "https://maps.apis.com/json?city="
city = "taipei"
r = 1000
type = "school"
print(url + city + '&radius=' + str(r) + '&type=' + type)
print(url + "{}&radius={}&type={}".format(city, r, type))



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_19.py

# ch4_19.py
score = 90
name = "洪錦魁"
count = 1
print(f"{name}你的第 {count} 次物理考試成績是 {score}")




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_2.py

# ch4_2.py
score = 90
name = "洪錦魁"
count = 1
print("%s你的第 %d 次物理考試成績是 %d" % (name, count, score))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_20.py

# ch4_20.py
r = 5
PI = 3.14159
area = PI * r ** 2
print(f"/半徑{r:3d}圓面積是{area:10.2f}/")
print(f"/半徑{r:>3d}圓面積是{area:>10.2f}/")
print(f"/半徑{r:<3d}圓面積是{area:<10.2f}/")
print(f"/半徑{r:^3d}圓面積是{area:^10.2f}/")





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_21.py

# ch4_21.py
name = '洪錦魁'
message = f"我是{name}"
print(message)

url = "https://maps.apis.com/json?city="
city = "taipei"
r = 1000
type = "school"
my_url = url + f"{city}&radius={r}&type={type}"
print(my_url)






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_22.py

# ch4_22.py
name = '洪錦魁'
score = 90.5
print(f"{name = }")
print(f"物理考試 {score = }")
print(f"物理考試 {score = :5.2f}")






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_23.py

# ch4_23.py
sp = " " * 40
print("%s   1231 Delta Rd" % sp)
print("%s   Oxford, Mississippi" % sp)
print("%s   USA\n\n\n" % sp)
print("Dear Ivan")
print("I am pleased to inform you that your application for fall 2025 has")
print("been favorably reviewed by the Electrical and Computer Engineering")
print("Office.\n\n")
print("Best Regards")
print("Peter Malong")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_24.py

# ch4_24.py
fobj1 = open("out24w.txt", mode="w")   # 取代先前資料
print("Testing mode=w, using utf-8 format", file=fobj1)
fobj1.close( )
fobj2 = open("out24a.txt", mode="a")   # 附加資料後面
print("測試 mode=a 參數, 預設 ANSI 編碼", file=fobj2)
fobj2.close( )




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_25.py

# ch4_25.py
fobj1 = open("out25w.txt", mode="w", encoding="utf-8")   
print("Testing mode=w, using utf-8 format", file=fobj1)
fobj1.close( )
fobj2 = open("out25a.txt", mode="a", encoding="cp950")   
print("測試 mode=a 參數, 預設 ANSI 編碼", file=fobj2)
fobj2.close( )




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_26.py

# ch4_26.py
print("歡迎使用成績輸入系統")
name = input("請輸入姓名：")
engh = input("請輸入英文成績：")
math = input("請輸入數學成績：")
total = int(engh) + int(math)
print(f"{name} 你的總分是 {total}")
print("="*60)
print(f"name資料型態是 {type(name)}")
print(f"engh資料型態是 {type(engh)}")


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_27.py

# ch4_27.py
numberStr = input("請輸入數值公式 : ")
number = eval(numberStr)
print(f"計算結果 : {number:5.2f}")




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_28.py

# ch4_28.py
print("歡迎使用成績輸入系統")
name = input("請輸入姓名：")
engh = eval(input("請輸入英文成績："))
math = eval(input("請輸入數學成績："))
total = engh + math
print(f"{name} 你的總分是 {total}")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_29.py

# ch4_29.py
n1, n2, n3 = eval(input("請輸入3個數字："))
average = (n1 + n2 + n3) / 3
print(f"3個數字平均是 {average:6.2f}")




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_3.py

# ch4_3.py
score = 90
name = "洪錦魁"
count = 1
formatstr = "%s你的第 %d 次物理考試成績是 %d"
print(formatstr % (name, count, score))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_30.py

# ch4_30.py
f = input("請輸入華氏溫度：")
c = ( int(f) - 32 ) * 5 / 9
print(f"華氏 {f} 等於攝氏 {c:4.1f}")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_31.py

# ch4_31.py
loan = eval(input("請輸入貸款金額："))
year = eval(input("請輸入年限："))
rate = eval(input("請輸入年利率："))
monthrate = rate / (12*100)             # 改成百分比的月利率

# 計算每月還款金額
molecules = loan * monthrate
denominator = 1 - (1 / (1 + monthrate) ** (year * 12))
monthlyPay = molecules / denominator    # 每月還款金額
totalPay = monthlyPay * year * 12       # 總共還款金額

print(f"每月還款金額 {int(monthlyPay)}")
print(f"總共還款金額 {int(totalPay)}")



           



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_32.py

# ch4_32.py
import math

r = 6371                        # 地球半徑
x1, y1 = 22.2838, 114.1731      # 香港紅磡車站經緯度
x2, y2 = 25.0452, 121.5168      # 台北車站經緯度

d = r*math.acos(math.sin(math.radians(x1))*math.sin(math.radians(x2))+
                math.cos(math.radians(x1))*math.cos(math.radians(x2))*
                math.cos(math.radians(y1-y2)))

print(f"distance = {d:6.1f}")








    


    








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_33.py

# ch4_33.py
h = int(input("請輸入頭的數量："))
f = int(input("請輸入腳的數量："))
chicken = int(2 * h - f / 2)
rabbit = int(f / 2 - h)
print(f'雞有 {chicken} 隻, 兔有 {rabbit} 隻')



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_34.py

# ch4_34.py
starting = 1
ending = 100
d = 1                       # 等差數列的間距
sum = int((starting + ending) * (ending - starting + d) / (2 * d))
print(f'1 到 100的總和是 {sum}')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_4.py

# ch4_4.py
x = 100
print("100的16進位 = %x\n100的 8進位 = %o" % (x, x))



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_5.py

# ch4_5.py
x = 10
print("整數%d \n浮點數%f \n字串%s" % (x, x, x))
y = 9.9
print("整數%d \n浮點數%f \n字串%s" % (y, y, y))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_6.py

# ch4_6.py
x = 100
print("x=/%6d/" % x)
y = 10.5
print("y=/%6.2f/" % y)
s = "Deep"
print("s=/%6s/" % s)
print("以下是保留格數空間不足的實例")
print("x=/%2d/" % x)
print("y=/%3.2f/" % y)
print("s=/%2s/" % s)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_7.py

# ch4_7.py
x = 100
print("x=/%-8d/" % x)
y = 10.5
print("y=/%-8.2f/" % y)
s = "Deep"
print("s=/%-8s/" % s)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_8.py

# ch4_8.py
x = 10
print("x=/%+8d/" % x)
y = 10.5
print("y=/%+8.2f/" % y)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch4\ch4_9.py

# ch4_9.py
print(" 姓名    國文    英文    總分")
print("%3s  %4d    %4d    %4d" % ("洪冰儒", 98, 90, 188))
print("%3s  %4d    %4d    %4d" % ("洪雨星", 96, 95, 191))
print("%3s  %4d    %4d    %4d" % ("洪冰雨", 92, 88, 180))
print("%3s  %4d    %4d    %4d" % ("洪星宇", 93, 97, 190))



print("------------------------------------------------------------")  # 60個




#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch5\ch5_1.py

# ch5_1.py
age = input("請輸入年齡: ")
if (int(age) < 20):
    print("你年齡太小")
    print("需年滿20歲才可以購買菸酒")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch5\ch5_10.py

# ch5_10.py
height = eval(input("請輸入身高(公分)："))
weight = eval(input("請輸入體重(公斤)："))
bmi = weight / (height / 100) ** 2 
if bmi >= 28:
    print(f"體重肥胖")
else:
    print(f"體重不肥胖")








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch5\ch5_11.py

# ch5_11.py
height = eval(input("請輸入身高(公分)："))
weight = eval(input("請輸入體重(公斤)："))
if bmi := weight / ( height / 100) ** 2 >= 28:      # Python 3.8
    print(f"體重肥胖")
else:
    print(f"體重不肥胖")








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch5\ch5_12.py

# ch5_12.py
height = eval(input("請輸入身高(公分)："))
weight = eval(input("請輸入體重(公斤)："))
bmi = weight / (height / 100) ** 2 
if bmi >= 18.5 and bmi < 24:
    print(f"{bmi = :5.2f}體重正常")

else:
    print(f"{bmi = :5.2f}體重不正常")








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch5\ch5_13.py

# ch5_13.py
ans = 0                         # 讀者心中的數字
print("猜數字遊戲,請心中想一個 0 - 7之間的數字, 然後回答問題")

truefalse = "輸入y或Y代表有, 其它代表無 : "
# 檢測2進位的第1位是否含1
q1 = "有沒有看到心中的數字 : \n" + \
     "1, 3, 5, 7 \n"
num = input(q1 + truefalse)
print(num)
if num == "y" or num == "Y":
    ans += 1
# 檢測2進位的第2位是否含1
truefalse = "輸入y或Y代表有, 其它代表無 : "
q2 = "有沒有看到心中的數字 : \n" + \
     "2, 3, 6, 7 \n"
num = input(q2 + truefalse)
if num == "y" or num == "Y":
    ans += 2
# 檢測2進位的第3位是否含1
truefalse = "輸入y或Y代表有, 其它代表無 : "
q3 = "有沒有看到心中的數字 : \n" + \
     "4, 5, 6, 7 \n"
num = input(q3 + truefalse)
if num == "y" or num == "Y":
    ans += 4

print("讀者心中所想的數字是 : ", ans)


    








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch5\ch5_14.py

# ch5_14.py
year = eval(input("請輸入西元出生年 : "))
year -= 1900
zodiac = year % 12
if zodiac == 0:
    print("你是生肖是 : 鼠")
elif zodiac == 1:
    print("你是生肖是 : 牛")
elif zodiac == 2:
    print("你是生肖是 : 虎")
elif zodiac == 3:
    print("你是生肖是 : 兔")
elif zodiac == 4:
    print("你是生肖是 : 龍")
elif zodiac == 5:
    print("你是生肖是 : 蛇")
elif zodiac == 6:
    print("你是生肖是 : 馬")
elif zodiac == 7:
    print("你是生肖是 : 羊")
elif zodiac == 8:
    print("你是生肖是 : 猴")
elif zodiac == 9:
    print("你是生肖是 : 雞")
elif zodiac == 10:
    print("你是生肖是 : 狗")
else:
    print("你是生肖是 : 豬")
                  


    








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch5\ch5_15.py

# ch5_15.py
a = 3
b = 5
c = 1

r1 = (-b + (b**2-4*a*c)**0.5)/(2*a)
r2 = (-b - (b**2-4*a*c)**0.5)/(2*a)
print(f"{r1 = :6.4f},    {r2 = :6.4f}")







    


    








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch5\ch5_16.py

# ch5_16.py
a = 2
b = 3
c = 1
d = -2
e = 13
f = -4

x = (e*d - b*f) / (a*d - b*c)
y = (a*f - e*c) / (a*d - b*c)
print(f"{x = :6.4f},    {y = :6.4f}")







    


    








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch5\ch5_17.py

# ch5_17.py
v = eval(input("請輸入火箭速度 : "))
if (v < 7.9):
    print("人造衛星無法進入太空")
elif (v == 7.9):
    print("人造衛星可以環繞地球作圓形移動")
elif (v > 7.9 and v < 11.2):
    print("人造衛星可以環繞地球作橢圓形移動")
elif (v >= 11.2 and v < 16.7):
    print("人造衛星可以環繞太陽移動")
else:
    print("人造衛星可以脫離太陽系")
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch5\ch5_18.py

# ch5_18.py
print("判斷輸入年份是否潤年")
year = input("請輸入年份: ")
rem4 = int(year) % 4
rem100 = int(year) % 100
rem400 = int(year) % 400
if rem4 == 0:
    if rem100 != 0 or rem400 == 0:
        print(f"{year} 是潤年")
    else:
        print(f"{year} 不是潤年")
else:
    print(f"{year} 不是潤年")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch5\ch5_2.py

# ch5_2.py
print("輸出絕對值")
num = input("請輸入任意整數值: ")
x = int(num)
if (int(x) < 0): x = -x
print(f"絕對值是 {x}")


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch5\ch5_3.py

# ch5_3.py
age = input("請輸入年齡: ")
if (int(age) < 20):
    print("你年齡太小")
    print("需年滿20歲才可以購買菸酒")
else:
    print("歡迎購買菸酒")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch5\ch5_4.py

# ch5_4.py
print("奇數偶數判斷")
num = eval(input("請輸入任意整值: "))
rem = num % 2
if (rem == 0):
    print(f"{num} 是偶數")
else:
    print(f"{num} 是奇數")
# PEP 8
if rem:
    print(f"{num} 是奇數")
else:
    print(f"{num} 是偶數")
# 高手用法
print(f"{num} 是奇數" if rem else f"{num} 是偶數")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch5\ch5_5.py

# ch5_5.py
x, y = eval(input("請輸入2個數字："))
max_ = x if x > y else y
print(f"方法 1 最大值是 : {max_}")
max_ = max(x, y)
print(f"方法 2 最大值是 : {max_}")

min_ = x if x < y else y
print(f"方法 1 最小值是 : {min_}")
min_ = min(x, y)
print(f"方法 2 最小值是 : {min_}")


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch5\ch5_6.py

# ch5_6.py
items = eval(input("請輸入 1 個數字："))
items = 10 if items >= 10 else items
print(items)






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch5\ch5_7.py

# ch5_7.py
print("計算最終成績")
score = input("請輸入分數 : ")
sc = int(score)
if (sc >= 90):
    print(" A")
elif (sc >= 80):
    print(" B")
elif (sc >= 70):
    print(" C")
elif (sc >= 60):
    print(" D")
else:
    print(" F")
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch5\ch5_8.py

# ch5_8.py
print("判斷輸入字元類別")
ch = input("請輸入字元 : ")
if ord(ch) >= ord("A") and ord(ch) <= ord("Z"):
    print("這是大寫字元")
elif ord(ch) >= ord("a") and ord(ch) <= ord("z"):
    print("這是小寫字元")
elif ord(ch) >= ord("0") and ord(ch) <= ord("9"):
    print("這是數字")
else:
    print("這是特殊字元")
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch5\ch5_9.py

# ch5_9.py
flag = None
if not flag:
    print("尚未定義flag")
if flag:
    print("有定義")
else:
    print("尚未定義flag")











print("------------------------------------------------------------")  # 60個



#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_1.py

# ch6_1.py
james = [23, 19, 22, 31, 18]                # 定義james串列
print("列印james串列", james)
James = ['Lebron James',23, 19, 22, 31, 18] # 定義James串列
print("列印James串列", James)
fruits = ['apple', 'banana', 'orange']      # 定義fruits串列
print("列印fruits串列", fruits)
cfruits = ['蘋果', '香蕉', '橘子']          # 定義cfruits串列
print("列印cfruits串列", cfruits)
ielts = [5.5, 6.0, 6.5]                     # 定義IELTS成績串列
print("列印IELTS成績", ielts)
# 列出串列資料型態
print("串列james資料型態是: ",type(james))


    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_10.py

# ch6_10.py
num1 = [1, 3, 5]
num2 = [1, 2, 4, 6]
num3 = num1 + num2  
print(num3)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_11.py

# ch6_11.py
cars = ['Benz', 'BMW', 'Honda']
nums = [1, 3, 5]
carslist = cars * 3           # 串列乘以數字
print(carslist)
numslist = nums * 5           # 串列乘以數字
print(numslist)   



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_12.py

# ch6_12.py
warriors = ['Curry','Durant','Iquodala','Bell','Thompson']
print("2025年初NBA勇士隊主將陣容", warriors)
del warriors[3]                 # 不明原因離隊
print("2025年末NBA勇士隊主將陣容", warriors)
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_13.py

# ch6_13.py
nums1 = [1, 3, 5]
print(f"刪除nums1串列索引1元素前   = {nums1}")
del nums1[1]
print(f"刪除nums1串列索引1元素後   = {nums1}")
nums2 = [1, 2, 3, 4, 5, 6]
print(f"刪除nums2串列索引[0:2]前   = {nums2}")
del nums2[0:2]
print(f"刪除nums2串列索引[0:2]後   = {nums2}")
nums3 = [1, 2, 3, 4, 5, 6]
print(f"刪除nums3串列索引[0:6:2]前 = {nums3}")
del nums3[0:6:2]
print(f"刪除nums3串列索引[0:6:2]後 = {nums3}")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_14.py

# ch6_14.py
cars = ['Toyota', 'Nissan', 'Honda']
print(f"cars串列長度是 = {len(cars)}")
if len(cars) != 0:              # 一般寫法
    del cars[0]
    print("刪除cars串列元素成功")
    print(f"cars串列長度是 = {len(cars)}")
else:
    print("cars串列內沒有元素資料")
nums = []
print(f"nums串列長度是 = {len(nums)}")
if len(nums):                   # 更好的寫法
    del nums[0]
    print("刪除nums串列元素成功")
else:
    print("nums串列內沒有元素資料")


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_15.py

# ch6_15.py
cars = ['bmw', 'benz', 'audi']     
carF = "我開的第一部車是 " + cars[1].title( )
carN = "我現在開的車子是 " + cars[0].upper( )
print(carF)
print(carN)


   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_16.py

# ch6_16.py
strN = " DeepWisdom       "
strL = strN.lstrip( )       # 刪除字串左邊多餘空白
strR = strN.rstrip( )       # 刪除字串右邊多餘空白
strB = strN.strip( )        # 一次刪除頭尾端多餘空白
print(f"/{strN}/")
print(f"/{strL}/")
print(f"/{strR}/")
print(f"/{strB}/")





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_17.py

# ch6_17.py
string = input("請輸入名字 : ")
print("/%s/" % string)
string = input("請輸入名字 : ")
print("/%s/" % string.strip())







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_18.py

# ch6_18.py
name = input("請輸入英文名字 : ")
print(f"/{name}/")
name = input("請輸入英文名字 : ").strip()
print(f"/{name}/")
name = input("請輸入英文名字 : ").strip().title()
print(f"/{name}/")







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_19.py

# ch6_19.py
title = "Ming-Chi Institute of Technology"
print(f"/{title.center(50)}/")
dt = "Department of ME"
print(f"/{dt.ljust(50)}/")
site = "JK Hung"
print(f"/{site.rjust(50)}/")
print(f"/{title.zfill(50)}/")












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_2.py

# ch6_2.py
james = [23, 19, 22, 31, 18]                # 定義james串列
print("列印james第1場得分", james[0])
print("列印james第2場得分", james[1])
print("列印james第3場得分", james[2])
print("列印james第4場得分", james[3])
print("列印james第5場得分", james[4])
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_20.py

# ch6_20.py
cars = []     
print(f"目前串列內容 = {cars}")
cars.append('Honda')
print(f"目前串列內容 = {cars}")
cars.append('Toyota')
print(f"目前串列內容 = {cars}")



    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_21.py

# ch6_21.py
cars = ['Honda','Toyota','Ford']     
print(f"目前串列內容 = {cars}")
print("在索引1位置插入Nissan")
cars.insert(1,'Nissan')
print(f"新的串列內容 = {cars}")
print("在索引0位置插入BMW")
cars.insert(0,'BMW')
print(f"最新串列內容 = {cars}")

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_22.py

# ch6_22.py
cars = ['Honda','Toyota','Ford','BMW']     
print("目前串列內容 = ",cars)
print("使用pop( )刪除串列元素")
popped_car = cars.pop( )          # 刪除串列末端值
print(f"所刪除的串列內容是 : {popped_car}")
print("新的串列內容 = ",cars)
print("使用pop(1)刪除串列元素")
popped_car = cars.pop(1)          # 刪除串列索引為1的值
print(f"所刪除的串列內容是 : {popped_car}")
print("新的串列內容 = ",cars)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_23.py

# ch6_23.py
cars = ['Honda','bmw','Toyota','Ford','bmw']     
print(f"目前串列內容 = {cars}")
print("使用remove( )刪除串列元素")
expensive = 'bmw'
cars.remove(expensive)      # 刪除第一次出現的元素bmw
print(f"所刪除的內容是 : {expensive.upper()} 因為重複了")
print(f"新的串列內容 = {cars}")

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_24.py

# ch6_24.py
cars = ['Honda','bmw','Toyota','Ford','bmw']     
print(f"目前串列內容 = {cars}")
# 直接列印cars[::-1]顛倒排序,不更改串列內容
print(f"列印使用[::-1]顛倒排序\n{cars[::-1]}")
# 更改串列內容
print("使用reverse( )顛倒排序串列元素")
cars.reverse()            # 顛倒排序串列
print(f"新的串列內容 = {cars}")

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_25.py

# ch6_25.py
# 基本排序
numbers = [3, 5, 1, 4, 2]
numbers.sort()
print(numbers)          # 輸出：[1, 2, 3, 4, 5]

# 降序排序
numbers = [3, 5, 1, 4, 2]
numbers.sort(reverse=True)
print(numbers)          # 輸出：[5, 4, 3, 2, 1]

# 使用函數定義排序
words = ["banana", "apple", "strawberry"]
words.sort(key=len)
print(words)            # 輸出：['apple', 'banana', 'strawberry]




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_26.py

# ch6_26.py
# 基本排序
numbers = [3, 5, 1, 4, 2]
sorted_numbers = sorted(numbers)
print(sorted_numbers)       # 輸出：[1, 2, 3, 4, 5]

# 按降序排序
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc)  # 輸出：[5, 4, 3, 2, 1]

# 使用 key 函數排序
words = ["banana", "apple", "strawberry"]
sorted_words = sorted(words, key=len)
print(sorted_words)         # 輸出：['apple', 'banana', 'strawberry]

# 對字串排序
string = "hello"
sorted_chars = sorted(string)
print(sorted_chars)         # 輸出：['e', 'h', 'l', 'l', 'o']



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_27.py

# ch6_27.py
# 在串列中使用 index()
fruits = ["apple", "banana", "cherry", "date"]
index = fruits.index("cherry")
print(index)                    # 輸出：2

# 指定搜索範圍, 搜尋的起始索引是 1
fruits = ["apple", "banana", "cherry", "date", "apple"]
index_range = fruits.index("apple", 1)
print(index_range)              # 輸出：4



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_28.py

# ch6_28.py
James = ['Lebron James',23, 19, 22, 31, 18] # 定義James串列
games = len(James)                          # 求元素數量
score_Max = max(James[1:games])             # 最高得分
i = James.index(score_Max)                  # 場次
print(f"{James[0]} 在第 {i} 場得最高分 {score_Max}")



    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_29.py

# ch6_29.py
# 在串列中使用 count()
fruits = ["apple", "banana", "cherry", "apple", "cherry"]
apple_count = fruits.count("apple")
print(apple_count)                  # 輸出：2

# 在字串中使用 count()
text = "Hello, how are you? How can I help you?"
how_count = text.count("how")
print(how_count)                    # 輸出：1

# 在字串中指定搜索範圍
how_count_range = text.count("how", 0, 15)
print(how_count_range)              # 輸出：1



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_3.py

# ch6_3.py
james = [23, 19, 22, 31, 18]                # 定義james串列
# 傳統設計方式
game1 = james[0]
game2 = james[1]
game3 = james[2]
game4 = james[3]
game5 = james[4]
print("列印james各場次得分", game1, game2, game3, game4, game5)
# Python高手好的設計方式
game1, game2, game3, game4, game5 = james
print("列印james各場次得分", game1, game2, game3, game4, game5)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_30.py

# ch6_30.py
James = [['Lebron James','SF','12/30/84'],23,19,22,31,18] # 定義James串列
games = len(James)                                        # 求元素數量
score_Max = max(James[1:games])                           # 最高得分
i = James.index(score_Max)                                # 場次
name, position, born = James[0]
print("姓名     : ", name)
print("位置     : ", position)
print("出生日期 : ", born)
print(f"在第 {i} 場得最高分 {score_Max}")



    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_31.py

# ch6_31.py
cars1 = ['toyota', 'nissan', 'honda']
cars2 = ['ford', 'audi']
print("原先cars1串列內容 = ", cars1)
print("原先cars2串列內容 = ", cars2)
cars1.append(cars2)
print(f"執行append()後串列cars1內容 = {cars1}")
print(f"執行append()後串列cars2內容 = {cars2}")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_32.py

# ch6_32.py
cars1 = ['toyota', 'nissan', 'honda']
cars2 = ['ford', 'audi']
cars1.extend(cars2)
print(f"執行extend()後串列cars1內容 = {cars1}")
print(f"執行extend()後串列cars2內容 = {cars2}")




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_33.py

# ch6_33.py
sc = [['洪錦魁', 80, 95, 88, 0],
      ['洪冰儒', 98, 97, 96, 0],
     ]
sc[0][4] = sum(sc[0][1:4])
sc[1][4] = sum(sc[1][1:4])
print(sc[0])
print(sc[1])









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_34.py

# ch6_34.py
mysports = ['basketball', 'baseball']
friendsports = mysports
print(f"我喜歡的運動     = {mysports}")
print(f"我朋友喜歡的運動 = {friendsports}")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_35.py

# ch6_35.py
mysports = ['basketball', 'baseball']
friendsports = mysports
print(f"我喜歡的運動     = {mysports}")
print(f"我朋友喜歡的運動 = {friendsports}")
mysports.append('football')
friendsports.append('soccer')
print(f"我喜歡的最新運動     = {mysports}")
print(f"我朋友喜歡的最新運動 = {friendsports}")
                   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_36.py

# ch6_36.py
mysports = ['basketball', 'baseball']
friendsports = mysports
print(f"列出mysports位址     = {id(mysports)}")
print(f"列出friendsports位址 = {id(friendsports)}")
print(f"我喜歡的運動     = {mysports}")
print(f"我朋友喜歡的運動 = {friendsports}")
mysports.append('football')
friendsports.append('soccer')
print(" -- 新增運動項目後 -- ")
print(f"列出mysports位址     = {id(mysports)}")
print(f"列出friendsports位址 = {id(friendsports)}")
print(f"我喜歡的最新運動     = {mysports}")
print(f"我朋友喜歡的最新運動 = {friendsports}")
                   


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_37.py

# ch6_37.py
mysports = ['basketball', 'baseball']
friendsports = mysports[:]
print(f"列出mysports位址     = {id(mysports)}")
print(f"列出friendsports位址 = {id(friendsports)}")
print(f"我喜歡的運動     = {mysports}")
print(f"我朋友喜歡的運動 = {friendsports}")
mysports.append('football')
friendsports.append('soccer')
print(" -- 新增運動項目後 -- ")
print(f"列出mysports位址     = {id(mysports)}")
print(f"列出friendsports位址 = {id(friendsports)}")
print(f"我喜歡的最新運動     = {mysports}")
print(f"我朋友喜歡的最新運動 = {friendsports}")
                   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_37_1.py

# ch6_37_1.py
mysports = ['basketball', 'baseball']
friendsports = mysports.copy()
print(f"列出mysports位址     = {id(mysports)}")
print(f"列出friendsports位址 = {id(friendsports)}")
print(f"我喜歡的運動     = {mysports}")
print(f"我朋友喜歡的運動 = {friendsports}")
mysports.append('football')
friendsports.append('soccer')
print(" -- 新增運動項目後 -- ")
print(f"列出mysports位址     = {id(mysports)}")
print(f"列出friendsports位址 = {id(friendsports)}")
print(f"我喜歡的最新運動     = {mysports}")
print(f"我朋友喜歡的最新運動 = {friendsports}")
                   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_38.py

# ch6_38.py
string = "Abc"
# 正值索引
print(f" {string[0] = }",
      f"\n {string[1] = }",
      f"\n {string[2] = }")
# 負值索引
print(f" {string[-1] = }",
      f"\n {string[-2] = }",
      f"\n {string[-3] = }")
# 多重指定觀念
s1, s2, s3 = string
print(f"多重指定觀念的輸出測試 {s1}{s2}{s3}")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_39.py

# ch6_39.py
string = "Deep Learning"                # 定義字串
print(f"列印string第0-2元素     = {string[0:3]}")
print(f"列印string第1-3元素     = {string[1:4]}")
print(f"列印string第1,3,5元素   = {string[1:6:2]}")
print(f"列印string第1到最後元素 = {string[1:]}")
print(f"列印string前3元素       = {string[0:3]}")
print(f"列印string後3元素       = {string[-3:]}")
print("="*60)     
print(f"列印string第1-3元素     = {'Deep Learning'[1:4]}")

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_4.py

# ch6_4.py
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"串列元素如下 : {x} ")
print(f"x[2:]       = {x[2:]}")
print(f"x[:2]       = {x[:2]}")
print(f"x[0:3]      = {x[0:3]}")
print(f"x[1:4]      = {x[1:4]}")
print(f"x[0:9:2]    = {x[0:9:2]}")
print(f"x[::2]      = {x[::2]}")
print(f"x[2::3]     = {x[2::3]}")
print(f"x[:]        = {x[:]}")
print(f"x[::-1]     = {x[::-1]}")
print(f"x[-3:-7:-1] = {x[-3:-7:-1]}")
print(f"x[-1]       = {x[-1]}")     # 這是取單一元素











 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_40.py

# ch6_40.py
str1 = "Silicon Stone Education"
str2 = "D:\Python\ch6"

sList1 = str1.split()                        # 字串轉成串列
sList2 = str2.split("\\")                    # 字串轉成串列
print(f"{str1} 串列內容是 {sList1}")         # 列印串列
print(f"{str1} 串列字數是 {len(sList1)}")    # 列印字數
print(f"{str2} 串列內容是 {sList2}")         # 列印串列
print(f"{str2} 串列字數是 {len(sList2)}")    # 列印字數




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_41.py

# ch6_41.py
path = ['D:','ch6','ch6_41.py']
connect = '\\'                   # 路徑分隔字元
print(connect.join(path))
connect = '*'                   # 普通字元
print(connect.join(path))












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_42.py

# ch6_42.py
msg = '''CIA Mark told CIA Linda that the secret USB had given to CIA Peter'''
print(f"字串開頭是CIA : {msg.startswith('CIA')}")
print(f"字串結尾是CIA : {msg.endswith('CIA')}")
print(f"CIA出現的次數 : {msg.count('CIA')}")
msg = msg.replace('Linda','Lxx')
print(f"新的msg內容 : {msg}")






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_43.py

# ch6_43.py
fruits = ['apple', 'banana', 'watermelon']
fruit = input("請輸入水果 = ")
if fruit in fruits:
    print("這個水果已經有了")
else:
    fruits.append(fruit)
    print("謝謝提醒已經加入水果清單: ", fruits)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_44.py

# ch6_44.py
# 比較兩個指向相同物件的變數
a = [1, 2, 3]
b = a
print(a is b)               # 輸出: True

# 比較兩個指向不同物件的變數, 即使它們的值相等
c = [1, 2, 3]
print(a is c)               # 輸出: False

# 比較兩個指向不同物件的變數
d = [4, 5, 6]
e = [4, 5, 6]
print(d is not e)           # 輸出: True

# 比較兩個指向相同物件的變數
f = d
print(d is not f)           # 輸出: False



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_45.py

# ch6_45.py
x = 10
y = 10
z = 15
r = 20
print("x = %d, y = %d, z = %d, r = %d" % (x, y, z, r))
print(f"x位址={id(x)}, y位址={id(y)}, z位址={id(z)}, r位址={id(r)}")
r = x                               # r的值將變為10
print(f"{x = }, {y = }, {z = }, {r = }")
print(f"x位址={id(x)}, y位址={id(y)}, z位址={id(z)}, r位址={id(r)}")







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_46.py

# ch6_46.py
x = 10
y = 10
z = 15
r = z - 5
print("is測試")
boolean = x is y
print(f"x位址 = {id(x)}, y位址 = {id(y)}")
print(f"{x = }, {y = }, {boolean}")
boolean = x is z
print(f"x位址 = {id(x)}, z位址 = {id(z)}")
print(f"{x = }, {z = }, {boolean}")
boolean = x is r
print(f"x位址 = {id(x)}, r位址 = {id(r)}")
print(f"{x = }, {r = }, {boolean}")
print("="*60)
print("is not測試")
boolean = x is not y
print(f"x位址 = {id(x)}, y位址 = {id(y)}")
print(f"{x = }, {y = }, {boolean}")
boolean = x is not z
print(f"x位址 = {id(x)}, z位址 = {id(z)}")
print(f"{x = }, {z = }, {boolean}")
boolean = x is not r
print(f"x位址 = {id(x)}, r位址 = {id(r)}")
print(f"{x = }, {r = }, {boolean}")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_47.py

# ch6_47.py
drinks = ["coffee", "tea", "wine"]
enumerate_drinks = enumerate(drinks)               # 數值初始是0
print("轉成串列輸出, 初始索引值是 0 = ",list(enumerate_drinks))

enumerate_drinks = enumerate(drinks, start = 10)   # 數值初始是10
print("轉成串列輸出, 初始索引值是10 = ",list(enumerate_drinks))










          



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_48.py

# ch6_48.py
accounts = []                       # 建立空帳號串列
account = input("請輸入新帳號 = ")
accounts.append(account)            # 將輸入加入帳號串列

print("深智公司系統")
ac = input("請輸入帳號 = ")
if ac in accounts:
    print("歡迎進入深智系統")
else:
    print("帳號錯誤")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_5.py

# ch6_5.py
warriors = ['Curry','Durant','Iquodala','Bell','Thompson']
first3 = warriors[:3]
print("前3名球員",first3)
n_to_last = warriors[1:]
print("球員索引1到最後",n_to_last)
last3 = warriors[-3:]
print("後3名球員",last3)



 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_6.py

# ch6_6.py
james = [23, 19, 22, 31, 18]       # 定義james的得分
print(f"James比賽場次 = {len(james)}")
print(f"最高得分 = {max(james)}")
print(f"最低得分 = {min(james)}")
print(f"得分總計 = {sum(james)}")
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_7.py

# ch6_7.py
James = ['Lebron James', 23, 19, 22, 31, 18]    # 比賽得分
print(f"James比賽場次 = {len(James[1:])}")
print(f"最高得分 = {max(James[1:])}")
print(f"最低得分 = {min(James[1:])}")
print(f"得分總計 = {sum(James[1:])}")

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_8.py

# ch6_8.py
cars = ['Toyota', 'Nissan', 'Honda']
print("舊汽車銷售品牌", cars)
cars[1] = 'Ford'           # 更改第二筆元素內容
print("新汽車銷售品牌", cars)


    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch6\ch6_9.py

# ch6_9.py
cars1 = ['Toyota', 'Nissan', 'Honda']
print("舊汽車銷售品牌", cars1)
cars2 = ['Audi', 'BMW']
cars1 += cars2
print("新汽車銷售品牌", cars1)


    

print("------------------------------------------------------------")  # 60個



#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_1.py

# ch7_1.py
sum = 1+2+3+4+5+6+7+8+9+10
print("總和 = ", sum)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_10.py

# ch7_10.py
n = int(input("請輸入n值 : "))
sum_ = 0    # sum是內建函數, 不適合當作變數, 所以加上 _ 
for num in range(1,n+1):
    sum_ += num
print("總和 = ", sum_)



    



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_11.py

# ch7_11.py
n = int(input("請輸入整數:"))
sum_ = sum(range(n + 1))
print(f"從1到{n}的總和是 = {sum_}")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_12.py

# ch7_12.py
squares = []                     # 建立空串列
n = int(input("請輸入整數:"))
if n > 10 : n = 10               # 最大值是10
for num in range(1, n+1):        
    squares.append(num ** 2)     # 加入串列
print(squares)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_13.py

# ch7_13.py
xlst = []
xlst.append(0)
xlst.append(1)
xlst.append(2)
xlst.append(3)
xlst.append(4)
xlst.append(5)
print(xlst)











print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_14.py

# ch7_14.py
xlst = []
for n in range(6):
    xlst.append(n)
print(xlst)











print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_15.py

# ch7_15.py
xlst = list(range(6))
print(xlst)











print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_16.py

# ch7_16.py
xlst = [ n for n in range(6)]
print(xlst)











print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_17.py

# ch7_17.py
n = int(input("請輸入整數:"))
if n > 10 : n = 10               # 最大值是10
squares = [num ** 2 for num in range(1, n+1)]
print(squares)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_17_1.py

# ch7_17_1.py
celsius = [21, 25, 29]
fahrenheit = [(x * 9 / 5 + 32) for x in celsius]
print(fahrenheit)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_17_2.py

# ch7_17_2.py
x = [[a, b, c] for a in range(1,20) for b in range(a,20) for c in range(b,20)
     if a ** 2 + b ** 2 == c **2]
print(x)








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_17_3.py

# ch7_17_3.py
colors = ["Red","Green","Blue"]
shapes = ["Circle","Square","Line"]
result = [[color,shape] for color in colors for shape in shapes]
print(result)







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_18.py

# ch7_18.py
colors = ["Red", "Green", "Blue"]
shapes = ["Circle", "Square"]
result = [[color, shape] for color in colors for shape in shapes]
for color, shape in result:
    print(color, shape)










print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_18_1.py

# ch7_18_1.py
for x in range(0x2160, 0x216a):
    print(chr(x), end=' ')




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_18_2.py

# ch7_18_2.py
fruits = ['蘋果', '香蕉', '西瓜']
print("目前fruits串列 : ", fruits)

for fruit in fruits[:]:
    fruits.remove(fruit)
    print(f"刪除 {fruit}")
    print("目前fruits串列 : ", fruits)








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_19.py

# ch7_19.py
for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print(f"{i}*{j}={result:<3d}", end=" ")
    print()         # 換列輸出
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_2.py

# ch7_2.py -- 不完整的程式
vipNames = ['James','Linda','Peter', ... , 'Kevin']
print("客戶1 = ", vipNames[0])
print("客戶2 = ", vipNames[1])
print("客戶3 = ", vipNames[2])
...
...
print("客戶1000 = ", vipNames[999])



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_20.py

# ch7_20.py
for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            print("aa", end="")
    print()                # 換列輸出
    


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_21.py

# ch7_21.py
players = ['Curry','Jordan','James','Durant','Obama','Kevin','Lin']
n = int(input("請輸入人數 = "))
if n > len(players) : n = len(players)  # 列出人數不大於串列元素數
index = 0                               # 索引
for player in players:
    if index == n:
        break
    print(player, end=" ")
    index += 1                          # 索引加1


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_22.py

# ch7_22.py
scores = [94, 82, 60, 91, 88, 79, 61, 93, 99, 77]
scores.sort(reverse = True)         # 從大到小排列
count = 0
for sc in scores:
    count += 1
    print(sc, end=" ")
    if count == 5:                  # 取前5名成績
        break                       # 離開for迴圈




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_23.py

# ch7_23.py
scores = [33, 22, 41, 25, 39, 43, 27, 38, 40]
games = 0
for score in scores:
    if score < 30:                  # 小於30則不往下執行
        continue
    games += 1                      # 場次加1              
print(f"有{games}場得分超過30分")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_24.py

# ch7_24.py
players = [['James', 202],
           ['Curry', 193],
           ['Durant', 205],
           ['Jordan', 199],
           ['David', 211]]
for player in players:
    if player[1] < 200:
        continue
    print(player)
    


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_25.py

# ch7_25.py
num = int(input("請輸入大於1的整數做質數測試 = "))
if num == 2:                            # 2是質數所以直接輸出
    print(f"{num}是質數")
else:
    for n in range(2, num):             # 用2 .. num-1當除數測試
        if num % n == 0:                # 如果整除則不是質數
            print(f"{num}不是質數")
            break                       # 離開迴圈
    else:                               # 否則是質數
        print(f"{num}是質數")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_26.py

# ch7_26.py
msg1 = '人機對話專欄,告訴我心事吧,我會重複你告訴我的心事!'
msg2 = '輸入 q 可以結束對話'
msg = msg1 + '\n' + msg2 + '\n' + '= '
input_msg = ''                  # 預設為空字串
while input_msg != 'q':
    input_msg = input(msg)
    if input_msg != 'q':        # 如果輸入不是q才輸出訊息         
        print(input_msg)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_27.py

# ch7_27.py
msg1 = '人機對話專欄,告訴我心事吧,我會重複你告訴我的心事!'
msg2 = '輸入 q 可以結束對話'
msg = msg1 + '\n' + msg2 + '\n' + '= '
active = True
while active:               # 迴圈進行直到active是False
    input_msg = input(msg)
    if input_msg != 'q':    # 如果輸入不是q才輸出訊息         
        print(input_msg)
    else:
        active = False      # 輸入是q所以將active設為False




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_28.py

# ch7_28.py
n = int(input("請輸入一個值 : "))
sum = 0
while n:
    sum += n
    n = int(input("請輸入一個值 : "))
print("輸入總和 = ", sum)






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_29.py

# ch7_29.py
i = 1                   # 設定i初始值
while i <= 9:           # 當i大於9跳出外層迴圈
    j = 1               # 設定j初始值
    while j <= 9:       # 當j大於9跳出內層迴圈
        result = i * j
        print(f"{i}*{j}={result:<3d}", end=" ")
        j += 1          # 內層迴圈加1
    print()             # 換列輸出
    i += 1              # 外層迴圈加1
    




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_3.py

# ch7_3.py
players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama']
for player in players:
    print(player)
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_30.py

# ch7_30.py
msg1 = '人機對話專欄,請告訴我妳喜歡吃的水果!'
msg2 = '輸入 q 可以結束對話'
msg = msg1 + '\n' + msg2 + '\n' + '= '
while True:                     # 這是while無限迴圈
    input_msg = input(msg)
    if input_msg == 'q':        # 輸入q可用break跳出迴圈          
        break
    else:
        print(f"我也喜歡吃 {input_msg.title()}")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_31.py

# ch7_31.py
players = ['Curry','Jordan','James','Durant','Obama','Kevin','Lin']
n = int(input("請輸入人數 = "))
if n > len(players) : n = len(players)  # 列出人數不大於串列元素數
index = 0                               # 索引index
while index < len(players):             # 是否index在串列長度範圍
    if index == n:                      # 是否達到想列出的人數
        break
    print(players[index], end=" ")
    index += 1                          # 索引index加1


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_32.py

# ch7_32.py
index = 0
while index <= 10:
    index += 1
    if index % 2:           # 測試是否奇數
        continue            # 不往下執行
    print(index)            # 輸出偶數
        



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_33.py

# ch7_33.py
fruits = ['apple', 'orange', 'apple', 'banana', 'apple']
fruit = 'apple'
print("刪除前的fruits", fruits)
while fruit in fruits:      # 只要串列內有apple迴圈就繼續
    fruits.remove(fruit)
print("刪除後的fruits", fruits)
    



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_34.py

# ch7_34.py
buyers = [['James', 1030],              # 建立買家購買紀錄
           ['Curry', 893],
           ['Durant', 2050],
           ['Jordan', 990],
           ['David', 2110]]
goldbuyers = []                         # Gold買家串列
vipbuyers =[]                           # VIP買家串列
while buyers:                           # 買家分類完成,迴圈才會結束
    index_buyer = buyers.pop()
    if index_buyer[1] >= 1000:          # 用1000圓執行買家分類條件
        vipbuyers.append(index_buyer)   # 加入VIP買家串列
    else:
        goldbuyers.append(index_buyer)  # 加入Gold買家串列
print("VIP 買家資料", vipbuyers)
print("Gold買家資料", goldbuyers)
    




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_35.py

# ch7_35.py
schools = ['明志科大', '台灣科大', '台北科大']
for school in schools:
    pass



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_36.py

# ch7_36.py
drinks = ["coffee", "tea", "wine"]
# 解析enumerate物件
for drink in enumerate(drinks):             # 數值初始是0
    print(drink)
for count, drink in enumerate(drinks):
    print(count, drink)
print("****************")   
# 解析enumerate物件
for drink in enumerate(drinks, 10):         # 數值初始是10
    print(drink)
for count, drink in enumerate(drinks, 10):
    print(count, drink)










          



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_37.py

# ch7_37.py
scores = [21,29,18,33,12,17,26,28,15,19] 
# 解析enumerate物件
for count, score in enumerate(scores, 1):   # 初始值是 1
    if score >= 20:
        print(f"場次 {count} : 得分 {score}")















          



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_38.py

# ch7_38.py
store = 'DeepMind購物中心'
products = ['電視','冰箱','洗衣機','電扇','冷氣機']
cart = []                       # 購物車
print(store)
print(products,"\n")
while True:                     # 這是while無限迴圈
    msg = input("請輸入購買商品(q=quit) : ")
    if msg == 'q' or msg=='Q':
        break
    else:
        if msg in products:
            cart.append(msg)
print("今天購買商品", cart)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_39.py

# ch7_39.py
sc = [[1, '洪錦魁', 80, 95, 88, 0, 0, 0],
      [2, '洪冰儒', 98, 97, 96, 0, 0, 0],
      [3, '洪雨星', 91, 93, 95, 0, 0, 0],
      [4, '洪冰雨', 92, 94, 90, 0, 0, 0],
      [5, '洪星宇', 92, 97, 80, 0, 0, 0],
     ]
# 計算總分與平均
print("填入總分與平均")
for i in range(len(sc)):
    sc[i][5] = sum(sc[i][2:5])              # 填入總分
    sc[i][6] = round((sc[i][5] / 3), 1)     # 填入平均
    print(sc[i])
sc.sort(key=lambda x:x[5],reverse=True)     # 依據總分高往低排序
# 以下填入名次
print("填入名次")
for i in range(len(sc)):                    # 填入名次
    sc[i][7] = i + 1
    print(sc[i])
# 以下依座號排序
sc.sort(key=lambda x:x[0])                  # 依據座號排序
print("最後成績單")
for i in range(len(sc)):
    print(sc[i])


















print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_4.py

# ch7_4.py
players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama']
for player in players:print(player)
    


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_40.py

# ch7_40.py
sc = [[1, '洪錦魁', 80, 95, 88, 0, 0, 0],
      [2, '洪冰儒', 98, 97, 96, 0, 0, 0],
      [3, '洪雨星', 91, 93, 95, 0, 0, 0],
      [4, '洪冰雨', 92, 94, 90, 0, 0, 0],
      [5, '洪星宇', 92, 97, 90, 0, 0, 0],
     ]
# 計算總分與平均
print("填入總分與平均")
for i in range(len(sc)):
    sc[i][5] = sum(sc[i][2:5])              # 填入總分
    sc[i][6] = round((sc[i][5] / 3), 1)     # 填入平均
    print(sc[i])
sc.sort(key=lambda x:x[5],reverse=True)     # 依據總分高往低排序
# 以下填入名次
print("填入名次")
for i in range(len(sc)):                    # 填入名次
    sc[i][7] = i + 1
    print(sc[i])
# 以下依座號排序
sc.sort(key=lambda x:x[0])                  # 依據座號排序
print("最後成績單")
for i in range(len(sc)):
    print(sc[i])


















print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_41.py

# ch7_41.py
x = 1000000
pi = 0
for i in range(1,x+1):
    pi += 4*((-1)**(i+1) / (2*i-1))
    if i % 100000 == 0:      # 隔100000執行一次
        print(f"當 {i = :7d} 時 PI = {pi:20.19f}")


  













          



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_42.py

# ch7_42.py
chicken = 0
while True:
    rabbit = 35 - chicken                       # 頭的總數
    if 2 * chicken + 4 * rabbit == 100:         # 腳的總數
        print(f'雞有 {chicken} 隻, 兔有 {rabbit} 隻')
        break
    chicken += 1





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_43.py

# ch7_43.py
sum = 0
for i in range(64):
    if i == 0:
        wheat = 1
    else:
        wheat = 2 ** i
    sum += wheat       
print(f'麥粒總共 = {sum}')







        






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_44.py

# ch7_44.py
print("電影院劃位系統")
sc = [[' ', ' 1', ' 2', ' 3', ' 4'],
      ['A', '□','□','□','□'],
      ['B', '■','□','□','□'],
      ['C', '□','■','■','□'],
      ['D', '□','□','□','□'],
     ]
for seatrow in sc:          # 輸出目前座位表
    for seat in seatrow:
        print(seat, end='  ')
    print()
row = input("請輸入 A - D 排 : ")
r = int(row,16) - 9
col = int(input("請輸入 1 - 4 號 : "))
sc[r][col] = '■'
print("="*60)
for seatrow in sc:          # 輸出最後座位表
    for seat in seatrow:
        print(seat, end='  ')
    print()








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_45.py

# ch7_45.py
fib = []
n = 9
fib.append(0)                   # fib[0] = 0
fib.append(1)                   # fib[1] = 1
for i in range(2,n+1):
    f = fib[i-1] + fib[i-2]     # fib[i] = fib[i-1]+fib[i-2]
    fib.append(f)               # 加入費式數列
for i in range(n+1):
    print(fib[i], end=', ')     # 輸出費式數列








    







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_5.py

# ch7_5.py
players = ['curry', 'jordan', 'james', 'durant', 'obama']
for player in players:
    print(f"{player.title()}, it was a great game.")
    print(f"我迫不及待想看下一場比賽 {player.title()}")


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_6.py

# ch7_6.py
players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama']
print("列印前3位球員")
for player in players[:3]:
    print(player)
print("列印後3位球員")
for player in players[-3:]:
    print(player)
    


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_7.py

# ch7_7.py
files = ['da1.c','da2.py','da3.py','da4.java']
py = []
for file in files:
    if file.endswith('.py'):    # 以.py為副檔名
        py.append(file)         # 加入串列
print(py)









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_8.py

# ch7_8.py
n = int(input("請輸入星號數量 : ")) # 定義星號的數量                           
for number in range(n):             # for迴圈    
    print("*",end="")               # 列印星號
    



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_8_1.py

# ch7_8_1.py
n = int(input("請輸入星號數量 : ")) # 定義星號的數量                           
for _ in range(n):                  # for迴圈    
    print("*",end="")               # 列印星號
    



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch7\ch7_9.py

# ch7_9.py
money = 50000
rate = 0.015
n = 5
for i in range(n):
    money *= (1 + rate)
    print(f"第 {i+1} 年本金和 : {int(money)}")





print("------------------------------------------------------------")  # 60個



#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch8\ch8_1.py

# ch8_1.py
numbers1 = (1, 2, 3, 4, 5)      # 定義元組元素是整數
fruits = ('apple', 'orange')    # 定義元組元素是字串
mixed = ('James', 50)           # 定義元組元素是不同型態資料
val_tuple = (10,)               # 只有一個元素的元祖
print(numbers1)
print(fruits)
print(mixed)
print(val_tuple)
# 列出元組資料型態
print("元組mixed資料型態是: ",type(mixed))



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch8\ch8_10.py

# ch8_10.py
keys = ('magic', 'xaab', 9099)      # 定義元組元素是字串與數字
list_keys = list(keys)              # 將元組改為串列
list_keys.append('secret')          # 增加元素
print("列印元組", keys)
print("列印串列", list_keys)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch8\ch8_11.py

# ch8_11.py
keys = ['magic', 'xaab', 9099]      # 定義串列元素是字串與數字
tuple_keys = tuple(keys)            # 將串列改為元組
print("列印串列", keys)
print("列印元組", tuple_keys)
tuple_keys.append('secret')         # 增加元素 --- 錯誤錯誤



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch8\ch8_12.py

# ch8_12.py
tup = (1, 3, 5, 7, 9)
print("tup最大值是", max(tup))
print("tup最小值是", min(tup))



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch8\ch8_13.py

# ch8_13.py
drinks = ["coffee", "tea", "wine"]
enumerate_drinks = enumerate(drinks)                # 數值初始是0
lst = list(enumerate_drinks)
print("轉成串列輸出, 初始索引值是 0 = ", lst)
print(type(lst[0]))



      









          



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch8\ch8_14.py

# ch8_14.py
drinks = ("coffee", "tea", "wine")
enumerate_drinks = enumerate(drinks)                # 數值初始是0
print("轉成元組輸出, 初始值是 0 = ", tuple(enumerate_drinks))

enumerate_drinks = enumerate(drinks, start = 10)    # 數值初始是10
print("轉成元組輸出, 初始值是10 = ", tuple(enumerate_drinks))










          



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch8\ch8_15.py

# ch8_15.py
drinks = ("coffee", "tea", "wine")
# 解析enumerate物件
for drink in enumerate(drinks):             # 數值初始是0
    print(drink)
for count, drink in enumerate(drinks):
    print(count, drink)
print("****************")   
# 解析enumerate物件
for drink in enumerate(drinks, 10):         # 數值初始是10
    print(drink)
for count, drink in enumerate(drinks, 10):
    print(count, drink)










          



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch8\ch8_16.py

# ch8_16.py
fields = ['Name', 'Age', 'Hometown']
info = ['Peter', '30', 'Chicago']
zipData = zip(fields, info)         # 執行zip
print(type(zipData))                # 列印zip資料類型
player = list(zipData)              # 將zip資料轉成串列
print(player)                       # 列印串列














print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch8\ch8_17.py

# ch8_17.py
fields = ['Name', 'Age', 'Hometown']
info = ['Peter', '30']
zipData = zip(fields, info)         # 執行zip
print(type(zipData))                # 列印zip資料類型
player = list(zipData)              # 將zip資料轉成串列
print(player)                       # 列印串列














print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch8\ch8_18.py

# ch8_18.py
fields = ['Name', 'Age', 'Hometown']
info = ['Peter', '30', 'Chicago']
zipData = zip(fields, info)         # 執行zip
print(type(zipData))                # 列印zip資料類型
player = list(zipData)              # 將zip資料轉成串列
print(player)                       # 列印串列

f, i = zip(*player)                 # 執行unzip
print("fields = ", f)
print("info   = ", i)
















print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch8\ch8_19.py

# ch8_19.py
dist = 384400                   # 地球到月亮距離
speed = 1225                    # 馬赫速度每小時1225公里
total_hours = dist // speed     # 計算小時數
data = divmod(total_hours, 24)  # 商和餘數
print("divmod傳回的資料型態是 : ", type(data))
print(f"總共需要 {data[0]} 天")
print(f"{data[1]} 小時")






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch8\ch8_2.py

# ch8_2.py
numbers1 = (1, 2, 3, 4, 5)      # 定義元組元素是整數
fruits = ('apple', 'orange')    # 定義元組元素是字串
val_tuple = (10,)               # 只有一個元素的元祖
print(numbers1[0])              # 以中括號索引值讀取元素內容
print(numbers1[4])
print(fruits[0],fruits[1])
print(val_tuple[0])
x, y = ('apple', 'orange')      
print(x,y)
x, y = fruits
print(x,y)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch8\ch8_20.py

# ch8_20.py
fields = ['台北', '台中', '高雄']
info = [80000, 50000, 60000]
zipData = zip(fields, info)             # 執行zip
sold_info = tuple(zipData)              # 將zip資料轉成元組
for city, sales in sold_info:
    print(f'{city} 銷售金額是 {sales}')














print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch8\ch8_3.py

# ch8_3.py
keys = ('magic', 'xaab', 9099)      # 定義元組元素是字串與數字
for key in keys:
    print(key)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch8\ch8_4.py

# ch8_4.py
fruits = ('apple', 'orange')        # 定義元組元素是字串
print(fruits[0])                    # 列印元組fruits[0]
fruits[0] = 'watermelon'            # 將元素內容改為watermelon
print(fruits[0])                    # 列印元組fruits[0]



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch8\ch8_5.py

# ch8_5.py
fruits = ('apple', 'orange')        # 定義元組元素是水果
print("原始fruits元組元素")
for fruit in fruits:
    print(fruit)

fruits = ('watermelon', 'grape')    # 定義新的元組元素
print("\n新的fruits元組元素")
for fruit in fruits:
    print(fruit)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch8\ch8_6.py

# ch8_6.py     
fruits = ('apple', 'orange', 'banana', 'watermelon', 'grape')
print(fruits[1:3])
print(fruits[:2])
print(fruits[1:])
print(fruits[-2:])
print(fruits[0:5:2])
      

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch8\ch8_7.py

# ch8_7.py
fruits = ("apple", "banana", "cherry", "date", "cherry")
print(f"fruits 元組長度是 {len(fruits)}")    # 輸出 5

index = fruits.index("cherry")
print(f"cherry 索引位置是 {index}")          # 輸出 2

cherry_count = fruits.count("cherry")
print(f"cherry 出現次數是 {cherry_count}")   # 輸出 2


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch8\ch8_8.py

# ch8_8.py
keys = ('magic', 'xaab', 9099)      # 定義元組元素是字串與數字
key = keys.pop( )                   # 錯誤


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch8\ch8_9.py

# ch8_9.py
keys = ('magic', 'xaab', 9099)      # 定義元組元素是字串與數字
keys.append('secret')               # 錯誤


print("------------------------------------------------------------")  # 60個




#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_1.py

# ch9_1.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
noodles = {'牛肉麵':100, '肉絲麵':80, '陽春麵':60}
print(fruits)
print(noodles)
# 列出字典資料型態
print("字典fruits資料型態是: ",type(fruits))



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_10.py

# ch9_10.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print("舊fruits字典內容:", fruits)
valueTup = fruits.popitem()
print("新fruits字典內容:", fruits)
print("刪除內容:", valueTup)



   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_11.py

# ch9_11.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print("舊fruits字典內容:", fruits)
fruits.clear()
print("新fruits字典內容:", fruits)

   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_12.py

# ch9_12.py
week = {}           # 建立空字典
print("星期字典", week)
week['Sunday'] = '星期日'
week['Monday'] = '星期一'
print("星期字典", week)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_13.py

# ch9_13.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25, '蘋果':18}
cfruits = fruits.copy( )
print("位址 = ", id(fruits), "  fruits元素 = ", fruits)
print("位址 = ", id(cfruits), "  fruits元素 = ", cfruits)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_14.py

# ch9_14.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25, '蘋果':18}
noodles = {'牛肉麵':100, '肉絲麵':80, '陽春麵':60}
empty_dict = {}
print("fruits字典元素數量     = ", len(fruits))
print("noodles字典元素數量    = ", len(noodles))
print("empty_dict字典元素數量 = ", len(empty_dict))



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_15.py

# ch9_15.py
players = {
    'Stephen Curry':'Golden State Warriors',
    'Kevin Durant':'Golden State Warriors',
    'Lebron James':'Cleveland Cavaliers',
    'James Harden':'Houston Rockets',
    'Paul Gasol':'San Antonio Spurs',
}
print(f"Stephen Curry是 {players['Stephen Curry']} 的球員")
print(f"Kevin Durant是 {players['Kevin Durant']} 的球員")
print(f"Paul Gasol是 {players['Paul Gasol']} 的球員") 



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_16.py

# ch9_16.py
dealerA = {1:'Nissan', 2:'Toyota', 3:'Lexus'}
dealerB = {11:'BMW', 12:'Benz'}
dealerA.update(dealerB)
print(dealerA)






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_16_1.py

# ch9_16_1.py
dealerA = {1:'Nissan', 2:'Toyota', 3:'Lexus'}
dealerB = {3:'BMW', 4:'Benz'}
dealerA.update(dealerB)
print(dealerA)








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_16_2.py

# ch9_16_2.py
nation = [['日本','東京'],['泰國','曼谷'],['英國','倫敦']]
nationDict = dict(nation)
print(nationDict)








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_16_3.py

# ch9_16_3.py
mydict = {"name":"Hung", "age":25, "city":"New York"}
for key in mydict:
    print(f"{key} : {mydict[key]}")








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_17.py

# ch9_17.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers'}
for name, team in players.items( ):
    print(f"姓名:{name}")
    print(f"隊名:{team}")


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_18.py

# ch9_18.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers'}
for name in players.keys():
    print(name)
    print(f"Hi! {name} 我喜歡看你在 {players[name]} 的表現")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_19.py

# ch9_19.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers'}
for name in players:
    print(name)
    print(f"Hi! {name} 我喜歡看你在 {players[name]} 的表現")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_19_1.py

# ch9_19_1.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers'}
keys_list = [key for key in players]
print(keys_list)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_2.py

# ch9_2.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
noodles = {'牛肉麵':100, '肉絲麵':80, '陽春麵':60}
print("水蜜桃一斤 = ", fruits['水蜜桃'], "元")
print("牛肉麵一碗 = ", noodles['牛肉麵'], "元")
   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_20.py

# ch9_20.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers'}
for name in sorted(players):
    print(name)
    print(f"Hi! {name} 我喜歡看你在 {players[name]} 的表現")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_21.py

# ch9_21.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers'}
for team in players.values():
    print(team)
    



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_21_1.py

# ch9_21_1.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers'}
for team in players:
    print(players[team])
    



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_21_2.py

# ch9_21_2.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers'}
for team in set(players.values()):
    print(team)
    



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_21_3.py

# ch9_21_3.py
noodles = {'牛肉麵':100, '肉絲麵':80, '陽春麵':60,
           '大滷麵':90, '麻醬麵':70}
print(noodles)
noodlesLst = sorted(noodles.items(), key=lambda item:item[1])
print(noodlesLst)
print(" 品項   價格")
for i in range(len(noodlesLst)):
    print(f"{noodlesLst[i][0]}   {noodlesLst[i][1]}")




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_21_4.py

# ch9_21_4.py
noodles = {'牛肉麵':100, '肉絲麵':80, '陽春麵':60,
           '大滷麵':90, '麻醬麵':70}
print(noodles)
noodlesLst = sorted(noodles.items(), key=lambda item:item[1])
print(noodlesLst)
print(" 品項   價格")
for i in range(len(noodlesLst)):
    print(f"{noodlesLst[i][0]}   {noodlesLst[i][1]}")




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_22.py

# ch9_22.py
soldier0 = {'tag':'red', 'score':3, 'speed':'slow'} # 建立小兵
soldier1 = {'tag':'blue', 'score':5, 'speed':'medium'}
soldier2 = {'tag':'green', 'score':10, 'speed':'fast'}
armys = [soldier0, soldier1, soldier2]              # 小兵組成串列
for army in armys:                                  # 列印小兵
    print(army)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_23.py

# ch9_23.py
armys = []                      # 建立小兵空串列
# 建立50個小兵
for soldier_number in range(50):
    soldier = {'tag':'red', 'score':3, 'speed':'slow'}
    armys.append(soldier)
# 列印前3個小兵
for soldier in armys[:3]:
    print(soldier)
# 列印小兵數量
print(f"小兵數量 = {len(armys)}")
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_24.py

# ch9_24.py
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
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_25.py

# ch9_25.py
# 建立內含字串的字典
sports = {'Curry':['籃球', '美式足球'],
          'Durant':['棒球'],
          'James':['美式足球', '棒球', '籃球']}
# 列印key名字 + 字串'喜歡的運動'
for name, favorite_sport in sports.items( ):
    print(f"{name} 喜歡的運動是: ")
# 列印value,這是串列
    for sport in favorite_sport:
        print(f"   {sport}")


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_26.py

# ch9_26.py
# 建立內含字典的字典
wechat_account = {'cshung':{
                        'last_name':'洪',
                        'first_name':'錦魁',
                        'city':'台北'},
                  'kevin':{
                        'last_name':'鄭',
                        'first_name':'義盟',
                        'city':'北京'}}
# 列印內含字典的字典
for account, account_info in wechat_account.items( ):
    print("使用者帳號 = ", account)                   # 列印鍵(key)
    name = account_info['last_name'] + " " + account_info['first_name']
    print(f"姓名       = {name}")                      # 列印值(value)
    print(f"城市       = {account_info['city']}")      # 列印值(value)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_27.py

# ch9_27.py
# 建立內含字典的字典
wechat = {'cshung':{
               'last_name':'洪',
               'first_name':'錦魁',
               'city':'台北'},
          'kevin':{
               'last_name':'鄭',
               'first_name':'義盟',
               'city':'北京'}}
# 列印字典元素個數
print(f"wechat字典元素個數       {len(wechat)}")
print(f"wechat['cshung']元素個數 {len(wechat['cshung'])}")
print(f"wechat['kevin']元素個數  {len(wechat['kevin'])}")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_28.py

# ch9_28.py
# 將串列轉成字典
seq1 = ['name', 'city']         # 定義串列
list_dict1 = dict.fromkeys(seq1)
print(f"字典1 {list_dict1}")
list_dict2 = dict.fromkeys(seq1, 'Chicago')
print(f"字典2 {list_dict2}")
# 將元組轉成字典
seq2 = ('name', 'city')         # 定義元組
tup_dict1 = dict.fromkeys(seq2)
print(f"字典3 {tup_dict1}")
tup_dict2 = dict.fromkeys(seq2, 'New York')
print(f"字典4 {tup_dict2}")


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_29.py

# ch9_29.py
fruits = {'Apple':20, 'Orange':25}
ret_value1 = fruits.get('Orange')
print(f"Value = {ret_value1}")
ret_value2 = fruits.get('Grape')
print(f"Value = {ret_value2}")
ret_value3 = fruits.get('Grape', 10)
print(f"Value = {ret_value3}")


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_3.py

# ch9_3.py
fruits = {0:'西瓜', 1:'香蕉', 2:'水蜜桃'}
print(fruits[0], fruits[1], fruits[2])


   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_30.py

# ch9_30.py
# key在字典內
my_dict = {'apple': 1, 'banana': 2}

# 使用 setdefault() 獲取 'apple' 的值
value1 = my_dict.setdefault('apple', 0)
print(value1)  

# 使用 setdefault() 獲取 'orange' 的值
value2 = my_dict.setdefault('orange', 3)
print(value2)  

# 輸出更新後的字典
print(my_dict)  



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_31.py

# ch9_31.py
person = {'name':'John'}
print("原先字典內容", person)

# 'age'鍵不存在
age = person.setdefault('age')
print(f"增加age鍵 {person}")
print(f"age = {age}")
# 'sex'鍵不存在
sex = person.setdefault('sex', 'Male')
print(f"增加sex鍵 {person}")
print(f"sex = {sex}")




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_31_1.py

# ch9_31_1.py
things = {'iWatch手錶':(15000, 0.1),    # 定義商品
          'Asus  筆電':(35000, 0.7),
          'iPhone手機':(38000, 0.3),
          'Acer  筆電':(40000, 0.8),          
          'Go Pro攝影':(12000, 0.1),
         }

# 商品依價值排序
th = sorted(things.items(), key=lambda item:item[1][0])   
print('所有商品依價值排序如下')
print('商品', '        商品價格 ',  ' 商品重量')
for i in range(len(th)):
    print(f"{th[i][0]:8s}{th[i][1][0]:10d}{th[i][1][1]:10.2f}")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_32.py

# ch9_32.py
song = """Are you sleeping, are you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong."""
mydict = {}                         # 空字典未來儲存單字計數結果
print("原始歌曲")
print(song)

# 以下是將歌曲大寫字母全部改成小寫
songLower = song.lower()            # 歌曲改為小寫
print("小寫歌曲")
print(songLower)

# 將歌曲的標點符號用空字元取代
for ch in songLower:                
        if ch in ".,?":
            songLower = songLower.replace(ch,'')
print("不再有標點符號的歌曲")    
print(songLower)

# 將歌曲字串轉成串列
songList = songLower.split()        
print("以下是歌曲串列")
print(songList)                     # 列印歌曲串列

# 將歌曲串列處理成字典 
for wd in songList:                 
        if wd in mydict:            # 檢查此字是否已在字典內
            mydict[wd] += 1         # 累計出現次數
        else:
            mydict[wd] = 1          # 第一次出現的字建立此鍵與值
    
print("以下是最後執行結果")
print(mydict)                       # 列印字典










print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_33.py

# ch9_33.py
word = 'deepmind'
alphabetCount = {alphabet:word.count(alphabet) for alphabet in word}
print(alphabetCount)












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_34.py

# ch9_34.py
song = """Are you sleeping, are you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong."""
#mydict = {}                         # 省略,空字典未來儲存單字計數結果
print("原始歌曲")
print(song)

# 以下是將歌曲大寫字母全部改成小寫
songLower = song.lower()            # 歌曲改為小寫
print("小寫歌曲")
print(songLower)

# 將歌曲的標點符號用空字元取代
for ch in songLower:                
    if ch in ".,?":
        songLower = songLower.replace(ch,'')
print("不再有標點符號的歌曲")    
print(songLower)

# 將歌曲字串轉成串列
songList = songLower.split()        
print("以下是歌曲串列")
print(songList)                     # 列印歌曲串列

# 將歌曲串列處理成字典 
mydict = {wd:songList.count(wd) for wd in songList}
print("以下是最後執行結果")
print(mydict)                       # 列印字典










print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_35.py

# ch9_35.py
season = {'水瓶座':'1月20日 - 2月18日, 需警惕小人',
          '雙魚座':'2月19日 - 3月20日, 凌亂中找立足',
          '白羊座':'3月21日 - 4月19日, 運勢比較低迷',
          '金牛座':'4月20日 - 5月20日, 財運較佳',
          '雙子座':'5月21日 - 6月21日, 運勢好可錦上添花',
          '巨蟹座':'6月22日 - 7月22日, 不可鬆懈大意',
          '獅子座':'7月23日 - 8月22日, 會有成就感',
          '處女座':'8月23日 - 9月22日, 會有挫折感',
          '天秤座':'9月23日 - 10月23日, 運勢給力',
          '天蠍座':'10月24日 - 11月22日, 中規中矩',
          '射手座':'11月23日 - 12月21日, 可羨煞眾人',
          '魔羯座':'12月22日 - 1月19日, 需保有謙虛',
          }

wd = input("請輸入欲查詢的星座 : ")
if wd in season:
    print(wd, " 本月運勢 : ", season[wd])
else:
    print("星座輸入錯誤")














print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_36.py

# ch9_36.py
abc = 'abcdefghijklmnopqrstuvwxyz'
encry_dict = {}
front3 = abc[:3]
end23 = abc[3:]
subText = end23 + front3
encry_dict = dict(zip(abc, subText))    # 建立字典
print("列印編碼字典\n", encry_dict)     # 列印字典

msgTest = input("請輸入原始字串 : ")

cipher = []
for i in msgTest:                       # 執行每個字元加密
    v = encry_dict[i]                   # 加密
    cipher.append(v)                    # 加密結果
ciphertext = ''.join(cipher)            # 將串列轉成字串

print("原始字串 ", msgTest)
print("加密字串 ", ciphertext)









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_37.py

# ch9_37.py
morse_code = {'A':'.-', 'B':'-...', 'C':'-.-.','D':'-..','E':'.',
              'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
              'K':'-.-', 'L':'.-..','M':'--', 'N':'-.','O':'---',
              'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-',
              'U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--',
              'Z':'--..'}

wd = input("請輸入大寫英文字: ")
for c in wd:
    print(morse_code[c])


























print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_4.py

# ch9_4.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
fruits['橘子'] = 18
print(fruits)
print("橘子一斤 = ", fruits['橘子'], "元")

   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_5.py

# ch9_5.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print("舊價格香蕉一斤 = ", fruits['香蕉'], "元")
fruits['香蕉'] = 12
print("新價格香蕉一斤 = ", fruits['香蕉'], "元")

   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_6.py

# ch9_6.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
key = input("請輸入鍵(key) = ")
if key in fruits:
    print(f"{key}已經在字典了")
else:
    value = input("請輸入值(value) = ")
    fruits[key] = value
    print("新的fruits字典內容 = ", fruits)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_7.py

# ch9_7.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print("水果字典:", fruits)
fruit = input("請輸入要刪除的水果 : ")
if fruit in fruits:
    del fruits[fruit]
    print("新水果字典:", fruits)
else:
    print(f"{fruit} 不在水果字典內")

   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_8.py

# ch9_8.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print("舊fruits字典內容:", fruits)
del fruits
print("新fruits字典內容:", fruits)       # 錯誤! 錯誤!

   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_8_1.py

# ch9_8_1.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
var_dict = input("請輸入要刪除的變數 : ")
if var_dict in locals():    # 檢查變數是否存在
    print(f"{var_dict} 變數存在")
    del fruits
    print(f"刪除 {var_dict} 變數成功")
else:
    print(f"{var_dict} 變數不存在")


   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_8_2.py

# ch9_8_2.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
var = input("請輸入要刪除的字典變數 : ")
if var in locals():
    var = eval(var)
    if isinstance(var, dict):
        print(f"'fruits' 字典變數存在")
        del fruits
        print(f"刪除字典變數成功")
    else:
        print(f"字典變數不存在")
else:
    print(f"{var} 變數不存在")

   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch9\ch9_9.py

# ch9_9.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print("舊fruits字典內容:", fruits)
objKey = '西瓜'
value = fruits.pop(objKey)
print("新fruits字典內容:", fruits)
print("刪除內容:", objKey + ":" + str(value))



   

print("------------------------------------------------------------")  # 60個

