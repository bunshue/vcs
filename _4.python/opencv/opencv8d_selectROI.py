"""

cv2之工具

cv2.selectROI


"""
import sys
import cv2

print("------------------------------------------------------------")  # 60個

print("OpenCV selectROI 之使用")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename)

roi = cv2.selectROI('image', image)
print('選取區域 :', roi)

keycode = cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

