"""
cv2之工具 偵測滑鼠事件

cv2.setMouseCallback

滑鼠 event 與 flag 列表

當滑鼠在指定視窗中滑動進行某些行為，都會觸發一些事件，相關事件列表如下：
代號 	事件 	                說明
0 	cv2.EVENT_MOUSEMOVE 	滑動
1 	cv2.EVENT_LBUTTONDOWN 	左鍵點擊
2 	cv2.EVENT_RBUTTONDOWN 	右鍵點擊
3 	cv2.EVENT_MBUTTONDOWN 	中鍵點擊
4 	cv2.EVENT_LBUTTONUP 	左鍵放開
5 	cv2.EVENT_RBUTTONUP 	右鍵放開
6 	cv2.EVENT_MBUTTONUP 	中鍵放開
7 	cv2.EVENT_LBUTTONDBLCLK 左鍵雙擊
8 	cv2.EVENT_RBUTTONDBLCLK 右鍵雙擊
9 	cv2.EVENT_MBUTTONDBLCLK 中鍵雙擊

除了事件，滑鼠的行為也會觸發一些 flag，相關 flag 列表如下：
代號 	flag 	                說明
1 	cv2.EVENT_FLAG_LBUTTON 	左鍵拖曳
2 	cv2.EVENT_FLAG_RBUTTON 	右鍵拖曳
4 	cv2.EVENT_FLAG_MBUTTON 	中鍵拖曳
8～15 	cv2.EVENT_FLAG_CTRLKEY 	按 Ctrl 不放事件
16～31 	cv2.EVENT_FLAG_SHIFTKEY 按 Shift 不放事件
32～39 	cv2.EVENT_FLAG_ALTKEY 	按 Alt 不放事件

印出相關參數的數值，param 可透過 setMouseCallback 第三個參數傳遞給函式

EVENT_MOUSEMOVE   0           //滑鼠移動  
EVENT_LBUTTONDOWN 1           //左鍵點擊  
EVENT_RBUTTONDOWN 2           //右鍵點擊  
EVENT_MBUTTONDOWN 3           //中鍵點擊  
EVENT_LBUTTONUP   4           //左鍵放開  
EVENT_RBUTTONUP   5           //右鍵放開  
EVENT_MBUTTONUP   6           //中鍵放開  
EVENT_LBUTTONDBLCLK 7         //左鍵雙擊  
EVENT_RBUTTONDBLCLK 8         //右鍵雙擊  
EVENT_MBUTTONDBLCLK 9         //中鍵雙擊  

EVENT_FLAG_LBUTTON 1       //左鍵拖曳  
EVENT_FLAG_RBUTTON 2       //右鍵拖曳  
EVENT_FLAG_MBUTTON 4       //中鍵拖曳  
EVENT_FLAG_CTRLKEY 8       //(8~15)按Ctrl不放事件  
EVENT_FLAG_SHIFTKEY 16     //(16~31)按Shift不放事件  
EVENT_FLAG_ALTKEY 32       //(32~39)按Alt不放事件

"""
from opencv_common import *

W, H = 640, 480  # 影像寬, 影像高

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("打印系統有支持的EVENT")
events = [i for i in dir(cv2) if "EVENT" in i]
for e in events:
    print(e)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.setMouseCallback 01 測試所有按鍵 按ESC離開")

# 還不能偵測 前一頁 後一頁

filename = "D:/_git/vcs/_4.python/_data/elephant.jpg"
image = cv2.imread(filename)


def OnMouseAction(event, x, y, flags, param):
    # print(flags, end= " ")
    # event == cv2.EVENT_MOUSEMOVE:
    # print("滑鼠移動")

    if event == cv2.EVENT_LBUTTONDOWN:
        color = image[y, x]
        print("左鍵點擊, 座標", x, y, "顏色", color)
        # print(f"左鍵點擊({x}, {y})", end=" ")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print(f"右鍵點擊({x}, {y})", end=" ")
    elif event == cv2.EVENT_MBUTTONDOWN:
        print(f"中鍵點擊({x}, {y})", end=" ")
    elif event == cv2.EVENT_LBUTTONUP:
        print("左鍵放開")
    elif event == cv2.EVENT_RBUTTONUP:
        print("右鍵放開")
    elif event == cv2.EVENT_MBUTTONUP:
        print("中鍵放開")
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        print("左鍵雙擊")
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        print("右鍵雙擊")
    elif event == cv2.EVENT_MBUTTONDBLCLK:
        print("中鍵雙擊")
    elif flags == cv2.EVENT_FLAG_LBUTTON:
        print(f"左鍵拖曳點擊({x}, {y})", end=" ")
    elif flags == cv2.EVENT_FLAG_RBUTTON:
        print("右鍵拖曳, 座標", x, y, end=" ")
    elif flags == cv2.EVENT_FLAG_MBUTTON:
        print("中鍵拖曳", end=" ")
    elif flags == cv2.EVENT_FLAG_CTRLKEY:
        print("(8~15)按Ctrl不放事件")
    elif flags == cv2.EVENT_FLAG_SHIFTKEY:
        print("(16~31)按Shift不放事件")
    elif flags == cv2.EVENT_FLAG_ALTKEY:
        print("(32~39)按Alt不放事件")
    elif event == cv2.EVENT_MOUSEWHEEL:
        print("滑鼠滾輪滾動", end=" ")
        if flags > 0:
            print("向上滾動", end=" ")
        else:
            print("向下滾動", end=" ")
    elif event == cv2.EVENT_MOUSEHWHEEL:  # 一般用不到，因為一般鼠標沒有這個滾輪，有的鼠標有這個滾輪
        print("xxx滾輪左右滾動", end=" ")
        if flags > 0:
            print("向左滾動", end=" ")
        else:
            print("向右滾動", end=" ")


cv2.imshow("OpenCV", image)
cv2.setMouseCallback("OpenCV", OnMouseAction)  # 建立視窗與函數的連接

while True:
    k = cv2.waitKey(1)
    if k == ESC:
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 隨機色彩球
def OnMouseAction(event, x, y, flags, param):
    # color可以產生隨機色彩
    color = np.random.randint(0, high=256, size=3).tolist()
    r = np.random.randint(10, 50)  # 隨機10-50半徑的圓
    if event == cv2.EVENT_LBUTTONDOWN:  # 按一下滑鼠左鍵
        # print(f"左鍵點擊({x}, {y})", end=" ")
        cv2.circle(image, (x, y), r, color, -1)  # 隨機的實心圓
    elif event == cv2.EVENT_RBUTTONDOWN:  # 按一下滑鼠右鍵
        # print(f"右鍵點擊({x}, {y})", end=" ")
        cv2.circle(image, (x, y), r, color, 3)  # 隨機的空心圓


def OnMouseAction(event, x, y, flags, param):
    # color可以產生隨機色彩
    color = np.random.randint(0, high=256, size=3).tolist()
    r = np.random.randint(10, 50)  # 隨機10-50半徑的圓
    if event == cv2.EVENT_LBUTTONDOWN:  # 按一下滑鼠左鍵
        # print(f"左鍵點擊({x}, {y})", end=" ")
        cv2.circle(image, (x, y), r, color, thickness)  # 隨機的圓


def OnMouseAction(event, x, y, flags, param):
    # color可以產生隨機色彩
    color = np.random.randint(0, high=256, size=3).tolist()
    if event == cv2.EVENT_LBUTTONDOWN:  # 按一下滑鼠左鍵
        # print(f"左鍵點擊({x}, {y})", end=" ")
        r = np.random.randint(10, 50)  # 隨機10-50半徑的圓
        if k == ord("s"):
            cv2.circle(image, (x, y), r, color, -1)  # 隨機的實心圓
        else:
            cv2.circle(image, (x, y), r, color, 3)  # 隨機的線寬是 3 的圓
    elif event == cv2.EVENT_RBUTTONDOWN:  # 按一下滑鼠右鍵
        # print(f"右鍵點擊({x}, {y})", end=" ")
        px = np.random.randint(10, 100)
        py = np.random.randint(10, 100)
        if k == ord("s"):
            cv2.rectangle(image, (x, y), (px, py), color, -1)  # 實心矩形
        else:
            cv2.rectangle(image, (x, y), (px, py), color, 3)  # 空心矩形


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.setMouseCallback 02 小畫家 按ESC離開")

dots = []  # 建立空串列記錄座標
image = np.zeros((H, W, 4), dtype="uint8")  # 建立黑圖 WxH RGBA


def OnMouseAction(event, x, y, flags, param):
    global dots, image  # 定義全域變數
    if event == cv2.EVENT_MOUSEMOVE:  # 滑鼠移動
        image2 = image.copy()  # 當滑鼠移動時，複製原本的圖片
        cv2.circle(image2, (x, y), 30, GREEN, 5)  # 繪製空心圓
        cv2.imshow("OpenCV", image2)

    if flags == 1:  # 左鍵點擊
        if event == cv2.EVENT_LBUTTONDOWN:  #  滑鼠左鍵
            # print(f"左鍵點擊({x}, {y})", end=" ")
            dots.append([x, y])  # 如果拖曳滑鼠剛開始，記錄第一點座標
        if event == cv2.EVENT_LBUTTONUP:  # 左鍵放開
            dots = []  # 如果放開滑鼠，清空串列內容
        if event == cv2.EVENT_MOUSEMOVE or event == cv2.EVENT_LBUTTONUP:  # 滑鼠移動 或 左鍵放開
            dots.append([x, y])  # 拖曳滑鼠時，不斷記錄座標
            x1 = dots[len(dots) - 2][0]  # 取得倒數第二個點的 x 座標
            y1 = dots[len(dots) - 2][1]  # 取得倒數第二個點的 y 座標
            x2 = dots[len(dots) - 1][0]  # 取得倒數第一個點的 x 座標
            y2 = dots[len(dots) - 1][1]  # 取得倒數第一個點的 y 座標
            cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255, 255), 2)  # 畫直線
        cv2.imshow("OpenCV", image)


cv2.imshow("OpenCV", image)
cv2.setMouseCallback("OpenCV", OnMouseAction)  # 建立視窗與函數的連接

while True:
    k = cv2.waitKey(1)
    if k == ESC:
        break
    elif k == ord("r"):
        # Reset
        image = np.zeros((H, W, 4), dtype="uint8")  # Reset
        cv2.imshow("OpenCV", image)

cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.setMouseCallback 08 按ESC離開")

print("滑鼠動作, 用滑鼠在cv2上寫字")
print("按S, 存檔")
print("按C, 清除")
print("按ESC, 離開")

W, H = 640, 480  # 影像寬, 影像高

drawing = False
cv2.namedWindow("OpenCV")

# 建立底圖影像方法一
image = np.full(shape=(H, W, 1), fill_value=0, dtype=np.uint8)

# 建立底圖影像方法二
# image = np.zeros((H, W, 3), np.uint8)  # 建立黑圖

# 建立底圖影像方法三
# np.ones(shape, dtype, order)
# shape(高，宽，色彩通道数)
# dtype 常用的是np.unit8
# image = np.ones((H, W, 3), np.uint8) * 255  # 白色圖像


def OnMouseAction(event, x, y, flags, param):
    global image, drawing  # 定義全域變數
    if event == cv2.EVENT_LBUTTONDOWN:  #  滑鼠左鍵
        # print(f"左鍵點擊({x}, {y})", end=" ")
        drawing = True
        cv2.circle(image, (x, y), 2, (255), -1)

    elif event == cv2.EVENT_MOUSEMOVE:  #  滑鼠移動
        if drawing == True:
            cv2.circle(image, (x, y), 2, (255), -1)

    elif event == cv2.EVENT_LBUTTONUP:  #  滑鼠左鍵放開
        drawing = False
        cv2.circle(image, (x, y), 2, (255), -1)


cv2.setMouseCallback("OpenCV", OnMouseAction)  # 建立視窗與函數的連接

while True:
    cv2.imshow("OpenCV", image)
    k = cv2.waitKey(1)
    if k == ord("s"):
        print("存圖")
        # cv2.imwrite("tmp_1.jpg", image)
        # CNN()
    elif k == ord("c"):
        print("清除")
        image = np.full(shape=(H, W, 1), fill_value=0, dtype=np.uint8)
    elif k == ESC:
        print("離開")
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.setMouseCallback 03 測試滑鼠移動")

filename = "D:/_git/vcs/_4.python/_data/elephant.jpg"
image = cv2.imread(filename)

dots = []  # 記錄座標的空串列


def OnMouseAction(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  #  滑鼠左鍵
        # print(f"左鍵點擊({x}, {y})", end=" ")
        dots.append([x, y])  # 記錄座標
        cv2.circle(image, (x, y), 10, RED, -1)  # 在點擊的位置，繪製圓形
        num = len(dots)  # 目前有幾個座標
        if num > 1:  # 如果有兩個點以上
            x1 = dots[num - 2][0]
            y1 = dots[num - 2][1]
            x2 = dots[num - 1][0]
            y2 = dots[num - 1][1]
            cv2.line(image, (x1, y1), (x2, y2), RED, 2)  # 取得最後的兩個座標，繪製直線
        cv2.imshow("OpenCV", image)


cv2.imshow("OpenCV", image)
cv2.setMouseCallback("OpenCV", OnMouseAction)  # 建立視窗與函數的連接

while True:
    k = cv2.waitKey(1)
    if k == ESC:
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.setMouseCallback 04a 滑鼠圈選圖片")

filename = "D:/_git/vcs/_4.python/_data/elephant.jpg"
image = cv2.imread(filename)

dot1 = []  # 記錄第一個座標
dot2 = []  # 記錄第二個座標


# 滑鼠事件發生時要執行的函式
def OnMouseAction(event, x, y, flags, param):
    # global dot1, dot2, image  # 在函式內使用全域變數  # 定義全域變數
    global dot1, dot2, image, image2  # 因為要讓 image = image2，所以也要宣告 image2 為全域變數
    # 滑鼠拖曳發生時
    if flags == 1:  # 左鍵點擊
        if event == cv2.EVENT_LBUTTONDOWN:  #  滑鼠左鍵
            # print(f"左鍵點擊({x}, {y})", end=" ")
            dot1 = [x, y]  # 按下滑鼠時記錄第一個座標
        if event == cv2.EVENT_MOUSEMOVE:  # 滑鼠移動
            image2 = image.copy()  # 拖曳時不斷複製 image
            dot2 = [x, y]  # 拖曳時不斷更新第二個座標
            # 根據兩個座標繪製四邊形
            cv2.rectangle(image2, (dot1[0], dot1[1]), (dot2[0], dot2[1]), RED, 2)
            # 不斷顯示新圖片 ( 如果不這麼做，會出現一堆四邊形殘影 )
            cv2.imshow("OpenCV", image2)


cv2.imshow("OpenCV", image)
cv2.setMouseCallback("OpenCV", OnMouseAction)  # 建立視窗與函數的連接

while True:
    k = cv2.waitKey(1)
    if k == ESC:
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.setMouseCallback 04b 滑鼠圈選圖片")

filename = "D:/_git/vcs/_4.python/_data/elephant.jpg"
image = cv2.imread(filename)

dot1 = []  # 記錄第一個座標
dot2 = []  # 記錄第二個座標


# 滑鼠事件發生時要執行的函式
def OnMouseAction(event, x, y, flags, param):
    global dot1, dot2, image, image2  # 因為要讓 image = image2，所以也要宣告 image2 為全域變數
    if flags == 1:  # 左鍵點擊
        if event == cv2.EVENT_LBUTTONDOWN:  #  滑鼠左鍵
            # print(f"左鍵點擊({x}, {y})", end=" ")
            dot1 = [x, y]
        if event == cv2.EVENT_MOUSEMOVE:  # 滑鼠移動
            image2 = image.copy()
            dot2 = [x, y]
            cv2.rectangle(image2, (dot1[0], dot1[1]), (dot2[0], dot2[1]), RED, 2)
            cv2.imshow("OpenCV", image2)
    if event == cv2.EVENT_LBUTTONUP:  # 左鍵放開
        image = image2  # 滑鼠放開時 ( event == cv2.EVENT_LBUTTONUP )，將 image 更新為 image2


cv2.imshow("OpenCV", image)
cv2.setMouseCallback("OpenCV", OnMouseAction)  # 建立視窗與函數的連接

while True:
    k = cv2.waitKey(1)
    if k == ESC:
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
