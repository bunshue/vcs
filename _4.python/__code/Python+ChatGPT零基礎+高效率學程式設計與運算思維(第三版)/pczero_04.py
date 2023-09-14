import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

import csv

fn = 'csvReport.csv'
with open(fn) as csvFile:               # 開啟csv檔案
    csvReader = csv.reader(csvFile)     # 讀檔案建立Reader物件
    listReport = list(csvReader)        # 將資料轉成串列
total2025 = 0
total2026 = 0
for row in listReport:
    if row[0] == 'Steve':
        if row[1] == '2025':
            total2025 += int(row[5])
        if row[1] == '2026':
            total2026 += int(row[5])

print("Steve's Total Revenue of 2025 = ", total2025)
print("Steveis Total Revenue of 2026 = ", total2026)

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import numpy as np

left = -2 * np.pi
right = 2 * np.pi
x = np.linspace(left, right, 50)

f1 = 3 * np.sin(x)                  # y陣列的變化
f2 = np.sin(x)
f3 = 0.2 * np.sin(x)

plt.plot(x, f1) 
plt.plot(x, f2, '-x')
plt.plot(x, f3)
plt.plot(x, f1, 'go')
plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import numpy as np

trials = 2000
Hits = 0
radius = 50
for i in range(trials):
    x = np.random.randint(1, 100)               # x軸座標
    y = np.random.randint(1, 100)               # y軸座標
    if np.sqrt((x-50)**2 + (y-50)**2) < radius: # 在圓內
        plt.scatter(x, y, marker='.', c='y')
        Hits += 1
    else:
        plt.scatter(x, y, marker='.', c='g')    
plt.axis('equal')
plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import random

def loc(index):
    ''' 處理座標的移動 '''
    x_mov = random.choice([-3,-2,-1,1,2,3])     # 隨機x軸移動值
    xloc = x[index-1] + x_mov                   # 計算x軸新位置
    y_mov = random.choice([-5,-3,-1,1,3,5])     # 隨機y軸移動值
    yloc = y[index-1] + y_mov                   # 計算y軸新位置
    x.append(xloc)                              # x軸新位置加入串列
    y.append(yloc)                              # y軸新位置加入串列
    
num = 10000                                     # 設定隨機點的數量
x = [0]                                         # 設定第一次執行x座標
y = [0]                                         # 設定第一次執行y座標

for i in range(1, num):                     # 建立點的座標
    loc(i)
t = x                                       # 色彩隨x軸變化
plt.scatter(x, y, s=2, c=t, cmap='brg')
plt.axis('off')
plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt

data1 = [1, 2, 3, 4, 5, 6, 7, 8]                # data1線條
data2 = [1, 4, 9, 16, 25, 36, 49, 64]           # data2線條
data3 = [1, 3, 6, 10, 15, 21, 28, 36]           # data3線條
data4 = [1, 7, 15, 26, 40, 57, 77, 100]         # data4線條
data5 = [1, 6, 11, 16, 21, 26, 31, 36]          # data5線條
seq = [1, 2, 3, 4, 5, 6, 7, 8]

plt.subplot(2, 3, 1)
plt.plot(seq, data1, '-*')

plt.subplot(2, 3, 2)
plt.plot(seq, data2, '-o')

plt.subplot(2, 3, 3)
plt.plot(seq, data3, '-^')

plt.subplot(2, 3, 4)
plt.plot(seq, data4, '-s')

plt.subplot(2, 3, 6)
plt.plot(seq, data5, '-v')

plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt 
import numpy as np
from random import randint

def dice_generator(times, sides):
    #處理隨機數
    for i in range(times):              
        ranNum1 = randint(1, sides)             # 產生1-6隨機數
        ranNum2 = randint(1, sides)             # 產生1-6隨機數
        dice.append(ranNum1+ranNum2)
def dice_count(sides):
    #計算2-11個出現次數
    for i in range(2, 13):
        frequency = dice.count(i)               # 計算i出現在dice串列的次數
        frequencies.append(frequency)       
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

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt 

country = ["美國","澳洲","日本","歐洲","英國"]
pou = [10543, 2105, 1190, 3346, 980]
          
plt.pie(pou,labels=country,explode=(0,0,0.2,0,0),
        autopct="%1.2f%%")                          # 繪製圓餅圖
plt.show()

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

import bs4, requests

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

print('------------------------------------------------------------')	#60個

from sklearn.metrics import r2_score
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,20,21,22,23,24]
y = [50,30,25,20,15,20,30,40,58,62,77,90,100,125,128,130,150,120,88,95,97,80]

coef = np.polyfit(x, y, 3)                          # 迴歸直線係數
model = np.poly1d(coef)                             # 線性迴歸方程式
print(f"18點購物人數預測 = {model(15).round(2)}")
print(f"20點購物人數預測 = {model(20).round(2)}")

print('------------------------------------------------------------')	#60個

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data, label = make_blobs(n_samples=1000,n_features=2,
                         centers=2,random_state=5)
d_sta = StandardScaler().fit_transform(data)    # 標準化
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(d_sta,
                   label,test_size=0.2,random_state=0)
# 建立分類模型                                             
lo_model = LogisticRegression()
# 建立訓練數據模型
lo_model.fit(dx_train, label_train)
# 對測試數據做預測
pred = lo_model.predict(dx_test)
# 輸出測試數據的 label
print(label_test)
# 輸出預測數據的 label
print(pred)
# 輸出準確性
print(f"訓練資料的準確性 = {lo_model.score(dx_train, label_train)}")
print(f"測試資料的準確性 = {lo_model.score(dx_test, label_test)}")

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

'''
import openai
import os

# 設定API金鑰
openai.api_key = "OPENAI_API_KEY"

# 設定模型和提示語
model_engine = "text-davinci-002"
prompt = "Hi!"

# 設定對話參數
temperature = 0.7
max_tokens = 60
top_p = 1.0

# 定義對話函數
def chat(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
    )
    message = response.choices[0].text.strip()
    return message
print("歡迎來到深智 Deepmind 客服中心")
# 執行對話
while True:
    user_input = input("親愛客戶 : ")
    if user_input == "bye":
        break
    prompt += user_input.strip() + "\n"
    response = chat(prompt)
    print("ChatGPT  : " + response)
    prompt += response + "\n"
'''


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

filename = 'data14_8.txt'         # 設定欲開啟的檔案
with open(filename, 'r', encoding='cp950') as fObj:
    print(f"指針位置 {fObj.tell()}")    
    txt1 = fObj.read(3)
    print(f"{txt1}, 指針位置 {fObj.tell()}")
    txt2 = fObj.read(3)
    print(f"{txt2}, 指針位置 {fObj.tell()}")
    txt3 = fObj.read(3)
    print(f"{txt3}, 指針位置 {fObj.tell()}")     

print('------------------------------------------------------------')	#60個

filename = 'data14_9.txt'             # 設定欲開啟的檔案
chunk = 100
msg = ''
with open(filename, 'r', encoding='cp950') as fObj: 
    while True:
        txt = fObj.read(chunk)  # 一次讀取chunk數量
        if not txt:
            break
        msg += txt
print(msg)

print('------------------------------------------------------------')	#60個

print('複製binary檔案')

filename1 = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2 = 'picture1_copied.jpg'

tmp = ''

with open(filename1, 'rb') as file_rd:
    tmp = file_rd.read()
    with open(filename2, 'wb') as file_wr:
        file_wr.write(tmp)

print('------------------------------------------------------------')	#60個

dst = 'random_data.bin'
bytedata = bytes(range(0,256))
with open(dst, 'wb') as file_dst:
    file_dst.write(bytedata)

print('------------------------------------------------------------')	#60個

src = 'random_data.bin'

with open(src, 'rb') as file_src:
    print("目前位移 : ", file_src.tell())
    file_src.seek(10)
    print("目前位移 : ", file_src.tell())
    data = file_src.read()
    print("目前內容 : ", data[0])
    file_src.seek(255)
    print("目前位移 : ", file_src.tell())
    data = file_src.read()
    print("目前內容 : ", data[0])

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


