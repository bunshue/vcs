# ch19_19.py
import numpy as np
import matplotlib.pyplot as plt
times = [1,2,3]                                         # 臉書行銷次數
rev = [10,18,19]                                        # 增加業績 

coef = np.polyfit(times, rev, 2)                        # 二次函數係數
reg = np.poly1d(coef)                                   # 二次函數迴歸方程式
print(reg)    
plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體
plt.scatter(times, rev)
plt.plot(times,reg(times),color='red')
plt.title('臉書行銷與業績增加金額')
plt.xlabel("臉書行銷次數", fontsize=14)
plt.ylabel("增加業績金額", fontsize=14)
plt.show()










