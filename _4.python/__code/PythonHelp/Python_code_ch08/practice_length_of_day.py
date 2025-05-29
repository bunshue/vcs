import os
import sys
from statistics import mean
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 切換到包含影像的資料夾路徑
os.chdir('br549_pixelated')
images = sorted(os.listdir())
intensity_samples = []

# 將影像轉換為灰階，將平均亮度值放入 list
for image in images:
    # print(image)
    img = cv.imread(image, cv.IMREAD_GRAYSCALE)    
    intensity = img.mean()
    intensity_samples.append(intensity)

# 建立相對亮度值 list
rel_intensity = intensity_samples[:]
max_intensity = max(rel_intensity)
for i, j in enumerate(rel_intensity):
    rel_intensity[i] = j / max_intensity

# 畫出相對亮度隨時間變化的曲線
plt.plot(rel_intensity, color='red', marker='o', linestyle='solid',
         linewidth=2, markersize=0, label='Relative Intensity')
plt.legend(loc='upper center')
plt.title('Exoplanet BR549 Relative Intensity vs. Time')
plt.ylim(0.8, 1.1)
plt.xticks(np.arange(0, 50, 5))
plt.grid()
plt.show()

# 估計亮度最大峰值以及它在影像上出現的位置
# 找出時間區段 (BR549 一天的長度)
peaks = signal.find_peaks(rel_intensity, height=0.95, distance=5)
print(f"peaks = {peaks}")
print("Period = {}".format(mean(np.diff(peaks[0]))))

