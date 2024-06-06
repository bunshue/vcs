import cv2
import time
import datetime
import tkinter as tk

RECORD_TIME_MINUTE = 10

print('------------------------------------------------------------')	#60個

def WebCamRecord():
    cap = cv2.VideoCapture(0)   #打開攝影機
    fps = cap.get(cv2.CAP_PROP_FPS)		#取得播放速率
    setFourcc=spinboxFourcc.get()   #讀取使用者選擇的編碼器
    print(setFourcc)
    width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    record_filename = 'Video_' + setFourcc + time.strftime("_%Y%m%d_%H%M%S", time.localtime()) + '.avi'
    record_time_st = time.time()
    now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    print('開始錄影時間 :', now)
    print('預計錄影時間 :', RECORD_TIME_MINUTE, '分')
    print('現在錄影時間(分): ', end = "")
    
    fourcc = cv2.VideoWriter_fourcc(*setFourcc)  #取得編碼器的四字元碼
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
        key_pressed = cv2.waitKey(1)
        if key_pressed == 27:  #若按Esc鍵
            break
    cap.release()    #關閉攝影機
    out.release()    #關閉寫入器
    cv2.destroyAllWindows()  #關閉視窗
    now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    print('\n完成錄影時間 :', now)
    print('存檔檔名 :', record_filename)
    

print('------------------------------------------------------------')	#60個

print('錄影程式')

window = tk.Tk()
window.title('錄製影片')
window.geometry('280x200')

tk.Label(window,text='編碼器：').grid(row=0,column=0,pady=3)

spinboxFourcc=tk.Spinbox(window,value=('XVID','DIVX','MJPG','I420'),width=10)
spinboxFourcc.grid(row=0,column=1,pady=3,sticky='w')

button1=tk.Button(window, text='開始錄影',command=WebCamRecord)
button1.grid(row=4,column=0,columnspan=1)

button2=tk.Button(window, text='停止錄影',command=WebCamRecord)
button2.grid(row=4,column=1,columnspan=1)

window.mainloop()

print('------------------------------------------------------------')	#60個
