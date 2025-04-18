"""
使用 pytube 做 YouTube下載

"""

print('------------------------------------------------------------')	#60個
print('準備工作')

import re
import os
import sys
import requests
from pytube import YouTube
from pytube import Playlist

#下載資料夾
foldername = 'C:/_git/vcs/_1.data/______test_files2/youtube_download'

#準備輸出資料夾 若不存在, 則建立
if not os.path.exists(foldername):
    os.mkdir(foldername)

# 超好用的10個Win10小技巧，學會讓你事半功倍！ | 零度解說
url = 'https://www.youtube.com/watch?v=36asE86iGmQ'
url = 'https://www.youtube.com/watch?v=BTMVYUZ2joI'
# 正直講史 11 片
url_playlist = 'https://www.youtube.com/watch?v=GwP1aUC_NKE&list=PLKtM4AyTKoVd1Ix3H0jP9Z5wYgDpat_tE'

# 初始化YouTube下載控件
yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)

print('------------------------------------------------------------')	#60個

print('Youtube 測試 1 影片資訊')

print("影片名稱:", yt.title)
print("影片作者:", yt.author)
print("影片長度:", yt.length, "秒")
print("縮圖網址:", yt.thumbnail_url)

videos = yt.streams

print("影片格式數:", len(videos))
print("第1個:", videos.first())
print("第1個:", videos[0])
print("最後1個:", videos.last())

length = len(yt.streams)
print("影片格式共有 " + str(length) + ' 種')
#print('所有影片格式')
#print(yt.streams)

print('所有影片格式')
for i in  range(length):
    print(yt.streams[i])
#print(yt.streams)

print('只有聲音 或 只有影像 者')
length = len(yt.streams.filter(adaptive = True))
print("共有 " + str(length) + ' 種')
cccc = yt.streams.filter(adaptive = True)
for i in  range(length):
    print(cccc[i])

print('聲音 和 影像 皆有 者')
length = len(yt.streams.filter(progressive = True))
print("共有 " + str(length) + ' 種')
cccc = yt.streams.filter(progressive = True)
for i in  range(length):
    print(cccc[i])

print("影片名稱：" + yt.title)

#print(yt.captions)
length = len(yt.captions)
print('字幕個數 : ', length)
if length > 0:
    for cc in yt.captions:
        print(type(cc))
        print(cc)
        print(cc.url)
        print(cc.name)
        print(cc.code)

# 打印出視頻支持下載的音頻/視頻格式，分辨率，視頻編解碼方式，音頻碼率，每條流對應的itag
print(type(yt.streams))
length = len(yt.streams)
print('有', length, '種格式')

"""
for media_type in yt.streams:
    print(media_type)
    print(media_type.type)
"""

print("影片名稱：" + yt.title)
print("影片格式共有 " + str(len(yt.streams)) + ' 種')
print("影片型態為 mp4 且影像及聲音都有的影片：")
print(yt.streams.filter(subtype = 'mp4', progressive = True)) #mp4 + True

print('------------------------------------------------------------')	#60個
print('Youtube 測試 2 下載 影片 / 聲音')

print('開始下載 mp4, 360p 的影片：')
#下載mp4影片 360p
#yt.streams.filter(subtype = 'mp4', res = '360p', progressive = True).first().download(foldername)

#yt.streams.first().download()                          #未指明則存檔在原處
#yt.streams.first().download(foldername)                #指明存檔路徑
#yt.streams.first().download(output_path = foldername)  #指明存檔路徑

#可下載720p影片, 有聲音
#stream = yt.streams.get_by_itag(22)
#stream.download(output_path = foldername)

#可下載1080p影片, 可是沒有聲音
#stream = yt.streams.get_by_itag(137)
#stream.download(output_path = foldername)

#print(yt.streams.filter(only_audio=True))
#print(yt.streams.filter(mime_type='audio/webm'))

print('開始下載聲音檔：')
#yt.streams.filter(mime_type='audio/mp4').first().download(foldername)  #下載mp4聲音檔
#yt.streams.filter(mime_type='audio/webm')[2].download(foldername)  #下載webm聲音檔
#yt.streams.filter(only_audio=True).first().download(foldername)  #下載聲音檔

print('取得檔案大小')
video = yt.streams.filter(progressive=True, file_extension='mp4').first()
print('FileSize : ' + str(round(video.filesize / (1024 * 1024))) + 'MB')

print('下載完成')


# Stream(video).on_progress()
        
print('測試下載進度條')
#这计算转换文件大小和剩余字节数的百分比
def percent(tem, total):
        perc = (float(tem) / float(total)) * float(100)
        return perc

#进度功能
def progress_function(stream, chunk,file_handle, bytes_remaining):
    size = stream.filesize
    p = 0
    while p <= 100:
        progress = p
        print(str(p)+'%')
        p = percent(bytes_remaining, size)

"""
from pytube import YouTube
from pytube.cli import on_progress #this module contains the built in progress bar.
# 初始化YouTube下載控件
#yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)
yt = YouTube(url, use_oauth = True, allow_oauth_cache = True, on_progress_callback = progress_function)
video = yt.streams.first()
video.download()

print('OK')
"""

print('------------------------------------------------------------')	#60個
print('Youtube 測試 3 下載字幕 TBD')

# 初始化YouTube下載控件
#yt = YouTube('https://www.youtube.com/watch?v=RIIU6rRj7Eo', use_oauth = True, allow_oauth_cache = True)

print("影片名稱：" + yt.title)

length = len(yt.captions)
print('字幕個數 : ', length)
if length > 0:
    for cc in yt.captions:
        print(cc)

print(type(yt.captions))
print(yt.captions)

"""
字幕個數 :  2
<Caption lang="Chinese (Simplified)" code="zh-Hans">
<Caption lang="Chinese (Traditional)" code="zh-Hant">
"""

#caption = yt.captions.get_by_language_code('zh-Hant') old
caption = yt.captions['zh-Hant']

#print(caption.xml_captions)

"""
'<?xml version="1.0" encoding="utf-8" ?><transcript><text start="10.2" dur="0.94">K-pop!</text>...'
"""

#srt = caption.generate_srt_captions() old
srt = caption.xml_captions
file = open(title + '.srt', 'w', encoding = 'UTF-8')
file.write(srt)
file.close()


print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個
print('Youtube 測試 1 播放清單 影片資訊')

print('從播放清單取得所有影片連結')

if '&list' not in url_playlist:
    print('這 不是 播放清單')
else:
    print('這 是 播放清單')

print('取得清單內的影片資料1')
playlist = Playlist(url_playlist)  #建立物件  
videolist = playlist.video_urls  #取得所有影片連結
print('共有 ' + str(len(videolist)) + ' 部影片')

for video in videolist:
    print('網址', video)
    # 初始化YouTube下載控件
    yt = YouTube(video, use_oauth = True, allow_oauth_cache = True)
    print('標題', yt.title)  #顯示標題

playlist = Playlist(url_playlist)  #建立物件
videos = list(playlist)
print(videos)

playlist = Playlist(url_playlist)  #建立物件
videolist = playlist.video_urls  #取得所有影片連結
print('共有 ' + str(len(videolist)) + ' 部影片')

print('取得清單內的影片資料2')
urlhead = url[:32]
urltail = url[43:]
res = requests.get(url_playlist)
vlist = re.findall(r'watch\?v=.*?list', res.text)
urls = []
for v in vlist:
    if len(v) < 100:
        tem = urlhead + v[8:19] + urltail
        if tem not in urls:
            urls.append(tem)
            
print('共有 ' + str(len(urls)) + ' 部影片')
print(urls)

print('------------------------------------------------------------')	#60個
print('Youtube 測試 2 播放清單 下載影片')

playlist = Playlist(url_playlist)  #建立物件  
videolist = playlist.video_urls  #取得所有影片連結
print('共有 ' + str(len(videolist)) + ' 部影片')

print('開始下載：')
n = 1
for video in videolist:
    # 初始化YouTube下載控件
    yt = YouTube(video, use_oauth = True, allow_oauth_cache = True)
    print(str(n) + '. ' + yt.title)  #顯示標題
    #下載mp4影片 360p
    #yt.streams.filter(subtype = 'mp4', res = '360p', progressive = True).first().download(foldername)
    n = n + 1

print('下載完成')

print('------------------------------------------------------------')	#60個
print('Youtube 測試 5 播放清單 下載影片')

videourlList = []  #儲存所有影片網址的串列

urltext = '/watch?v=36asE86iGmQ'    # 超好用的10個Win10小技巧，學會讓你事半功倍！ | 零度解說
url = 'https://www.youtube.com' + urltext  #影片網址
print(url)

html = requests.get(url)
#print(html.text)

res1 = re.findall(r'/watch[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]', html.text)  #取得包含「/watch」的網址內容
print('連線到某youtube影片, 抓取此頁面的所有影片連結')
print('共有', len(res1), '個連結')
print(res1)

for temurl in res1:
    print(temurl)
    if temurl not in videourlList:  #如果串列中不存在就加入串列
        print(temurl)
        videourlList.append(temurl)

print('開始下載：')
n = 1

for video in videourlList:
    print('網址', video)
    # 初始化YouTube下載控件
    #yt = YouTube(video, use_oauth = True, allow_oauth_cache = True)
    #yt = YouTube('https://www.youtube.com' + video, use_oauth = True, allow_oauth_cache = True)
    #print('標題', yt.title)  #顯示標題
    
    """
    #有些有問題
    if len(video) > 16 and len(video) < 30::
        print('https://www.youtube.com' + video)
        # 初始化YouTube下載控件
        yt = YouTube('https://www.youtube.com' + video, use_oauth = True, allow_oauth_cache = True)
        print(str(n) + '. ' + yt.title)  #顯示標題
        #下載mp4影片 360p
        #yt.streams.filter(subtype = 'mp4', res = '360p', progressive = True).first().download(foldername)
        n = n + 1
    """

print('下載完成')

print('\n\nYoutube 測試 作業完成\n')


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('Pytube：下載Youtube影片')

# pip install pytube

from pytube import YouTube

url = 'https://www.youtube.com/watch?v=36asE86iGmQ'

yt = YouTube(url)
print(yt.title)

print(yt.streams)

yt.streams.first().download("youtube")

print(len(yt.streams.filter(adaptive=True)))

print(yt.streams.filter(progressive=True))

yt.streams.filter(subtype='mp4', res='360p', progressive=True).first().download("youtube")

yt.streams.filter(subtype='mp4')[1].download("youtube")


print('------------------------------------------------------------')	#60個

print('應用：批次下載Youtube影片')


from pytube import Playlist

url_playlist = 'https://www.youtube.com/watch?v=GwP1aUC_NKE&list=PLKtM4AyTKoVd1Ix3H0jP9Z5wYgDpat_tE'

playlist = Playlist(url_playlist)
print("共有 " + str(len(playlist.video_urls)) + " 部影片")
pathdir = "download"  #下載資料夾
print("開始下載：")
try:
  for index, video in enumerate(playlist.videos):
    print(str(index+1) + '. ' + video.title)  #顯示標題
    #video.streams.first().download(pathdir)
except:
  pass
print("下載完成！")

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個
print('新進測試')


import sys

print('------------------------------------------------------------')	#60個

url = 'https://www.youtube.com/watch?v=BTMVYUZ2joI'

from pytube import YouTube

yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)
print("正在下載影片:", yt.title)

yt.streams.first().download()
print("影片下載完成...")

print('------------------------------------------------------------')	#60個

from pytube import YouTube
import os

yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)
print("正在下載影片:", yt.title)

pathdir = 'yt_download'
if not os.path.isdir(pathdir):
    os.mkdir(pathdir)
yt.streams.first().download(pathdir)
print("影片下載完成...")

print('------------------------------------------------------------')	#60個

from pytube import YouTube

yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)

videos = yt.streams
results = videos.filter(progressive=True)

print("符合的影片數:", len(results))
print("第1個:", results.first())

results = videos.filter(adaptive=True)
print("符合的影片數:", len(results))
print("第1個:", results.first())

print('------------------------------------------------------------')	#60個

from pytube import YouTube

yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)
videos = yt.streams

results = videos.filter(subtype="mp4",res="720p")
print("符合的影片數:", len(results))
print("第1個:", results.first())

print('------------------------------------------------------------')	#60個

from pytube import YouTube

yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)
results = yt.streams.filter(only_audio=True)
length = len(results)
print("符合的影片數:", length)
print(results)
for i in range(length):
    print(results[i])

#下載某一個   
#results[0].download()

print("下載完成...")

print('------------------------------------------------------------')	#60個

from pytube import YouTube
from moviepy.editor import VideoFileClip

filename = "test"
#yt = YouTube("https://www.youtube.com/watch?v=I0Btsq2bdRk&t=34s", use_oauth = True, allow_oauth_cache = True)
yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)
videos = yt.streams
results = videos.filter(subtype="mp4")
print("符合的影片數:", len(results))
print("第1個:", results.first())
#不存檔
#results.first().download(filename = filename)

#存檔有問題
#clip = VideoFileClip(filename + ".mp4")
#clip.audio.write_audiofile(filename + ".mp3")

print('------------------------------------------------------------')	#60個

from pytube import YouTube

yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)
captions = yt.captions
print("符合的字幕數:", len(captions))
print(captions)

print('------------------------------------------------------------')	#60個

""" 字幕下載有問題
from pytube import YouTube

yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)
caption = yt.captions["en"]
srt = caption.generate_srt_captions()
with open("youtube.srt", "w", encoding="utf-8") as fp:
    fp.write(srt)
print("字幕檔下載完成...")
"""

print('------------------------------------------------------------')	#60個

print('播放清單')

# 正直講史 11 片
url_playlist = 'https://www.youtube.com/watch?v=GwP1aUC_NKE&list=PLKtM4AyTKoVd1Ix3H0jP9Z5wYgDpat_tE'

from pytube import Playlist
import re

playlist = Playlist(url_playlist)
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print(len(playlist.video_urls))
for url in playlist.video_urls:
    print(url)

print('------------------------------------------------------------')	#60個

print('播放清單')

from pytube import Playlist
from pytube import YouTube
import re, os

playlist = Playlist(url_playlist)
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
print(len(playlist.video_urls))
  
pathdir = "download"
if not os.path.isdir(pathdir):
    os.mkdir(pathdir)
for url in playlist.video_urls:
    yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)
    print("正在下載影片:", yt.title)
    video = yt.streams.first()
    #不存檔
    #video.download(pathdir)
print("影片清單下載完成...")

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個
