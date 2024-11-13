"""

cv2之工具

cv2.setMouseCallback


"""

print("------------------------------------------------------------")  # 60個

import sys
import cv2
import numpy as np

print('用滑鼠在cv2上寫字')

W, H = 640, 480

def draw_circle(event, x, y, flags, param):
    global img, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        cv2.circle(img, (x, y), 1, (255), -1)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img, (x, y), 1, (255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img, (x, y), 1, (255), -1)


img = np.full(shape=(H, W, 1), fill_value=0, dtype=np.uint8)
cv2.namedWindow("image")

drawing = False

cv2.setMouseCallback("image", draw_circle)

while 1:
    cv2.imshow("image", img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord("s"):
        print('Save')
        #cv2.imwrite("tmp_1.jpg", img)
        #CNN()
    elif k == ord("c"):
        print('Clear')
        img = np.full(shape=(H, W, 1), fill_value=0, dtype=np.uint8)
    elif k == 27:
        print('ESC')
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


