import tkinter as tk
import cv2

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

def fnColor():
    img = cv2.imread(filename)    
    cv2.namedWindow('show')   	#建立show視窗
    cv2.imshow('show',img)		#在show視窗顯示img圖像
    cv2.waitKey(0)
    cv2.destroyWindow('show')	#關閉show視窗

def fnBW():
    img = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    cv2.namedWindow('show')     #建立show視窗
    cv2.imshow('show',img)		#在show視窗顯示img圖像
    cv2.waitKey(3000)
    cv2.destroyWindow('show')	#關閉show視窗
    
def fnSave():
    img = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(fn.get()+spnExe.get(), img)

win = tk.Tk()
win.title('圖像')
win.geometry('300x140')
btnColor = tk.Button(win, text='原圖載入', command=fnColor)
btnColor.pack(padx=5,pady=5,fill='x')
btnBW = tk.Button(win, text='灰階載入', command=fnBW)
btnBW.pack(padx=5,pady=5,fill='x')
tk.Label(win,text='檔名：').pack(side='left')

fn = tk.StringVar()
fn.set('test')
entFN = tk.Entry(win, textvariable = fn,width=8)
entFN.pack(side='left')
tk.Label(win,text='副檔名：').pack(side='left')
spnExe=tk.Spinbox(win,values=['.bmp','.jpg','.png','.tif'],width=5)
spnExe.pack(side='left')
btnSave = tk.Button(win, text='存成灰階', command=fnSave)
btnSave.pack(side='left')

win.mainloop()

cv2.destroyAllWindows() #關閉所有視窗
