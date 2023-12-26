# ch33_9_1.py
import matplotlib.pyplot as plt
from scipy.io import wavfile

mywav = 'out33_8.wav'
# 讀取.wav文件
sample_rate, data = wavfile.read(mywav)

# 繪製聲波圖
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.figure(figsize=(10, 4))
plt.plot(data)
plt.title('早安 聲波圖')
plt.ylabel('Amplitude')
plt.xlabel('Sample')
plt.show()



