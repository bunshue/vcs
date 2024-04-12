import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def svd_restore(sigma, u, v, K):
    K = min(len(sigma)-1, K)     #当K超过sigma的长度时会造成越界
    print('现在用%d等级恢复图像' % K)
    m = len(u)
    n = v[0].size
    SigRecon = np.zeros((m, n)) #新建一int矩阵，储存恢复的灰度图像素
    for k in range(K+1):    #计算X=u*sigma*v
        for i in range(m):
            SigRecon[i] += sigma[k] * u[i][k] * v[k]
    #计算得到的矩阵还是float型，需要将其转化为uint8以转为图片
    SigRecon = SigRecon.astype('uint8') 
    Image.fromarray(SigRecon).save("svd_" + str(K) + "_" +image_file) #保存灰度图
    
image_file = u'frog.jpg'
if __name__ == '__main__':
    im = Image.open(image_file)    #打开图像文件
    im = im.convert('L')           #将原图像转化为灰度图
    im.save("Gray_" + image_file)  #保存灰度图
    
    w, h = im.size                 #得到原图的长与宽
    #新建一int矩阵，储存灰度图各像素点数据
    dt = np.zeros((w, h), 'uint8') 
    #逐像素点复制，由于直接对im.getdata()进行数据类型转换会有偏差
    for i in range(w):            
        for j in range(h):
            dt[i][j] = im.getpixel((i, j))  # 取得該點之像素值
    #复制过来的图像是原图的翻转，因此将其再次翻转到正常角度
    dt = dt.transpose()            
    u, sigma, v = np.linalg.svd(dt)#调用numpy库进行SVM
    u = np.array(u)                #转为array格式，方便进行乘法运算
    v = np.array(v)                #同上
    for k in [1, 10, 30, 50, 80, 100, 150, 200, 300, 500]:
        svd_restore(sigma, u, v, k)#使用前k个奇异值进行恢复
        
