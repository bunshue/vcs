"""


"""

import cv2


print("------------------------------------------------------------")  # 60個


import cv2
import numpy as np

img = np.full(shape=(480, 640, 1), fill_value=0, dtype=np.uint8)
cv2.namedWindow("image")

drawing = False


def draw_circle(event, x, y, flags, param):
    global img, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        cv2.circle(img, (x, y), 2, (255), -1)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img, (x, y), 2, (255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img, (x, y), 2, (255), -1)


cv2.setMouseCallback("image", draw_circle)


def keyboard_function():
    print("keyboard")


print("滑鼠動作 + 鍵盤按鍵s c")
while True:
    cv2.imshow("image", img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord("s"):
        keyboard_function()
    elif k == ord("c"):
        img = np.full(shape=(480, 640, 1), fill_value=0, dtype=np.uint8)
        print("clear")
    elif k == 27:
        break

cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
