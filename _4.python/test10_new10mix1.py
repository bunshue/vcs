"""
範例來的混合資料 1


"""


import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個



x = -10
print("以下輸出abs( )函數的應用")
print(x)            # 輸出x變數
print(abs(x))       # 輸出abs(x)
x = 5
y = 3
print("以下輸出pow( )函數的應用")
print(pow(x, y))    # 輸出pow(x,y)
x = 47.5
print("以下輸出round(x)函數的應用")
print(x)            # 輸出x變數
print(round(x))     # 輸出round(x)
x = 48.5
print(x)            # 輸出x變數
print(round(x))     # 輸出round(x)
x = 49.5
print(x)            # 輸出x變數
print(round(x))     # 輸出round(x)
print("以下輸出round(x,n)函數的應用")
x = 2.15
print(x)            # 輸出x變數
print(round(x,1))   # 輸出round(x,1)
x = 2.25
print(x)            # 輸出x變數
print(round(x,1))   # 輸出round(x,1)
x = 2.151
print(x)            # 輸出x變數
print(round(x,1))   # 輸出round(x,1)
x = 2.251
print(x)            # 輸出x變數
print(round(x,1))   # 輸出round(x,1)


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


dist = 384400                   # 地球到月亮距離
speed = 1225                    # 馬赫速度每小時1225公里
total_hours = dist // speed     # 計算小時數
days, hours = divmod(total_hours, 24)   # 商和餘數
print("總供需要天數")
print(days)
print("小時數")
print(hours)


print('------------------------------------------------------------')	#60個


score = 90
name = "洪錦魁"
count = 1
print("%s你的第 %d 次物理考試成績是 %d" % (name, count, score))

# ch4_7.py
score = 90
name = "洪錦魁"
count = 1
print("{}你的第 {} 次物理考試成績是 {}".format(name, count, score))


print('------------------------------------------------------------')	#60個

# ch4_4.py
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


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python超零基礎最快樂學習之路-王者歸來\ch4\ch4_5.py

# ch4_5.py
x = 100
print("x=/%-6d/" % x)
y = 10.5
print("y=/%-6.2f/" % y)
s = "Deep"
print("s=/%-6s/" % s)


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python超零基礎最快樂學習之路-王者歸來\ch4\ch4_6.py

# ch4_6.py
print(" 姓名    國文    英文    總分")
print("%3s  %4d    %4d    %4d" % ("洪冰儒", 98, 90, 188))
print("%3s  %4d    %4d    %4d" % ("洪雨星", 96, 95, 191))
print("%3s  %4d    %4d    %4d" % ("洪冰雨", 92, 88, 180))
print("%3s  %4d    %4d    %4d" % ("洪星宇", 93, 97, 190))

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python超零基礎最快樂學習之路-王者歸來\ch6\ch6_19.py

# ch6_19.py
cars = ['Honda','Toyota','Ford','BMW']     
print("目前串列內容 = ",cars)
print("使用pop( )刪除串列元素")
popped_car = cars.pop( )          # 刪除串列末端值
print("所刪除的串列內容是 : ", popped_car)
print("新的串列內容 = ",cars)
print("使用pop(1)刪除串列元素")
popped_car = cars.pop(1)          # 刪除串列索引為1的值
print("所刪除的串列內容是 : ", popped_car)
print("新的串列內容 = ",cars)

print('------------------------------------------------------------')	#60個

cars = ['toyota', 'nissan', 'honda']
search_str = 'nissan'
i = cars.index(search_str)
print("所搜尋元素 %s 第一次出現位置索引是 %d" % (search_str, i))
nums = [7, 12, 30, 12, 30, 9, 8]
search_val = 30
j = nums.index(search_val)
print("所搜尋元素 %s 第一次出現位置索引是 %d" % (search_val, j))

print('------------------------------------------------------------')	#60個

cars = ['toyota', 'nissan', 'honda']
search_str = 'nissan'
num1 = cars.count(search_str)
print("所搜尋元素 %s 出現 %d 次" % (search_str, num1))
nums = [7, 12, 30, 12, 30, 9, 8]
search_val = 30
num2 = nums.count(search_val)
print("所搜尋元素 %s 出現 %d 次" % (search_val, num2))


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

sc = [['洪錦魁', 80, 95, 88, 0],
      ['洪冰儒', 98, 97, 96, 0],
     ]
sc[0][4] = sum(sc[0][1:4])
sc[1][4] = sum(sc[1][1:4])
print(sc[0])
print(sc[1])


print('------------------------------------------------------------')	#60個

aaa = 123

print('%-10d 保留10位向左靠齊')
print('|%-10d|' % aaa)

print('%10d  保留10位向右靠齊')
print('|%10d|' % aaa)


print('------------------------------------------------------------')	#60個

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



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python超零基礎最快樂學習之路-王者歸來\ch7\ch7_25.py

# ch7_25.py
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



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

# 5-2-1 陣列: list 與 tuple

arr = ['one', 'two', 'three']

print(arr[0])

arr[1] = 'hello'

print(arr)

del arr[1]

print(arr)

arr.append(23)

print(arr)

arr = ('one', 'two', 'three')

print(arr[0])

print(arr)

#arr[1] = 'hello'

print('------------------------------------------------------------')	#60個

# 5-5-1 list - 最基本簡單的堆疊

s = []
s.append('吃飯')
s.append('睡覺')
s.append('寫程式')

print(s)
print(s.pop())
print(s.pop())
print(s.pop())
#print(s.pop())

print('------------------------------------------------------------')	#60個

# 5-7-1 list - 麻煩的優先佇列

q = []
q.append((2, '寫程式'))
q.append((1, '吃飯'))
q.append((3, '睡覺'))

q.sort(reverse=True)

while q:
    next_item = q.pop()
    print(next_item)
    
print('------------------------------------------------------------')	#60個

    
print('------------------------------------------------------------')	#60個




# 6-3-2 用切片清除或複製 list 元素

lst = [0, 1, 2, 3, 4]
del lst[:]

print(lst)

lst = [1, 2, 3]
new_lst = lst

print(new_lst)
print(new_lst is lst)

lst[:] = [7, 8, 9]

print(lst)
print(new_lst)
print(new_lst is lst)

copied_lst = lst[:]

print(copied_lst)
print(copied_lst is lst)

lst = [0, 1, 2, 3, 4]
s = slice(1, 4)
print(lst[s])

    
print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個


import random

for _ in range(10):
    cc = random.randrange(0, 100)
    print(cc)



print('------------------------------------------------------------')	#60個

squares = [value**2 for value in range(1, 11)]
print(squares)

    
    
print('------------------------------------------------------------')	#60個


cal_dict = {
    '加': lambda x, y: x + y,
    '減': lambda x, y: x - y,
    '乘': lambda x, y: x * y,
    '除': lambda x, y: x / y,
    }

def calculator(x, operator, y):
    return cal_dict.get(operator, lambda: None)(x, y)

print(calculator(6, '乘', 7))



calculator = {
    '加': lambda x, y: x + y,
    '減': lambda x, y: x - y,
    '乘': lambda x, y: x * y,
    '除': lambda x, y: x / y,
    }

default = lambda: None

print(calculator.get('加', default)(1, 2))

print(calculator.get('乘', default)(3, 5))


    
print('------------------------------------------------------------')	#60個


# 7-6-1 使用 json.dumps() 美觀列印 dict

import json

config = {
    'lang': 'Python',
    'version': [3.6, 3.7, 3.8],
    'date': '2019-10-14',
    'platform': 'linux',
    'org': 'Python Software Foundation',
    'config_status': 0xc0ffee,
    'the_answer': 42
    }

print(json.dumps(config, indent=4, sort_keys=False))
    
print('------------------------------------------------------------')	#60個

# 8-1 以 dir() 與 help() 探索 Python 模組與物件

import datetime

print(dir(datetime))

print('')

print([_ for _ in dir(datetime) if 'date' in _.lower()])

#help(datetime)

    
print('------------------------------------------------------------')	#60個


    
print('------------------------------------------------------------')	#60個




print('有f代入數字')

price = 12345
print(f"Your admission cost is ${price}.")

price = 12345
print("Your admission cost is ${price}.")



print('------------------------------------------------------------')	#60個

print('小寫字串轉全大寫')
car = 'bmw'
print(car.upper())

print('小寫字串轉全首字大寫')
car = 'toyota'
print(car.title())

    
    
print('------------------------------------------------------------')	#60個


    
    
print('------------------------------------------------------------')	#60個


"""
print('11')
filename = 'engnews.txt'
with open(filename, "r", encoding="utf-8") as f:
    print(f.readline())#讀一行

print('22')
filename = 'engnews.txt'    
with open(filename, "r", encoding="utf-8") as f:
    data = f.read() #讀全部成一行串列

print(repr(data))
print(data)
print(data.split())
data = data.split()
for d in data:
    d.strip()
print(data)

print('33')
filename = 'engnews.txt'    
with open(filename, "r", encoding="utf-8") as f:
    print(f.readlines())#讀全部成多行串列
"""


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('用字典建立個人資料')
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)


print('------------------------------------------------------------')	#60個


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python超零基礎最快樂學習之路-王者歸來\ch11\ch11_14.py

# ch11_14.py
def printmsg( ):
    # 函數本身沒有定義變數, 只有執行列印全域變數功能
    print("函數列印: ", msg)    # 列印全域變數

msg = 'Global Variable'         # 設定全域變數
print("主程式列印: ", msg)      # 列印全域變數
printmsg( )                     # 呼叫函數



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python超零基礎最快樂學習之路-王者歸來\ch11\ch11_15.py

# ch11_15.py
def printmsg( ):
    # 函數本身有定義變數, 將執行列印區域變數功能
    msg = 'Local Variable'      # 設定區域變數
    print("函數列印: ", msg)    # 列印區域變數

msg = 'Global Variable'         # 這是全域變數
print("主程式列印: ", msg)      # 列印全域變數
printmsg( )                     # 呼叫函數



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python超零基礎最快樂學習之路-王者歸來\ch11\ch11_16.py

# ch11_16.py
def printmsg():
    global msg
    msg = "Java"        # 更改全域變數
    print("更改後: ", msg)
msg = "Python"
print("更改前: ", msg)
printmsg()




   


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python超零基礎最快樂學習之路-王者歸來\ch11\ch11_17.py

# ch11_17.py
# 定義lambda函數
square = lambda x: x ** 2

# 輸出平方值
print(square(10))


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python超零基礎最快樂學習之路-王者歸來\ch11\ch11_18.py

# ch11_18.py
# 使用一般函數
def square(x):
    value = x ** 2
    return value

# 輸出平方值
print(square(10))




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


import locale

print(locale.getpreferredencoding())



print('------------------------------------------------------------')	#60個
"""
file_Obj =  open(fn, encoding='cp950')  # 用預設encoding='cp950'開啟檔案
file_Obj =  open(fn, encoding='cp950')  # 用預設encoding='cp950'開啟檔案
file_Obj =  open(fn, encoding='utf-8')  # 用encoding='utf-8'開啟檔案
with open(fn, encoding='utf-8') as file_Obj:    # 開啟utf-8檔案
    obj_list = file_Obj.readlines()             # 每次讀一行
with open(fn, encoding='utf-8-sig') as file_Obj:  # 開啟utf-8檔案
    obj_list = file_Obj.readlines()               # 每次讀一行
"""

print('------------------------------------------------------------')	#60個

import random                               # 導入模組random

lotterys = random.sample(range(1,50), 7)    # 7組號碼
specialNum = lotterys.pop()                 # 特別號

print("第xxx期大樂透號碼 ", end="")
for lottery in sorted(lotterys):            # 排序列印大樂透號碼
    print(lottery, end=" ")
print("\n特別號:%d" % specialNum)           # 列印特別號


print('------------------------------------------------------------')	#60個

        

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python超零基礎最快樂學習之路-王者歸來\ch13\ch13_14.py

# ch13_14.py
import time                         # 導入模組time

print(time.asctime())               # 列出目前系統時間 




print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python超零基礎最快樂學習之路-王者歸來\ch13\ch13_15.py

# ch13_15.py
import time                         # 導入模組time

xtime = time.localtime()
print(xtime)                        # 列出目前系統時間
print("年 ", xtime[0])
print("月 ", xtime[1])
print("日 ", xtime[2])
print("時 ", xtime[3])
print("分 ", xtime[4])
print("秒 ", xtime[5])
print("星期幾   ", xtime[6])
print("第幾天   ", xtime[7])
print("夏令時間 ", xtime[8])





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python超零基礎最快樂學習之路-王者歸來\ch13\ch13_16.py

# ch13_16.py
import calendar

print("2020年是否潤年", calendar.isleap(2020))    
print("2021年是否潤年", calendar.isleap(2021))



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python超零基礎最快樂學習之路-王者歸來\ch13\ch13_17.py

# ch13_17.py
import calendar

print(calendar.month(2020,1))






print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python超零基礎最快樂學習之路-王者歸來\ch13\ch13_18.py

# ch13_18.py
import calendar

print(calendar.calendar(2020))

print('------------------------------------------------------------')	#60個

# ch12_2.py
class Banks():
    # 定義銀行類別
    title = 'Taipei Bank'       # 定義屬性
    def motto(self):            # 定義方法
        return "以客為尊"

userbank = Banks()              # 定義物件userbank
print("目前服務銀行是 ", userbank.title)
print("銀行服務理念是 ", userbank.motto())




print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


