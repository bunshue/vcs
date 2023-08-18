# ch23_4.py
from sklearn.metrics import r2_score
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,21,22,23,24]
y = [100,88,75,60,50,55,55,56,58,58,61,63,68,71,71,75,76,88,93,97,97,100]

coef = np.polyfit(x, y, 3)                              # 迴歸直線係數
model = np.poly1d(coef)                                 # 線性迴歸方程式
print(f"18點購物人數預測 = {model(18).round(2)}")
print(f"20點購物人數預測 = {model(20).round(2)}")


















