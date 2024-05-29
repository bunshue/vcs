import os
import sys
import time
import random



print('------------------------------------------------------------')	#60個
'''
print('string.printable 的用法 ')

import string

print(string.printable)
print(len(string.printable))
abc = string.printable[:-5]  # 取消不可列印字元
print(abc)

print('------------------------------------------------------------')	#60個

"""
def batch_resize_images(input_folder, output_folder, size=(300, 300)):
    # 確保輸出資料夾存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 遍歷輸入資料夾中的所有影像檔案
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.png')):
            # 打開影像
            image = Image.open(os.path.join(input_folder, filename))
            # 調整影像尺寸
            image = image.resize(size, Image.ANTIALIAS)
            # 保存調整尺寸後的影像到輸出資料夾
            #image.save(os.path.join(output_folder, filename))

# 假設有一個包含原始圖片的資料夾 'input_images' 和
# 一個用於存放調整後圖片的資料夾 'output_images'
input_folder = 'input_images'
output_folder = 'output_images'

# 呼叫函數，將所有圖片調整為300x300大小
batch_resize_images(input_folder, output_folder)
"""

print("------------------------------------------------------------")  # 60個

"""
def batch_convert_images(directory, target_format='.jpg'):
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            path = os.path.join(directory, filename)
            image = Image.open(path)
            image_rgb = image.convert('RGB')  # 轉換為RGB模式以便保存為JPEG
            #image_rgb.save(path.replace('.png', target_format), quality=95)

# 呼叫批次更改函數
batch_convert_images('images_directory')
"""

print("------------------------------------------------------------")  # 60個

"""
#pitems = ps.split()
pfile = input("請輸入讀取檔案名稱：").strip()

pfile = input("請輸入讀取檔案名稱：").strip()
pinfile = open(pfile, "r")
ps = pinfile.read()  
print(str(len(ps)) + " 字元數") 
print(str(len(ps.split())) + " 單字數") 
print(str(len(ps.split('\n'))) + " 行數") 
pinfile.close()
"""
print("------------------------------------------------------------")  # 60個


"""
#print
#print("當半徑為%d時，圓面積為%6.2f，圓周長為%6.2f"%(pvalue, result1, result2))
print("當半徑為%d時，圓面積為%6.2f，圓周長為%6.2f"%(pvalue, result1, result2))
print("圓柱的半徑%6.2f長度%6.2f體積為%6.2f"%(pradius,plength,pvolume))
"""

print("------------------------------------------------------------")  # 60個

"""
f=open('data/file_u8.txt','r',encoding='UTF-8-sig')
str=f.readlines()
print(str)
f.close()

f=open('data/file_u8.txt','r',encoding='UTF-8-sig')
str1=f.read(7)
print(str1)
f.close()

print("------------------------------------------------------------")  # 60個

#讀出前7拜
f=open('file.txt','r')
str1=f.read(7)
print(str1)
f.close()


# Filename: ex08_14.py
while True:
    try:
        x = int(input("請輸入一個數字: "))
        break
    except ValueError:
        print("抱歉!!您所輸入並非是有效的數字，請再輸入一次...")
"""

print("------------------------------------------------------------")  # 60個

import numpy as np

# 數據處理
# 正常顯示
x1 = np.linspace(-1.5, 1.5, 31)
y1 = np.cos(x1) ** 2

# 移除 y1 > 0.6 的點
x2 = x1[y1 <= 0.6]
y2 = y1[y1 <= 0.6]

# 遮罩 y1 > 0.7 的點, 遮罩就是不要的
y3 = np.ma.masked_where(y1 > 0.7, y1)

# 將 y1 > 0.8 的點設為 NaN
y4 = y1.copy()
y4[y4 > 0.8] = np.nan


print("------------------------------------------------------------")  # 60個


#去掉警告信息
import warnings
warnings.filterwarnings('ignore')




print("------------------------------------------------------------")  # 60個


import pathlib
print(pathlib.Path.cwd())



print("------------------------------------------------------------")  # 60個

import random

print(dir(random))

print("------------------------------------------------------------")  # 60個


import openai

openai.api_key = 'kkkkkkk'

response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt="講個笑話來聽聽",
    max_tokens=128,
    temperature=0.5,
)

completed_text = response["choices"][0]["text"]
print(completed_text)

print("------------------------------------------------------------")  # 60個

import time
import pyautogui

for i in range(10):
    #全屏截圖
    #myScreenshot = pyautogui.screenshot()
    #myScreenshot.save(f'./pic_all{i}.png')

    #部分截圖
    x_st, y_st, w, h = 1920//2, 1080//2, 1920//2-50, 1080//2-50
    myScreenshot = pyautogui.screenshot(region=(x_st, y_st, w, h))
    #偽存檔
    #myScreenshot.save(f'./pic_part{i}.png')

    time.sleep(5)

print("------------------------------------------------------------")  # 60個

print('filter 的用法')

a = [1,2,3,4,5,6,7,8,9]

b = filter(lambda x:x>5, a)
c = list(b)
print(c)


"""
python內建函數
lambda匿名函數
map
filter
sorted

"""


print("------------------------------------------------------------")  # 60個

import time
print(time.time(), " 秒")
print(time.time_ns(), " 微秒")

"""

time.ctime 本地時間
time.localtime() 轉換為struct_time格式的本地時間
time.gmtime() 回傳UTC時間

time.mktime(t) 將struct_time格式的時間轉換回秒數
time.asctime() 將struct_time格式的時間轉換為文字顯示
time.strftime() 將時間轉換為特定格式字串
time.strptime() 將特定格式的字串轉換為struct_time格式的時間



"""

print("------------------------------------------------------------")  # 60個

"""
import time
n = 20                   # 設定進度條總長
for i in range(n+1):
    print(f'\r[{"█"*i}{" "*(n-i)}] {i*100/n}%', end='')   # 輸出不換行的內容
    time.sleep(0.5)

print("------------------------------------------------------------")  # 60個


import time
n = 100
icon = '⋮⋰⋯⋱'          # 建立旋轉的符號清單
for i in range(n+1):
    print(f'\r{icon[i%4]} {i*100/n}%', end='')
    time.sleep(0.1)

"""

print("------------------------------------------------------------")  # 60個

"""
import datetime

now = datetime.datetime.now().strftime('%H:%M:%S')
print(now)    # 14:30:23

print("------------------------------------------------------------")  # 60個

import datetime
import time

while True:
    now = datetime.datetime.now().strftime('%H:%M:%S')
    print(f'\r{now}', end = '')     # 前方加上 \r
    time.sleep(1)
"""

print("------------------------------------------------------------")  # 60個

print('末N碼')

string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print('末10碼', string[-10:])
print('末20碼', string[-20:])
print('末26碼', string[-26:])


print("------------------------------------------------------------")  # 60個

import sys

# 匯入 指定目錄下的模組
sys.path.append(r'C:\_git\vcs\_4.python\import_module')

from module_my import say_hello

say_hello()

# 以下為模組 \data\income_tax.py 的內容：

#字典
TAX_RATE = {
    0: 0.1,
    10000: 0.2,
    50000: 0.3,
    100000: 0.4,
    500000: 0.5
    }

print(type(TAX_RATE))
for income, rate in TAX_RATE.items():
    print(income, rate)

print('------------------------------------------------------------')	#60個

# 函式選單模組

def menu(**options):
    def menu_selector():
        option_string = '/'.join(options)
        while True:
            choice = input(f'選擇項目 ({option_string}): ')
            if choice in options:
                return options[choice]
                break
            print('選項不存在!')
    return menu_selector

# 主程式
#from menu import menu

def func_a():
    return '執行函式 A'

def func_b():
    return '執行函式 B'

def func_x():
    return '執行函式 X'

my_menu = menu(a=func_a, b=func_b, x=func_x)

func = my_menu()
print(func())
'''
print('------------------------------------------------------------')	#60個

"""
import glob
import pathlib

print('touch當前目錄下所有檔案')
files = glob.glob("*.*") 
for filename in files:
    print(filename)
    pathlib.Path(filename).touch()
"""
print("------------------------------------------------------------")  # 60個

# Count each letter in the string 
def countLetters(line, counts): 
    for ch in line:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1

filename = 'data/engnews.txt'

infile = open(filename, "r") # Open the file, 格式要unicode轉ascii

counts = 26 * [0] # Create and initialize counts
for line in infile:
    # Invoke the countLetters function to count each letter
    countLetters(line.lower(), counts)
    
# Display results
for i in range(len(counts)):
    if counts[i] != 0:
        print(chr(ord('a') + i) + " appears " + str(counts[i])
          + (" time" if counts[i] == 1 else " times"))

infile.close() # Close file
  

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

name = '鼠'
weight = 3
print('動物{0}的體重是{1}公斤'.format(name, weight))

print('動物%s的體重是%d公斤' %(name, weight))

"""
name = input('輸入品名：')
num = int(input('輸入數量：'))
price = float(input('輸入單價：'))
print()
print('品名\t\t數量\t單價\t金額')
print('=========================================')
print('%-14s%-9d%-9.1f%-9.1f' %(name,num,price,num*price))



data = []
site = input("請輸入平台名稱：")
data.append(input("請輸入帳號："))
data.append(input("請輸入密碼："))
print(f"{site}的帳號：{data[0]}；密碼：{data[1]}")


radius = int(input("請輸入球半徑(公分) :"))
volume = compute(radius)
print(f"球半徑 = {radius}公分  球體積 = {volume}立方公分")
"""


from random import randint
rand = set()

while (len(rand) < 7):
    rand.add(randint(1,49))
print ("本期樂透彩號碼：")
for idx,num in enumerate(rand, 1):
    print (f"({idx})={num}", end='  ')


print("------------------------------------------------------------")  # 60個

print(543.21)     #顯示浮點數常值 543.21
print(5.4321e2)   #顯示浮點數常值 543.21
print(5.4321e6)   #顯示浮點數常值 5432100.0
print(5.4321e-3)  #顯示浮點數常值 0.0054321

print("------------------------------------------------------------")  # 60個

name = '李金星'          # 宣告字串變數name，初值設為'李金星'
score = 73               # 宣告整數變數score，初值設為73
msg = '{}的成績是{}分'.format(name, score)
print(msg)

name = '李金星'          # 宣告字串變數name，初值設為'李金星'
score = 73               # 宣告整數變數score，初值設為73
msg = '{0}的成績是{1}分'.format(name, score)
print(msg)

name = '李金星'          # 宣告字串變數name，初值設為'李金星'
score = 73               # 宣告整數變數score，初值設為73
print('{0}的成績是{1}'.format(name, score))
                                   	
print("------------------------------------------------------------")  # 60個

price = 100
qty = 30
print('單價：{0}     數量：{1}'.format(price, qty))
print('打八折後,總金額：{0}'.format(price * qty * 0.8))

print("------------------------------------------------------------")  # 60個

print('%s風景區在%s境內' %('日月潭','南投縣'));
wt=3
price=25
print('%s%d斤，共%d元' %('香蕉', wt, wt*price));

print("------------------------------------------------------------")  # 60個

print('%d' %1234)  		# 顯示整數,未設寬度
print('%8d' %1234) 	# 顯示整數,寬度有剩補空格,靠右對齊
print('%8d' %-1234)     # 顯示整數,寬度有剩補空格,靠右對齊
print('%3d' %-1234)     # 顯示整數,寬度不足設定無效

print("------------------------------------------------------------")  # 60個

print('%f' %123.456)	# 顯示數值「123.456000」,小數預設6位
print('%f' %-123.456)	# 顯示數值「-123.456000」,小數預設6位
print('%.2f' %123.456)	# 顯示數值「123.46」,小數2位,第3位四捨五入
print('%8.2f' %-12.3456)# 顯示「ΔΔ-12.35」,總寬度8位,小數2位
print('%3.1f' %123.456)	# 顯示「123.5」,寬度不足設定無效,小數位數1位
print('%8.0f' %-123.456)# 顯示數值「ΔΔΔ-1235」,小數第1位四捨五入
print('%8.0f' %123.456)	# 顯示數值「ΔΔΔ1235」,小數第1位四捨五入
print('%g' %12345.6789)	# 顯示數值「12345.7」,總寬度預設7位
print('%g' %1.23456789)	# 顯示數值「1.23457」,總寬度預設7位
print('%g' %12.3)		# 顯示數值「12.3」, 寬度低於預設,直接顯示
print('%g' %123456.789)	# 顯示數值「123457」,最後1位為小數點不顯示
print('%g' %1234567.89)	# 顯示數值「1.23457e+06」,整數7位以上,
                             	# 改用科學記號顯示,指數位數佔2位(不含+-號)
print('%10.3G' %1234.5)	# 顯示「ΔΔ1.23E+03」,寬度10位,E及小數3位

print("------------------------------------------------------------")  # 60個

print('%c' %'M')            # 顯示字元「M」
print('%4c' %'M')           # 顯示字元「ΔΔΔM」,靠右對齊,寬度有剩補空格
print('%c' %65)             # 顯示字元「A」,65的ASCII碼為「A」
print('%s' %'ABCDE')        # 顯示字串「ABCDE」
print('%8s' %'ABCDE')       # 顯示字串「ΔΔΔABCDE」
print('%3s' %'ABCDE')       # 顯示字串「ABCDE」,總寬度不足設定無效
print('%6.2s' %'ABCDE')     # 顯示字串「ΔΔΔΔAB」,寬度設為6,顯示2字元

print("------------------------------------------------------------")  # 60個

print('%+8d' %12345)        # 顯示「ΔΔ+12345」,靠右對齊,正數值前加「+」號
print('%+8d' %-12345)       # 顯示「ΔΔ-12345」,靠右對齊,負數值前加「-」號
print('%-8d' %12345)        # 顯示「12345ΔΔΔ」,靠左對齊,正數值前不加號
print('%-8d' %-12345)       # 顯示「-12345ΔΔ」,靠左對齊,負數值前加「-」號
print('%+8.2f' %12.345)     # 顯示「ΔΔ+12.35」,靠右對齊,正數值加「+」號
print('%-8.2f' %12.345)     # 顯示「12.35ΔΔΔ」,靠左對齊,正數值不加號
print('%-8.2f' %-12.345)    # 顯示「-12.35ΔΔ」,靠左對齊,負數值加「-」號
print('%-8s' %'ABCDE')      # 顯示字串「ABCDEΔΔΔ」,靠左對齊,寬度有剩補空格
print('%-6.2s' %'ABCDE')    # 顯示字串「ABΔΔΔΔ」,寬度設為6,顯示2個字元

print("------------------------------------------------------------")  # 60個

print('1234567890!\a')       # 出現音效聲,游標位置在'!'字元後面
print('12345\b67890!')       # 顯示字串「123467890!」,刪除字元'5'
print('1234567890!\n')       # 顯示字串「123467890!」,游標跳到下一行行首
print('123\r4567890!')       # 游標跳到行首,刪除'123',顯示字串「4567890!」
print('123\t45\\67')         # 顯示字串「123ΔΔΔΔΔ45\67」
print('123\"45\"67')         # 顯示字串「123"45"67」
print('123\'4\'567')         # 顯示字串「123'4'567」
print('ASCII碼41(Hex):\x41') # 顯示字串「ASCII碼41(Hex):A」

print("------------------------------------------------------------")  # 60個

a = 100	     	
b = 20			   
print(a, b)  	        # 輸出a和b的變數值,分別為100,20
print(id(a), id(b))     # 顯示a和b變數所在的記憶體位址
a, b = b, a             # a,b兩變數的記憶體位址交換
print(a, b)  	        # 輸出a和b的變數值,分別為20,100
print(id(a), id(b))     # 顯示a和b變數所在的記憶體位址

print("------------------------------------------------------------")  # 60個

data = (("張三", 86, 60),("李四", 93, 55),("王五", 72, 66), ("劉六", 89, 84))

print ("編號    姓名      學科    術科    總分")
for idx, dt in enumerate(data):
    print (f"{idx + 1}\t{dt[0]}\t{dt[1]}\t{dt[2]}\t{dt[1] + dt[2]}")

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

