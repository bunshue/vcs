from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=i5sgmjOMLJY")
videos = yt.streams

results = videos.filter(progressive=True)
print("符合的影片數:", len(results))
print("第1個:", results.first())

