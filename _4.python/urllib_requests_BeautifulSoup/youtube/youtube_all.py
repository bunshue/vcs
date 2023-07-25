print('----------------------------------------------------------------------')	#70個
print('準備工作')

import re
import os
import time
import threading as th
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
url_playlist = 'https://www.youtube.com/watch?v=GwP1aUC_NKE&list=PLKtM4AyTKoVd1Ix3H0jP9Z5wYgDpat_tE'

print('----------------------------------------------------------------------')	#70個
print('Youtube 測試 1')

yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)

print(type(yt))
print(yt)
print('影片標題：' + yt.title)


#print('所有影片格式')
#print(yt.streams)

length = len(yt.streams)
print("影片格式共有 " + str(length) + ' 種')

print("影片型態為 mp4 且影像及聲音都有的影片：")
print(yt.streams.filter(subtype = 'mp4', progressive = True).all())

print('開始下載 mp4, 360p 的影片：')
#yt.streams.filter(subtype = 'mp4', res = '360p', progressive = True).first().download(foldername)  #下載mp4, 360p影片


#下載mp4影片
#yt.streams.filter(subtype = 'mp4', res = getvideo, progressive = True).first().download(foldername)

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

videos = list(Playlist(url_playlist))
print(videos)
'''


'''

print('----------------------------------------------------------------------')	#70個
print('Youtube 測試 1')


yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)
print('開始下載：' + yt.title)
yt.streams.first().download(foldername)
print('「' + yt.title + '」下載完成！')


print('----------------------------------------------------------------------')	#70個
print('Youtube 測試 1')

yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)
print("影片名稱：" + yt.title)
print("影片格式共有 " + str(len(yt.streams)) + ' 種')
print("影片型態為 mp4 且影像及聲音都有的影片：")
print(yt.streams.filter(subtype = 'mp4', progressive = True))
print('開始下載 mp4, 360p 的影片：')
yt.streams.filter(subtype='mp4', res='360p', progressive=True).first().download(foldername)  #下載mp4,360p影片

print('下載完成！ 下載檔案存於 ' + foldername + ' 資料夾')

print('----------------------------------------------------------------------')	#70個
print('Youtube 測試 1')

playlist = Playlist(url_playlist)  #建立物件  
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

print('----------------------------------------------------------------------')	#70個
print('Youtube 測試 1')

yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)

#print(yt.streams.filter(only_audio=True))
#print(yt.streams.filter(mime_type='audio/webm'))

print('開始下載聲音檔：')
yt.streams.filter(mime_type='audio/mp4').first().download(foldername)  #下載mp4聲音檔
yt.streams.filter(mime_type='audio/webm')[2].download(foldername)  #下載webm聲音檔
#yt.streams.filter(only_audio=True).first().download(foldername)  #下載聲音檔
print('下載完成！')

print('----------------------------------------------------------------------')	#70個
print('Youtube 測試 1')

yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)
#print(yt.captions)
caption = yt.captions['en']
srt = caption.generate_srt_captions()
file = open('download/youtube.srt', 'w', encoding = 'UTF-8')
file.write(srt)
file.close()
print(srt)

'''

yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)

print(yt)
print(yt.captions)

#caption = yt.captions.get_by_language_code('a.en')
caption = yt.captions['en']
srt = caption.generate_srt_captions()
file = open('download/youtube.srt', 'w', encoding='UTF-8')
file.write(srt)
file.close()
print(srt)



#下載資料夾
foldername = 'C:/_git/vcs/_1.data/______test_files2/youtube_download'

#準備輸出資料夾 若不存在, 則建立
if not os.path.exists(foldername):
        os.mkdir(foldername)

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
        print('1111')
        print(temurl)
        videourlList.append(temurl)

'''
print('222')
print(videourlList)
print('開始下載：')
n = 1
for video in videourlList:
    print('333')
    print(video)
    if len(video) > 16:
        print('https://www.youtube.com' + video)
        yt = YouTube('https://www.youtube.com' + video, use_oauth = True, allow_oauth_cache = True)
        print(str(n) + '. ' + yt.title)  #顯示標題
        yt.streams.filter(subtype='mp4', res='360p', progressive=True).first().download(foldername)  #下載mp4,360p影片
        n = n + 1
print('下載完成！')
print('下載影片資料夾 : ', foldername)

'''

playlist = Playlist(url_playlist)  #建立物件  
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


#-------------------------------------------------------------------------------------------------------------

urlhead = url[:32]
urltail = url[43:]
if '&list' not in url_playlist:
    print('這不是播放清單')
else:
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

print('開始下載：')
n = 1
try:
    for video in urls:
        yt = YouTube(video, use_oauth = True, allow_oauth_cache = True)
        print(str(n) + '. ' + yt.title)  #顯示標題
        yt.streams.filter(subtype='mp4', res='360p', progressive=True).first().download(foldername)  #下載mp4,360p影片
        n = n + 1
except:
    pass

print('下載完成！')



print('\n\nYoutube 測試 作業完成\n')







