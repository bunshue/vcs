import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

"""
gTTS：文字轉語音
pip install gTTS
"""

import gtts

print('目前支援的語音種類 :')
print(gtts.lang.tts_langs())

print('gTTS可以透過線上翻譯，將文字轉換為語音，並將語音存檔')
print('將文字分解為多個段落，分別轉換為語音')

txt1 = '王之渙 涼州詞'
txt2 = '黃河遠上白雲間，一片孤城萬仞山。羌笛何須怨楊柳？春風不度玉門關。'

filename = 'tmp_gtts1.mp3'
tts = gtts.gTTS(text=txt2, lang='zh-tw')
tts.save(filename)
print('存檔完成, 檔名 :', filename)

filename = 'tmp_gtts2.mp3'
f = open(filename, "wb")

tts1 = gtts.gTTS(text=txt1, lang='zh-tw')
tts1.write_to_fp(f)

tts2 = gtts.gTTS(text=txt2, lang='zh-tw')
tts2.write_to_fp(f)

print('存檔完成, 檔名 :', filename)

print('------------------------------------------------------------')	#60個

mp3_filename = 'tmp_mp3_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.mp3'

import gtts

text = "Welcome to the United States and have a nice day."
tts = gtts.gTTS(text=text, lang='en')
tts.save(mp3_filename)

print("------------------------------------------------------------")  # 60個

mp3_filename = 'tmp_mp3_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.mp3'

import gtts

text = "黃河遠上白雲間，一片孤城萬仞山。羌笛何須怨楊柳？春風不度玉門關。"

tts = gtts.gTTS(text=text, lang='zh-tw')
tts.save(mp3_filename)


print('------------------------------------------------------------')	#60個

"""
SpeechRecognition：語音轉文字(聲音檔)
pip install SpeechRecognition

"""

print('語音轉文字')

import speech_recognition

r = speech_recognition.Recognizer()
with speech_recognition.WavFile("record1.wav") as source:  #讀取wav檔
    audio = r.record(source)
try:
    word = r.recognize_google(audio, language = "zh-TW")
    print("語音辨識OK, 內容 :")
    print(word)
except:
    print("語音辨識失敗！")

print('------------------------------------------------------------')	#60個

"""
#SpeechRecognition：語音轉文字(麥克風)
!pip install pydub
!pip install ffmpeg
!pip install google.colab

"""

print('------------------------------------------------------------')	#60個

import speech_recognition
from pydub import AudioSegment
from IPython.display import display, Javascript
#from google.colab.output import eval_js
from base64 import b64decode
 
def record_audio(filename):
  js=Javascript("""
    async function recordAudio() {
      const div = document.createElement('div');
      const capture = document.createElement('button');
      capture.textContent = "開始錄音";
      capture.style.background = "orange";
      capture.style.color = "white";
      div.appendChild(capture);
      const stopCapture = document.createElement("button");
      stopCapture.textContent = "停止錄音";
      stopCapture.style.background = "red";
      stopCapture.style.color = "white";
      const audio = document.createElement('audio');
      const recordingVid = document.createElement("audio");
      audio.style.display = 'block';
      const stream = await navigator.mediaDevices.getUserMedia({audio:true});
     
      let recorder = new MediaRecorder(stream);
      document.body.appendChild(div);
      div.appendChild(audio);
      audio.srcObject = stream;
      audio.muted = true;
      await audio.play();
      google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);
      await new Promise((resolve) => {capture.onclick = resolve; });
      recorder.start();
      capture.replaceWith(stopCapture);
      await new Promise((resolve) => stopCapture.onclick = resolve);
      recorder.stop();
      let recData = await new Promise((resolve) => recorder.ondataavailable = resolve);
      let arrBuff = await recData.data.arrayBuffer();
      stream.getAudioTracks()[0].stop();
      div.remove();
 
      let binaryString = "";
      let bytes = new Uint8Array(arrBuff);
      bytes.forEach((byte) => {
        binaryString += String.fromCharCode(byte);
      })
    return btoa(binaryString);
    }
  """)
  try:
    display(js)
    data=eval_js('recordAudio({})')
    binary=b64decode(data)
    with open(filename,"wb") as audio_file:
      audio_file.write(binary)
  except Exception as err:
    print(str(err))
"""
#record.webm 無此檔
record_audio("record.webm")
sound = AudioSegment.from_file("record.webm")
sound.export("record.wav", format ='wav')
r = speech_recognition.Recognizer()
with speech_recognition.WavFile("record.wav") as source:
    audio = r.record(source)
try:
    word = r.recognize_google(audio, language="zh-TW")
    print("語音辨識結果：\n" + word)
except:
    print("語音辨識失敗！")
"""

print('------------------------------------------------------------')	#60個

"""
google_trans_new：文字翻譯
pip install google_trans_new

"""

"""fail
from google_trans_new import google_translator
translator = google_translator()
text="今天天氣很好"
word = translator.translate(text, lang_src='zh-TW', lang_tgt='ja', pronounce=True)
print(word)

from google_trans_new import google_translator
translator = google_translator()
print(translator.translate("今日の天気は良いです"))

lang = translator.detect("今日の天気は良いです")
print(lang)
"""

print('------------------------------------------------------------')	#60個

"""
應用：AI智慧讀報機
!pip install newspaper3k
!pip install gTTS
!pip install google_trans_new
"""

""" fail
import newspaper
from newspaper import Article
from google_trans_new import google_translator
import gtts
import IPython.display as display
import random

paper = newspaper.build('http://cnn.com', language='en')
# paper = newspaper.build('http://www.cnbc.com', language='en')
# paper = newspaper.build('http://www.bbc.co.uk', language='en')
# paper = newspaper.build('http://www.foxnews.com', language='en')
urls = []
for article in paper.articles:
    url = article.url
    if '.html' in url:
        try:  #有時會產生無法擷取的錯誤,故使用try
          article = Article(url)
          article.download()
          article.parse()
          content = article.text
          if len(content)>0:
              urls.append(url)
              if len(urls)>10:
                break
        except: pass
if len(urls)>0:
    r = random.randint(0,len(urls)-1)
    url = urls[r]
    article = Article(url)
    article.download()
    article.parse()
    content = article.text
    if len(content)>5000: content = content[:4999]
    translator = google_translator()
    ret = translator.translate(content, lang_tgt='zh-TW')
    print(ret)
else: 
  ret = '無可用新聞！'
tts = gtts.gTTS(text=ret, lang='zh-tw')
tts.save('news.mp3')
display.Audio("news.mp3", autoplay=True)

"""
print('------------------------------------------------------------')	#60個

#需安裝playsound
#pip install playsound

import newspaper
from newspaper import Article
from google_trans_new import google_translator
import gtts
from playsound import playsound 

# paper = newspaper.build('http://cnn.com', language='en')
paper = newspaper.build('http://www.cnbc.com', language='en')
# paper = newspaper.build('http://www.bbc.co.uk', language='en')
# paper = newspaper.build('http://www.foxnews.com', language='en')

print(type(paper.articles))
print(len(paper.articles))
print(paper.articles)

for article in paper.articles:
    url = article.url
    if '.html' in url:
        print(url)
        """
        try:  #有時會產生無法擷取的錯誤,故使用try
            article = Article(url)
            article.download()
            article.parse()
            content = article.text
            if len(content)>0:
                if len(content)>5000: content = content[:4999]
                translator = google_translator()
                ret = translator.translate(content, lang_tgt='zh-TW')
                print(ret)
                tts = gtts.gTTS(text=ret, lang='zh-tw')
                tts.save('news.mp3')
                playsound('news.mp3')
        except:
            pass
        """

print('------------------------------------------------------------')	#60個

"""
import speech_recognition

r = speech_recognition.Recognizer()        
r.energy_threshold = 4000   #設定聲音辨識的靈敏度
while True:           
    try:
        with speech_recognition.Microphone() as source:  # 打開麥克風
            print("請開始說話:")
            audio = r.listen(source) #等待語音輸入        
            listen_text = r.recognize_google(audio, language="zh-TW")
            print(listen_text + "\n")
            if listen_text=="結束":
                break
    except:
        print("語音無法辨識\n")
"""
print('------------------------------------------------------------')	#60個

""" 播放OK
from pydub import AudioSegment
from pydub.playback import play

print('播放wav檔')
record1 = AudioSegment.from_wav("record1.wav")
play(record1)

print('------------------------------------------------------------')	#60個

import moviepy.editor

filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

print('播放影片檔')

vsr = moviepy.editor.VideoFileClip(filename)
vsr.preview()
"""

print('------------------------------------------------------------')	#60個

#pydub：聲音處理

import IPython.display as display

display.Audio("record1.wav", autoplay=True)

#!pip install pydub
#!pip install pydub==0.24.1

from pydub import AudioSegment

record1 = AudioSegment.from_wav("record1.wav")

print(record1.duration_seconds)

display.Audio("record1.wav", autoplay=True)

#record2 = record1[3000:9000]

#record2 = record1[:6000]

record2 = record1[-5000:]

print(record2.duration_seconds)

record2.export("tmp_record2.wav", format="wav")

display.Audio("tmp_record2.wav", autoplay=True)

#record3 = record1 + 8

record3 = record1 - 5

record3.export("tmp_record3.wav", format="wav")

display.Audio("tmp_record3.wav", autoplay=True)

birth = AudioSegment.from_wav("birth.wav")

print("birth 長度：" + str(birth.duration_seconds))

record4 = birth + record1

print("合併長度：" + str(record4.duration_seconds))

record4.export("tmp_record4.wav", format="wav")

display.Audio("tmp_record4.wav", autoplay=True)

#record5 = record1.fade_in(5000)  #5秒淡入

#record5 = record1.fade_out(3000)  #3秒淡出

record5 = record1.fade_in(5000).fade_out(3000)  #5秒淡入,3秒淡出

record5.export("tmp_record5.wav", format="wav")

display.Audio("tmp_record5.wav", autoplay=True)

record6 = record1.reverse()

record6.export("tmp_record6.wav", format="wav")

display.Audio("tmp_record6.wav", autoplay=True)

print('------------------------------------------------------------')	#60個

#moviepy：影片處理

video_filename = 'C:/_git/big_files/holo1.mp4'

from IPython.display import HTML

from base64 import b64encode

mp4 = open(video_filename,'rb').read()

data_url = "data:video/mp4;base64," + b64encode(mp4).decode()

HTML("""

<video width=400 controls>

      <source src="%s" type="video/mp4">

</video>

""" % data_url)

from moviepy.editor import *

vsr = VideoFileClip(video_filename)

print('長度：' + str(vsr.duration))

print('幀數：' + str(vsr.fps))

print('解析度：' + str(vsr.size))

clip1 = vsr.subclip(10, 20)

print('clip1 長度：' + str(clip1.duration))

clip1.write_videofile('tmp_clip1.mp4')  #有點久

clip2 = vsr.subclip(30, 50)

print('clip2 長度：' + str(clip2.duration))

"""
#clip2.write_videofile('tmp_clip2.mp4')  #做很久

clip1 = VideoFileClip('tmp_clip1.mp4')

clip2 = VideoFileClip('tmp_clip2.mp4')

clip3 = concatenate_videoclips([clip1, clip2])

print('clip3 長度：' + str(clip3.duration))

clip3.write_videofile('tmp_clip3.mp4')

audio1 = AudioFileClip('tmp_holo1.mp4')

audio1.write_audiofile('tmp_holo1.mp3')

clip1_margin = clip1.margin(20)  #加黑邊

clip1_margin.write_videofile('tmp_clip1_margin.mp4')

clip1_mirrorx = clip1.fx(vfx.mirror_x)  #水平翻轉

clip1_mirrorx.write_videofile('tmp_clip1_mirrorx.mp4')

clip1_mirrory = clip1.fx(vfx.mirror_y)  #垂直翻轉

clip1_mirrory.write_videofile('tmp_clip1_mirrory.mp4')

clip1_resize = clip1.resize(0.50)  #改變尺寸

clip1_resize.write_videofile('tmp_clip1_resize.mp4')

clip1_mir_size = clip1.fx(vfx.mirror_x).resize(0.50)  #水平翻轉並改變尺寸

clip1_resize.write_videofile('tmp_clip1_resize.mp4')
"""
print('------------------------------------------------------------')	#60個



"""
圖片內容偵測


#ImageAI：物體偵測

!pip uninstall tensorflow
!pip install tensorflow==2.7
!pip install imageai


!wget -O yolo.h5 https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5
!wget -O resnet50_imagenet_tf.2.0.h5 https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/resnet50_imagenet_tf.2.0.h5

"""

""" fail in sugar
from imageai.Detection import ObjectDetection
detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("yolo.h5")
detector.loadModel()
detections = detector.detectObjectsFromImage(
    input_image="img3.jpg", 
    output_image_path="detect.jpg", 
    minimum_percentage_probability=30)
#print(detections)

for eachObject in detections:
    print("{} ： {} ： {}".format(eachObject["name"], eachObject["percentage_probability"], eachObject["box_points"]))
"""

print('------------------------------------------------------------')	#60個


""" fail in sugar
from imageai.Detection import VideoObjectDetection

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()


#detector.setModelPath("yolo.h5")

detector.loadModel()

detector.detectObjectsFromVideo(
    input_file_path="traffic-mini.mp4",
    output_file_path= "traffic_detected",
    frames_per_second=20, 
    log_progress=True)
"""

print('------------------------------------------------------------')	#60個

"""
安裝 imageai.Prediction

下載 ImageAI whl file
https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.2/imageai-2.0.2-py3-none-any.whl

pip install imageai-2.0.2-py3-none-any.whl
.whl在放在prompt所在地


"""

""" fail in sugar
from imageai.Prediction import ImagePrediction

prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath("resnet50_imagenet_tf.2.0.h5")
prediction.loadModel()
predictions, probabilities = prediction.predictImage("img3.jpg")
# predictions, probabilities = prediction.predictImage("img3.jpg", result_count=10 )
# print(predictions)
# print(probabilities)
for i in range(len(predictions)):
  print('{} ： {}'.format(predictions[i], probabilities[i]))
"""

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

