# pytube1.py
from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=27ob2G3GUCQ')
print('開始下載影片，請稍候！')
yt.streams.first().download()
print('影片下載完成')



# pytube2.py
from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=27ob2G3GUCQ')
print('開始下載：' + yt.title)
pathdir = 'd:\\tem1'  #下載資料夾
yt.streams.first().download(pathdir)
print('「' + yt.title + '」下載完成！')

# pytube3.py
from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=27ob2G3GUCQ')
print("影片名稱：" + yt.title)
print("影片格式共有 " + str(len(yt.streams)) + ' 種')
print("影片型態為 mp4 且影像及聲音都有的影片：")
print(yt.streams.filter(subtype='mp4', progressive=True))
print('開始下載 mp4, 360p 的影片：')
pathdir = 'd:\\tem'  #下載資料夾
yt.streams.filter(subtype='mp4', res='360p', progressive=True).first().download(pathdir)  #下載mp4,360p影片
print('下載完成！ 下載檔案存於 ' + pathdir + ' 資料夾')



# youtube_batch.py
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

# youtube_audio.py
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

# youtube_caption.py
from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=RIIU6rRj7Eo')
#print(yt.captions)
caption = yt.captions['en']
srt = caption.generate_srt_captions()
file = open('download/youtube.srt', 'w', encoding='UTF-8')
file.write(srt)
file.close()
print(srt)
