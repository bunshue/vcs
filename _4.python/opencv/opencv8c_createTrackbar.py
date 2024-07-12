"""

cv2之工具

cv2.setMouseCallback


"""
import sys
import cv2
import numpy as np

W = 640
H = 480

ESC = 27
SPACE = 32

print("------------------------------------------------------------")  # 60個

print("OpenCV_41 Trackbar之使用")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename)

cv2.imshow("ImageShow", image)

def apply_function(val):
    print('數值 :', val, end = " ")


# cv2.createTrackbar('滑桿名稱', '視窗名稱', min, max, fn)
# min 最小值 ( 最小為 0，不可為負值 )
# max 最大值
# fn 滑桿數值改變時要執行的函式
# 加入滑桿 0 ~ 200, 預設 100
cv2.createTrackbar("TrackbarName", "ImageShow", 0, 200, apply_function)
cv2.setTrackbarPos("TrackbarName", "ImageShow", 100)

#取得Trackbar數值
value = cv2.getTrackbarPos("TrackbarName", "ImageShow")

apply_function(value) #套用一次設定值

keycode = cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

def setup_bg_color(x):
  r = cv2.getTrackbarPos('R','image')
  g = cv2.getTrackbarPos('G','image')
  b = cv2.getTrackbarPos('B','image')
  s = cv2.getTrackbarPos(switch,'image')

  if s == 0:
   img[:] = 0
  else:
   img[:] = [b,g,r]
  cv2.imshow('image',img)

# Create a black image, a window
img = np.zeros((240,180,3), np.uint8)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,setup_bg_color)
cv2.createTrackbar('G','image',0,255,setup_bg_color)
cv2.createTrackbar('B','image',0,255,setup_bg_color)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,setup_bg_color)
cv2.setTrackbarPos(switch, "image", 1)

while(1):
 k = cv2.waitKey(1) & 0xFF
 if k == 27:
  break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

