# ch15_21.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]    
product = ["家電","生活用品","圖書","保健","彩妝"]  # 產品標籤
revenue = [23000,18000,12000,15000,16000]           # 業績
patches = plt.pie(revenue,labels=product,autopct="%1.2f%%")
plt.legend(patches[0],product,loc='center left',
           title="產品類別",
           bbox_to_anchor=(1,0,0.5,1))
plt.title("銷售品項分析",fontsize=16,color='b')
plt.show()


