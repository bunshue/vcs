from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=i5sgmjOMLJY")
print("正在下載影片:", yt.title)
video = yt.streams.first()
video.download()
print("影片下載完成...")
