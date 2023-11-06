from pytube import Playlist
import re

url = "https://www.youtube.com/watch?v=c9IeFunTWbU&list=PLOq648KQvJ234tvAIQAluCTyuhjYmZrHa&index=2&t=0s"
playlist = Playlist(url)
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print(len(playlist.video_urls))
for url in playlist.video_urls:
    print(url)