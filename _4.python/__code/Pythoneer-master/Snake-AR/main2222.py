import numpy as np
import cv2
import math
import time
import random

cap = cv2.VideoCapture(0)

last = 0
new = 0

# 兩個 frame 相距的時間
lastFrameTime = int(round(time.time() * 1000))


def FrameDeltaTime():
    global lastFrameTime
    delta = int(round(time.time() * 1000)) - lastFrameTime
    lastFrameTime = int(round(time.time() * 1000))
    return delta


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    new = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    new = cv2.flip(new, 1)

    # Calculate game logic below
    diff = new.copy()
    cv2.absdiff(last, new, diff)
    diff = cv2.medianBlur(diff, 5)
    if np.amax(diff) > 100:
        ret3, diff = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    else:
        diff = diff - diff

    h, w = diff.shape[:2]
    start_row, start_col = int(0), int(0)
    end_row, end_col = int(h), int(w * 0.5)
    cropped_top = diff[start_row:end_row, start_col:end_col]
    leftSum = cv2.sumElems(cropped_top)

    start_row, start_col = int(0), int(w * 0.5)
    end_row, end_col = int(h), int(w)
    cropped_bot = diff[start_row:end_row, start_col:end_col]
    rightSum = cv2.sumElems(cropped_bot)

    # 兩個 frame 相距的時間
    # time_diff = FrameDeltaTime()
    # print(time_diff)

    # reset images and draw game
    last = new.copy()
    draw = new.copy()
    draw = cv2.cvtColor(draw, cv2.COLOR_GRAY2RGB)

    overlay = draw.copy()

    cv2.rectangle(overlay, (start_col, start_row), (end_col, end_row), (0, 255, 0), -1)

    cv2.imshow("Diff", diff)
    cv2.imshow("Game", draw)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


"""

兩圖 alpha 疊合
cv2.addWeighted(overlay, 0.1, draw, 1 - 0.1, 0, draw)


"""
