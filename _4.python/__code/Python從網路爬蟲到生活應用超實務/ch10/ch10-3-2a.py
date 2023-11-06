from pytube import YouTube

yt = YouTube("https://youtube.com/watch?v=XJGiS83eQLk")
caption = yt.captions["en"]
srt = caption.generate_srt_captions()
with open("youtube.srt", "w", encoding="utf-8") as fp:
    fp.write(srt)
print("字幕檔下載完成...")
