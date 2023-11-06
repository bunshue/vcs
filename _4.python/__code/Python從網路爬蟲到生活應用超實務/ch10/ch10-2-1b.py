from pytube import YouTube
import os

yt = YouTube("https://www.youtube.com/watch?v=i5sgmjOMLJY")
print("正在下載影片:", yt.title)
pathdir = "Arduino"
if not os.path.isdir(pathdir):
    os.mkdir(pathdir)
yt.streams.first().download(pathdir)
print("影片下載完成...")
