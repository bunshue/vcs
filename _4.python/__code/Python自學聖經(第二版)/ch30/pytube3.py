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
