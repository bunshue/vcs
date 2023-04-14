from pytube import YouTube

url = 'https://www.youtube.com/watch?v=36asE86iGmQ'
yt = YouTube(url)

print('開始下載影片，請稍候！, 僅能下載成 .3gpp 檔案')
yt.streams.first().download()
print('影片下載完成')
