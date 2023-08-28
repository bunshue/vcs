# ch13_11.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
revenue = [300, 320, 400, 350]
cost = [250, 280, 310, 290]
quarter = ['Q1','Q2','Q3','Q4']

barH = 0.5
plt.barh(quarter,revenue,color='g',height=barH,label='收入')
plt.barh(quarter,-np.array(cost),color='m',height=barH,label='支出')
plt.title("公司收支表", fontsize=24, color='b')
plt.xlabel("收入與支出", fontsize=14, color='b')
plt.ylabel("季度", fontsize=14, color='b')
plt.legend()
plt.show()


      
