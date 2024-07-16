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
"""
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
    if k == ESC:
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

"""
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

img = cv2.imread(filename)
cv2.imshow("opencv", img)


def get_trackbar_value(val):
    print(val, end=" ")


cv2.createTrackbar("Trackbar", "opencv", 0, 255, get_trackbar_value)
cv2.setTrackbarPos("Trackbar", "opencv", 50)  # 預設

keycode = cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


print("OpenCV之控件 Trackbar")
print("滑桿 ( Trackbar ) 又稱作滑動條、Slider bar，是一種可以用滑鼠調整數值的 UI 介面")

print("測試cv2視窗的Trackbar")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
# image = cv2.imread(filename)

# 調整對比度後，圖像的效果顯示窗口
cv2.namedWindow("TrackbarTest", cv2.WND_PROP_AUTOSIZE)

cv2.imshow("TrackbarTest", image)

MAX_VALUE = 80
MIN_VALUE = 30  # 無效，看起來最小值一定要0
initial_value = 40


def callback_trackbar_test(_value):
    print(_value, end=" ")


callback_trackbar_test(initial_value)  # 做一次

cv2.createTrackbar(
    "value", "TrackbarTest", MIN_VALUE, MAX_VALUE, callback_trackbar_test
)  # callback function
cv2.setTrackbarPos("value", "TrackbarTest", initial_value)  # 預設

cv2.waitKey(0)
cv2.destroyAllWindows()
