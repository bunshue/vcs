# ch33_9.py
import matplotlib.pyplot as plt
from scipy.io import wavfile

mywav = 'out33_7.wav'
# 讀取.wav文件
sample_rate, data = wavfile.read(mywav)

# 繪製聲波圖
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.figure(figsize=(10, 4))
plt.plot(data)
plt.title('Good Morning聲波圖')
plt.ylabel('Amplitude')
plt.xlabel('Sample')
plt.show()



