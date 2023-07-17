from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=27ob2G3GUCQ')
print('開始下載：' + yt.title)
pathdir = 'd:\\tem1'  #下載資料夾
yt.streams.first().download(pathdir)
print('「' + yt.title + '」下載完成！')
