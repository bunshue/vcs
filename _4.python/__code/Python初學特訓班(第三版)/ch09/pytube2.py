from pytube import YouTube
import os

yt = YouTube('https://www.youtube.com/watch?v=27ob2G3GUCQ')
print('開始下載：' + yt.title)
pathdir = 'd:\\tem1'  #下載資料夾
if not os.path.isdir(pathdir):  #如果資料夾不存在就建立
    os.mkdir(pathdir)
yt.streams.first().download(pathdir)
print('「' + yt.title + '」下載完成！')
