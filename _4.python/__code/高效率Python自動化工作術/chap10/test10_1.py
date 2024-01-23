from mutagen.mp3 import MP3
import datetime

infile = "testmusic1.mp3"      #要載入的檔案名稱

audio = MP3(infile)             #載入檔案
sec = audio.info.length         #播放時間（秒）
timestr = str(datetime.timedelta(seconds=sec))  #轉換成時分秒格式
print("播放時間=",timestr)
