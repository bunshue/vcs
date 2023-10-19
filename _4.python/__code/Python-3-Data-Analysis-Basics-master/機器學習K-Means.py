"""
機器學習 K-Means

K-Means 自動分類

"""

import sys
import numpy as np
import matplotlib.pyplot as plt

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

#K-Means 會自動分類!
#我們介紹一個很好用的 unsupervised learning, 叫 K-Means。
#我們可以指定把我們資料分成幾類, 然後它就會快速分好!

#隨便生個 100 點
x = np.random.rand(100, 2)

plt.scatter(x[:,0], x[:,1], s = 50)
plt.title('原始資料')
plt.show()

#製做一個 K-Means 分類器
#和 SVM 很像。

from sklearn.cluster import KMeans

#記得要告訴 K-Means 要分成幾類 (我們這裡是 3 類)。

clf = KMeans(n_clusters = 3)

clf.fit(x)

#訓練好的結果, 在神秘的 labels_ 之下。
Z = clf.labels_
#print(Z)

plt.scatter(x[:,0], x[:,1], s = 50, c = Z)
plt.title('訓練好的結果1')
plt.show()


gd = np.array([[i, j] for i in np.arange(-0.8, 1.2, 0.1) for j in np.arange(-0.8, 1.2, 0.1)])
gdc = clf.predict(gd)
plt.scatter(gd[:,0], gd[:,1], s=50, cmap=plt.cm.coolwarm, c=gdc)
plt.title('訓練好的結果2')
plt.show()

plt.scatter(gd[:,0], gd[:,1], s=50, cmap=plt.cm.prism, c=gdc)
plt.title('訓練好的結果3')
plt.show()

plt.scatter(gd[:,0], gd[:,1], s=50, cmap=plt.cm.Set1, c=gdc)

plt.title('訓練好的結果4')
plt.show()


#畫完整分類
#和以前一樣, 未來新的資料進來, 我們訓練好的也可以再做分類。

x1, x2 = np.meshgrid(np.arange(-0.2,1.2,0.02), np.arange(-0.2,1.2,0.02))
Z = clf.predict(np.c_[x1.ravel(), x2.ravel()])

z = Z.reshape(x1.shape)

plt.contourf(x1, x2, z, alpha = 0.3)
plt.scatter(x[:, 0], x[:, 1], s = 100, c = clf.labels_)

plt.title('畫完整分類')
plt.show()

print('------------------------------------------------------------')	#60個

import pickle

f = open("clf.pkl", "wb")
pickle.dump(clf, f)
f.close()

f = open("clf.pkl", 'rb')
clf2 = pickle.load(f)
print(clf2.predict([[3,4]]))

f.close()


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('作業完成')

