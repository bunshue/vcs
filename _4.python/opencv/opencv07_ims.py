import cv2
import sys

ESC = 27

print("------------------------------------------------------------")  # 60個

W, H = 640, 480
cx, cy = W//2, H//2
mode = 0 # 0 預設模式 1: 中心放大兩倍

print("把 直方圖均衡化處理 套用在webcam上 黑白")
print("把 直方圖均衡化處理 套用在webcam上 彩色")

video_filename = "D:/內視鏡影片/NBI錄影_V20241009_081309.mp4"
# cap = cv2.VideoCapture(video_filename)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

def OnMouseAction(event, x, y, flags, param):
    global cx, cy
    global mode
    if event == cv2.EVENT_LBUTTONDOWN:
        print("mode =", mode, "左鍵畫點, 取得座標 :", x, y)
        x = x//2
        y = y//2
        if x < W//4:
            x=W//4
        if x > W//4*3:
            x=W//4*3
        if y < H//4:
            y=H//4
        if y > H//4*3:
            y=H//4*3
        cx, cy = x, y
        if mode == 0:
            mode = 1

cv2.namedWindow("Original")
cv2.setMouseCallback("Original", OnMouseAction)

while True:
    ret, frame = cap.read()  # 從攝影機擷取一張影像

    if ret == False:
        print("無影像, 離開")
        break

    if mode == 1:
        # 裁切圖片
        x_st = cx - W//4
        y_st = cy - H//4
        ww = W//2
        hh = H//2
        frame = frame[y_st : y_st + hh, x_st : x_st + ww]
        frame = cv2.resize(frame, (W, H))
        

    cut = 80

    # 畫一些標記
    dd = 5
    topLeft = (cut - dd, cut - dd)
    topLeft = (cx - W//2 + cut - dd, cy - H//2 + cut - dd)
    
    bottomRight = (W - cut + dd, H - cut + dd)
    bottomRight = (cx + W//2 - cut + dd, cy+ H//2 - cut + dd)

    #cv2.rectangle(frame, topLeft, bottomRight, 255, 2)  #藍色框

    # 原圖
    #cv2.imshow("Original", frame)

    # 裁切圖片 ST
    # 裁切區域的 x 與 y 座標（左上角）
    x_st, y_st = cut, cut
    # 裁切區域的長度與寬度
    w, h = W - x_st * 2, H - y_st * 2
    frame2 = frame[y_st : y_st + h, x_st : x_st + w]
    frame3 = frame2
    # 裁切圖片 SP

    gray1 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Gray", gray1)

    gray2 = cv2.equalizeHist(gray1)
    cv2.imshow("Histogram1", gray2)
    # 裁切圖片 SP

    b, g, r = cv2.split(frame3)

    bb = cv2.equalizeHist(b)
    gg = cv2.equalizeHist(g)
    rr = cv2.equalizeHist(r)

    frame3 = cv2.merge([bb, gg, rr])
    cv2.imshow("Histogram2", frame3)

    # 原圖放大兩倍
    frame4 = cv2.resize(frame, (W*2, H*2))
    cv2.imshow("Original", frame4)

    k = cv2.waitKey(1)  # 等待按鍵輸入
    if k == ESC:
        cx, cy = W//2, H//2
        mode = 0
    elif k == ord("Q") or k == ord("q"):  # 按下 Q(q), 離開
        break

cap.release()
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

# plt.hist 參數
# plt.hist(cc, bins=num_bins, color="g", alpha=0.5, density=False)
# density=True   #以密度表示
