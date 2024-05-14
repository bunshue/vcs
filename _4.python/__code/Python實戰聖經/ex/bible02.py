"""
製作影片字幕

聲音轉字幕

"""

import sys

print("------------------------------------------------------------")  # 60個

"""
#影片轉wav, 但是要跑很久

video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

from moviepy.editor import *
audio1 = AudioFileClip('cccc.mp4')
audio1.write_audiofile('cccc.wav')

print('ok')

sys.exit()
"""
print("------------------------------------------------------------")  # 60個


"""
!pip install pydub
!pip install SpeechRecognition
!pip install opencc-python-reimplemented
"""

from pydub import AudioSegment
from pydub.silence import detect_silence
import speech_recognition as sr
from opencc import OpenCC
import glob
import shutil, os
from time import sleep

def emptydir(dirname):  #清空資料夾
    if os.path.isdir(dirname):  #資料夾存在就刪除
        shutil.rmtree(dirname)
        sleep(2)  #需延遲,否則會出錯
    os.mkdir(dirname)  #建立資料夾

cc = OpenCC('s2twp')
delay = 1300  #聲音延遟時間
fname = 'cccc'
sound = AudioSegment.from_file(fname + ".wav", format="wav")
start_end = detect_silence(sound, delay, sound.dBFS, 1)  #偵測靜音

#每個分割區間的結束位置
mslist = []
for i in range(len(start_end)):
    if i== (len(start_end)-1): data = start_end[i][1]  #最後一筆不必減1秒
    else:  data = start_end[i][1] - delay  #結束位置提前1秒
    mslist.append(data)

#毫秒轉為xx:xx.xxx字串
timelist = []
for sss in mslist: 
    h,ms = divmod(float(sss),3600000)  #時
    m,ms = divmod(float(ms),60000)  #分
    s,ms = divmod(float(ms),1000)  #秒
    ts="%02d:%02d:%02d.%03d" % (h,m,s,ms)
    timelist.append(ts)

#分割聲音檔
emptydir('soundSlice')
for i in range(len(timelist)):  
    if i==0:  start = 0
    else:  start = mslist[i-1]
    end = mslist[i]
    filename = 'soundSlice/slice{:0>3d}.wav'.format(i+1)
    sound[start:end].export(filename, format='wav')

r = sr.Recognizer()  #建立語音辨識物件
file = open(fname + '.srt', 'w', encoding='UTF-8')  #儲存辨識結果
wavfiles = glob.glob('soundSlice/*.wav')
data = ''
count = 1
for i in range(len(wavfiles)):
    try:
        with sr.WavFile("soundSlice/slice{:0>3d}.wav".format(i+1)) as source: 
            audio = r.record(source)
        result = r.recognize_google(audio, language="zh-TW")  #辨識結果
        result = cc.convert(result)  #轉繁體中文
        print('{}. {}'.format(count, result))
        #組合SRT格式
        data += str(count) + '\n'
        if i==0: start = '00:00:00,000'
        else: start = timelist[i-1].replace('.', ',')
        end = timelist[i].replace('.', ',')
        data += (start + ' --> ' + end + '\n')
        data += (result + '\n\n')
        count +=1
    except sr.UnknownValueError:
        print("Google Speech Recognition 無法辨識此語音！")
    except sr.RequestError as e:
        print("無法由 Google Speech Recognition 取得結果; {0}".format(e))
file.write(data)
file.close()


