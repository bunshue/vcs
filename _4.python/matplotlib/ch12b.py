
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)
plt.scatter(x, y)
plt.show()




print('------------------------------')  #30個

x = np.random.rand(1000)
y = np.random.rand(1000)
size = np.random.rand(1000) * 50
color = np.random.rand(1000)
plt.scatter(x, y, size, color)
plt.colorbar()
plt.show()


print('------------------------------')  #30個

labels = ["Python","C++","Java","JS","C","C#"]
index = np.arange(len(labels))
ratings = [5.16, 5.73, 14.99, 3.17, 11.86, 4.45]
change = [1.12, 0.3, -1.69, 0.29, 3.41, -0.45]


plt.bar(index, ratings)
plt.xticks(index, labels)
plt.ylabel("使用率")
plt.title("程式語言的使用率") 
plt.show()



print('------------------------------')  #30個

plt.barh(index, ratings)
plt.yticks(index, labels)
plt.xlabel("使用率")
plt.title("程式語言的使用率") 
plt.show()



print('------------------------------')  #30個

index = np.arange(len(labels)*2)

plt.bar(index[0::2], ratings, label="rating")
plt.bar(index[1::2], change, label="change",
        color="r")
plt.legend()
plt.xticks(index[0::2], labels)
plt.ylabel("使用率")
plt.title("程式語言的使用率") 
plt.show()

print('------------------------------')  #30個

x = [21,42,23,4,5,26,77,88,9,10,31,32,33,
     34,35,36,37,18,49,50,100]
num_bins = 5
n, bins, patches = plt.hist(x, num_bins)
print(n)
print(bins)
plt.show()




print('------------------------------')  #30個


x = np.random.randn(1000)
num_bins = 50
plt.hist(x, num_bins)
plt.show()


print('------------------------------')  #30個

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







print('------------------------------')  #30個






print('------------------------------')  #30個


print('------------------------------')  #30個





print('------------------------------')  #30個


print('------------------------------')  #30個





