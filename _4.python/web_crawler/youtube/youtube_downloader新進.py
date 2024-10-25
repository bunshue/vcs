import sys

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("Youtube pytube ST")
print("------------------------------------------------------------")  # 60個

from pytube import YouTube

url = "https://www.youtube.com/watch?v=R93ce4FZGbc"  # baby shark 的音樂
yt = YouTube(url)

# print('影片標題 :', yt.title)  # NG
# print('影片長度 :', yt.length, '秒')  # NG
print('影片作者 :', yt.author)
print('影片作者頻道網址 :', yt.channel_url)
print('影片縮圖網址 :', yt.thumbnail_url)
# print('影片觀看數 :', yt.views)  # NG
print('取得所有語系 :', yt.captions)

print("------------------------------------------------------------")  # 60個

""" NG
from pytube import YouTube

url = "https://www.youtube.com/watch?v=R93ce4FZGbc"
yt = YouTube(url)
print("download...1")
yt.streams.filter().get_highest_resolution().download(filename="baby_shart.mp4")
# 下載最高畫質影片，如果沒有設定 filename，則以原本影片的 title 作為檔名
print("ok!")
"""
print("------------------------------------------------------------")  # 60個

""" NG
from pytube import YouTube

url = "https://www.youtube.com/watch?v=R93ce4FZGbc"
yt = YouTube(url)
print("download...2")
yt.streams.filter().get_by_resolution("360p").download(filename="oxxostudio_360p.mp4")
# 下載 480p 的影片畫質
print("ok!")
"""
print("------------------------------------------------------------")  # 60個

""" NG
from pytube import YouTube

url = "https://www.youtube.com/watch?v=R93ce4FZGbc"
yt = YouTube(url)
print(yt.streams.all())
"""

print("------------------------------------------------------------")  # 60個

""" NG
from pytube import YouTube


def onProgress(stream, chunk, remains):
    total = stream.filesize  # 取得完整尺寸
    percent = (total - remains) / total * 100  # 減去剩餘尺寸 ( 剩餘尺寸會抓取存取的檔案大小 )
    print(f"下載中… {percent:05.2f}", end="\r")  # 顯示進度，\r 表示不換行，在同一行更新


print("download...3")
url = "https://www.youtube.com/watch?v=R93ce4FZGbc"
yt = YouTube(url, on_progress_callback=onProgress)
yt.streams.filter().get_highest_resolution().download(filename="oxxostudio.mp4")
# on_progress_callback 參數等於 onProgress 函式
print()
print("ok!")
"""
print("------------------------------------------------------------")  # 60個

""" fail
from pytube import YouTube

url = "https://www.youtube.com/watch?v=R93ce4FZGbc"
yt = YouTube(url)
print("download...4")
yt.streams.filter().get_audio_only().download(filename="oxxostudio.mp3")
# 儲存為 mp3
print("ok!")
"""
print("------------------------------------------------------------")  # 60個

from pytube import YouTube
from bs4 import BeautifulSoup

url = "https://www.youtube.com/watch?v=R93ce4FZGbc"
yt = YouTube(url)
print('取得所有語系 :', yt.captions)
caption = yt.captions.get_by_language_code("en")  # 取得英文語系
xml = caption.xml_captions  # 將語系轉換成 xml
# print(xml)


def xml2srt(text):
    soup = BeautifulSoup(text)  # 使用 BeautifulSoup 轉換 xml
    ps = soup.findAll("p")  # 取出所有 p tag 內容

    output = ""  # 輸出的內容
    num = 0  # 每段字幕編號
    for i, p in enumerate(ps):
        try:
            a = p["a"]  # 如果是自動字幕，濾掉有 a 屬性的 p tag
        except:
            try:
                num = num + 1  # 每段字幕編號加 1
                text = p.text  # 取出每段文字
                t = int(p["t"])  # 開始時間
                d = int(p["d"])  # 持續時間

                h, tm = divmod(t, (60 * 60 * 1000))  # 轉換取得小時、剩下的毫秒數
                m, ts = divmod(tm, (60 * 1000))  # 轉換取得分鐘、剩下的毫秒數
                s, ms = divmod(ts, 1000)  # 轉換取得秒數、毫秒

                t2 = t + d  # 根據持續時間，計算結束時間
                if t2 > int(ps[i + 1]["t"]):
                    t2 = int(ps[i + 1]["t"])  # 如果時間算出來比下一段長，採用下一段的時間
                h2, tm = divmod(t2, (60 * 60 * 1000))  # 轉換取得小時、剩下的毫秒數
                m2, ts = divmod(tm, (60 * 1000))  # 轉換取得分鐘、剩下的毫秒數
                s2, ms2 = divmod(ts, 1000)  # 轉換取得秒數、毫秒

                output = output + str(num) + "\n"  # 產生輸出的檔案，\n 表示換行
                output = (
                    output
                    + f"{h:02d}:{m:02d}:{s:02d},{ms:03d} --> {h2:02d}:{m2:02d}:{s2:02d},{ms2:03d}"
                    + "\n"
                )
                output = output + text + "\n"
                output = output + "\n"
            except:
                pass

    return output


# print(xml2srt(xml))
with open("tmp_oxxostudio.srt", "w") as f1:
    f1.write(xml2srt(xml))  # 儲存為 srt

print("下載字幕 ok!")

print("------------------------------------------------------------")  # 60個

from pytube import Playlist, YouTube

url = "https://www.youtube.com/watch?v=mOPRaLPh-YU&list=PL9ACDjBMkp9wViVmgpYweGkNqh62pHspF"

playlist = Playlist(url)  # 讀取影片清單

#print(playlist.video_urls)  # 印出清單結果
for _ in playlist.video_urls:
    print(_)

"""
['https://www.youtube.com/watch?v=mOPRaLPh-YU',
 'https://www.youtube.com/watch?v=wARhTJH1fJI',
 'https://www.youtube.com/watch?v=WLjePGUCRqc']
"""

""" fail
print("download...5")
for i in playlist.video_urls:
    print(i)
    yt = YouTube(i)  # 讀取影片
    yt.streams.filter().get_highest_resolution().download()  # 下載為最高畫質影片
print("ok!")
"""

print("------------------------------------------------------------")  # 60個

""" fail
from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=52B8s2zrdeE")
stream = yt.streams.filter(file_extension='mp4', res='360p').first()
stream.download("c:\\dddddddddd")
"""

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("Youtube pytube SP")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

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
print("作業完成")
print("------------------------------------------------------------")  # 60個

