import sys

print('------------------------------------------------------------')	#60個

url = 'https://www.youtube.com/watch?v=BTMVYUZ2joI'

from pytube import YouTube

yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)
print("正在下載影片:", yt.title)

yt.streams.first().download()
print("影片下載完成...")

print('------------------------------------------------------------')	#60個

from pytube import YouTube
import os

yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)
print("正在下載影片:", yt.title)

pathdir = 'yt_download'
if not os.path.isdir(pathdir):
    os.mkdir(pathdir)
yt.streams.first().download(pathdir)
print("影片下載完成...")

print('------------------------------------------------------------')	#60個

from pytube import YouTube

yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)

print("影片名稱:", yt.title)
print("影片作者:", yt.author)
print("影片長度:", yt.length, "秒")
print("縮圖網址:", yt.thumbnail_url)

print('------------------------------------------------------------')	#60個

from pytube import YouTube

yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)

videos = yt.streams

print("影片格式數:", len(videos))
print("第1個:", videos.first())
print("第1個:", videos[0])
print("最後1個:", videos.last())

print('------------------------------------------------------------')	#60個

from pytube import YouTube

yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)
videos = yt.streams

results = videos.filter(progressive=True)

print("符合的影片數:", len(results))
print("第1個:", results.first())

results = videos.filter(adaptive=True)
print("符合的影片數:", len(results))
print("第1個:", results.first())

print('------------------------------------------------------------')	#60個

from pytube import YouTube

yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)
videos = yt.streams

results = videos.filter(subtype="mp4",res="720p")
print("符合的影片數:", len(results))
print("第1個:", results.first())

print('------------------------------------------------------------')	#60個

from pytube import YouTube

yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)
results = yt.streams.filter(only_audio=True)
length = len(results)
print("符合的影片數:", length)
print(results)
for i in range(length):
    print(results[i])

#下載某一個   
#results[0].download()

print("下載完成...")

print('------------------------------------------------------------')	#60個

from pytube import YouTube
from moviepy.editor import VideoFileClip

filename = "test"
#yt = YouTube("https://www.youtube.com/watch?v=I0Btsq2bdRk&t=34s", use_oauth = True, allow_oauth_cache = True)
yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)
videos = yt.streams
results = videos.filter(subtype="mp4")
print("符合的影片數:", len(results))
print("第1個:", results.first())
#不存檔
#results.first().download(filename = filename)

#存檔有問題
#clip = VideoFileClip(filename + ".mp4")
#clip.audio.write_audiofile(filename + ".mp3")

print('------------------------------------------------------------')	#60個

from pytube import YouTube

yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)
captions = yt.captions
print("符合的字幕數:", len(captions))
print(captions)

print('------------------------------------------------------------')	#60個

""" 字幕下載有問題
from pytube import YouTube

yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)
caption = yt.captions["en"]
srt = caption.generate_srt_captions()
with open("youtube.srt", "w", encoding="utf-8") as fp:
    fp.write(srt)
print("字幕檔下載完成...")
"""

print('------------------------------------------------------------')	#60個

print('播放清單')

# 正直講史 11 片
url_playlist = 'https://www.youtube.com/watch?v=GwP1aUC_NKE&list=PLKtM4AyTKoVd1Ix3H0jP9Z5wYgDpat_tE'

from pytube import Playlist
import re

playlist = Playlist(url_playlist)
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print(len(playlist.video_urls))
for url in playlist.video_urls:
    print(url)

print('------------------------------------------------------------')	#60個

print('播放清單')

from pytube import Playlist
from pytube import YouTube
import re, os

playlist = Playlist(url_playlist)
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
print(len(playlist.video_urls))
  
pathdir = "download"
if not os.path.isdir(pathdir):
    os.mkdir(pathdir)
for url in playlist.video_urls:
    yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)
    print("正在下載影片:", yt.title)
    video = yt.streams.first()
    #不存檔
    #video.download(pathdir)
print("影片清單下載完成...")

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個




