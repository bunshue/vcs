from pytube import YouTube
from pytube import Playlist

playlist = Playlist("https://www.youtube.com/watch?v=hGRplpwjbr0&list=PL316wRwpvsnHZprsPfXM8yPzyZ41bvuWl")  #建立物件  
videolist = playlist.video_urls  #取得所有影片連結
print('共有 ' + str(len(videolist)) + ' 部影片')

pathdir = 'download'  #下載資料夾
print('開始下載：')
n = 1
for video in videolist:
    yt = YouTube(video)
    print(str(n) + '. ' + yt.title)  #顯示標題
    yt.streams.filter(subtype='mp4', res='360p', progressive=True).first().download(pathdir)  #下載mp4,360p影片
    n = n + 1
print('下載完成！')
