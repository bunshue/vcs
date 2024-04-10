"""
cv2.setMouseCallback



"""

print("------------------------------------------------------------")  # 60個

import cv2
import numpy as np

print("------------------------------------------------------------")  # 60個

print("滑鼠動作 + 鍵盤按鍵s c, 按ESC離開")

img = np.full(shape=(480, 640, 1), fill_value=0, dtype=np.uint8)
cv2.namedWindow("image")

drawing = False

def keyboard_function():
    print("keyboard")

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

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print("用滑鼠座標取得圖片之位置資料")

img = cv2.imread(filename)

def show_xy(event,x,y,flags,userdata):
    #print(event,x,y,flags)
    pass
    # 印出相關參數的數值，userdata 可透過 setMouseCallback 第三個參數垂遞給函式

cv2.imshow('ImageShow', img)
cv2.setMouseCallback('ImageShow', show_xy)  # 設定偵測事件的函式與視窗

cv2.waitKey(0)     # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)

def show_xy(event,x,y,flags,param):
    if event == 0:
        img2 = img.copy()                         # 當滑鼠移動時，複製原本的圖片
        cv2.circle(img2, (x,y), 10, (0,0,0), 1)   # 繪製黑色空心圓
        cv2.imshow('ImageShow', img2)            # 顯示繪製後的影像
    if event == 1:
        color = img[y,x]                          # 當滑鼠點擊時
        print(color)                              # 印出顏色

cv2.imshow('ImageShow', img)
cv2.setMouseCallback('ImageShow', show_xy)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)

dots = []   # 記錄座標的空串列
def show_xy(event,x,y,flags,param):
    if event == 1:
        dots.append([x, y])                          # 記錄座標
        cv2.circle(img, (x, y), 10, (0,0,255), -1)   # 在點擊的位置，繪製圓形
        num = len(dots)                              # 目前有幾個座標
        if num > 1:                                  # 如果有兩個點以上
            x1 = dots[num-2][0]
            y1 = dots[num-2][1]
            x2 = dots[num-1][0]
            y2 = dots[num-1][1]
            cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)  # 取得最後的兩個座標，繪製直線
        cv2.imshow('ImageShow', img)

cv2.imshow('ImageShow', img)
cv2.setMouseCallback('ImageShow', show_xy)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread('data/lena.png')

dot1 = []                          # 記錄第一個座標
dot2 = []                          # 記錄第二個座標

# 滑鼠事件發生時要執行的函式
def show_xy(event,x,y,flags,param):
    global dot1, dot2, img         # 在函式內使用全域變數
    # 滑鼠拖曳發生時
    if flags == 1:
        if event == 1:
            dot1 = [x, y]          # 按下滑鼠時記錄第一個座標
        if event == 0:
            img2 = img.copy()      # 拖曳時不斷複製 img
            dot2 = [x, y]          # 拖曳時不斷更新第二個座標
            # 根據兩個座標繪製四邊形
            cv2.rectangle(img2, (dot1[0], dot1[1]), (dot2[0], dot2[1]), (0,0,255), 2)
            # 不斷顯示新圖片 ( 如果不這麼做，會出現一堆四邊形殘影 )
            cv2.imshow('ImageShow', img2)

cv2.imshow('ImageShow', img)
cv2.setMouseCallback('ImageShow', show_xy)

cv2.waitKey(0)   # 按下任意鍵結束
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread('data/lena.png')

dot1 = []
dot2 = []
def show_xy(event,x,y,flags,param):
    global dot1, dot2, img, img2    # 因為要讓 img = img2，所以也要宣告 img2 為全域變數
    if flags == 1:
        if event == 1:
            dot1 = [x, y]
        if event == 0:
            img2 = img.copy()
            dot2 = [x, y]
            cv2.rectangle(img2, (dot1[0], dot1[1]), (dot2[0], dot2[1]), (0,0,255), 2)
            cv2.imshow('ImageShow', img2)
        if event == 4:
            img = img2   # 滑鼠放開時 ( event == 4 )，將 img 更新為 img2

cv2.imshow('ImageShow', img)
cv2.setMouseCallback('ImageShow', show_xy)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread('data/lena.png')

dot1 = []
dot2 = []
def show_xy(event,x,y,flags,param):
    global dot1, dot2, img, img2
    if flags == 1:
        if event == 1:
            dot1 = [x, y]
        if event == 0:
            img2 = img.copy()
            dot2 = [x, y]
            cv2.rectangle(img2, (dot1[0], dot1[1]), (dot2[0], dot2[1]), (0,0,255), 2)
            cv2.imshow('ImageShow', img2)
        if event == 4:
            level = 8                                         # 縮小比例 ( 可當作馬賽克的等級 )
            h = int((dot2[0] - dot1[0]) / level)              # 按照比例縮小後的高度 ( 使用 int 去除小數點 )
            w = int((dot2[1] - dot1[1]) / level)              # 按照比例縮小後的寬度 ( 使用 int 去除小數點 )
            mosaic = img[dot1[1]:dot2[1], dot1[0]:dot2[0]]    # 取得馬賽克區域
            mosaic = cv2.resize(mosaic, (w, h), interpolation=cv2.INTER_LINEAR)   # 根據縮小尺寸縮小
            mosaic = cv2.resize(mosaic, (dot2[0] - dot1[0], dot2[1] - dot1[1]), interpolation=cv2.INTER_NEAREST) # 放大到原本的大小
            img[dot1[1]:dot2[1], dot1[0]:dot2[0]] = mosaic   # 置換成馬賽克的影像
            cv2.imshow('ImageShow', img)

cv2.imshow('ImageShow', img)
cv2.setMouseCallback('ImageShow', show_xy)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

dots = []   # 建立空串列記錄座標
w = 420
h = 240
draw = np.zeros((h,w,4), dtype='uint8')   # 建立 420x240 的 RGBA 黑色畫布

def show_xy(event,x,y,flags,param):
    global dots, draw                     # 定義全域變數
    if flags == 1:
        if event == 1:
            dots.append([x,y])            # 如果拖曳滑鼠剛開始，記錄第一點座標
        if event == 4:
            dots = []                     # 如果放開滑鼠，清空串列內容
        if event == 0 or event == 4:
            dots.append([x,y])            # 拖曳滑鼠時，不斷記錄座標
            x1 = dots[len(dots)-2][0]     # 取得倒數第二個點的 x 座標
            y1 = dots[len(dots)-2][1]     # 取得倒數第二個點的 y 座標
            x2 = dots[len(dots)-1][0]     # 取得倒數第一個點的 x 座標
            y2 = dots[len(dots)-1][1]     # 取得倒數第一個點的 y 座標
            cv2.line(draw,(x1,y1),(x2,y2),(0,0,255,255),2)  # 畫直線
        cv2.imshow('ImageShow', draw)

cv2.imshow('ImageShow', draw)
cv2.setMouseCallback('ImageShow', show_xy)

while True:
    keyboard = cv2.waitKey(5)                    # 每 5 毫秒偵測一次鍵盤事件
    if keyboard == ord('q'):
        break                                    # 如果按下 q 就跳出
    if keyboard == ord('r'):
        draw = np.zeros((h,w,4), dtype='uint8')  # 如果按下 r 就變成原本全黑的畫布
        cv2.imshow('ImageShow', draw)

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
