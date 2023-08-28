# ch16_2.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
x = [9, 12, 30, 31, 31, 32, 33, 33, 35, 35,
     38, 38, 41, 42, 43, 46, 46, 48, 52, 70]
labels = ["x_label"]
plt.boxplot(x, labels=labels)
plt.title("使用Boxplot函數") 
plt.show()


      
