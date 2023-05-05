from pytube import YouTube

#下載資料夾
foldername = 'C:/_git/vcs/_1.data/______test_files2/youtube_download'

# 超好用的10個Win10小技巧，學會讓你事半功倍！ | 零度解說
url = 'https://www.youtube.com/watch?v=36asE86iGmQ'

yt = YouTube(url)
print('開始下載, 僅能下載成 .3gpp 檔案')
print('開始下載：' + yt.title)

yt.streams.first().download(foldername)

print('「' + yt.title + '」下載完成！')

