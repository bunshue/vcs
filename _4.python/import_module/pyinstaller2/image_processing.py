"""
測試 Pyinstaller

"""
import cv2
import numpy as np

ESC = 27

print("cv讀取鍵盤 按上下調整亮度 按左右調整對比度 按ESC離開")

image = cv2.imread("images/elephant.jpg")  # 彩色讀取


# 定義調整亮度對比的函式
def adjust(i, c, b):
    output = i * (c / 100 + 1) - c + b  # 轉換公式
    output = np.clip(output, 0, 255)
    output = np.uint8(output)
    return output


contrast = 0  # 初始化要調整對比度的數值
brightness = 0  # 初始化要調整亮度的數值

cv2.imshow("Up/Down/Left/Right/Q/ESC", image)

while True:
    k = cv2.waitKey(0)
    if k == 0:
        brightness = brightness + 5  # 按下鍵盤的「上」，增加亮度
    if k == 1:
        brightness = brightness - 5  # 按下鍵盤的「下」，減少亮度
    if k == 2:
        contrast = contrast - 5  # 按下鍵盤的「右」，增加對比度
    if k == 3:
        contrast = contrast + 5  # 按下鍵盤的「左」，減少對比度
    if k == 113:
        contrast, brightness = 0, 0  # 按下鍵盤的「q」，恢復預設值
    if k == ESC:
        break
    show_image = image.copy()  # 複製原始圖片
    show_image = adjust(show_image, contrast, brightness)  # 根據亮度和對比度的調整值，輸出新的圖片
    cv2.imshow("Up/Down/Left/Right/Q/ESC", show_image)

cv2.destroyAllWindows()
