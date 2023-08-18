# ch23_6.py
from sklearn.metrics import r2_score
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,21,22,23,24]
y = [100,21,75,49,15,98,55,31,33,82,61,80,32,71,99,15,66,88,21,97,30,5]

coef = np.polyfit(x, y, 3)                              # 迴歸直線係數
model = np.poly1d(coef)                                 # 線性迴歸方程式
print(r2_score(y, model(x)).round(3))














