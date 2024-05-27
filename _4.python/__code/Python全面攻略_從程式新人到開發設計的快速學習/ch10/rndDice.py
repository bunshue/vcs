import matplotlib.pyplot as plt
import random as rnd

plt.rcParams['font.sans-serif']='mingliu'
dices=['1點','2點','3點','4點','5點','6點']
data=[]
times=[]
for i in range(1000):
    data.append(rnd.randint(1,6))

for i in range(1,7):
    times.append(data.count(i))
    
plt.pie(times,labels=dices,autopct='%2.1f%%',explode=[0.1,0.1,0.1,0.1,0.1,0.1],shadow=True)
plt.title('擲骰子機率圖',fontsize=18)
plt.show()

