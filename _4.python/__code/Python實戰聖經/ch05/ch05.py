"""
gTTS：文字轉語音
pip install gTTS

"""

import sys
import gtts

print('目前支援的語音種類 :')
print(gtts.lang.tts_langs())

txt = 'gTTS可以透過線上翻譯，將文字轉換為語音，並將語音存檔'
tts = gtts.gTTS(text=txt, lang='zh-tw')
filename = 'gtts1.mp3'
tts.save(filename)
print('存檔完成, 檔名 :', filename)


filename = 'gtts2.mp3'
f = open(filename, "wb")
tts1 = gtts.gTTS(text='gTTS可以透過線上翻譯，將文字轉換為語音，並將語音存檔', lang='zh-tw')
tts1.write_to_fp(f)
tts2 = gtts.gTTS(text='將文字分解為多個段落，分別轉換為語音', lang='zh-tw')
tts2.write_to_fp(f)
print('存檔完成, 檔名 :', filename)

print('------------------------------------------------------------')	#60個


"""
SpeechRecognition：語音轉文字(聲音檔)

pip install SpeechRecognition

"""

print('語音轉文字')
import speech_recognition as sr
r = sr.Recognizer()
with sr.WavFile("record1.wav") as source:  #讀取wav檔
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

#google.colab 安裝失敗

import speech_recognition as sr
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

#record.webm 無此檔
record_audio("record.webm")
sound = AudioSegment.from_file("record.webm")
sound.export("record.wav", format ='wav')
r = sr.Recognizer()
with sr.WavFile("record.wav") as source:
    audio = r.record(source)
try:
    word = r.recognize_google(audio, language="zh-TW")
    print("語音辨識結果：\n" + word)
except:
    print("語音辨識失敗！")


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


#需安裝playsound:pip install playsound
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
import speech_recognition as sr

r = sr.Recognizer()        
r.energy_threshold = 4000   #設定聲音辨識的靈敏度
while True:           
    try:
        with sr.Microphone() as source:  # 打開麥克風
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



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



