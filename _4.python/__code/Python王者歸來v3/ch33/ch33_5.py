# ch33_5.py
from pydub import AudioSegment

mywav = r'C:Windows\Media\notify.wav'
# 讀取.wav文件
wav_audio = AudioSegment.from_wav(mywav)

# 轉換為.mp3
wav_audio.export("notify.mp3", format="mp3")


