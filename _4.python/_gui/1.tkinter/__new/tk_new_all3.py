def choose():  # 選曲
    global playsong
    msg.set("\n播放歌曲：" + choice.get())
    playsong = choice.get()


def exitmp3():  # 結束
    win.destroy()


import tkinter as tk
import glob

win = tk.Tk()
win.geometry("640x380")
win.title("mp3 播放器")

labeltitle = tk.Label(win, text="\nmp3 播放器", fg="red", font=("新細明體", 12))
labeltitle.pack()

frame1 = tk.Frame(win)  # mp3 歌曲容器
frame1.pack()


# 撈出單層mp3檔
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
button1 = tk.Button(frame2, text="播放", width=8)
button1.grid(row=0, column=0, padx=5, pady=5)
button2 = tk.Button(frame2, text="暫停", width=8)
button2.grid(row=0, column=1, padx=5, pady=5)
button3 = tk.Button(frame2, text="音量調大", width=8)
button3.grid(row=0, column=2, padx=5, pady=5)
button4 = tk.Button(frame2, text="音量調小", width=8)
button4.grid(row=0, column=3, padx=5, pady=5)
button5 = tk.Button(frame2, text="停止", width=8)
button5.grid(row=0, column=4, padx=5, pady=5)
button6 = tk.Button(frame2, text="結束", width=8)
button6.grid(row=0, column=5, padx=5, pady=5)

win.protocol("WM_DELETE_WINDOW", exitmp3)
win.mainloop()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
