from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=27ob2G3GUCQ', use_oauth = True, allow_oauth_cache = True)
print('開始下載影片，請稍候！')
yt.streams.first().download()
print('影片下載完成')
