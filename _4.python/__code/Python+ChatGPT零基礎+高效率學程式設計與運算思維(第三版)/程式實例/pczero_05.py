import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

# ex21_2.ipynb
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


# ex24_2.ipynb
from sklearn.metrics import r2_score
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,20,21,22,23,24]
y = [50,30,25,20,15,20,30,40,58,62,77,90,100,125,128,130,150,120,88,95,97,80]

coef = np.polyfit(x, y, 3)                          # 迴歸直線係數
model = np.poly1d(coef)                             # 線性迴歸方程式
print(f"18點購物人數預測 = {model(15).round(2)}")
print(f"20點購物人數預測 = {model(20).round(2)}")


print('------------------------------------------------------------')	#60個


# ex24_4.ipynb
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




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個





