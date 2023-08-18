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




