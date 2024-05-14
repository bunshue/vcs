import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('geometry.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#寻找Harris角点
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
dst = np.uint8(dst)
#找到重心
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
# 定义停止和细化拐角的标准
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)
#绘图
res = np.hstack((centroids,corners))
res = np.int0(res)
img[res[:,1],res[:,0]] = [0,0,255]
img[res[:,3],res[:,2]] = [0,255,0]
cv2.imshow('dst',img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
