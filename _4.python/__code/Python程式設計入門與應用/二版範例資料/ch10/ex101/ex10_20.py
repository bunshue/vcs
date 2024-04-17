from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=BRcudpJzy1I")
stream = yt.streams.filter(file_extension='mp4', res='360p').first()
stream.download("d:\\music")