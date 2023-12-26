# ch35_3.py
from pytube import YouTube
import os

path = "d:\\myYouTube"
if not os.path.isdir(path):         # 如果不存在則建立此資料夾
    os.mkdir(path)

yt = YouTube("https://www.youtube.com/watch?v=p9QU72Tzhg8")
videoViews = yt.views
print("影片觀賞次數 : ", videoViews)
videoSeconds = yt.length
print("影片長度(秒) : ", videoSeconds)
videoRating = yt.rating
print("影片評價     : ", videoRating)
videoTitle = yt.title
print("影片標題     : ", videoTitle, "下載中   ... ")
yt.streams.first().download(path)   # 所下載影音檔案儲存在path
print("下載完成 ... ")









