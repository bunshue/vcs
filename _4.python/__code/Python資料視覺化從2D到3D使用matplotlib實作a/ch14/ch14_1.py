# ch14_1.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
x = [4,3,3,2,5,4,5,6,9,4,5,5,3,0,1,7,8,7,5,6,4]
plt.hist(x)
plt.title('直方圖')
plt.xlabel('值')
plt.ylabel('頻率')
plt.show()


      
