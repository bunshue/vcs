# pytube1.py
from pytube import YouTube
from pytube import Playlist
import threading as th
import time

#下載資料夾
foldername = 'C:/_git/vcs/_1.data/______test_files2/youtube_download'

url = 'https://www.youtube.com/watch?v=V1EmrH7nju8'

yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)

print(type(yt))
print(yt)

print('開始下載影片，請稍候！')
#yt.streams.first().download()  #未指明則存檔在原處
#yt.streams.first().download(foldername)#指明存檔路徑
#stream.download(output_path = foldername)
print('影片下載完成')

# 初始化YouTube下载控件
yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)

# 打印出视频支持下载的音频/视频格式，分辨率，视频编解码方式，音频码率，每条流对应的itag
print(type(yt.streams))
length = len(yt.streams)
print('有', length, '種格式')

for media_type in yt.streams:
    print(media_type)
    print(media_type.type)

'''
可下載1080p影片, 可是沒有聲音
stream  = yt.streams.get_by_itag(137)
stream.download(output_path = foldername)

'''

'''
OK
print('列印播放清單')
plist = 'https://www.youtube.com/watch?v=GwP1aUC_NKE&list=PLKtM4AyTKoVd1Ix3H0jP9Z5wYgDpat_tE'

videos = list(Playlist(plist))
print(videos)
'''


'''

# pytube2.py
from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=27ob2G3GUCQ', use_oauth = True, allow_oauth_cache = True)
print('開始下載：' + yt.title)
yt.streams.first().download(foldername)
print('「' + yt.title + '」下載完成！')


# pytube3.py
from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=27ob2G3GUCQ', use_oauth = True, allow_oauth_cache = True)
print("影片名稱：" + yt.title)
print("影片格式共有 " + str(len(yt.streams)) + ' 種')
print("影片型態為 mp4 且影像及聲音都有的影片：")
print(yt.streams.filter(subtype='mp4', progressive=True))
print('開始下載 mp4, 360p 的影片：')
yt.streams.filter(subtype='mp4', res='360p', progressive=True).first().download(foldername)  #下載mp4,360p影片
print('下載完成！ 下載檔案存於 ' + foldername + ' 資料夾')



# youtube_batch.py
from pytube import YouTube
from pytube import Playlist

playlist = Playlist("https://www.youtube.com/watch?v=hGRplpwjbr0&list=PL316wRwpvsnHZprsPfXM8yPzyZ41bvuWl")  #建立物件  
videolist = playlist.video_urls  #取得所有影片連結
print('共有 ' + str(len(videolist)) + ' 部影片')

print('開始下載：')
n = 1
for video in videolist:
    yt = YouTube(video, use_oauth = True, allow_oauth_cache = True)
    print(str(n) + '. ' + yt.title)  #顯示標題
    yt.streams.filter(subtype='mp4', res='360p', progressive=True).first().download(foldername)  #下載mp4,360p影片
    n = n + 1
print('下載完成！')


# youtube_audio.py
from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=27ob2G3GUCQ', use_oauth = True, allow_oauth_cache = True)

#print(yt.streams.filter(only_audio=True))
#print(yt.streams.filter(mime_type='audio/webm'))

print('開始下載聲音檔：')
yt.streams.filter(mime_type='audio/mp4').first().download(foldername)  #下載mp4聲音檔
yt.streams.filter(mime_type='audio/webm')[2].download(foldername)  #下載webm聲音檔
#yt.streams.filter(only_audio=True).first().download(foldername)  #下載聲音檔
print('下載完成！')


# youtube_caption.py
from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=RIIU6rRj7Eo', use_oauth = True, allow_oauth_cache = True)
#print(yt.captions)
caption = yt.captions['en']
srt = caption.generate_srt_captions()
file = open('download/youtube.srt', 'w', encoding = 'UTF-8')
file.write(srt)
file.close()
print(srt)

'''

print('----------done---------')



