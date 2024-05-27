import tkinter as tk
import winsound

def fnRead():
    n=str(sclNum.get())
    if len(n)==1:   #若字串長度為1表個位數
        fnSound(n)  #呼叫fnSound播放該數的音檔
    else:           #兩位數時
        if n[0] !='1':      #若第一個字不是1
            fnSound(n[0])   #呼叫fnSound播放十位數的音檔
        fnSound('10')       #呼叫fnSound播放10.wav
        if n[1] !='0':      #若第一個字不是0
            fnSound(n[1])   #呼叫fnSound播放個位數的音檔        
        
def fnSound(s):
    winsound.PlaySound(s+'.wav', winsound.SND_FILENAME)   
     
win = tk.Tk()
win.title('讀數值')
win.geometry('260x140')
sclNum=tk.Scale(win,label='數值：',orient='horizontal',from_=1,to=99,length=200)
sclNum.pack(pady=10)
btnRead=tk.Button(win, text=' 確定 ',command=fnRead)
btnRead.pack(pady=20)
win.mainloop()

