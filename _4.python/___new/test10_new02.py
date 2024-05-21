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
'''
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

print('------------------------------------------------------------')	#60個






print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

