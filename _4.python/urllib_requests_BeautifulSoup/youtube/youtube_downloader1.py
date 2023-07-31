'''
使用 pytube 做 YouTube下載

'''

print('----------------------------------------------------------------------')	#70個
print('準備工作')

import re
import os
import sys
import requests
import threading as th
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

print('----------------------------------------------------------------------')	#70個
print('Youtube 測試 1 影片資訊')

#print('所有影片格式')
#print(yt.streams)
length = len(yt.streams)
print("影片格式共有 " + str(length) + ' 種')

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

for media_type in yt.streams:
    print(media_type)
    print(media_type.type)

print("影片名稱：" + yt.title)
print("影片格式共有 " + str(len(yt.streams)) + ' 種')
print("影片型態為 mp4 且影像及聲音都有的影片：")
print(yt.streams.filter(subtype = 'mp4', progressive = True)) #mp4 + True

print('----------------------------------------------------------------------')	#70個
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

'''
print('開始下載聲音檔：')
yt.streams.filter(mime_type='audio/mp4').first().download(foldername)  #下載mp4聲音檔
yt.streams.filter(mime_type='audio/webm')[2].download(foldername)  #下載webm聲音檔
#yt.streams.filter(only_audio=True).first().download(foldername)  #下載聲音檔
'''

print('下載完成')

print('----------------------------------------------------------------------')	#70個
print('Youtube 測試 3 下載字幕 TBD')

# 初始化YouTube下載控件
#yt = YouTube('https://www.youtube.com/watch?v=RIIU6rRj7Eo', use_oauth = True, allow_oauth_cache = True)

print("影片名稱：" + yt.title)

length = len(yt.captions)
print('字幕個數 : ', length)
if length > 0:
    for cc in yt.captions:
        print(cc)

# 目前無法下載字幕

'''
#caption = yt.captions.get_by_language_code('a.en')
caption = yt.captions['Chinese (Traditional)']
srt = caption.generate_srt_captions()
file = open('youtube.srt', 'w', encoding = 'UTF-8')
file.write(srt)
file.close()
print(srt)
'''

'''
#caption = yt.captions.get_by_language_code('a.en')
caption = yt.captions['zh-Hans']
srt = caption.generate_srt_captions()
file = open('download/youtube.srt', 'w', encoding = 'UTF-8')
file.write(srt)
file.close()
print(srt)
'''

'''
#{'a.en': <Caption lang="English (auto-generated)" code="a.en">}

caption = yt.captions['en']
srt = caption.generate_srt_captions()
file = open('youtube.srt', 'w', encoding='UTF-8')
file.write(srt)
file.close()
print(srt)
'''

'''
<Caption lang="Chinese (Simplified)" code="zh-Hans">
<Caption lang="Chinese (Traditional)" code="zh-Hant">
'''

print('----------------------------------------------------------------------')	#70個
print('----------------------------------------------------------------------')	#70個
print('----------------------------------------------------------------------')	#70個
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

print('----------------------------------------------------------------------')	#70個
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

print('----------------------------------------------------------------------')	#70個
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
    
    '''
    #有些有問題
    if len(video) > 16 and len(video) < 30::
        print('https://www.youtube.com' + video)
        # 初始化YouTube下載控件
        yt = YouTube('https://www.youtube.com' + video, use_oauth = True, allow_oauth_cache = True)
        print(str(n) + '. ' + yt.title)  #顯示標題
        #下載mp4影片 360p
        #yt.streams.filter(subtype = 'mp4', res = '360p', progressive = True).first().download(foldername)
        n = n + 1
    '''

print('下載完成')

print('\n\nYoutube 測試 作業完成\n')
