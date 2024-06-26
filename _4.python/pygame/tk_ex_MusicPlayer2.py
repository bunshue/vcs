#MP3播放器
def choose():
    global playsong
    message.set("\n播放歌曲：" + choice.get())
    playsong=choice.get()
def pausemp3(): 
    mixer.music.pause() 
    message.set("\n暫停播放 {}".format(playsong))   
def increase():
    global volume
    volume +=0.1
    if volume>=1.0:
        volume=1.0
    mixer.music.set_volume(volume) 
def decrease():
    global volume
    volume -=0.1
    if volume<=0.2:
        volume=0.2
    mixer.music.set_volume(volume)  
def playmp3():
    global status,playsong,preplaysong
    if playsong==preplaysong:
        if not mixer.music.get_busy():
            mixer.music.load(playsong)
            mixer.music.play(loops=-1) 
        else:
            mixer.music.unpause() 
        message.set("\n正在播放：{}".format(playsong))
    else:
        playnewmp3()
        preplaysong=playsong 
def playnewmp3():
    global playsong
    mixer.music.stop()
    mixer.music.load(playsong)   
    mixer.music.play(loops=-1)  
    message.set("\n正在播放：{}".format(playsong))
def stopmp3():
    mixer.music.stop()
    message.set("\n停止播放") 
def loadmp3():
    global volume
    global playsong
    global preplaysong
    global choice
    global pdir
    frame1 = tk.Frame(win)
    frame1.pack()
    mp3files = []
    mp3files = glob.glob(pdir.get()+"*.mp3")
    playsong=preplaysong = ""
    index = 0
    volume= 0.8
    choice = tk.StringVar()    
    for mp3 in mp3files:  
        prbutton = tk.Radiobutton(frame1,text=mp3,variable=choice,value=mp3,command=choose)
        if(index==0):     
            prbutton.select()
            playsong=preplaysong=mp3
        prbutton.grid(row=index, column=0, sticky="w")
        index += 1      
    message.set("\n讀取檔案")
def exitmp3():
    mixer.music.stop()
    win.destroy() 

import tkinter as tk
from pygame import mixer
import glob

mixer.init()
win=tk.Tk()
win.geometry("640x380")
win.title("MP3播放程式")
labeltitle = tk.Label(win, text="\nMP3播放程式", fg="blue",font=("標楷體",12))
labeltitle.pack()
frame0 = tk.Frame(win)
frame0.pack()
pdir = tk.StringVar()
plabel1 = tk.Label(frame0, text="請輸入目錄:", width=8)
plabel1.grid(row=0, column=0, padx=5, pady=5)
pentry = tk.Entry(frame0, textvariable=pdir, width=12)
pdir.set('music/')
pentry.grid(row=0, column=1, padx=5, pady=5)   
button1 = tk.Button(frame0, text="播放", width=8,command=playmp3)
button1.grid(row=1, column=0, padx=5, pady=5)
button2 = tk.Button(frame0, text="暫停", width=8,command=pausemp3)
button2.grid(row=1, column=1, padx=5, pady=5)
button3 = tk.Button(frame0, text="調大音量", width=8,command=increase)
button3.grid(row=1, column=2, padx=5, pady=5)
button4 = tk.Button(frame0, text="調小音量", width=8,command=decrease)
button4.grid(row=1, column=3, padx=5, pady=5)
button5 = tk.Button(frame0, text="停止", width=8,command=stopmp3)
button5.grid(row=1, column=4, padx=5, pady=5)
button7 = tk.Button(frame0, text="讀取檔案", width=8,command=loadmp3)
button7.grid(row=1, column=5, padx=5, pady=5)
button6 = tk.Button(frame0, text="結束", width=8,command=exitmp3)
button6.grid(row=1, column=6, padx=5, pady=5)
win.protocol("WM_DELETE_WINDOW", exitmp3)   
message = tk.StringVar()
message.set("\n播放歌曲：")
plabel2 = tk.Label(win, textvariable=message,fg="blue",font=("標楷體",10))
plabel2.pack() 
plabel3 = tk.Label(win, text="\n")
plabel3.pack()   
win.mainloop()

print("------------------------------------------------------------")  # 60個

