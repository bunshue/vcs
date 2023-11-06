from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=9bZkp7q19f0")
results = yt.streams.filter(only_audio=True)
print("符合的影片數:", len(results))
print(results)
results[0].download()
print("下載完成...")
