# ch15_14.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
area = ['大陸','東南亞','東北亞','美國','歐洲','澳紐']
people = [10000,12600,9600,7500,5100,4800]

fig, axs = plt.subplots(nrows=2, ncols=2)       # 建立 2 x 2 子圖
# 建立 [0,0]子圖
axs[0,0].pie(people,labels=area,autopct="%1.2f%%",
        wedgeprops={'ec':'w','hatch':'-'})
axs[0,0].set_title("hatch = '-'",color='m')
# 建立 [0,1]子圖
axs[0,1].pie(people,labels=area,autopct="%1.2f%%",
        wedgeprops={'ec':'w','hatch':'+'})
axs[0,1].set_title("hatch = '+'",color='m')
# 建立 [1,0]子圖
axs[1,0].pie(people,labels=area,autopct="%1.2f%%",
        wedgeprops={'ec':'w','hatch':'o'})
axs[1,0].set_title("hatch = 'o'",color='m')
# 建立 [1,1]子圖
axs[1,1].pie(people,labels=area,autopct="%1.2f%%",
        wedgeprops={'ec':'w','hatch':'*'})
axs[1,1].set_title("hatch = '*'",color='m')
plt.suptitle('使用 wedgeprops 字典的 hatch 參數',fontsize=16,color='b')
fig.tight_layout()
plt.show()


      
