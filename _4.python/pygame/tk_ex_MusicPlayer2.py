def choose():  # 選曲
    global playsong
    msg.set("\n播放歌曲：" + choice.get())
    playsong = choice.get()


def pausemp3():  # 暫停
    mixer.music.pause()
    msg.set("\n暫停播放 {}".format(playsong))


def increase():  # 音量大
    global volume
    volume += 0.1
    if volume >= 1:
        volume = 1
    mixer.music.set_volume(volume)


def decrease():  # 音量小
    global volume
    volume -= 0.1
    if volume <= 0.3:
        volume = 0.3
    mixer.music.set_volume(volume)


def playmp3():  # 播放
    global status, playsong, preplaysong
    if playsong == preplaysong:  # 同一首歌曲
        if not mixer.music.get_busy():
            mixer.music.load(playsong)
            mixer.music.play(loops=-1)
        else:
            mixer.music.unpause()
        msg.set("\n正在播放：{}".format(playsong))
    else:  # 更換歌曲
        playNewmp3()
        preplaysong = playsong


def playNewmp3():  # 播放新曲
    global playsong
    mixer.music.stop()
    mixer.music.load(playsong)
    mixer.music.play(loops=-1)
    msg.set("\n正在播放：{}".format(playsong))


def stopmp3():  # 停止播放
    mixer.music.stop()
    msg.set("\n停止播放")


def exitmp3():  # 結束
    mixer.music.stop()
    win.destroy()


### 主程式從這裡開始 ###

import tkinter as tk
from pygame import mixer
import glob

mixer.init()
win = tk.Tk()
win.geometry("640x380")
win.title("mp3 播放器")

labeltitle = tk.Label(win, text="\nmp3 播放器", fg="red", font=("新細明體", 12))
labeltitle.pack()

frame1 = tk.Frame(win)  # mp3 歌曲容器
frame1.pack()

source_dir = "mp3/"
mp3files = glob.glob(source_dir + "*.mp3")

playsong = preplaysong = ""
index = 0
volume = 0.6
choice = tk.StringVar()

for mp3 in mp3files:  # 建立歌曲選項按鈕
    rbtem = tk.Radiobutton(frame1, text=mp3, variable=choice, value=mp3, command=choose)
    if index == 0:  # 選取第1個選項按鈕
        rbtem.select()
        playsong = preplaysong = mp3
    rbtem.grid(row=index, column=0, sticky="w")
    index += 1

msg = tk.StringVar()
msg.set("\n播放歌曲：")
label = tk.Label(win, textvariable=msg, fg="blue", font=("新細明體", 10))
label.pack()
labelsep = tk.Label(win, text="\n")
labelsep.pack()

frame2 = tk.Frame(win)  # 按鈕容器
frame2.pack()
button1 = tk.Button(frame2, text="播放", width=8, command=playmp3)
button1.grid(row=0, column=0, padx=5, pady=5)
button2 = tk.Button(frame2, text="暫停", width=8, command=pausemp3)
button2.grid(row=0, column=1, padx=5, pady=5)
button3 = tk.Button(frame2, text="音量調大", width=8, command=increase)
button3.grid(row=0, column=2, padx=5, pady=5)
button4 = tk.Button(frame2, text="音量調小", width=8, command=decrease)
button4.grid(row=0, column=3, padx=5, pady=5)
button5 = tk.Button(frame2, text="停止", width=8, command=stopmp3)
button5.grid(row=0, column=4, padx=5, pady=5)
button6 = tk.Button(frame2, text="結束", width=8, command=exitmp3)
button6.grid(row=0, column=5, padx=5, pady=5)
win.protocol("WM_DELETE_WINDOW", exitmp3)
win.mainloop()
