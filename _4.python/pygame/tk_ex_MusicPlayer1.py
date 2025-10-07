"""
Python 聲音處理 pygame

mp3 播放器

用 pygame 播放 mp3 檔案
用 pygame 播放 wav 檔案
用 pygame 播放 midi 檔案

"""

print("------------------------------------------------------------")  # 60個

import os
import sys
import glob
import time
import tkinter as tk
from tkinter.filedialog import askopenfile  # tk之openFileDialog
from tkinter.filedialog import asksaveasfile  # tk之saveFileDialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

import pygame

count = 0
flag_pause_mode = False
flag_new_mp3_file = False
mp3_foldernames = []
mp3_filenames = []
mp3_play_index = 0
volume_setup = 100
total_mp3_files = 0
current_playing_mp3_filename = ""  # 現正播放檔案

STATUS_STOP = 0
STATUS_PLAY = 1
STATUS_PAUSE = 2
STATUS_OTHER = 3

flag_play_status = STATUS_STOP

print("------------------------------------------------------------")  # 60個


def pausemp3():  # 暫停
    global flag_pause_mode
    global flag_play_status
    if flag_pause_mode == False:
        flag_pause_mode = True
        pygame.mixer.music.pause()  # 暫停播放
        button02.config(text="恢復")
        flag_play_status = STATUS_PAUSE
    else:
        flag_pause_mode = False
        pygame.mixer.music.unpause()  # 恢復播放
        button02.config(text="暫停")
        flag_play_status = STATUS_PLAY
    show_play_status()


def increase():  # 音量大
    global volume
    volume += 0.02
    if volume >= 1:
        volume = 1
    pygame.mixer.music.set_volume(volume)
    show_play_status()


def decrease():  # 音量小
    global volume
    volume -= 0.02
    if volume <= 0.2:
        volume = 0.2
    pygame.mixer.music.set_volume(volume)
    show_play_status()


def playmp3():  # 播放
    global flag_new_mp3_file
    if flag_new_mp3_file == True:  # 更換歌曲
        playNewmp3a()
    else:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(current_playing_mp3_filename)
            pygame.mixer.music.play(loops=-1)  # -1: 循環播放
        else:
            print("沒事")
    flag_new_mp3_file = False


def playNewmp3a():  # 播放mp3檔案, 要先stop, 再load, 再play
    global current_playing_mp3_filename
    pygame.mixer.music.stop()  # 停止播放, 要先stop, 才不會冒出一個雜音
    pygame.mixer.music.load(current_playing_mp3_filename)
    pygame.mixer.music.play(loops=-1)  # -1: 循環播放


def playNewmp3b(song):
    current_playing_mp3_filename = mp3_filenames[mp3_play_index]
    pygame.mixer.music.stop()  # 停止播放
    pygame.mixer.music.load(current_playing_mp3_filename)
    pygame.mixer.music.play()  # 無參數, 單次播放
    mp3_index.set(str(mp3_play_index + 1) + "/" + str(total_mp3_files))
    main_message1.set("{}".format(os.path.basename(current_playing_mp3_filename)))


def stopmp3():  # 停止播放
    pygame.mixer.music.stop()  # 停止播放


def exitmp3():  # 結束
    global mp3_play_index
    global mp3_foldernames
    global volume_setup

    filename = "tk_ex_MusicPlayer1.txt"
    print("檔名 :", filename)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(str(mp3_play_index))
        f.write("\n")
        f.write(str(volume_setup))
        f.write("\n")

        for _ in mp3_foldernames:
            print(_)
            f.write(_)
            f.write("\n")

    print("離開mp3播放器 要先stop再關閉window")
    pygame.mixer.music.stop()  # 停止播放
    window.destroy()  # 關閉視窗


def show_play_status():
    mesg = ""
    global flag_play_status

    if flag_play_status == STATUS_STOP:
        mesg += "停止 "
    elif flag_play_status == STATUS_PLAY:
        mesg += "播放 "
    elif flag_play_status == STATUS_PAUSE:
        mesg += "暫停 "
    else:
        mesg += "其他 "

    global volume
    mesg += "音量 :" + str(volume)

    main_message2.set(mesg)


def button00Click():
    print("你按了 選取檔案")
    button00_text.set("選取檔案...")
    file = askopenfile(
        parent=window, mode="rb", title="選取mp3", filetypes=[("mp3檔案", "*.mp3")]
    )
    if file:
        global current_playing_mp3_filename
        global flag_new_mp3_file
        current_playing_mp3_filename_old = current_playing_mp3_filename
        flag_new_mp3_file = False
        if current_playing_mp3_filename != file.name:
            flag_new_mp3_file = True
            current_playing_mp3_filename = file.name
            message = "檔案 : " + os.path.basename(current_playing_mp3_filename)
            print(message)
            text1.insert("end", message)
            main_message1.set(message)

    button00_text.set("選取檔案")


def button01Click():
    # print("你按了 播放")
    playmp3()
    main_message1.set("{}".format(os.path.basename(current_playing_mp3_filename)))
    global flag_play_status
    flag_play_status = STATUS_PLAY
    show_play_status()


def button02Click():
    print("你按了 暫停")
    pausemp3()


def button03Click():
    # print("你按了 音量調大")
    increase()


def button04Click():
    # print("你按了 音量調小")
    decrease()


def button05Click():
    print("你按了 停止")
    stopmp3()
    global flag_play_status
    flag_play_status = STATUS_STOP
    show_play_status()


def button10Click():
    print("你按了")
    # pygame.mixer.music.play()# 無參數, 單次播放
    status = pygame.mixer.music.get_busy()  # True:正在播放, False:不在播放中
    print(status)


def button11Click():
    print("你按了 選取資料夾")


def button12Click():
    # print("你按了 上一首")
    global mp3_play_index
    mp3_play_index -= 1
    if mp3_play_index < 0:
        mp3_play_index = len(mp3_filenames) - 1
    current_playing_mp3_filename = mp3_filenames[mp3_play_index]
    playNewmp3b(current_playing_mp3_filename)
    mp3_index.set(str(mp3_play_index + 1) + "/" + str(total_mp3_files))
    main_message1.set("{}".format(os.path.basename(current_playing_mp3_filename)))


def button13Click():
    # print("你按了  下一首")
    global mp3_play_index
    mp3_play_index += 1
    if mp3_play_index == len(mp3_filenames):
        mp3_play_index = 0
    current_playing_mp3_filename = mp3_filenames[mp3_play_index]
    playNewmp3b(current_playing_mp3_filename)
    mp3_index.set(str(mp3_play_index + 1) + "/" + str(total_mp3_files))
    main_message1.set("{}".format(os.path.basename(current_playing_mp3_filename)))


def button14Click():
    # print('你按了button14')
    set_data()
    clear_text1()


def button15Click():
    # print('你按了button15')
    exitmp3()


def button20Click():
    print("你按了button20 測試0")
    filename = (
        "D:/_git/vcs/_1.data/______test_files1/_mp3/02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3"
    )

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()


def button21Click():
    print("你按了button21 測試1 wave / midi")

    """
    print('播放wav檔')
    filename = 'D:/_git/vcs/_1.data/______test_files1/_wav/hit.wav'
    filename = 'test_wave.wav'
    filename = "D:/_git/vcs/_1.data/______test_files1/_wav/harumi99.wav"
    filename = r'C:\Windows\Media\notify.wav'
    
    print('使用 mixer.sound 播放 wave')
    sound = pygame.mixer.Sound(filename)      # 建立Sound物件
    print('此檔案之長度 :', sound.get_length(), '秒')
    sound.play()#播放一次
    #sound.play(loops=0) # 0: 播放一次
    #sound.play(5)#播放N次

    pygame.time.wait(int(sound.get_length()) * 1000)

    print('使用 mixer.music 播放 wave')
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    #print('此檔案之長度 :', pygame.mixer.music.get_length(), '秒') 無
    pygame.mixer.music.play()

    """
    mymidi = r"C:\Windows\Media\town.mid"
    # mymidi = r'C:\Windows\Media\onestop.mid'

    pygame.mixer.music.load(mymidi)

    pygame.mixer.music.play()

    print("完成")


def button22Click():
    print("你按了button22 測試 看list")
    print("目前位置")
    print(mp3_play_index)

    print("資料夾")
    for _ in mp3_foldernames:
        print(_)

    print("檔案")
    cnt = 1
    for _ in mp3_filenames:
        print(str(cnt), _)
        cnt += 1


def button23Click():
    print("你按了button23 測試3")

    # ok
    # pygame.mixer.music.set_pos(10)#設定播放位置(秒)

    # ok
    pygame.mixer.music.fadeout(5000)  # 再播放指定時間后就淡出并停止播放音樂
    # 單位：毫秒
    # 此函數將阻塞，直到音樂淡出

    # ok
    playtime = pygame.mixer.music.get_pos()  # 獲得音樂播放時間(msec), 不是播放位置
    print("目前播放時間 :", playtime)

    """
    
    print('快進 10 秒')
    
    current_pos += 100
    pygame.mixer.music.set_pos(30)
    current_pos = pygame.mixer.music.get_pos()
    print('目前播放位置 :', current_pos)
    """


def button24Click():
    print("你按了button24 測試4")


def button25Click():
    print("你按了button25 測試5")


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

main_message1 = tk.StringVar()  # 放 現正播放檔案
main_message2 = tk.StringVar()  # 放 播放狀態 播放 / 暫停 / 停止 播放時間 單次 循環 聲量......
mp3_index = tk.StringVar()

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

icon_filename = "D:/_git/vcs/_1.data/______test_files1/_icon/唐.ico"
window.iconbitmap(icon_filename)  # 更改圖示

x_st = 80
y_st = 100
dx = 120
dy = 80
w = 12
h = 3


def setVolume(val):
    global volume_setup
    volume = int(scale1.get())
    pygame.mixer.music.set_volume(volume / 100)
    volume_setup = volume


scale1 = tk.Scale(window, from_=100, to=0, length=200, command=setVolume)
scale1.place(x=x_st - 70 + dx * 0, y=y_st + dy * 0 + 30)
scale1.set(100)

scale2 = tk.Scale(window, orient=tk.HORIZONTAL, from_=0, to=100, length=700, command="")
scale2.place(x=x_st + dx * 0, y=y_st + dy * 2 + 55)
scale2.set(100)

button00_text = tk.StringVar()
button00 = tk.Button(
    window,
    textvariable=button00_text,
    width=w,
    height=h,
    command=button00Click,
    text="",
)
button00_text.set("選取檔案")

button01 = tk.Button(window, width=w, height=h, command=button01Click, text="播放")
button02 = tk.Button(window, width=w, height=h, command=button02Click, text="暫停")
button03 = tk.Button(window, width=w, height=h, command=button03Click, text="音量調大")
button04 = tk.Button(window, width=w, height=h, command=button04Click, text="音量調小")
button05 = tk.Button(window, width=w, height=h, command=button05Click, text="停止")
button00.place(x=x_st + dx * 0, y=y_st + dy * 0)
button01.place(x=x_st + dx * 1, y=y_st + dy * 0)
button02.place(x=x_st + dx * 2, y=y_st + dy * 0)
button03.place(x=x_st + dx * 3, y=y_st + dy * 0)
button04.place(x=x_st + dx * 4, y=y_st + dy * 0)
button05.place(x=x_st + dx * 5, y=y_st + dy * 0)

button10 = tk.Button(window, width=w, height=h, command=button10Click, text="循環播放")
button11 = tk.Button(window, width=w, height=h, command=button11Click, text="選取資料夾")
button12 = tk.Button(window, width=w, height=h, command=button12Click, text="上一首")
button13 = tk.Button(window, width=w, height=h, command=button13Click, text="下一首")
button14 = tk.Button(
    window, width=w, height=h, command=button14Click, text="Set/Clear Data"
)
button15 = tk.Button(window, width=w, height=h, command=button15Click, text="離開")

button10.place(x=x_st + dx * 0, y=y_st + dy * 1)
button11.place(x=x_st + dx * 1, y=y_st + dy * 1)
button12.place(x=x_st + dx * 2, y=y_st + dy * 1)
button13.place(x=x_st + dx * 3, y=y_st + dy * 1)
button14.place(x=x_st + dx * 4, y=y_st + dy * 1)
button15.place(x=x_st + dx * 5, y=y_st + dy * 1)

button20 = tk.Button(window, width=w, height=h, command=button20Click, text="測試0")
button21 = tk.Button(
    window, width=w, height=h, command=button21Click, text="播放 wave/midi"
)
button22 = tk.Button(window, width=w, height=h, command=button22Click, text="測試 看list")
button23 = tk.Button(window, width=w, height=h, command=button23Click, text="測試3")
button24 = tk.Button(window, width=w, height=h, command=button24Click, text="測試4")
button25 = tk.Button(window, width=w, height=h, command=button25Click, text="測試5")

button20.place(x=x_st + dx * 0, y=y_st + dy * 2)
button21.place(x=x_st + dx * 1, y=y_st + dy * 2)
button22.place(x=x_st + dx * 2, y=y_st + dy * 2)
button23.place(x=x_st + dx * 3, y=y_st + dy * 2)
button24.place(x=x_st + dx * 4, y=y_st + dy * 2)
button25.place(x=x_st + dx * 5, y=y_st + dy * 2)

# 加入 Label
font_size = 18
label_message1 = tk.Label(
    window, font=("標楷體", font_size), fg="red", textvariable=main_message1
)
label_message1.place(x=5, y=0 + 10)
main_message1.set("")

label_message2 = tk.Label(
    window, font=("標楷體", font_size), fg="red", textvariable=main_message2
)
label_message2.place(x=5, y=0 + 10 + 40)
main_message2.set("")

font_size = 16
label_index = tk.Label(
    window, font=("標楷體", font_size), fg="red", textvariable=mp3_index
)
label_index.place(x=10, y=0 + 10 + 40 + 40)
mp3_index.set("AAA")


# 加入 Text
text1 = tk.Text(window, width=100, height=30)  # 放入多行輸入框
text1.place(x=x_st + dx * 0, y=y_st + dy * 3 + 20)


def get_mp3_filenames():
    global mp3_filenames
    global total_mp3_files
    global mp3_play_index
    global mp3_foldernames
    global volume_setup
    """
    mp3_foldername = "D:/vcs/astro/_DATA2/_mp3/japanese/昭和の歌--演歌系列1/"

    # 撈出單層mp3檔
    mp3_filenames = glob.glob(mp3_foldername + "*.mp3")
    """

    filename = "tk_ex_MusicPlayer1.txt"
    if not os.path.exists(filename):
        print("檔案不存在")
    else:
        print("檔案存在")

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        print(lines)
        mp3_foldernames = []
        cnt = 0
        for line in lines:
            # print('第', cnt, '行 :', line.strip())
            if cnt == 0:
                mp3_play_index = int(line.strip())
                print("取得 mp3_play_index =", mp3_play_index)
            elif cnt == 1:
                volume_setup = int(line.strip())
                scale1.set(volume_setup)
                print("取得 音量 =", volume_setup)
            else:
                if os.path.isdir(line.strip()):
                    mp3_foldernames.append(line.strip())
                else:
                    print("不是資料夾")
            cnt += 1
        for _ in mp3_foldernames:
            # 撈出單層mp3檔
            mp3_filenames += glob.glob(_ + "*.mp3")
            # print(_)
            # print(mp3_filenames)
    total_mp3_files = len(mp3_filenames)
    print("共有", total_mp3_files, "個mp3檔案")


volume = 0.6  # 起始音量

show_play_status()

mp3_play_index = 0

get_mp3_filenames()
# print(mp3_filenames)

current_playing_mp3_filename = mp3_filenames[mp3_play_index]  # 現正播放檔案

mp3_index.set(str(mp3_play_index + 1) + "/" + str(total_mp3_files))

main_message1.set("{}".format(os.path.basename(current_playing_mp3_filename)))

pygame.mixer.init()  # 初始化 mixer

window.protocol("WM_DELETE_WINDOW", exitmp3)

window.mainloop()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


"""
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(filename)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():#讀取播放狀態, True:正在播放, False:不在播放中
    pygame.time.delay(10)  # msec
    print('.')

print('結束播放')

"""


"""

#要能夠順利讀取各種奇怪的檔名中日文字

print("測試寫檔")
mp3_foldername1 = 'D:/_git/vcs/_1.data/______test_files1/_mp3/'
mp3_foldername2 = 'D:/vcs/astro/_DATA2/_mp3/陳一郎_台語精選集6CD/disc2/'
mp3_foldername3 = 'D:/vcs/astro/_DATA2/_mp3/japanese/昭和の歌--演歌系列9/'
mp3_foldername4 = 'D:/vcs/astro/_DATA2/_________整理_mp3/_mp3_日本_new/(アルバム)演歌 八代亜紀 -[全曲集(Disc1-2)](全24曲)/渕_辙 - [葢轿瘅(Disc1)]'
mp3_foldername5 = 'D:/vcs/astro/_DATA2/_mp3/japanese/美空ひばり(美空云雀).-.[美空ひばり全曲集1].专辑.(MP3)/'

mp3_foldernames = [mp3_foldername1, mp3_foldername2, mp3_foldername3, mp3_foldername4, mp3_foldername5]

print(mp3_foldernames)

filename = "tk_ex_MusicPlayer1.txt"

print("檔名 :", filename)
with open(filename, "w", encoding="utf-8") as f:
    for _ in mp3_foldernames:
        f.write(_)
        f.write("\n")

print("測試讀檔")
filename = "tk_ex_MusicPlayer1.txt"

with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)

"""

import pygame
import time

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("my mp3 player")

filename = "D:/_git/vcs/_1.data/______test_files1/_mp3/02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3"

pygame.mixer.music.load(filename)  # 載入音樂
# 音樂可以是ogg、mp3、wav等格式
# 載入的音樂不會全部放到內容中，而是以流的形式播放的，即在播放的時候才會一點點從文件中讀取

pygame.mixer.music.play()  # 播放載入的音樂
# 該函數立即返回，音樂播放在后臺進行。play方法還可以使用兩個參數
# 如果音樂已經播放，它就會重新啟動
# play(loops=0, start=0.0) -> None
# 參數1:控制音樂播放的次數。播放(5)將使音樂播放一次，然后重復5次，總共是6次。如果循環是-1，那么音樂就會無限重復
# 起始位置的參數控制著歌曲開始播放的地方。起始位置取決于音樂演奏的格式。MP3和OGG以時間為單位(以秒為單位)。MOD音樂是模式的序號。如果不能設置起始位置，通過一個startpos將會拋出一個NotImplementedError


time.sleep(5)

pygame.mixer.music.load(filename)  # 如果一個音樂流已經播放，它就會被停止。這并不是音樂的開始
pygame.mixer.music.play()  # 播放載入的音樂


pygame.mixer.music.set_endevent(pygame.KEYDOWN)  # 當播放停止時，音樂會發送一個事件
# 參數：事件
# 每次音樂結束時，這個事件都會被排隊，而不僅僅是第一次[只要不在播放狀態，會一直發送]。為了防止事件被排隊，請調用這個方法，沒有參數

b = pygame.mixer.music.get_endevent()  # 當播放停止時，獲取set_endevent發送的事件--int
# pygame.KEYDOWN=2
# 如果沒有endevent，函數將返回pygame.NOEVENT

print("xxxxxxx", b)

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        print("aaaaa")
        exit()
        print("bbbbb")
    # print('aaaaaa',event)
    pygame.display.update()
