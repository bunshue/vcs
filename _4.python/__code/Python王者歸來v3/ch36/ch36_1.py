# ch36_1.py
from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=dhzsf5QXmns")
print("下載中   ... ")
yt.streams[0].download()
print("下載完成 ... ")




