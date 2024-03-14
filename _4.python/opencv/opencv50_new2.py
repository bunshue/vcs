"""
opencv 集合

"""

import cv2

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

import cv2
import numpy as np

def salt_pepper_noise(image, fraction, salt_vs_pepper):
    img = np.copy(image)
    size = img.size
    num_salt = np.ceil(fraction * size * salt_vs_pepper).astype('int')
    num_pepper = np.ceil(fraction * size * (1 - salt_vs_pepper)).astype('int')
    row, column = img.shape

    # 隨機的座標點
    x = np.random.randint(0, column - 1, num_pepper)
    y = np.random.randint(0, row - 1, num_pepper)
    img[y, x] = 0   # 撒上胡椒

    # 隨機的座標點
    x = np.random.randint(0, column - 1, num_salt)
    y = np.random.randint(0, row - 1, num_salt)
    img[y, x] = 255 # 撒上鹽
    return img

fraction = 0.1        # 雜訊佔圖的比例
salt_vs_pepper = 0.5  # 鹽與胡椒的比例

filename = 'C:/_git/vcs/_4.python/_data/tiger.jpg'
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
noisy = salt_pepper_noise(img, fraction, salt_vs_pepper)

plt.imshow(cv2.cvtColor(noisy, cv2.COLOR_BGR2RGB))
plt.title('胡椒(黑)鹽(白)效果')

plt.show()

#黑點就好比胡椒，白點就像是鹽，這種加上雜訊的方式，就稱為椒鹽雜訊（Salt & Pepper Noise）


print('------------------------------------------------------------')	#60個


import cv2
import matplotlib.pyplot as plt

filename = 'C:/_git/vcs/_4.python/_data/tiger.jpg'

img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
plt.hist(img.ravel(), 256, [0, 256], log = True)
plt.show()

"""
plt.hist(img.ravel(), 256, [0, 256], log = True)
這邊使用到 matplotlib.pyplot 的 hist，它接受一組資料，計算清單中各值出現的次數，上面的範例
透過 NumPy 陣列的 ravel 方法，取得圖片攤平後的資料（只是個 NumPy 視圖）
，hist 的第二個參數指定要切出幾個直條，第三個參數指定要計算的值範圍，log 指定了是否 y 軸是否使用對數結果顯示。
"""
print('------------------------------------------------------------')	#60個

"""
OpenCV 本身也有計算直方圖資料的函式 cv2.calcHist，而且是專門針對圖片進行計算，它的參數有：

    images：一組要分析的圖片。
    channels：要分析的頻道，若是灰階圖片就指定 [0]，若是彩色圖片，可分別使用 [0]、[1]、[2] 指定 BGR 頻道。
    mask：圖片遮罩，預設為 None。
    histSize：各頻道要切分出幾個直條。
    ranges：要計算的像素值範圍，通常都是設為 [0, 256]。

計算出來的資料，可以直接透過 matplotlib.pyplot 的 plot 繪製折線圖，或者是透過 bar 繪製直條圖。

"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

filename = 'C:/_git/vcs/_4.python/_data/tiger.jpg'

img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.bar(np.arange(0, 256), np.log(hist.ravel()))
plt.show()

print('------------------------------------------------------------')	#60個


import cv2
import numpy as np
import matplotlib.pyplot as plt

width = 250
height = 250

image = np.random.choice([0, 255], size = width * height).reshape(height, width).astype(np.uint8)

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
#cv2.imshow('Salt & Pepper Noise', image)

plt.subplot(122)
plt.hist(image.ravel(), 256, [0, 256])

plt.show()

print('------------------------------------------------------------')	#60個






print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

