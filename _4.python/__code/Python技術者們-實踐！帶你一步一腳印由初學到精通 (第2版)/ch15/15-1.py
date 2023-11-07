from gtts import gTTS

tts = gTTS(text='我是萱萱', lang='zh-tw')
tts.save('我是萱萱的語音檔.mp3')
