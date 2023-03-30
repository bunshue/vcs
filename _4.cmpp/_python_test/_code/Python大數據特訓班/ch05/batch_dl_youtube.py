import requests
from pytube import YouTube
import re
import os

videourlList = []  #儲存所有影片網址的串列

urltext = '/watch?v=hGRplpwjbr0&list=PL316wRwpvsnHZprsPfXM8yPzyZ41bvuWl'  #黑豹預告片
url = 'https://www.youtube.com' + urltext  #影片網址

pathdir = 'download'  #下載資料夾
if not os.path.isdir(pathdir):  #如果資料夾不存在就建立
    os.mkdir(pathdir)

html = requests.get(url)
res1 = re.findall(r'/watch[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]', html.text)  #取得包含「/watch」的網址內容
for temurl in res1:
    if 'list=' and 'index=' in temurl: #必須包含list=及index=
        if temurl not in videourlList:  #如果串列中不存在就加入串列
            videourlList.append(temurl)

print('開始下載：')
n = 1
for video in videourlList:
    yt = YouTube('https://www.youtube.com' + video)
    print(str(n) + '. ' + yt.title)  #顯示標題
    yt.streams.filter(subtype='mp4', res='360p', progressive=True).first().download(pathdir)  #下載mp4,360p影片
    n = n + 1
print('下載完成！')
