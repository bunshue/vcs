# ch15_23.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]  
fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
fig.subplots_adjust()
# 定義程式語言人數 
lang = ['Python','C','Java', 'C++','PHP']
people = [350,200,250,150,270]
# 定義男女生人數
labelgender = ['男生', '女生']
gender = [720,500]
# 繪製程式語言人數圓餅圖
ax1.pie(people,autopct='%1.1f%%',startangle=20,labels=lang)
ax1.set_title("程式語言使用調查表",color='b')
# 繪製男女生圓餅圖
ax2.pie(gender,autopct='%1.1f%%',startangle=70,labels=labelgender,
        radius=0.7,colors=['lightgreen','yellow'])
ax2.set_title("男女生比例調查表",color='b')
plt.show()

