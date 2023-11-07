import os
from gtts import gTTS

if not os.path.isfile('hello.mp3'):
    tts = gTTS(text = '不重要的語音檔', lang = 'zh-tw')
    tts.save('hello.mp3')
    print('已產生不重要的語音檔 hello.mp3')