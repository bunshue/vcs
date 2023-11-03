# ch20_29.py
import matplotlib.pyplot as plt

sorts = ["Travel","Entertainment","Education","Transporation","Food"]
fee = [8000,2000,3000,5000,6000]
          
plt.pie(fee,labels=sorts,explode=(0,0.3,0,0,0),
        autopct="%1.2f%%")      # 繪製圓餅圖
plt.show()

