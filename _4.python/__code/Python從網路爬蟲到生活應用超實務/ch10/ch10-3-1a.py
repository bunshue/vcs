from pytube import YouTube
from moviepy.editor import VideoFileClip

filename = "test"
yt = YouTube("https://www.youtube.com/watch?v=I0Btsq2bdRk&t=34s")
videos = yt.streams
results = videos.filter(subtype="mp4")
print("符合的影片數:", len(results))
print("第1個:", results.first())
results.first().download(filename=filename)

clip = VideoFileClip(filename + ".mp4")
clip.audio.write_audiofile(filename + ".mp3")

