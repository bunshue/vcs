import sys

import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個




#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch14\ch14_1.py

# ch14_1.py
import matplotlib.pyplot as plt
import math 
def probability(k):
    num = (math.factorial(n))/(math.factorial(n-k)*math.factorial(k))
    pro = num * success**k * (1-success)**(n-k)
    return pro
    
n = 5                                           # 銷售次數                       # 成功機率
success = 0.75                                  # 銷售成功機率
fail = 1 - success                              # 銷售失敗機率
p = []                                          # 儲存成功機率

for k in range(0,n+1):
    if k == 0:
        p.append(fail**n)                       # 連續n次失敗機率
        continue
    if k == n:
        p.append(success**n)                    # 連續n次成功機率
        continue
    p.append(probability(k))                    # 計算其他次成功機率

for i in range(len(p)):
    print('銷售 {} 單位成功機率 {}%'.format(i, p[i]*100))
        
x = [i for i in range(0, n+1)]                  # 長條圖x軸座標
width = 0.35                                    # 長條圖寬度
plt.xticks(x)
plt.bar(x, p, width, color='g')                 # 繪製長條圖
plt.ylabel('Probability')
plt.xlabel('unit:100')
plt.title('Binomial Dristribution')
plt.show()





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch14\ch14_2.py

# ch14_2.py
import matplotlib.pyplot as plt
import math 
def probability(k):
    num = (math.factorial(n))/(math.factorial(n-k)*math.factorial(k))
    pro = num * success**k * (1-success)**(n-k)
    return pro
    
n = 10                                          # 銷售次數                       # 成功機率
success = 0.35                                  # 銷售成功機率
fail = 1 - success                              # 銷售失敗機率
p = []                                          # 儲存成功機率

for k in range(0,n+1):
    if k == 0:
        p.append(fail**n)                       # 連續n次失敗機率
        continue
    if k == n:
        p.append(success**n)                    # 連續n次成功機率
        continue
    p.append(probability(k))                    # 計算其他次成功機率

for i in range(len(p)):
    print('銷售 {} 單位成功機率 {}%'.format(i, p[i]*100))
        
x = [i for i in range(0, n+1)]                  # 長條圖x軸座標
width = 0.35                                    # 長條圖寬度
plt.xticks(x)
plt.bar(x, p, width, color='g')                 # 繪製長條圖
plt.ylabel('Probability')
plt.xlabel('unit:100')
plt.title('Binomial Dristribution')
plt.show()





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch14\ch14_3.py

import matplotlib.pyplot as plt
import numpy as np

import seaborn as sns #海生, 自動把圖畫得比較好看

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.title('二項式分布 Binomial')
plt.xlabel("銷售張數", fontsize=14)
plt.ylabel("成功次數", fontsize=14)
sns.histplot(np.random.binomial(n=5, p=0.75, size=1000), kde=False)

plt.show()













print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch14\ch14_4.py

import matplotlib.pyplot as plt
import numpy as np

import seaborn as sns #海生, 自動把圖畫得比較好看

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.title('二項式分布 Binomial')
plt.xlabel("銷售張數", fontsize=14)
plt.ylabel("成功次數", fontsize=14)
sns.histplot(np.random.binomial(n=10, p=0.35, size=1000), kde=False)

plt.show()













print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

