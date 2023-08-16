'''
有 numpy 的 matplotlib

'''

import matplotlib.pyplot as plt
import numpy as np

selected_font = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, x, cosinus)
plt.show()

print('------------------------------------------------------------')	#60個

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, "r-o",
         x, cosinus, "g--")
plt.xlabel("徑度")
plt.ylabel("振幅")
plt.title("Sin 和 Cos 波形")
plt.show()

print('------------------------------------------------------------')	#60個

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, "r-o", label="sin(x)")
plt.plot(x, cosinus, "g--", label="cos(x)")
plt.legend(loc=1)
plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.subplot(2, 1, 1)
plt.plot(x, sinus, "r-o")
plt.subplot(2, 1, 2)
plt.plot(x, cosinus, "g--")
plt.show()

print('------------------------------------------------------------')	#60個


x = np.linspace(0, 10, 50)
plt.subplot(1, 2, 1)
plt.plot(x, np.sin(x), "r-o")
plt.subplot(1, 2, 2)
plt.plot(x, np.cos(x), "g--")
plt.show()

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
sinhs = np.sinh(x)

fig, ax = plt.subplots()
ax.plot(x, sinus, "r-o")
ax2 = ax.twinx()
ax2.plot(x, sinhs, "g--")
plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)
plt.scatter(x, y)
plt.show()

print('------------------------------------------------------------')	#60個

x = np.random.rand(1000)
y = np.random.rand(1000)
size = np.random.rand(1000) * 50
color = np.random.rand(1000)
plt.scatter(x, y, size, color)
plt.colorbar()
plt.show()


print('------------------------------------------------------------')	#60個

labels = ["Python","C++","Java","JS","C","C#"]
index = np.arange(len(labels))
ratings = [5.16, 5.73, 14.99, 3.17, 11.86, 4.45]
change = [1.12, 0.3, -1.69, 0.29, 3.41, -0.45]


plt.bar(index, ratings)
plt.xticks(index, labels)
plt.ylabel("使用率")
plt.title("程式語言的使用率") 
plt.show()



print('------------------------------------------------------------')	#60個

plt.barh(index, ratings)
plt.yticks(index, labels)
plt.xlabel("使用率")
plt.title("程式語言的使用率") 
plt.show()



print('------------------------------------------------------------')	#60個

index = np.arange(len(labels)*2)

plt.bar(index[0::2], ratings, label="rating")
plt.bar(index[1::2], change, label="change",
        color="r")
plt.legend()
plt.xticks(index[0::2], labels)
plt.ylabel("使用率")
plt.title("程式語言的使用率") 
plt.show()

print('------------------------------------------------------------')	#60個

x = [21,42,23,4,5,26,77,88,9,10,31,32,33,
     34,35,36,37,18,49,50,100]
num_bins = 5
n, bins, patches = plt.hist(x, num_bins)
print(n)
print(bins)
plt.show()




print('------------------------------------------------------------')	#60個


x = np.random.randn(1000)
num_bins = 50
plt.hist(x, num_bins)
plt.show()


print('------------------------------------------------------------')	#60個

labels = ["Python","C++","Java","JS","C","C#"]
ratings = [5, 6, 15, 3, 12, 4]

plt.pie(ratings, labels=labels)
plt.title("程式語言的使用率") 
plt.axis("equal")
plt.show()


patches, texts = plt.pie(ratings, labels=labels)
plt.legend(patches, labels, loc="best")
plt.title("程式語言的使用率") 
plt.axis("equal")
plt.show()







print('------------------------------------------------------------')	#60個






print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個







print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個





