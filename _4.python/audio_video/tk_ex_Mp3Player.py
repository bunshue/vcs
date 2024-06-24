"""
mp3 播放器

"""

print("------------------------------------------------------------")  # 60個

import os
import sys
import glob
import tkinter as tk
from tkinter.filedialog import askopenfile  # tk之openFileDialog
from tkinter.filedialog import asksaveasfile  # tk之saveFileDialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

import pygame

count = 0
flag_pause_mode = False
flag_new_mp3_file = False

print("------------------------------------------------------------")  # 60個


def pausemp3():  # 暫停
    global flag_pause_mode
    if flag_pause_mode == False:
        flag_pause_mode = True
        pygame.mixer.music.pause() #暫停播放
    else:
        flag_pause_mode = False
        pygame.mixer.music.unpause() #恢復播放


def increase():  # 音量大
    global volume
    volume += 0.02
    if volume >= 1:
        volume = 1
    pygame.mixer.music.set_volume(volume)


def decrease():  # 音量小
    global volume
    volume -= 0.02
    if volume <= 0.2:
        volume = 0.2
    pygame.mixer.music.set_volume(volume)


def playmp3():  # 播放
    print(mp3_filename)
    global status
    global flag_new_mp3_file
    if flag_new_mp3_file == True:  # 更換歌曲
        playNewmp3a()
    else:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(mp3_filename)
            pygame.mixer.music.play(loops=-1)  # -1: 循環播放
        else:
            print("沒事")
    flag_new_mp3_file = False


def playNewmp3a():  # 播放新曲
    global mp3_filename
    pygame.mixer.music.stop() # 停止播放
    pygame.mixer.music.load(mp3_filename)
    pygame.mixer.music.play(loops=-1)


def playNewmp3b(song):
    global status
    pygame.mixer.music.stop() # 停止播放
    pygame.mixer.music.load(mp3files[index])
    pygame.mixer.music.play() # 無參數, 單次播放
    status = "正在播放 {}".format(mp3files[index])


def stopmp3():  # 停止播放
    pygame.mixer.music.stop() # 停止播放


def exitmp3():  # 結束
    pygame.mixer.music.stop() # 停止播放
    window.destroy()  # 關閉視窗


def button00Click():
    print("你按了 選取檔案")
    button00_text.set("選取檔案...")
    file = askopenfile(
        parent=window, mode="rb", title="選取mp3", filetypes=[("mp3檔案", "*.mp3")]
    )
    if file:
        global mp3_filename
        global flag_new_mp3_file
        mp3_filename_old = mp3_filename
        flag_new_mp3_file = False
        if mp3_filename != file.name:
            flag_new_mp3_file = True
            mp3_filename = file.name
            message = "檔案 : " + mp3_filename
            print(message)
            text1.insert("end", message)
            main_message1.set(message)

    button00_text.set("選取檔案")


def button01Click():
    print("你按了 播放")
    playmp3()


def button02Click():
    print("你按了 暫停")
    pausemp3()


def button03Click():
    print("你按了 音量調大")
    increase()


def button04Click():
    print("你按了 音量調小")
    decrease()


def button05Click():
    print("你按了 停止")
    stopmp3()


def button10Click():
    print("你按了")
    #pygame.mixer.music.play()# 無參數, 單次播放
    status = pygame.mixer.music.get_busy() # True:正在播放, False:不在播放中
    print(status)


def button11Click():
    print("你按了 選取資料夾")


def button12Click():
    print("你按了 上一首")
    global index
    index -= 1
    if index < 0:
        index = len(mp3files) - 1
    playNewmp3b(mp3files[index])
    mp3_filename = mp3files[index]
    main_message1.set(mp3_filename)


def button13Click():
    print("你按了  下一首")
    global index
    index += 1
    if index == len(mp3files):
        index = 0
    playNewmp3b(mp3files[index])
    mp3_filename = mp3files[index]
    main_message1.set(mp3_filename)


def button14Click():
    # print('你按了button14')
    set_data()
    clear_text1()


def button15Click():
    # print('你按了button15')
    exitmp3()


def set_data():
    """
    print('set_data')
    #回傳結果
    mesg = text1.get("1.0","end")
    mesg= mesg + dummy_data
    print(mesg)
    text1.insert('end', mesg)
    """
    global count
    count = count + 1
    message = "  次數" + str(count)
    text1.insert("end", message)


def clear_text1():
    text1.delete(1.0, "end")
    # 執行 clear 函式時，清空內容


window = tk.Tk()
window.geometry("600x800")

main_message1 = tk.StringVar()
main_message2 = tk.StringVar()

# 設定主視窗大小
W = 800
H = 800
x_st = 100
y_st = 100
# size = str(W)+'x'+str(H)
# size = str(W)+'x'+str(H)+'+'+str(x_st)+'+'+str(y_st)
# window.geometry(size)
# window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
# print('{0:d}x{1:d}+{2:d}+{3:d}'.format(W, H, x_st, y_st))

# 顯示在正中央
screenWidth = window.winfo_screenwidth()  # 螢幕寬度
screenHeight = window.winfo_screenheight()  # 螢幕高度
W = 800  # 視窗寬
H = 800  # 視窗高
x_st = (screenWidth - W) / 2  # 視窗左上角x軸位置
y_st = (screenHeight - H) / 2  # 視窗左上角Y軸位置
window.geometry("%dx%d+%d+%d" % (W, H, x_st, y_st))

# 設定主視窗標題
window.title("mp3播放器")

# 設定主視窗之背景色
# window.configure(bg = "#7AFEC6")
# window.configure(bg = '#00ff00')   # 視窗背景顏色
# window.configure(bg = 'yellow')    # 視窗背景顏色

icon_filename = "C:/_git/vcs/_1.data/______test_files1/_icon/唐.ico"
window.iconbitmap(icon_filename)  # 更改圖示

x_st = 50
y_st = 50
dx = 120
dy = 80
w = 12
h = 3

button00_text = tk.StringVar()
button00 = tk.Button(
    window,
    textvariable=button00_text,
    width=w,
    height=h,
    command=button00Click,
    text="",
)
button00.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button00_text.set("選取檔案")

button01 = tk.Button(window, width=w, height=h, command=button01Click, text="播放")
button01.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button02 = tk.Button(window, width=w, height=h, command=button02Click, text="暫停")
button02.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button03 = tk.Button(window, width=w, height=h, command=button03Click, text="音量調大")
button03.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button04 = tk.Button(window, width=w, height=h, command=button04Click, text="音量調小")
button04.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button05 = tk.Button(window, width=w, height=h, command=button05Click, text="停止")
button05.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button00.place(x=x_st + dx * 0, y=y_st + dy * 0)
button01.place(x=x_st + dx * 1, y=y_st + dy * 0)
button02.place(x=x_st + dx * 2, y=y_st + dy * 0)
button03.place(x=x_st + dx * 3, y=y_st + dy * 0)
button04.place(x=x_st + dx * 4, y=y_st + dy * 0)
button05.place(x=x_st + dx * 5, y=y_st + dy * 0)

button10 = tk.Button(window, width=w, height=h, command=button10Click, text="循環播放")
button10.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button11 = tk.Button(window, width=w, height=h, command=button11Click, text="選取資料夾")
button11.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button12 = tk.Button(window, width=w, height=h, command=button12Click, text="上一首")
button12.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button13 = tk.Button(window, width=w, height=h, command=button13Click, text="下一首")
button13.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button14 = tk.Button(
    window, width=w, height=h, command=button14Click, text="Set/Clear Data"
)
button14.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button15 = tk.Button(window, width=w, height=h, command=button15Click, text="離開")
button15.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)

button10.place(x=x_st + dx * 0, y=y_st + dy * 1)
button11.place(x=x_st + dx * 1, y=y_st + dy * 1)
button12.place(x=x_st + dx * 2, y=y_st + dy * 1)
button13.place(x=x_st + dx * 3, y=y_st + dy * 1)
button14.place(x=x_st + dx * 4, y=y_st + dy * 1)
button15.place(x=x_st + dx * 5, y=y_st + dy * 1)

font_size = 20

# 加入 Label
label_message1 = tk.Label(
    window, font=("標楷體", font_size), fg="red", textvariable=main_message1
)
label_message1.pack()
label_message1.place(x=5, y=0 + 10)
main_message1.set("")

label_message2 = tk.Label(
    window, font=("標楷體", font_size), fg="red", textvariable=main_message2
)
label_message2.pack()
label_message2.place(x=5 + W * 3 / 4, y=0 + 10)
main_message2.set("")

# 加入 Text
text1 = tk.Text(window, width=100, height=30)  # 放入多行輸入框
text1.pack()
text1.place(x=x_st + dx * 0, y=y_st + dy * 2 + 20)

# mp3_foldername = 'C:/_git/vcs/_1.data/______test_files1/_mp3/'

# 日文資料夾名稱有問題
# mp3_foldername = 'D:/vcs/astro/_DATA2/_mp3/japanese/美空ひばり(美空云雀).-.[美空ひばり全曲集1].专辑.(MP3)/'

mp3_foldername = "D:/vcs/astro/_DATA2/_mp3/japanese/昭和の歌--演歌系列1/"

mp3files = glob.glob(mp3_foldername + "*.mp3")
index = 0
print(mp3files)

# mp3_filename = 'C:/_git/vcs/_1.data/______test_files1/_mp3/02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3'
mp3_filename = mp3files[index]

message = mp3_filename
main_message1.set(message)

pygame.mixer.init()  # 最初化mixer

volume = 0.6  # 起始音量

window.protocol("WM_DELETE_WINDOW", exitmp3)

window.mainloop()

print("------------------------------------------------------------")  # 60個


""" 新進

# 撥放音樂
def playmusic():                                        # 處理按撥放紐

    pygame.mixer.music.load('notify.mp3')           # 撥放選項1音樂
    
    town = r'C:\Windows\Media\town.mid'
    pygame.mixer.music.load(town)                   # 撥放選項2音樂

pygame.mixer.music.load(r'C:\Windows\Media\town.mid')

    onestop = r'C:\Windows\Media\onestop.mid'
    pygame.mixer.music.load(onestop)                # 撥放選項3音樂

# 停止撥放音樂
def stopmusic():                                        # 處理按結束紐

          soundObj = pygame.mixer.Sound(r'C:\Windows\Media\notify.wav')  # 建立碰撞聲音物件            
            soundObj.play()                     # 發出碰撞聲音
"""

