import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def watershed_demo(img):
    print(img.shape)
    #去噪声
    blurred = cv.pyrMeanShiftFiltering(img, 10, 100)
    #灰度/二值图像
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow('thresh', thresh)
    # 有很多的黑点，所以我们去黑点噪声
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=2)
    cv.imshow('opening ', opening)
    sure_bg = cv.dilate(opening, kernel, iterations=3)
    cv.imshow('mor-opt', sure_bg)
    #距离变换
    dist = cv.distanceTransform(opening, cv.DIST_L2, 3)
    dist_output = cv.normalize(dist, 0, 1.0, cv.NORM_MINMAX)
    cv.imshow('distance-t', dist_output * 50)
    ret, surface = cv.threshold(dist, dist.max()*0.6, 255, cv.THRESH_BINARY)
    cv.imshow('surface', surface)
    #发现未知的区域
    surface_fg = np.uint8(surface)
    cv.imshow('surface_bin', surface_fg)
    unknown = cv.subtract(sure_bg,surface_fg)
    # 标记标签
    ret, markers = cv.connectedComponents(surface_fg)
    #添加一个标签到所有标签，这样确保背景不是0，而是1
    markers = markers + 1
    #令未知区域为零
    markers[unknown==255] = 0
    markers = cv.watershed(img, markers)
    img[markers==-1] = [255, 0, 0]
    cv.imshow('result', img)

img = cv.imread('37.jpg')
cv.namedWindow('img',cv.WINDOW_AUTOSIZE)
cv.imshow('img',img)
watershed_demo(img)
cv.waitKey(0)
cv.destroyAllWindows()
