import cv2
import time
import datetime
import tkinter as tk

ESC = 27
SPACE = 32
RECORD_TIME_MINUTE = 10

ENCODING_TYPE = 'XVID'  # 編碼器
#'XVID','DIVX','MJPG','I420'

print('------------------------------------------------------------')	#60個

def StartWebCamRecord():
    global flag_stop_webcam_record
    flag_stop_webcam_record = False
    cap = cv2.VideoCapture(0)   #打開攝影機
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # 取得影像寬度
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 取得影像高度
    fps = cap.get(cv2.CAP_PROP_FPS)		#取得播放速率
    record_filename = 'Video_' + ENCODING_TYPE + time.strftime("_%Y%m%d_%H%M%S", time.localtime()) + '.avi'
    record_time_st = time.time()
    now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    print('開始錄影時間 :', now)
    print('預計錄影時間 :', RECORD_TIME_MINUTE, '分')
    print('錄影時間(分) :', end = "")

    #建立視訊編碼 fourcc XVID
    ENCODING_TYPE = 'XVID'  # 編碼器
    #建立視訊編碼 fourcc
    fourcc = cv2.VideoWriter_fourcc(*ENCODING_TYPE)

    #建立影像寫入器 out
    out = cv2.VideoWriter(record_filename,fourcc,fps,(width,height))
    cv2.namedWindow('show')

    show_minitues_info = 0
    while(True):
        ret,img = cap.read()    #擷取一張影像
        
        now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        cv2.putText(img, now, (20, 40),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
        
        out.write(img)          #影像寫入影片檔
        cv2.imshow('show',img)  #顯示影像

        record_time_elapsed = time.time() - record_time_st
        record_minute = int(record_time_elapsed//60)
        if record_minute != show_minitues_info:
            show_minitues_info = record_minute
            print(record_minute, end = " ")
        
        if record_time_elapsed > 60 * RECORD_TIME_MINUTE:
            break
        """ fail
        if flag_stop_webcam_record == True:
            print('停止錄影')
            #break
        """
        k = cv2.waitKey(1)
        if k == ESC:     #ESC
            break
    cap.release()    #關閉攝影機
    out.release()    #關閉寫入器
    cv2.destroyAllWindows()  #關閉視窗
    now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    print('\n完成錄影時間 :', now)
    print('存檔檔名 :', record_filename)
    
def StopWebCamRecord():
    pass
    """
    錄影中無法接受tk按鍵
    global flag_stop_webcam_record
    flag_stop_webcam_record = True
    print('你按了 停止錄影')
    """
    
print('------------------------------------------------------------')	#60個

print('錄影程式')

flag_stop_webcam_record = False

window = tk.Tk()
window.title('錄製影片')
window.geometry('280x200')

button1=tk.Button(window, text='開始錄影',command=StartWebCamRecord)
button1.grid(row=4,column=0,columnspan=1)

button2=tk.Button(window, text='停止錄影',command=StopWebCamRecord)
button2.grid(row=4,column=1,columnspan=1)

window.mainloop()

print('------------------------------------------------------------')	#60個
