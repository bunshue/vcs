from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=i5sgmjOMLJY")
videos = yt.streams
print("影片格式數:", len(videos))
print("第1個:", videos.first())
print("第1個:", videos[0])
print("最後1個:", videos.last())
