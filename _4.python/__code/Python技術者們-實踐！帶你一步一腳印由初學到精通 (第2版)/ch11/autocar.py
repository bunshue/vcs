import cv2
import autocar_module as m
import numpy as np

video_filename = 'C:/_git/__大檔與暫存區/GRENZEL 雲創 E3W WiFi 行車記錄器 1080 30fps 日間測試 高速公路 - Mobile01.mp4'
video_filename = 'C:/_git/__大檔與暫存區/DOD行車記錄器-LS300W 日間高速公路實拍.mp4'
video_filename = 'C:/_git/__大檔與暫存區/響尾蛇行車記錄器高解析度1080P - 高速公路白天行駛記錄 -.mp4'
video_filename = 'road.mp4'

capture = cv2.VideoCapture(video_filename)      # 建立 VideoCapture 物件
if capture.isOpened():
    while True:
        sucess, img = capture.read()            # 讀取影像
        if sucess:
            edge = m.get_edge(img)                   # 邊緣偵測
            roi = m.get_roi(edge)                   # 取得 ROI
            lines = cv2.HoughLinesP(image=roi,      # Hough 轉換
                                    rho=3,
                                    theta=np.pi/180,
                                    threshold=30,
                                    minLineLength=50,
                                    maxLineGap=40)
            avglines = m.get_avglines(lines)          # 取得左右 2 條平均線方程式
            if avglines is not None:
                lines = m.get_sublines(img, avglines)  # 取得要畫出的左右 2 條線段
                img = m.draw_lines(img, lines)      # 畫出線段
            cv2.imshow('Frame', img)      # 顯示影像
        k = cv2.waitKey(1)                # 等待按鍵輸入
        if k == ord('q') or k == ord('Q'):  # 按下 Q(q) 結束迴圈
            print('exit')
            cv2.destroyAllWindows()         # 關閉視窗
            capture.release()               # 關閉攝影機
            break
else:
    print('開啟攝影機失敗')
