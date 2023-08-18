# ch23_3.py
from sklearn.metrics import r2_score
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,21,22,23,24]
y = [100,88,75,60,50,55,55,56,58,58,61,63,68,71,71,75,76,88,93,97,97,100]

coef = np.polyfit(x, y, 3)                              # 迴歸直線係數
model = np.poly1d(coef)                                 # 線性迴歸方程式
print(r2_score(y, model(x)).round(3))


















