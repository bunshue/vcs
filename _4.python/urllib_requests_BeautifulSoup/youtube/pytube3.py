print('可下載成 .mp4 檔案')

#下載資料夾
foldername = 'C:/_git/vcs/_1.data/______test_files2/youtube_download'

#準備輸出資料夾 若不存在, 則建立
if not os.path.exists(target_dir):
        os.mkdir(target_dir)

from pytube import YouTube

# 超好用的10個Win10小技巧，學會讓你事半功倍！ | 零度解說
url = 'https://www.youtube.com/watch?v=36asE86iGmQ'

yt = YouTube(url)
print("影片名稱：" + yt.title)

#print('所有影片格式')
#print(yt.streams)

length = len(yt.streams)
print("影片格式共有 " + str(length) + ' 種')

print("影片型態為 mp4 且影像及聲音都有的影片：")
print(yt.streams.filter(subtype = 'mp4', progressive = True).all())

print('開始下載 mp4, 360p 的影片：')
yt.streams.filter(subtype = 'mp4', res = '360p', progressive = True).first().download(foldername)  #下載mp4, 360p影片

print("完成")
print('下載影片資料夾 : ', foldername)


