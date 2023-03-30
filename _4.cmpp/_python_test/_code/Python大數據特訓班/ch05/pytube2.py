from pytube import YouTube
import os

url = 'https://www.youtube.com/watch?v=36asE86iGmQ'

yt = YouTube(url)
print('開始下載, 僅能下載成 .3gpp 檔案')
print('開始下載：' + yt.title)
pathdir = 'download'  #下載資料夾
if not os.path.isdir(pathdir):  #如果資料夾不存在就建立
    os.mkdir(pathdir)
yt.streams.first().download(pathdir)
print('「' + yt.title + '」下載完成！')
