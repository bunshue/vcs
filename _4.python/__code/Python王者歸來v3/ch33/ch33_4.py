# ch33_4.py
import matplotlib.pyplot as plt
from scipy.io import wavfile

mywav = r'C:Windows\Media\notify.wav'
# 讀取.wav文件
sample_rate, data = wavfile.read(mywav)

# 繪製聲波圖
plt.figure(figsize=(10, 4))
plt.plot(data)
plt.title('Waveform of nofity.wav file')
plt.ylabel('Amplitude')
plt.xlabel('Sample')
plt.show()



