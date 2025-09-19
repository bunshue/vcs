import sys
import cv2


def Fast_detect_fault(img_01):
    # FastFeatureDetector_create()创建一个搜寻特征点的对象，并寻找图像中的特征点
    fast = cv2.FastFeatureDetector_create()    #初始化(参数可不写,也可以写入数字)
    keypoint = fast.detect(img_01,None)
    img_01 = cv2.drawKeypoints(img_01,keypoint,img_01,color=(255,0,0))
    cv2.imshow('brid.png',img_01)

    #打印所有默认参数
    print ("阈值: ", fast.getThreshold())
    print ("非最大抑制值: ", fast.getNonmaxSuppression())
    print ("邻近值: ", fast.getType())
    print ("带有非非最大抑制的总关键点: ", len(keypoint))

def Fast_detect_Setparam(img_02): 
    #fast.setNonmaxSuppression(100)使用fast.setNonmaxSuppression来设置默认参数
    threshold=(5,10,100)
    for thre in threshold:
        fast_02 = cv2.FastFeatureDetector_create(threshold=thre, nonmaxSuppression=True,
                                              type=cv2.FAST_FEATURE_DETECTOR_TYPE_5_8) #获取FAST角点探测器
        kp = fast_02.detect(img_02, None)         #描述符
        img_0 = cv2.drawKeypoints(img_02, kp, img_02, color=(255, 0, 0)) #画到img上面
        cv2.imshow('sp_'+str(thre),img_02)
        # Print all set params
        print("阈值: ", fast_02.getThreshold())        #输出阈值
        print("非最大抑制值: ", fast_02.getNonmaxSuppression()) #是否使用非极大值抑制
        print("邻近值: ", fast_02.getType())
        print("带有非非最大抑制的总关键点: ", len(kp))#特征点个数
        cv2.waitKey(0)

img_01 = cv2.imread('brid.png')
img_02 = cv2.imread('house.png')
Fast_detect_fault(img_01)
Fast_detect_Setparam(img_02)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import pylab as pl
import numpy as np
import matplotlib
import cv2
import numpy as np
from PIL import Image


img1 = cv2.imread("brid.png")
img2 = cv2.imread("house.png")

fast = cv2.FastFeatureDetector_create()
points = fast.detect(img1, None)
points1 = np.array([p.pt for p in points], dtype=np.float32)

pl.imshow(img1[:, :, ::-1])
pl.plot(points1[:, 0], points1[:, 1], "s", color="yellow", alpha=0.5, ms=1)
pl.axis("off")
pl.show()


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個






