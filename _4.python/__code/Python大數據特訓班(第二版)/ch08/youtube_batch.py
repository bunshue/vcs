from pytube import YouTube
import requests
import re

url = "https://www.youtube.com/watch?v=hGRplpwjbr0&list=PL316wRwpvsnHZprsPfXM8yPzyZ41bvuWl"
urlhead = url[:32]
urltail = url[43:]
if '&list' not in url:
    print('這不是播放清單')
else:
    res = requests.get(url)
    vlist = re.findall(r'watch\?v=.*?list', res.text)
    urls = []
    for v in vlist:
        if len(v) < 100:
            tem = urlhead + v[8:19] + urltail
            if tem not in urls:
                urls.append(tem)
            
print('共有 ' + str(len(urls)) + ' 部影片')
print(urls)

pathdir = 'download'  #下載資料夾
print('開始下載：')
n = 1
try:
    for video in urls:
        yt = YouTube(video)
        print(str(n) + '. ' + yt.title)  #顯示標題
        yt.streams.filter(subtype='mp4', res='360p', progressive=True).first().download(pathdir)  #下載mp4,360p影片
        n = n + 1
except:
    pass

print('下載完成！')

