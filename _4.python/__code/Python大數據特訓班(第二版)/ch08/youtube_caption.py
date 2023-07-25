from pytube import YouTube

url = 'https://www.youtube.com/watch?v=TfhlV9_w-nQ'

#yt = YouTube('https://www.youtube.com/watch?v=RIIU6rRj7Eo')
yt = YouTube(url)
print(yt)
print(yt.captions)


'''
caption = yt.captions['en']
srt = caption.generate_srt_captions()
file = open('download/youtube.srt', 'w', encoding='UTF-8')
file.write(srt)
file.close()
print(srt)
'''

