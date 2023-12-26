# ch36_3.py
from pytube import YouTube
import os

path = r"d:\myYouTube"
if not os.path.isdir(path):         # 如果不存在則建立此資料夾
    os.mkdir(path)

yt = YouTube("https://www.youtube.com/watch?v=dhzsf5QXmns")
videoViews = yt.views
print(f"影片觀賞次數 : {videoViews}")
videoSeconds = yt.length
print(f"影片長度(秒) : {videoSeconds}")
videoRating = yt.rating
print(f"影片評價     : {videoRating}")
videoTitle = yt.title
print(f"影片標題     : {videoTitle}\n下載中 ... ")
yt.streams[0].download(path)        # 所下載影音檔案儲存在path
print("下載完成 ... ")









