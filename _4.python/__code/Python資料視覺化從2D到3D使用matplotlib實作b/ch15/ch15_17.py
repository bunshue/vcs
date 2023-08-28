# ch15_17.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]    
sorts = ["交通","娛樂","教育","交通","餐費"]
fee = [8000,2000,3000,5000,6000]
fee_no = [1,0,0,0]          
plt.pie(fee,pctdistance=0.8,labels=sorts,autopct="%1.2f%%")      
plt.pie(fee_no,radius=0.6,colors='w')
plt.title("統計個人花費的環圈圖設計",fontsize=16,color='b')
plt.show()

