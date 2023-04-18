'''
簡易播放一個檔案 簡易即可
1. 純文字檔 單純 cat
2. 播放圖片
3. 播放聲音檔案
4. 播放影片檔案


簡易顯示圖片的各種方法

'''

from PIL import Image

filename = 'C:/______test_files/picture1.jpg'

import cv2
from matplotlib import pyplot as plt
'''
img_bgr = cv2.imread(filename)  # 使用 OpenCV 讀取圖檔
img_rgb = img_bgr[:,:,::-1]     # 將 BGR 圖片轉為 RGB 圖片

# 或是這樣亦可
# img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# 使用 Matplotlib 顯示圖片
plt.imshow(img_rgb)
plt.show()
'''

im = Image.open(filename)
print("%s:" % filename, im.format, "%dx%d" % im.size, im.mode)
print(im.info, im.tile)




'''
filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/poetry.txt'
fp = open(filename)
try:
    while 1:
        line = fp.readline()
        if not line:
            break
        print(line)
finally:
    fp.close()

'''
'''
fp = open(filename)
options.toexclude = fp.readlines()
fp.close()
'''



