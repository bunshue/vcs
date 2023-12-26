# ch35_1.py
from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=p9QU72Tzhg8")
print("下載中   ... ")
yt.streams.first().download()
print("下載完成 ... ")




