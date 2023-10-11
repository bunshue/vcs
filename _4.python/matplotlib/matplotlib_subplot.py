# plot 集合 subplot的另一種寫法

import sys
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

#          編號                                     圖像大小[英吋]      解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = '不使用subplot畫多圖', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

print("在圖表的指定地方畫圖, 不用subplot")

listx = [1, 2, 3, 4, 5]
listy = [15, 50, 80, 40, 70]

print("1左下開始(0.1, 0.1), w = 0.3, h = 0.3, 左下圖")
plt.axes([0.1, 0.1, 0.3, 0.3])
plt.plot(listx, listy, 'r-s')

print("2左下開始(0.6, 0.1), w = 0.3, h = 0.3, 右下圖")
plt.axes([0.6, 0.1, 0.3, 0.3])
plt.plot(listx, listy, 'g--o')

print("3左下開始(0.1, 0.6), w = 0.3, h = 0.3, 左上圖")
plt.axes([0.1, 0.6, 0.3, 0.3])
plt.plot(listx, listy, 'b-s')

print("4左下開始(0.6, 0.6), w = 0.3, h = 0.3, 右上圖")
plt.axes([0.6, 0.6, 0.3, 0.3])
plt.plot(listx, listy, 'y--o')

plt.show()

print('------------------------------------------------------------')	#60個

#subplot 搭配 gridspec

import matplotlib.gridspec as gridspec

x = np.linspace(-np.pi, np.pi, num=100, endpoint=True)
c,s,t = np.cos(x), np.sin(x), np.tan(x)

# 建立 3x3 的 GridSpec 
gs = gridspec.GridSpec(3, 3)

# 第0列 第0張
plt.subplot(gs[0, 0])
plt.plot(x, c)

# 第0列 第1張
plt.subplot(gs[0, 1])
plt.plot(x, c)

# 第0列 第2張
plt.subplot(gs[0, 2])
plt.plot(x, c)

# 第1列，index 從 0 開始，也可用 [1,0:3] 表示
plt.subplot(gs[1,:])
plt.plot(x, c)

# 第2列 第0張
plt.subplot(gs[2, 0])
plt.plot(x, c)

# 第2列 第1張
plt.subplot(gs[2, 1])
plt.plot(x, c)

# 第2列 第2張
plt.subplot(gs[2, 2])
plt.plot(x, s)

plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/imagedata/2.jpg'

import cv2

# imshow 集合

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'

import matplotlib.image as img
from PIL import Image, ImageEnhance

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示


print('------------------------------------------------------------')	#60個


''' OK
image1 = Image.open(filename)              # 開啟圖片

# 顯示原圖
plt.imshow(image1)                  # 在子圖表中繪製圖片
'''

plt.gcf().set_size_inches(12, 14)   #設定圖框大小

#usage
#ax=plt.subplot(5,5, i+1)
#ax.imshow(images[start_id], cmap='binary')  #顯示黑白圖片

image = cv2.imread(filename)	#讀取本機圖片
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  #灰階
_, image = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY_INV) #轉為反相黑白

#第1張子圖
ax1 = plt.subplot(2, 2, 1)
ax1.imshow(image, cmap = 'binary')  #顯示黑白圖片
title = 'apple'
ax1.set_title(title, fontsize = 12)
#X,Y軸不顯示刻度
ax1.set_xticks([])
ax1.set_yticks([])        

#第2張子圖
ax2 = plt.subplot(2, 2, 2)
ax2.imshow(image, cmap = 'binary')  #顯示黑白圖片
title = 'banana'
ax2.set_title(title, fontsize = 12)
#X,Y軸不顯示刻度
ax2.set_xticks([])
ax2.set_yticks([])        

#第3張子圖
ax3 = plt.subplot(2, 2, 3)
ax3.imshow(image, cmap = 'binary')  #顯示黑白圖片
title = 'cat'
ax3.set_title(title, fontsize = 12)
#X,Y軸不顯示刻度
ax3.set_xticks([])
ax3.set_yticks([])        

#第4張子圖
ax4 = plt.subplot(2, 2, 4)
ax4.imshow(image, cmap = 'binary')  #顯示黑白圖片
title = 'dog'
ax4.set_title(title, fontsize = 12)
#X,Y軸不顯示刻度
ax4.set_xticks([])
ax4.set_yticks([])        

plt.show()

print('------------------------------------------------------------')	#60個

foldername = 'C:/_git/vcs/_1.data/______test_files1/__pic/imagedata/'

import cv2
import glob

def show_images_labels_predictions(images, labels, start_id, num = 10):
    plt.gcf().set_size_inches(12, 14)
    if num > 25:
        num = 25 
    for i in range(0, num):
        ax = plt.subplot(5,5, i + 1)
        ax.imshow(images[start_id], cmap = 'binary')  #顯示黑白圖片
        title = 'label = ' + str(labels[start_id])
        ax.set_title(title, fontsize = 12)
        #X,Y軸不顯示刻度
        ax.set_xticks([])
        ax.set_yticks([])        
        start_id += 1 
    plt.show()
    
files = glob.glob(foldername+'*.jpg')  #建立測試資料
test_feature=[]
test_label=[]
for file in files:
    img = cv2.imread(file)	#讀取本機圖片
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #灰階    
    _, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV) #轉為反相黑白 
    test_feature.append(img)
    label=file[54:55]  #"imagedata\1.jpg"第10個字元1為label
    test_label.append(int(label))
   
show_images_labels_predictions(test_feature, test_label, 0, len(test_feature))

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


