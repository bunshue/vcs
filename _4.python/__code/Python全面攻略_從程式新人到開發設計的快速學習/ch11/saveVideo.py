import tkinter as tk
import cv2
def fnSave():
    cap = cv2.VideoCapture(0)   #打開攝影機
    fps = cap.get(cv2.CAP_PROP_FPS)		#取得播放速率
    setFourcc=spnFourcc.get()   #讀取使用者選擇的編碼器
    width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fileName=entFN.get()+'.avi'         #讀取使用者輸入的檔名
    fourcc = cv2.VideoWriter_fourcc(*setFourcc)  #取得編碼器的四字元碼
    #建立影像寫入器 out
    out = cv2.VideoWriter(fileName,fourcc,fps,(width,height))
    cv2.namedWindow('show')
    while(True):
        ret,img = cap.read()    #擷取一張影像
        out.write(img)          #影像寫入影片檔
        cv2.imshow('show',img)  #顯示影像
        key_pressed = cv2.waitKey(1)
        if key_pressed == 27:  #若按Esc鍵
            break
    cap.release()    #關閉攝影機
    out.release()    #關閉寫入器
    cv2.destroyAllWindows()  #關閉視窗

win = tk.Tk()
win.title('錄製影片')
win.geometry('280x160')
lfrmSet=tk.LabelFrame(win,text='設定：',relief='raised',borderwidth=2)
lfrmSet.pack(pady=5)
tk.Label(lfrmSet,text='編碼器：').grid(row=0,column=0,pady=3)
spnFourcc=tk.Spinbox(lfrmSet,value=('XVID','DIVX','MJPG','I420'),width=10)
spnFourcc.grid(row=0,column=1,pady=3,sticky='w')
tk.Label(lfrmSet,text='檔名：').grid(row=2,column=0,pady=3)
entFN = tk.Entry(lfrmSet, width=20)
entFN.grid(row=2,column=1,pady=3,sticky='w')
tk.Label(lfrmSet,text='按<確定>鈕開始錄製，按<Esc>鍵停止').grid(row=3,column=0,columnspan=2)
btnSave=tk.Button(win, text=' 確定 ',command=fnSave)
btnSave.pack(pady=10)
win.mainloop()



