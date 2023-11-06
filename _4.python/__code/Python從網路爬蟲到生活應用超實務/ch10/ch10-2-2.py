from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=i5sgmjOMLJY")
print("影片名稱:", yt.title)
print("影片作者:", yt.author)
print("影片長度:", yt.length, "秒")
print("縮圖網址:", yt.thumbnail_url)
