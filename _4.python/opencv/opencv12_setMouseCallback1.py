"""
cv2之工具

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

print("cv2.setMouseCallback 01 小畫家 按ESC離開")

dots = []  # 建立空串列記錄座標
image = np.zeros((H, W, 4), dtype="uint8")  # 建立黑圖 WxH RGBA


def show_xy(event, x, y, flags, param):
    global dots, image  # 定義全域變數
    if flags == 1:
        if event == cv2.EVENT_LBUTTONDOWN:  #  滑鼠左鍵
            print(f"左鍵點擊({x}, {y})", end=" ")
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
cv2.setMouseCallback("OpenCV", show_xy)  # 建立視窗與函數的連接

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

print("cv2.setMouseCallback 02 測試所有按鍵 按ESC離開")

# 還不能偵測 前一頁 後一頁

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"
image = cv2.imread(filename)


# 創建回調函數
def OnMouseAction(event, x, y, flags, param):
    # event == cv2.EVENT_MOUSEMOVE:
    # print("滑鼠移動")

    if event == cv2.EVENT_LBUTTONDOWN:
        color = image[y, x]
        print("左鍵點擊, 座標", x, y, "顏色", color)
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("f右鍵點擊({x}, {y})", end=" ")
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

print("cv2.setMouseCallback 03 測試滑鼠移動")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"
image = cv2.imread(filename)


# 印出相關參數的數值，param 可透過 setMouseCallback 第三個參數傳遞給函式
def show_xy(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:  # 滑鼠移動
        image2 = image.copy()  # 當滑鼠移動時，複製原本的圖片
        cv2.circle(image2, (x, y), 30, RED, 5)  # 繪製紅色空心圓
        cv2.imshow("OpenCV", image2)  # 顯示繪製後的影像


cv2.imshow("OpenCV", image)
cv2.setMouseCallback("OpenCV", show_xy)  # 建立視窗與函數的連接

while True:
    k = cv2.waitKey(1)
    if k == ESC:
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.setMouseCallback 04")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"
image = cv2.imread(filename)

dots = []  # 記錄座標的空串列


def show_xy(event, x, y, flags, param):
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
cv2.setMouseCallback("OpenCV", show_xy)  # 建立視窗與函數的連接

while True:
    k = cv2.waitKey(1)
    if k == ESC:
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.setMouseCallback 05 滑鼠圈選圖片")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"
image = cv2.imread(filename)

dot1 = []  # 記錄第一個座標
dot2 = []  # 記錄第二個座標


# 滑鼠事件發生時要執行的函式
def show_xy(event, x, y, flags, param):
    global dot1, dot2, image  # 在函式內使用全域變數  # 定義全域變數
    # 滑鼠拖曳發生時
    if flags == 1:
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
cv2.setMouseCallback("OpenCV", show_xy)  # 建立視窗與函數的連接

while True:
    k = cv2.waitKey(1)
    if k == ESC:
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.setMouseCallback 06 滑鼠圈選圖片")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"
image = cv2.imread(filename)

dot1 = []
dot2 = []


def show_xy(event, x, y, flags, param):
    global dot1, dot2, image, image2  # 因為要讓 image = image2，所以也要宣告 image2 為全域變數
    if flags == 1:
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
cv2.setMouseCallback("OpenCV", show_xy)  # 建立視窗與函數的連接

while True:
    k = cv2.waitKey(1)
    if k == ESC:
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.setMouseCallback 07 滑鼠圈選圖片")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"
image = cv2.imread(filename)

dot1 = []
dot2 = []


def show_xy(event, x, y, flags, param):
    global dot1, dot2, image, image2  # 因為要讓 image = image2，所以也要宣告 image2 為全域變數
    if flags == 1:
        if event == cv2.EVENT_LBUTTONDOWN:  #  滑鼠左鍵
            # print(f"左鍵點擊({x}, {y})", end=" ")
            dot1 = [x, y]
        if event == cv2.EVENT_MOUSEMOVE:  # 滑鼠移動
            image2 = image.copy()
            dot2 = [x, y]
            cv2.rectangle(image2, (dot1[0], dot1[1]), (dot2[0], dot2[1]), RED, 2)
            cv2.imshow("OpenCV", image2)
        if event == cv2.EVENT_LBUTTONUP:  # 左鍵放開
            level = 8  # 縮小比例 ( 可當作馬賽克的等級 )
            H = int((dot2[0] - dot1[0]) / level)  # 按照比例縮小後的高度 ( 使用 int 去除小數點 )
            W = int((dot2[1] - dot1[1]) / level)  # 按照比例縮小後的寬度 ( 使用 int 去除小數點 )
            mosaic = image[dot1[1] : dot2[1], dot1[0] : dot2[0]]  # 取得馬賽克區域
            mosaic = cv2.resize(
                mosaic, (W, H), interpolation=cv2.INTER_LINEAR
            )  # 根據縮小尺寸縮小
            mosaic = cv2.resize(
                mosaic,
                (dot2[0] - dot1[0], dot2[1] - dot1[1]),
                interpolation=cv2.INTER_NEAREST,
            )  # 放大到原本的大小
            image[dot1[1] : dot2[1], dot1[0] : dot2[0]] = mosaic  # 置換成馬賽克的影像
            cv2.imshow("OpenCV", image)


cv2.imshow("OpenCV", image)
cv2.setMouseCallback("OpenCV", show_xy)  # 建立視窗與函數的連接

while True:
    k = cv2.waitKey(1)
    if k == ESC:
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" TBD
print("cv2.setMouseCallback 08 按ESC離開")

d = 400
def draw(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        #矩形之左上點
        p1x = x
        p1y = y
        #矩形之右下點
        p2x = np.random.randint(1, d - 50)  #np.random之randint不含尾
        p2y = np.random.randint(1, d - 50)  #np.random之randint不含尾
        color = np.random.randint(0, high = 256, size = (3,)).tolist()  #np.random之randint不含尾
        cv2.rectangle(image,(p1x, p1y),(p2x, p2y), color, 2)

W, H = 400, 400
image = np.ones((H, W, 3), dtype = "uint8") * 255  # 白圖

cv2.namedWindow("OpenCV")
cv2.setMouseCallback("OpenCV", draw)  # 建立視窗與函數的連接

while True:
    cv2.imshow("OpenCV", image)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")	#60個

print("cv2.setMouseCallback 09 按ESC離開")

#fail
d = 400
global thickness  # 定義全域變數
thickness = -1

def fill(x):
    pass

def draw(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        #矩形之左上點
        p1x = x
        p1y = y
        #矩形之右下點
        p2x = np.random.randint(1, d - 50)  #np.random之randint不含尾
        p2y = np.random.randint(1, d - 50)  #np.random之randint不含尾
        color = np.random.randint(0, high = 256, size = (3,)).tolist()  #np.random之randint不含尾
        cv2.rectangle(image,(p1x,p1y),(p2x,p2y),color,thickness)

W, H = 400, 400
image = np.ones((H, W, 3), np.uint8) * 255  # 白圖

cv2.namedWindow("OpenCV")
cv2.setMouseCallback("OpenCV", draw)  # 建立視窗與函數的連接

cv2.createTrackbar("R", "OpenCV", 0, 1, fill)

while True:
    cv2.imshow("OpenCV", image)
    k = cv2.waitKey(1)
    if k == ESC:
        break
    g = cv2.getTrackbarPos("R", "OpenCV")
    if g == 0:
        thickness = -1
    else:
        thickness = 2        

cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" TBD
print("cv2.setMouseCallback 10 按ESC離開")

thickness=-1
mode=1
d=400
def draw_circle2(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN: #  滑鼠左鍵
        a=np.random.randint(1,d-50)
        r=np.random.randint(1,d/5)
        angle = np.random.randint(0,361)
        color = np.random.randint(0,high = 256,size = (3,)).tolist()
        if mode==1:
            cv2.rectangle(image,(x,y),(a,a),color,thickness)
        elif mode==2:
            cv2.circle(image,(x,y),r,color,thickness)
        elif mode==3:
            cv2.line(image,(a,a),(x,y),color,3)  
        elif mode==4:
            cv2.ellipse(image, (x,y), (100,150), angle, 0, 360,color,thickness)                  
        elif mode==5:
            cv2.putText(image,"OpenCV",(0,round(d/2)), 
                        cv2.FONT_HERSHEY_SIMPLEX, 2,color,5)    

W, H = 400, 400
image = np.ones((H, W, 3), np.uint8) * 255  # 白圖

cv2.namedWindow("OpenCV")
cv2.setMouseCallback("OpenCV",draw_circle2)  # 建立視窗與函數的連接

while True:
    cv2.imshow("OpenCV",image)
    k = cv2.waitKey(1)
    if k == ESC:
        break
    elif k==ord("r"):
        mode=1
    elif k==ord("c"):
        mode=2
    elif k==ord("l"):
        mode=3
    elif k==ord("e"):
        mode=4
    elif k==ord("t"):
        mode=5
    elif k==ord("f"):
        thickness=-1
    elif k==ord("u"):
        thickness=3

cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.setMouseCallback 11 按ESC離開")

"""
0 : 畫點
1 : 拖曳
"""
mode = 0

if mode == 0:
    print("左鍵畫點")
elif mode == 1:
    print("左鍵拖曳")


def OnMouseAction(event, x, y, flags, param):
    global x1, y1  # 定義全域變數

    if mode == 0 and event == cv2.EVENT_LBUTTONDOWN:
        # print(f"左鍵點擊({x}, {y})", end=" ")
        print("左鍵畫點")
        # cv2.line(image, (0, 0), (x, y), CYAN, 2)#畫直線連線
        cv2.circle(image, (x, y), 10, (255), -1)  # 畫點

    if mode == 1 and event == cv2.EVENT_LBUTTONDOWN:
        # print(f"左鍵點擊({x}, {y})", end=" ")
        x1, y1 = x, y
    elif mode == 1 and event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        # print(f"左鍵拖曳點擊({x}, {y})", end=" ")
        cv2.rectangle(image, (x1, y1), (x, y), GREEN, -1)


W, H = 640, 480  # 影像寬, 影像高
image = np.zeros((H, W, 3), np.uint8)  # 建立黑圖

cv2.namedWindow("OpenCV")
cv2.setMouseCallback("OpenCV", OnMouseAction)  # 建立視窗與函數的連接

while True:
    cv2.imshow("OpenCV", image)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.setMouseCallback 13 在影像上畫圖 按ESC離開")

cap = cv2.VideoCapture(1)

W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 取得影像寬度
H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 取得影像高度

image = np.zeros((H, W, 4), dtype="uint8")

if not cap.isOpened():
    print("Cannot open camera")
    exit()


def show_xy(event, x, y, flags, param):
    global dots, image  # 定義全域變數
    if flags == 1:
        if event == 1:
            dots.append([x, y])
        if event == 4:
            dots = []
        if event == 0 or event == 4:
            dots.append([x, y])
            x1 = dots[len(dots) - 2][0]
            y1 = dots[len(dots) - 2][1]
            x2 = dots[len(dots) - 1][0]
            y2 = dots[len(dots) - 1][1]
            cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255, 255), 2)


cv2.imshow("OpenCV", image)
cv2.setMouseCallback("OpenCV", show_xy)  # 建立視窗與函數的連接

dots = []

while True:
    ret, frame = cap.read()  # 讀取影片的每一個影格
    if not ret:
        print("Cannot receive frame")
        break

    # 透過 for 迴圈合成影像
    for i in range(W):
        frame[:, i, 0] = frame[:, i, 0] * (1 - image[:, i, 3] / 255) + image[
            :, i, 0
        ] * (image[:, i, 3] / 255)
        frame[:, i, 1] = frame[:, i, 1] * (1 - image[:, i, 3] / 255) + image[
            :, i, 1
        ] * (image[:, i, 3] / 255)
        frame[:, i, 2] = frame[:, i, 2] * (1 - image[:, i, 3] / 255) + image[
            :, i, 2
        ] * (image[:, i, 3] / 255)

    k = cv2.waitKey(1)
    if k == ESC:
        break
    elif k == ord("r"):
        image = np.zeros((H, W, 4), dtype="uint8")  # Reset

    cv2.imshow("OpenCV", frame)

cap.release()  # 釋放資源
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.setMouseCallback 14 擦亮影片 按ESC離開")

W = 640  # 定義影片寬度
H = 480  # 定義影像高度

dots = []  # 記錄座標
mask_b = np.zeros((H, W, 3), dtype="uint8")  # 產生黑色遮罩 -> 套用清楚影像
mask_w = np.zeros((H, W, 3), dtype="uint8")  # 產生白色遮罩 -> 套用模糊影像
mask_w[0:H, 0:W] = 255  # 白色遮罩背景為白色


# 滑鼠繪圖函式
def show_xy(event, x, y, flags, param):
    global dots, mask  # 定義全域變數
    if flags == 1:
        if event == 1:
            dots.append([x, y])
        if event == 4:
            dots = []
        if event == 0 or event == 4:
            dots.append([x, y])
            x1 = dots[len(dots) - 2][0]
            y1 = dots[len(dots) - 2][1]
            x2 = dots[len(dots) - 1][0]
            y2 = dots[len(dots) - 1][1]
            cv2.line(mask_w, (x1, y1), (x2, y2), BLACK, 50)  # 在白色遮罩上畫出黑色線條
            cv2.line(mask_b, (x1, y1), (x2, y2), WHITE, 50)  # 在黑色遮罩上畫出白色線條


cv2.imshow("OpenCV", mask_b)
cv2.setMouseCallback("OpenCV", show_xy)  # 建立視窗與函數的連接

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break

    frame = cv2.resize(frame, (W, H))  # 縮小尺寸，加快速度
    frame = cv2.flip(frame, 1)  # 翻轉影像
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)  # 轉換顏色為 BGRA ( 計算時需要用到 Alpha 色版 )
    frame2 = frame.copy()  # 複製影像
    frame2 = cv2.blur(frame, (55, 55))  # 套用模糊

    mask1 = cv2.cvtColor(mask_b, cv2.COLOR_BGR2GRAY)  # 轉換遮罩為灰階
    frame = cv2.bitwise_and(frame, frame, mask=mask1)  # 清楚影像套用黑遮罩
    mask2 = cv2.cvtColor(mask_w, cv2.COLOR_BGR2GRAY)  # 轉換遮罩為灰階
    frame2 = cv2.bitwise_and(frame2, frame2, mask=mask2)  # 模糊影像套用白遮罩

    output = cv2.add(frame, frame2)  # 合併影像

    cv2.imshow("OpenCV", output)

    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

video_filename = "D:/內視鏡影片/NBI錄影_V20241009_081309.mp4"
cap = cv2.VideoCapture(video_filename)

if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")


def OnMouseAction(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"左鍵點擊({x}, {y})", end=" ")


cv2.namedWindow("OpenCV")
cv2.setMouseCallback("OpenCV", OnMouseAction)  # 建立視窗與函數的連接

while True:
    ret, frame = cap.read()  # 從攝影機擷取一張影像

    if ret == False:
        print("無影像, 離開")
        break

    cv2.imshow("OpenCV", frame)

    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.setMouseCallback 15 按ESC離開")

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


def draw_circle(event, x, y, flags, param):
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


cv2.setMouseCallback("OpenCV", draw_circle)  # 建立視窗與函數的連接

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

print("cv2.setMouseCallback 17 按ESC離開")


def OnMouseAction(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # print("左鍵({x}, {y})", end=" ")
        print(f"左鍵點擊({x}, {y})", end=" ")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print(f"右鍵點擊({x}, {y})", end=" ")
    elif event == cv2.EVENT_MBUTTONDOWN:
        print(f"中鍵點擊({x}, {y})", end=" ")
    elif flags == cv2.EVENT_FLAG_LBUTTON:
        print(f"左鍵拖曳點擊({x}, {y})", end=" ")
    elif flags == cv2.EVENT_FLAG_RBUTTON:
        print("右鍵拖曳, 座標", x, y, end=" ")


W, H = 640, 480  # 影像寬, 影像高

image = np.ones((H, W, 3), np.uint8) * 255  # 白圖

cv2.namedWindow("OpenCV")
cv2.setMouseCallback("OpenCV", OnMouseAction)  # 建立視窗與函數的連接

cv2.imshow("OpenCV", image)

while True:
    k = cv2.waitKey(1)
    if k == ESC:
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.setMouseCallback 18 按ESC離開")


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


W, H = 640, 480  # 影像寬, 影像高

image = np.ones((H, W, 3), np.uint8) * 255  # 白圖

cv2.namedWindow("OpenCV")
cv2.setMouseCallback("OpenCV", OnMouseAction)  # 建立視窗與函數的連接

while True:
    cv2.imshow("OpenCV", image)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def onChange(x):
    pass


def OnMouseAction(event, x, y, flags, param):
    # color可以產生隨機色彩
    color = np.random.randint(0, high=256, size=3).tolist()
    r = np.random.randint(10, 50)  # 隨機10-50半徑的圓
    if event == cv2.EVENT_LBUTTONDOWN:  # 按一下滑鼠左鍵
        # print(f"左鍵點擊({x}, {y})", end=" ")
        cv2.circle(image, (x, y), r, color, thickness)  # 隨機的圓


thickness = -1  # 預設寬度是 0

W, H = 640, 480  # 影像寬, 影像高

image = np.ones((H, W, 3), np.uint8) * 255  # 白圖

cv2.namedWindow("OpenCV")
cv2.setMouseCallback("OpenCV", OnMouseAction)  # 建立視窗與函數的連接

cv2.createTrackbar("Thickness", "OpenCV", 0, 1, onChange)

while True:
    cv2.imshow("OpenCV", image)
    k = cv2.waitKey(1)
    num = cv2.getTrackbarPos("Thickness", "OpenCV")
    if num == 0:
        thickness = -1  # 實心設定
    else:
        thickness = 3  # 寬度是 3
    if k == ESC:
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.setMouseCallback 19 按ESC離開")


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


W, H = 640, 480  # 影像寬, 影像高

image = np.ones((H, W, 3), np.uint8) * 255  # 白圖

cv2.namedWindow("OpenCV")
cv2.setMouseCallback("OpenCV", OnMouseAction)  # 建立視窗與函數的連接

while True:
    cv2.imshow("OpenCV", image)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("cv2.setMouseCallback 20 按ESC離開")


def onChange(x):
    b = cv2.getTrackbarPos("B", "OpenCV")  # 建立B通道顏色
    g = cv2.getTrackbarPos("G", "OpenCV")  # 建立G通道顏色
    r = cv2.getTrackbarPos("R", "OpenCV")  # 建立R通道顏色
    image[:] = [b, g, r]  # 設定背景色


W, H = 640, 480  # 影像寬, 影像高
image = np.ones((H, W, 3), np.uint8) * 255  # 白圖

cv2.namedWindow("OpenCV")
cv2.createTrackbar("B", "OpenCV", 0, 255, onChange)  # 藍色通道控制
cv2.createTrackbar("G", "OpenCV", 0, 255, onChange)  # 綠色通道控制
cv2.createTrackbar("R", "OpenCV", 0, 255, onChange)  # 紅色通道控制

while True:
    cv2.imshow("OpenCV", image)
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

"""
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
