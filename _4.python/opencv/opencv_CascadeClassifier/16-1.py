import cv2
import time
from datetime import datetime


xml_filename = r'C:\_git\vcs\_4.python\_data\haarcascade_frontalface_default.xml'


def face_add(img):
    print('稍後在此加入新增人員功能')
#-----------------------------------#


def face_who(img):
    print('稍後在此加入人臉身分辨識功能')
#-----------------------------------#


def face_shot(function):
    isCnt = False       # 用來判斷是否正在進行倒數計時中
    face_detector = cv2.CascadeClassifier(xml_filename)  # 建立臉部辨識物件
    capture = cv2.VideoCapture(0)                   # 開啟編號 0 的攝影機
    while capture.isOpened():                      # 判斷攝影機是否開啟成功
        sucess, img = capture.read()            # 讀取攝影機影像
        if not sucess:
            print('讀取影像失敗')
            continue
        img_copy = img.copy()                       # 複製影像
        faces = face_detector.detectMultiScale(     # 從攝影機影像中偵測人臉
            img,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(200, 200))
        if len(faces) == 1:                     # 如果偵測到一張人臉
            if isCnt == False:
                t1 = time.time()                # 紀錄現在的時間
                isCnt = True                    # 告訴程式目前進入倒數狀態
            cnter = 5 - int(time.time() - t1)   # 更新倒數計時器
            for (x, y, w, h) in faces:          # 畫出人臉位置
                cv2.rectangle(                  # 繪製矩形
                    img_copy, (x, y), (x+w, y+h),
                    (0, 255, 255), 2)
                cv2.putText(                    # 繪製倒數數字
                    img_copy, str(cnter),
                    (x+int(w/2), y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 255), 2)
            if cnter == 0:                  # 倒數結束
                isCnt = False               # 告訴程式離開倒數狀態
                filename = datetime.now().strftime(
                    '%Y-%m-%d %H.%M.%S')        # 時間格式化
                cv2.imwrite(filename + '.jpg', img)  # 儲存影像檔案
                #-----------------------------------------#
                if function == 'add':         # 打卡系統新增人員
                    face_add(img)
                elif function == 'who':  # 進行人臉身分識別功能
                    face_who(img)
                #-----------------------------------------#
        else:                                 # 如果不是一張人臉
            isCnt = False                     # 設定非倒數狀態

        cv2.imshow('Frame', img_copy)         # 顯示影像
        k = cv2.waitKey(1)                    # 讀取按鍵輸入(若無會傳回 -1)
        if k == ord('q') or k == ord('Q'):  # 按下 q 離開迴圈, 結束程式
            print('exit')
            cv2.destroyAllWindows()           # 關閉視窗
            capture.release()                 # 關閉攝影機
            break                             # 離開無窮迴圈, 結束程式
    else:
        print('開啟攝影機失敗')


#-----------------------------------#
face_shot('who')                         # 呼叫自訂函式
