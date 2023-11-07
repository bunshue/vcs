from pygame import mixer		# 匯入 mixer 物件
from gtts import gTTS

tts = gTTS(text='我是萱萱', lang='zh-tw')
tts.save('我是萱萱的語音檔.mp3')

mixer.init()					# 初始化
mixer.music.load('我是萱萱的語音檔.mp3')  # 讀取聲音檔
mixer.music.play()		# 播放 聲音檔
