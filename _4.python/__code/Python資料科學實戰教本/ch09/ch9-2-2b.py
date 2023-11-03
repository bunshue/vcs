import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
 
labels = ["Python", "C++", "Java", "JS", "C", "C#"]
index = np.arange(len(labels)*2)
ratings = [5.168, 5.726, 14.988, 3.165, 11.857, 4.453]
change = [1.12, 0.3, -1.69, 0.29, 3.41, -0.45]
 
plt.bar(index[0::2], ratings, label="使用率")
plt.bar(index[1::2], change, label="增減值", color="r")
plt.legend()
plt.xticks(index[0::2], labels)
plt.ylabel("使用率")
plt.title("程式語言的使用率") 
plt.show()
