import sys


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

import random                               # 導入模組random

lotterys = random.sample(range(1,50), 7)    # 7組號碼
specialNum = lotterys.pop()                 # 特別號

print("第xxx期大樂透號碼 ", end="")
for lottery in sorted(lotterys):            # 排序列印大樂透號碼
    print(lottery, end=" ")
print(f"\n特別號:{specialNum}")             # 列印特別號

print("------------------------------------------------------------")  # 60個

import random
random.seed(5)
for i in range(5):
    print(random.random())
    
print("------------------------------------------------------------")  # 60個

import random                       # 導入模組random
import time                         # 導入模組time

min, max = 1, 10
ans = random.randint(min, max)      # 隨機數產生答案
yourNum = int(input("請猜1-10之間數字: "))
starttime = int(time.time())        # 起始秒數
while True:    
    if yourNum == ans:
        print("恭喜!答對了")
        endtime = int(time.time())  # 結束秒數
        print("所花時間: ", endtime - starttime, " 秒")
        break
    elif yourNum < ans:
        print("請猜大一些")
    else:
        print("請猜小一些")
    yourNum = int(input("請猜1-10之間數字: "))
        



print("------------------------------------------------------------")  # 60個

import random                       # 導入模組random
money = 300                         # 賭金總額
bet = 100                           # 賭注
min, max = 1, 100                   # 隨機數最小與最大值設定
winPercent = int(input("請輸入莊家贏的比率(0-100)之間 :"))

while True:
    print(f"歡迎光臨 : 目前籌碼金額 {money} 美金 ")
    print(f"每次賭注 {bet} 美金 ")
    print("猜大小遊戲: L或l表示大,  S或s表示小, Q或q則程式結束")
    customerNum = input("= ")       # 讀取玩家輸入
    if customerNum == 'Q' or customerNum == 'q':    # 若輸入Q或q
        break                                       # 程式結束
    num = random.randint(min, max)  # 產生是否讓玩家答對的隨機數
    if num > winPercent:            # 隨機數在此區間回應玩家猜對
        print("恭喜!答對了\n")
        money += bet                # 賭金總額增加
    else:                           # 隨機數在此區間回應玩家猜錯
        print("答錯了!請再試一次\n")
        money -= bet                # 賭金總額減少
    if money <= 0:
        break

print("歡迎下次再來")

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

import string
import random
def encrypt(text, encryDict):           # 加密文件
    cipher = []
    for i in text:                      # 執行每個字元加密
        v = encryDict[i]                # 加密
        cipher.append(v)                # 加密結果
    return ''.join(cipher)              # 將串列轉成字串
    
abc = string.printable[:-5]             # 取消不可列印字元
newAbc = abc[:]                         # 產生新字串拷貝
abclist = list(newAbc)                  # 轉成串列
random.shuffle(abclist)                 # 打亂串列順序
subText = ''.join(abclist)              # 轉成字串
encry_dict = dict(zip(subText, abc))    # 建立字典
print("列印編碼字典\n", encry_dict)     # 列印字典

msg = 'If the implementation is easy to explain, it may be a good idea.'
ciphertext = encrypt(msg, encry_dict)

print("原始字串 ", msg)
print("加密字串 ", ciphertext)

print("------------------------------------------------------------")  # 60個

import random

# 假設一家公司想要測試兩種不同的廣告設計, 以看哪一種效果更好
ad_designs = ['Design A', 'Design B']

# 公司有一個1000人的郵件列表, 想要隨機選擇一半接收A廣告, 一半接收B廣告
recipients = {'Design A': [], 'Design B': []}

# 隨機分配郵件
for i in range(1, 1001):
    chosen_design = random.choice(ad_designs)       # 隨機選擇一種設計
    recipients[chosen_design].append(f'user_{i}')

# 確保每種設計都有500個用戶
while len(recipients['Design A']) != 500:
    if len(recipients['Design A']) > 500:
        user_to_move = recipients['Design A'].pop()
        recipients['Design B'].append(user_to_move)
    else:
        user_to_move = recipients['Design B'].pop()
        recipients['Design A'].append(user_to_move)

# 假設這裡會發送郵件，然後根據用戶反饋進行分析

# 輸出每種設計的接收者數量，確保它們是平均分配的
print(f"A 廣告接收者數量 : {len(recipients['Design A'])}")
print(f"B 廣告接收者數量 : {len(recipients['Design B'])}")

print("------------------------------------------------------------")  # 60個

import random

# 假設有一組伺服器
servers = ['Server1', 'Server2', 'Server3', 'Server4']

# 模擬1000次請求, 隨機分配到這些伺服器
requests = {server:0 for server in servers}
for _ in range(1000):
    selected_server = random.choice(servers)
    requests[selected_server] += 1

print(requests)         # 顯示每個伺服器獲得的請求數

print("------------------------------------------------------------")  # 60個

import random

# 假設生產線上有一批產品序列號
product_serials = list(range(1000, 2000))

# 抽檢10個產品進行品質檢查
samples = random.sample(product_serials, 10)

for serial in samples:
    # 這裡會有一個品質檢查的函數
    print(f"檢查序列號 : {serial}")

print("------------------------------------------------------------")  # 60個

import numpy as np
import matplotlib.pyplot as plt
from random import randint

def dice_generator(times, sides):
    """ 處理隨機數 """
    for i in range(times):              
        ranNum1 = randint(1, sides)             # 產生1-6隨機數
        ranNum2 = randint(1, sides)             # 產生1-6隨機數
        dice.append(ranNum1+ranNum2)
def dice_count(sides):
    """計算2-11個出現次數"""
    for i in range(2, 13):
        frequency = dice.count(i)               # 計算i出現在dice串列的次數
        frequencies.append(frequency)
plt.rcParams["font.family"] = ["Microsoft JhengHei"]          
times = 1000                                    # 擲骰子次數
sides = 6                                       # 骰子有幾面
dice = []                                       # 建立擲骰子的串列
frequencies = []                                # 儲存每一面骰子出現次數串列
dice_generator(times, sides)                    # 產生擲骰子的串列
dice_count(sides)                               # 將骰子串列轉成次數串列
N = len(frequencies)
x = np.arange(N)                                # 長條圖x軸座標
width = 0.35                                    # 長條圖寬度
plt.bar(x, frequencies, width, color='g')       # 繪製長條圖
plt.ylabel('出現次數')
plt.title('測試 1000 次', fontsize=16)
plt.xticks(x, ('2','3','4','5','6','7','8','9','10','11','12'))
plt.yticks(np.arange(0, 150, 15))
plt.show()



print("------------------------------------------------------------")  # 60個


import string
import random

def encrypt(text, encryDict):           # 加密文件
    cipher = []
    for i in text:                      # 執行每個字元加密
        v = encryDict[i]                # 加密
        cipher.append(v)                # 加密結果
    return ''.join(cipher)              # 將串列轉成字串

def decrypt(cipher, decryDict):         # 解密文件
    text = []
    for i in cipher:                    # 執行每個字元解密
        v = decryDict[i]                # 加密
        text.append(v)                  # 解密結果
    return ''.join(text)                # 將串列轉成字串
   
abc = string.printable[:-5]             # 取消不可列印字元
newAbc = abc[:]                         # 產生新字串拷貝
abclist = list(newAbc)                  # 轉成串列
random.shuffle(abclist)                 # 打亂串列順序
subText = ''.join(abclist)              # 轉成字串
encry_dict = dict(zip(subText, abc))    # 建立加密字典
decry_dict = dict(zip(abc, subText))    # 建立解密字典
print("列印解碼字典\n", decry_dict)     # 列印解碼字典

msg = 'If the implementation is easy to explain, it may be a good idea.'
ciphertext = encrypt(msg, encry_dict)
print("原始字串 ", msg)
print("加密字串 ", ciphertext)
decryMsg = decrypt(ciphertext, decry_dict)
print("解密字串 ", decryMsg)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

import random                               # 導入模組random
dices = []
for loop in range(1,4):
    for i in range(3):
        dice = random.randint(1,6)
        dices.append(dice)
    print("%d : 隨機3組骰子值 : " % loop, sorted(dices))
    for i in range(3):
        dices.pop()
    
print("------------------------------------------------------------")  # 60個

import random                       # 導入模組random

num = []
for i in range(600):
    num.append(random.choice([1,2,3,4,5,6]))
    
numCount = {i:num.count(i) for i in num}
for num in sorted(numCount.keys()):
    print(num, ':', numCount[num])

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

