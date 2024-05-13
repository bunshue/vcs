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
'''

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
    myScreenshot.save(f'./pic_part{i}.png')

    time.sleep(5)

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

