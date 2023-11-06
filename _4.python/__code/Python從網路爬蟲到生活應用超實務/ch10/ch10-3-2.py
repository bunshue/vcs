from pytube import YouTube

yt = YouTube("https://youtube.com/watch?v=XJGiS83eQLk")
captions = yt.captions
print("符合的字幕數:", len(captions))
print(captions)

