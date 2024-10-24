from __future__ import unicode_literals
from pytube import YouTube
import youtube_dl
import os


import sys

import tkinter as tk

print("------------------------------------------------------------")  # 60個


def Downmp4():
    yt = YouTube()
    yt.url = purl.get()
    fpath = ppath.get()
    fpath = fpath.replace("\\", "\\\\")
    fvideo = yt.get("mp4", "360p")
    fvideo.download(fpath)


def Downmp3():
    fpath = ppath.get()
    fpath = fpath.replace("\\", "\\\\")
    os.chdir(fpath)
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([purl.get()])


# main program
# 製作2個視窗
window = tk.Tk()
window.geometry("600x400")
window.title("MP4與MP3下載")

frame1 = tk.Frame(window, width=600)
frame1.pack()

label1 = tk.Label(frame1, text="網址:")
label1.grid(row=0, column=0)
# label1.pack()
label2 = tk.Label(frame1, text="路徑:")
label2.grid(row=1, column=0)
# label2.pack()
# 網址
purl = tk.StringVar()
# 路徑
ppath = tk.StringVar()

entry1 = tk.Entry(frame1, textvariable=purl, width=60)
entry1.grid(row=0, column=1)
# entry1.pack()
entry2 = tk.Entry(frame1, textvariable=ppath, width=60)
ppath.set("d:\music")
entry2.grid(row=1, column=1)
# entry2.pack()

button1 = tk.Button(frame1, text="mp4", command=Downmp4)
# button1.pack()
button1.grid(row=2, column=1)

button2 = tk.Button(frame1, text="mp3", command=Downmp3)
# button2.pack()
button2.grid(row=3, column=1)

# 注意事項
label3 = tk.Label(frame1, text="本程式使用時請注意時間，保護眼睛。")
label3.grid(row=4, column=1)

window.mainloop()

print("------------------------------------------------------------")  # 60個


def Downmp4():
    # yt = YouTube()
    # yt.url = purl.get()
    yt = YouTube("%s" % purl.get())
    fpath = ppath.get()
    fpath = fpath.replace("\\", "\\\\")
    # fvideo = yt.get("mp4", "360p")
    fvideo = yt.streams.filter(file_extension="mp4", res="360p").first()
    fvideo.download(fpath)


def Downmp3():
    fpath = ppath.get()
    fpath = fpath.replace("\\", "\\\\")
    os.chdir(fpath)
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([purl.get()])


# main program
# 製作2個視窗
window = tk.Tk()
window.geometry("600x400")
window.title("MP4與MP3下載")

frame1 = tk.Frame(window, width=600)
frame1.pack()

label1 = tk.Label(frame1, text="網址:")
label1.grid(row=0, column=0)
# label1.pack()
label2 = tk.Label(frame1, text="路徑:")
label2.grid(row=1, column=0)
# label2.pack()
# 網址
purl = tk.StringVar()
# 路徑
ppath = tk.StringVar()

entry1 = tk.Entry(frame1, textvariable=purl, width=60)
entry1.grid(row=0, column=1)
# entry1.pack()
entry2 = tk.Entry(frame1, textvariable=ppath, width=60)
ppath.set("d:\music")
entry2.grid(row=1, column=1)
# entry2.pack()

button1 = tk.Button(frame1, text="mp4", command=Downmp4)
# button1.pack()
button1.grid(row=2, column=1)

button2 = tk.Button(frame1, text="mp3", command=Downmp3)
# button2.pack()
button2.grid(row=3, column=1)

# 注意事項
label3 = tk.Label(frame1, text="本程式使用時請注意時間，保護眼睛。")
label3.grid(row=4, column=1)

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
