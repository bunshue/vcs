from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=27ob2G3GUCQ')
#print(yt.streams.filter(only_audio=True))
#print(yt.streams.filter(mime_type='audio/webm'))
pathdir = 'download'  #下載資料夾
print('開始下載聲音檔：')
yt.streams.filter(mime_type='audio/mp4').first().download(pathdir)  #下載mp4聲音檔
yt.streams.filter(mime_type='audio/webm')[2].download(pathdir)  #下載webm聲音檔
#yt.streams.filter(only_audio=True).first().download(pathdir)  #下載聲音檔
print('下載完成！')
