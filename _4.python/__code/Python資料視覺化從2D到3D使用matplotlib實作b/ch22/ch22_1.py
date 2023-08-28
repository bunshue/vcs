# ch22_1.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
x = [9, 12, 30, 31, 31, 32, 33, 33, 35, 35,
     38, 38, 41, 42, 43, 46, 46, 48, 52, 70]
fig, ax = plt.subplots(nrows=1, ncols=2)
ax[0].set_title("小提琴圖")
ax[0].violinplot(x)
ax[1].set_title("箱線圖")
ax[1].boxplot(x)
plt.show()


      
