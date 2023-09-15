import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個


import random
random.seed(5)  #固定亂數種子
for i in range(5):
    print(random.random())
    


print('------------------------------------------------------------')	#60個

import random                       # 導入模組random

for i in range(5):
    print("uniform(1,10) : ", random.uniform(1, 10))

print('------------------------------------------------------------')	#60個

import random                   # 導入模組random

for i in range(10):
    print(random.choice([1,2,3,4,5,6]), end=",")

print('------------------------------------------------------------')	#60個

import random                 # 導入模組random

porker = ['2', '3', '4', '5', '6', '7', '8',
          '9', '10', 'J', 'Q', 'K', 'A']
for i in range(3):
    random.shuffle(porker)    # 將次序打亂重新排列
    print(porker)

print('------------------------------------------------------------')	#60個

import random                               # 導入模組random

lotterys = random.sample(range(1,50), 7)    # 7組號碼
specialNum = lotterys.pop()                 # 特別號

print("第xxx期大樂透號碼 ", end="")
for lottery in sorted(lotterys):            # 排序列印大樂透號碼
    print(lottery, end=" ")
print(f"\n特別號:{specialNum}")             # 列印特別號

print('------------------------------------------------------------')	#60個

import time                         # 導入模組time

xtime = time.localtime()
print(xtime)                        # 列出目前系統時間
print("年 ", xtime[0])
print("年 ", xtime.tm_year)         # 物件設定方式顯示
print("月 ", xtime[1])
print("日 ", xtime[2])
print("時 ", xtime[3])
print("分 ", xtime[4])
print("秒 ", xtime[5])
print("星期幾   ", xtime[6])
print("第幾天   ", xtime[7])
print("夏令時間 ", xtime[8])

print('------------------------------------------------------------')	#60個

import time

x = 1000000
pi = 0
time.process_time()
for i in range(1,x+1):
    pi += 4*((-1)**(i+1) / (2*i-1))
    if i != 1 and i % 100000 == 0:      # 隔100000執行一次
        e_time = time.process_time()
        print(f"當 {i=:7d} 時 PI={pi:8.7f}, 所花時間={e_time}")

print('------------------------------------------------------------')	#60個

import sys

print("目前Python版本是: ", sys.version)
print("目前Python版本是: ", sys.version_info)


print('------------------------------------------------------------')	#60個

import keyword

keywordLists = ['as', 'while', 'break', 'sse', 'Python']
for x in keywordLists:
    print(f"{x:>8s} {keyword.iskeyword(x)}")

print('------------------------------------------------------------')	#60個

import random

trials = 1000000
Hits = 0
for i in range(trials):
    x = random.random() * 2 - 1     # x軸座標
    y = random.random() * 2 - 1     # y軸座標
    if x * x + y * y <= 1:          # 判斷是否在圓內
        Hits += 1
PI = 4 * Hits / trials

print("PI = ", PI)

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個

sc = [['John', 80],['Tom', 90], ['Kevin', 77]]
sc.sort(key = lambda x:x[1])
print(sc)





print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


