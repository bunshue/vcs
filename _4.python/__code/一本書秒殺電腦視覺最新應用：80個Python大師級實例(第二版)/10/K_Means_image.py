import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans  #导入kmeans
from sklearn.utils import shuffle
import numpy as np
from skimage import io
import warnings

#plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

warnings.filterwarnings('ignore')
#original = mpl.image.imread('frog.jpg')
original = plt.imread('frog.jpg')
width,height,depth = original.shape
temp = original.reshape(width*height,depth)
temp = np.array(temp, dtype=np.float64) / 255

original_sample = shuffle(temp, random_state=0)[:1000] #随机取1000个RGB值作为训练集


def cluster(k):
    estimator = KMeans(n_clusters=k,n_jobs=8,random_state=0)#构造聚类器
    kmeans = estimator.fit(original_sample)#聚类   
    return kmeans

    
def recreate_image(codebook, labels, w, h):
    d = codebook.shape[1]
    image = np.zeros((w, h, d))
    label_idx = 0
    for i in range(w):
        for j in range(h):
            image[i][j] = codebook[labels[label_idx]]
            label_idx += 1
    return image


kmeans = cluster(32)
labels = kmeans.predict(temp)
kmeans_32 = recreate_image(kmeans.cluster_centers_, labels,width,height)
kmeans = cluster(64)
labels = kmeans.predict(temp)
kmeans_64 = recreate_image(kmeans.cluster_centers_, labels,width,height)
kmeans = cluster(128)
labels = kmeans.predict(temp)
kmeans_128 = recreate_image(kmeans.cluster_centers_, labels,width,height)

plt.figure(figsize = (15,10))

plt.subplot(2,2,1)
plt.axis('off')
plt.title('原始图像')
plt.imshow(original.reshape(width,height,depth))

plt.subplot(2,2,2)
plt.axis('off')
plt.title('量化的图像(128颜色, K-Means)')
plt.imshow(kmeans_128)
io.imsave('kmeans_128.png',kmeans_128)

plt.subplot(2,2,3)
plt.axis('off')
plt.title('量化的图像(64颜色, K-Means)')
plt.imshow(kmeans_64)
io.imsave('kmeans_64.png',kmeans_64)

plt.subplot(2,2,4)
plt.axis('off')
plt.title('量化的图像(32颜色, K-Means)')
plt.imshow(kmeans_32)
io.imsave('kmeans_32.png',kmeans_32)

plt.show()
