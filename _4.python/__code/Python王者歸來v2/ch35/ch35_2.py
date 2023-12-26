# ch35_2.py
from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=p9QU72Tzhg8")
videoViews = yt.views
print("影片觀賞次數 : ", videoViews)
videoSeconds = yt.length
print("影片長度(秒) : ", videoSeconds)
videoRating = yt.rating
print("影片評價     : ", videoRating)
videoTitle = yt.title
print("影片標題     : ", videoTitle, "下載中   ... ")
yt.streams.first().download()
print("下載完成 ... ")









