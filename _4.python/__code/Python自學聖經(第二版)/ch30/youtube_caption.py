from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=RIIU6rRj7Eo', use_oauth = True, allow_oauth_cache = True)
#print(yt.captions)
caption = yt.captions.get_by_language_code('a.en')
srt = caption.generate_srt_captions()
file = open('download/youtube.srt', 'w', encoding='UTF-8')
file.write(srt)
file.close()
print(srt)
