# ch36_4.py
from pytube import YouTube
import os

path = r"d:\myYouTube"
if not os.path.isdir(path):             # 如果不存在則建立此資料夾
    os.mkdir(path)

links = ["https://www.youtube.com/watch?v=dhzsf5QXmns",
         "https://www.youtube.com/watch?v=z8eE3CGyQiE"]
for video in links:
    yt = YouTube(video)
    videoViews = yt.views
    print(f"影片觀賞次數 : {videoViews}")
    videoSeconds = yt.length
    print(f"影片長度(秒) : {videoSeconds}")
    videoRating = yt.rating
    print(f"影片評價     : {videoRating}")
    videoTitle = yt.title
    print(f"影片標題     : {videoTitle}\n下載中 ... ")
    print(f"影片格式數量 : {len(yt.streams)}")
    yt.streams[0].download(path)        # 所下載影音檔案儲存在path
    print("下載完成 ... ")









