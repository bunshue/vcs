"""
Python資料科學實戰教本



"""


import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個



import matplotlib.pyplot as plt

data = [-1, -4.3, 15, 21, 31]
plt.plot(data)  # x軸是 0,1,2,3,4
plt.show()




#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-1-1a.py

import matplotlib.pyplot as plt

data = [-1, -4.3, 15, 21, 31]
plt.plot(data, "o--b")  # x軸是 0,1,2,3,4
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-1-1b.py

import matplotlib.pyplot as plt

days = range(0, 22, 3)
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]
plt.plot(days, celsius)
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-1-1c.py

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, x, cosinus)
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-1-2.py

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, "r-o",
         x, cosinus, "g--")
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-1-2a.py

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, "r-o",
         x, cosinus, "g--")
plt.grid(True)
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-1-3.py

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

days = range(0, 22, 3)
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]
plt.plot(days, celsius)
plt.xlabel("日")
plt.ylabel("攝氏溫度")
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-1-3a.py

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, "r-o",
         x, cosinus, "g--")
plt.xlabel("徑度")
plt.ylabel("振幅")
plt.title("Sin和Cos三角函數的波型")
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-1-4.py

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, "r-o", label="sin(x)")
plt.plot(x, cosinus, "g--", label="cos(x)")
plt.legend()
plt.xlabel("徑度")
plt.ylabel("振幅")
plt.title("Sin和Cos三角函數的波型")
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-1-4a.py

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, "r-o", label="sin(x)")
plt.plot(x, cosinus, "g--", label="cos(x)")
plt.legend(loc=1)
plt.xlabel("徑度")
plt.ylabel("振幅")
plt.title("Sin和Cos三角函數的波型")
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-1-4b.py

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, "r-o", label="sin(x)")
plt.plot(x, cosinus, "g--", label="cos(x)")
plt.legend(loc=2)
plt.xlabel("徑度")
plt.ylabel("振幅")
plt.title("Sin和Cos三角函數的波型")
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-1-4c.py

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, "r-o", label="sin(x)")
plt.plot(x, cosinus, "g--", label="cos(x)")
plt.legend(loc=3)
plt.xlabel("徑度")
plt.ylabel("振幅")
plt.title("Sin和Cos三角函數的波型")
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-1-4d.py

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, "r-o", label="sin(x)")
plt.plot(x, cosinus, "g--", label="cos(x)")
plt.legend(loc=4)
plt.xlabel("徑度")
plt.ylabel("振幅")
plt.title("Sin和Cos三角函數的波型")
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-1-5.py

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

days = range(0, 22, 3)
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]
plt.plot(days, celsius)
plt.title("軸範圍: " + str(plt.axis()))
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-1-5a.py

import matplotlib.pyplot as plt

days = range(0, 22, 3)
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]
plt.plot(days, celsius)
xmin, xmax, ymin, ymax = -5, 25, 15, 35
plt.axis([xmin, xmax, ymin, ymax])
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-1-5b.py

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

days = range(1, 9)
celsius_min = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]
celsius_max = [27.6, 26.1, 22.5, 30.4, 29.5, 31.5, 35.1, 39.4]
plt.plot(days, celsius_min, "r-o",
         days, celsius_max, "g--o")
plt.xlabel("日")
plt.ylabel("攝氏溫度")
plt.axis([0, 10, 15, 40])
plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-1-6.py

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

days = range(1, 9)
celsius_min = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]
celsius_max = [27.6, 26.1, 22.5, 30.4, 29.5, 31.5, 35.1, 39.4]
plt.plot(days, celsius_min, "r-o",
         days, celsius_max, "g--o")
plt.xlabel("日")
plt.ylabel("攝氏溫度")
plt.axis([0, 10, 15, 40])
plt.savefig("Celsius.png")
plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-1-6a.py

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

days = range(1, 9)
celsius_min = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]
celsius_max = [27.6, 26.1, 22.5, 30.4, 29.5, 31.5, 35.1, 39.4]
plt.plot(days, celsius_min, "r-o",
         days, celsius_max, "g--o")
plt.xlabel("日")
plt.ylabel("攝氏溫度")
plt.axis([0, 10, 15, 40])
plt.savefig("Celsius.svg")
plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-1-6b.py

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

days = range(1, 9)
celsius_min = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]
celsius_max = [27.6, 26.1, 22.5, 30.4, 29.5, 31.5, 35.1, 39.4]
plt.plot(days, celsius_min, "r-o",
         days, celsius_max, "g--o")
plt.xlabel("日")
plt.ylabel("攝氏溫度")
plt.axis([0, 10, 15, 40])
plt.savefig("Celsius.pdf")
plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-2-1.py

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)
plt.scatter(x, y)
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-2-1a.py

import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(1000)
y = np.random.rand(1000)
size = np.random.rand(1000) * 50
color = np.random.rand(1000)
plt.scatter(x, y, size, color)
plt.colorbar()
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-2-2.py

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
 
labels = ["Python", "C++", "Java", "JS", "C", "C#"]
index = np.arange(len(labels))
ratings = [5.168, 5.726, 14.988, 3.165, 11.857, 4.453]
 
plt.bar(index, ratings)
plt.xticks(index, labels)
plt.ylabel("使用率")
plt.title("程式語言的使用率") 
plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-2-2a.py

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
 
labels = ["Python", "C++", "Java", "JS", "C", "C#"]
index = np.arange(len(labels))
ratings = [5.168, 5.726, 14.988, 3.165, 11.857, 4.453]
 
plt.barh(index, ratings)
plt.yticks(index, labels)
plt.ylabel("使用率")
plt.title("程式語言的使用率") 
plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-2-2b.py

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

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-2-3.py

import matplotlib.pyplot as plt

x = [21,42,23,4,5,26,77,88,9,10,31,32,33,34,35,36,37,18,49,50,100]
num_bins = 5
n, bins, patches = plt.hist(x, num_bins)
plt.title(str(n) + "\n" + str(bins))
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-2-3a.py

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)
num_bins = 50
plt.hist(x, num_bins)
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-2-4.py

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
 
labels = ["Python", "C++", "Java", "JS", "C", "C#"]
ratings = [5, 6, 15, 3, 12, 4]
 
plt.pie(ratings, labels=labels)
plt.title("程式語言的使用率")  
plt.axis("equal")
plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-2-4a.py

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
 
labels = ["Python", "C++", "Java", "JS", "C", "C#"]
ratings = [5, 6, 15, 3, 12, 4]
explode = (0, 0, 0, 0.2, 0, 0.2)
 
plt.pie(ratings, 
        labels=labels,
        explode=explode)
plt.title("程式語言的使用率")
plt.axis("equal")
plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-2-4b.py

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
 
labels = ["Python", "C++", "Java", "JS", "C", "C#"]
ratings = [5, 6, 15, 3, 12, 4]
explode = (0, 0, 0, 0.2, 0, 0.2)
 
patches, texts = plt.pie(ratings, 
                         labels=labels,
                         explode=explode)
plt.legend(patches, labels, loc="best")
plt.title("程式語言的使用率") 
plt.axis("equal")
plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-3-1.py

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.subplot(2, 1, 1)
plt.plot(x, sinus, "r-o")
plt.subplot(2, 1, 2)
plt.plot(x, cosinus, "g--")
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-3-1a.py

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.subplot(1, 2, 1)
plt.plot(x, sinus, "r-o")
plt.subplot(1, 2, 2)
plt.plot(x, cosinus, "g--")
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-3-1b.py

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
plt.subplot(231)
plt.plot(x, np.sin(x))
plt.subplot(232)
plt.plot(x, np.cos(x))
plt.subplot(233)
plt.plot(x, np.tan(x))
plt.subplot(234)
plt.plot(x, np.sinh(x))
plt.subplot(235)
plt.plot(x, np.cosh(x))
plt.subplot(236)
plt.plot(x, np.tanh(x))
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-3-2.py

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
sinhs = np.sinh(x)
fig, ax = plt.subplots()
ax.plot(x, sinus, "r-o")
ax2 = ax.twinx()
ax2.plot(x, sinhs, "g--")
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-3-2a.py

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
sinhs = np.sinh(x)
fig, ax = plt.subplots()
ax.plot(x, sinus, "r-o")
ax.set_xlabel("x", color="green")
ax.set_ylabel("Sin(x)", color="red")
ax2 = ax.twinx()
ax2.plot(x, sinhs, "g--")
ax2.set_ylabel("Sinh(x)", color="blue")
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-3-2b.py

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
sinhs = np.sinh(x)
fig, ax = plt.subplots()
ax.plot(x, sinus, "r-o", label="Sin(x)")
ax.set_xlabel("x", color="green")
ax.set_ylabel("Sin(x)", color="red")
ax.legend(loc="best")
ax2 = ax.twinx()
ax2.plot(x, sinhs, "g--", label="Sinh(x)")
ax2.set_ylabel("Sinh(x)", color="blue")
ax2.legend(loc="best")
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-3-2c.py

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
sinhs = np.sinh(x)
fig, ax = plt.subplots()
lns1 = ax.plot(x, sinus, "r-o", label="Sin(x)")
ax.set_xlabel("x", color="green")
ax.set_ylabel("Sin(x)", color="red")
ax2 = ax.twinx()
lns2 = ax2.plot(x, sinhs, "g--", label="Sinh(x)")
ax2.set_ylabel("Sinh(x)", color="blue")
# 自行建立圖例來顯示所有標籤
lns = lns1 + lns2
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc="best")
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-3-3.py

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
sinhs = np.sinh(x)
fig, ax = plt.subplots()
ax.plot(x, sinus, "r-o")
ax.set_xlabel("x", color="green")
ax.set_ylabel("Sin(x)", color="red")
ax2 = ax.twinx()
ax2.plot(x, sinhs, "g--")
ax2.set_ylabel("Sinh(x)", color="blue")
# 指定圖表標題文字
ax.set_title("Sin和Cos三角函數的波型", fontsize="large")
# 更改刻度的外觀
for tick in ax.xaxis.get_ticklabels():
    tick.set_fontsize("large")
    tick.set_fontname("Times New Roman")
    tick.set_color("blue")
    tick.set_weight("bold")   
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-3-3a.py

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

days = range(0, 22, 3)
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]
plt.plot(days, celsius)
plt.xlabel("日")
plt.ylabel("攝氏溫度")
locs1, labels = plt.xticks()
locs2, labels = plt.yticks()
plt.title(str(locs1) + "\n" + str(locs2))
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-3-3b.py

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

days = range(0, 22, 3)
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]
plt.plot(days, celsius)
plt.xlabel("日")
plt.ylabel("攝氏溫度")
plt.xticks(range(0, 25, 2))
plt.yticks(range(15, 35, 3))
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-3-3c.py

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
sinhs = np.sinh(x)
fig, ax = plt.subplots()
ax.plot(x, sinus, "r-o")
ax.set_xlabel("x", color="green")
ax.set_ylabel("Sin(x)", color="red")
ax2 = ax.twinx()
ax2.plot(x, sinhs, "g--")
ax2.set_ylabel("Sinh(x)", color="blue")
plt.xticks(range(0, 11))
ax.set_yticks(np.linspace(-1, 1, 10))
ax2.set_yticks(np.linspace(0, 12000, 10))
plt.show()


print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




