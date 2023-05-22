import requests
from pytube import YouTube
import re

import os

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
        yt = YouTube('https://www.youtube.com' + video)
        print(str(n) + '. ' + yt.title)  #顯示標題
        yt.streams.filter(subtype='mp4', res='360p', progressive=True).first().download(foldername)  #下載mp4,360p影片
        n = n + 1
print('下載完成！')
print('下載影片資料夾 : ', foldername)

'''

