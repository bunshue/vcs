from pytube import Playlist
from pytube import YouTube
import re, os

url = "https://www.youtube.com/watch?v=c9IeFunTWbU&list=PLOq648KQvJ234tvAIQAluCTyuhjYmZrHa&index=2&t=0s"
playlist = Playlist(url)
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
print(len(playlist.video_urls))
  
pathdir = "download"
if not os.path.isdir(pathdir):
    os.mkdir(pathdir)
for url in playlist.video_urls:
    yt = YouTube(url)
    print("正在下載影片:", yt.title)
    video = yt.streams.first()
    video.download(pathdir)
print("影片清單下載完成...")
 
    