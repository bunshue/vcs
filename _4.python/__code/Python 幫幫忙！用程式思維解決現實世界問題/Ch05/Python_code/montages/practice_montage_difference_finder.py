import cv2 as cv

filename1 = 'montage_left.JPG'
filename2 = 'montage_right_gray.JPG'

img1 = cv.imread(filename1, cv.IMREAD_GRAYSCALE)
img2 = cv.imread(filename2, cv.IMREAD_GRAYSCALE)

# 比較影像
diff_imgs1_2 = cv.absdiff(img1, img2)

cv.namedWindow('Difference', cv.WINDOW_NORMAL)
diff_imgs1_2_resize = cv.resize(diff_imgs1_2, (699, 700))
cv.imshow('Difference', diff_imgs1_2_resize)
#cv.waitKey(3000)
#cv.destroyAllWindows()

crop_diff = diff_imgs1_2[10:2795, 10:2445]  # x, y, w, h = 10, 10, 2790, 2440

# 預處理影像模糊化(減少影像雜訊)
blurred = cv.GaussianBlur(crop_diff, (5, 5), 0)

(minVal, maxVal, minLoc, maxLoc2) = cv.minMaxLoc(blurred) # 傳回影像中像素值最小和最大的值及其位置 tuple
cv.circle(img2, maxLoc2, 100, 255, 3) # 畫圓圈
x, y = int(img2.shape[1]/4), int(img2.shape[0]/4) # 設定視窗大小
img2_resize = cv.resize(img2, (x, y)) # 視窗停滯 7 秒
cv.imshow('Change', img2_resize) # 顯示視窗
cv.waitKey(10000) # 視窗停滯 10 秒
cv.destroyAllWindows() # 關閉視窗
