# ch15_19.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]    
lang = ["Python","C","Java","C++","PHP"]    # 程式語言標籤
people = [350,200,250,150,270]              # 人數
labelgender = ['男生','女生']               # 性別標籤
gender = [720,500]                          # 性別人數
colors = ['lightyellow','lightgreen']       # 自定性別色彩
data_no = [1,0,0,0]
# 建立外層程式語言圓餅圖
plt.pie(people,pctdistance=0.8,labels=lang,autopct="%1.2f%%")
# 建立內層性別標籤
plt.pie(gender,radius=0.6,labels=labelgender,colors=colors,
        autopct="%1.2f%%",labeldistance=0.45)
plt.pie(data_no,radius=0.2,colors='w')      # 建立最內層空的圓餅
plt.title("程式語言調查表",fontsize=16,color='b')
plt.show()


