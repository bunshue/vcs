def makeFace(facename, msg, endstr):
    print(msg)  #顯示提示訊息
    cv2.namedWindow("frame")
    cv2.waitKey(0)
    cap = cv2.VideoCapture(0)  #開啟攝影機
    while(cap.isOpened()):  #攝影機為開啟狀態
        ret, img = cap.read()  #讀取影像
        if ret == True:  #讀取成功
            cv2.imshow("frame", img)  #顯示影像
            k = cv2.waitKey(100)  #每0.1秒讀一次鍵盤
            if k == ord("z") or k == ord("Z"):  #使用者按「z」鍵
                cv2.imwrite(facename,img)  #存檔
                image = cv2.imread(facename)  #讀檔做人臉辨識
                faces = faceCascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), flags = cv2.CASCADE_SCALE_IMAGE)
                (x, y, w, h) = (faces[0][0], faces[0][1], faces[0][2], faces[0][3])  #只取第一張人臉
                image1 = Image.open(facename).crop((x, y, x+w, y+h))  #擷取人臉
                image1 = image1.resize((200, 200), Image.ANTIALIAS)  #轉為解析度200x200
                image1.save(facename)  #存檔
                break;
    cap.release()  #關閉攝影機攝影機
    cv2.destroyAllWindows()
    print(endstr)
    return

import cv2, os, math, operator
from PIL import Image
from functools import reduce

# OpenCV 人臉識別分類器
xml_filename = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(xml_filename)   #建立辨識物件

recogname = "media\\recogface.jpg"  #使用者人臉檔案
loginname = "media\\loginface.jpg"  #登入者人臉檔案
os.system("cls")  #清除螢幕
if(os.path.exists(recogname)):  #如果使用者人臉檔案已存在
    msg = "按任意鍵建立登入者臉譜。\n攝影機開啟後按「z」拍照比對！"
    makeFace(loginname, msg, "")  #建立登入者人臉檔案
    pic1 = Image.open(recogname)  #開啟使用者人臉檔案
    pic2 = Image.open(loginname)  #開啟登入者人臉檔案
    h1 = pic1.histogram()  #計算圖形差異度
    h2 = pic2.histogram()
    diff = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1))
    if(diff <= 100):  #若差度在100內視為通過驗證
        print("通過驗證，歡迎使用本系統！ diff=%4.2f" % diff)
    else:
        print("臉譜不正確，無法使用本系統！ diff=%4.2f" % diff)
else:  #如果使用者人臉檔案不存在
    msg = "按任意鍵建立使用者臉譜。\n攝影機開啟後按「z」拍照！\n"
    endstr = "使用者臉譜建立完成！"
    makeFace(recogname, msg, endstr)  #建立使用者人臉檔案
