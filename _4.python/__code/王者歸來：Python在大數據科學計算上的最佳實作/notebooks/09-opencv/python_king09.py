print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個
'''
import numpy as np
import pylab as pl
import cv2

#OpenCV-圖形處理和電腦視覺

filename = "lena.jpg"
img = cv2.imread( filename ) #❶
print(type(img), img.shape, img.dtype)
cv2.namedWindow("demo1")     #❷
cv2.imshow("demo1", img)     #❸
cv2.waitKey(0)  #❹;


print("------------------------------------------------------------")  # 60個


#%hidecell
filename = "lena.jpg"
img = cv2.imread( filename )
cv2.namedWindow("demo1")
cv2.imshow("demo1", img)
cv2.waitKey(0)

print("------------------------------------------------------------")  # 60個

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img_gray.shape)

print("------------------------------------------------------------")  # 60個

#圖形型態

#%hide
from matplotlib import cm
from itertools import product

def func(x, y):
    return (x+y)*np.exp(-5.0*(x**2 + y**2))

y, x = np.mgrid[-1:1:100j, -1:1:100j]
z = func(x, y)
zabs = np.abs(z)
alpha = cm.ScalarMappable(cmap="gray").to_rgba(zabs)[:, :, 0].copy()
z1 = cm.ScalarMappable(cmap="gray").to_rgba(z)[:, :, 0].copy()
z4 = cm.ScalarMappable(cmap="jet").to_rgba(z)
z3 = z4[:, :, 2::-1].copy()
z4[:, :, -1] = alpha
z4[:, :, :3] = z3

for dtype, img in product(["uint8", "uint16"], [z1, z3, z4]):
    nchannel = 1 if img.ndim == 2 else img.shape[2]
    img = (img * np.iinfo(dtype).max).astype(dtype)
    fn = "{}_{}.png".format(dtype, nchannel)
    cv2.imwrite(fn, img)

#%hide
from glob import glob
from IPython import display

files = glob("uint*.png")
flags = ["ANYCOLOR",
"ANYDEPTH",
"COLOR",
"GRAYSCALE",
"UNCHANGED"]

def f(fn, flag):
    _flag = getattr(cv2, "IMREAD_" + flag)
    img = cv2.imread(fn, _flag)
    nchannel = 1 if img.ndim == 2 else img.shape[2]
    return "{}, {}ch".format(img.dtype, nchannel)


#圖形輸出

img = cv2.imread("lena.jpg")
for quality in [90, 60, 30]:
    cv2.imwrite("lena_q{:02d}.jpg".format(quality), img, 
                [cv2.IMWRITE_JPEG_QUALITY, quality])

from matplotlib.cm import ScalarMappable
from IPython.display import Image

def func(x, y, a):
    return (x*x - y*y) * np.sin((x + y) / a) / (x*x + y*y)

def make_image(x, y, a, dtype="uint8"):
    z = func(x, y, a) #❶
    img_rgba = ScalarMappable(cmap="jet").to_rgba(z)
    img = (img_rgba[:, :, 2::-1] * np.iinfo(dtype).max).astype(dtype) #❷
    return img

y, x = np.ogrid[-10:10:250j, -10:10:500j]
img_8bit = make_image(x, y, 0.5, dtype="uint8")
img_16bit = make_image(x, y, 0.5, dtype="uint16")
cv2.imwrite("img_8bit.jpg", img_8bit)
cv2.imwrite("img_16bit.jpg", img_16bit)
cv2.imwrite("img_8bit.png", img_8bit)
cv2.imwrite("img_16bit.png", img_16bit);

#位元組序列與圖形相互轉換

with open("img_8bit.png", "rb") as f:
    png_str = f.read()
    
png_data = np.frombuffer(png_str, np.uint8) #❶
img = cv2.imdecode(png_data, cv2.IMREAD_UNCHANGED) #❷
res, jpg_data = cv2.imencode(".jpg", img) #❸
jpg_str = jpg_data.tobytes() #❹

#%fig=使用`Image`將`imencode()`解碼的結果直接內嵌到Notebook中
res, jpg_data = cv2.imencode(".jpg", img_8bit) 
Image(data=jpg_data.tobytes())

#視訊輸出

def test_avi_output(fn, fourcc):
    #fourcc = cv2.FOURCC(*fourcc) #❶
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    vw = cv2.VideoWriter(fn, fourcc, 15, (500, 250), True) #❷
    if not vw.isOpened():
        return 
    for a in np.linspace(0.1, 2, 100):
        img = make_image(x, y, a)
        vw.write(img)  #❸
    vw.release()  #❹
    
test_avi_output("tmp_fmp4.avi", "fmp4")

print("------------------------------------------------------------")  # 60個

from os import path

for quantizer in [1, 10, 20, 30, 40]:
    fn = "x264_q{:02d}.avi".format(quantizer)
    test_avi_output(fn, "x264")
    fsize = path.getsize(fn)
    print("quantizer = {:02d}, size = {:07d} bytes".format(quantizer, fsize))

#視訊輸入

video = cv2.VideoCapture("x264_q10.avi")
print("FPS:", video.get(cv2.CAP_PROP_FPS)) #❶
print("FRAMES:", video.get(cv2.CAP_PROP_FRAME_COUNT))
print("WIDTH:", video.get(cv2.CAP_PROP_FRAME_WIDTH))
print("HEIGHT:", video.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("CURRENT FRAME:", video.get(cv2.CAP_PROP_POS_FRAMES))
res, frame0 = video.read() #❷
print("CURRENT FRAME:", video.get(cv2.CAP_PROP_POS_FRAMES))
video.set(cv2.CAP_PROP_POS_FRAMES, 50) #❸
print("CURRENT FRAME:", video.get(cv2.CAP_PROP_POS_FRAMES))
res, frame50 = video.read()
print("CURRENT FRAME:", video.get(cv2.CAP_PROP_POS_FRAMES))
video.release()
'''
print("------------------------------------------------------------")  # 60個

import numpy as np
import pylab as pl
import cv2

#圖形處理
#二維卷冊積

#%fig=使用filter2D()製作的各種圖形處理效果
src = cv2.imread("lena.jpg")

kernels = [ 
    (u"低通濾波器",np.array([[1,  1, 1],[1, 2, 1],[1, 1, 1]])*0.1),
    (u"高通濾波器",np.array([[0.0, -1, 0],[-1, 5, -1],[0, -1, 0]])),
    (u"邊緣檢驗",np.array([[-1.0, -1, -1],[-1, 8, -1],[-1, -1, -1]]))
]

index = 0
fig, axes = pl.subplots(1, 3, figsize=(12, 4.3))
for ax, (name, kernel) in zip(axes, kernels):
    dst = cv2.filter2D(src, -1, kernel)
    # 由於matplotlib的彩色順序和OpenCV的順序相反
    ax.imshow(dst[:, :, ::-1])
    ax.set_title(name)
    ax.axis("off")
fig.subplots_adjust(0.02, 0, 0.98, 1, 0.02, 0)


img = np.random.rand(1000,1000) #❶

row = cv2.getGaussianKernel(7, -1) #❷
col = cv2.getGaussianKernel(5, -1)

kernel = np.dot(col[:], row[:].T) #❸

img2 = cv2.filter2D(img, -1, kernel) #❹
img3 = cv2.sepFilter2D(img, -1, row, col) #❺
print("error=", np.max(np.abs(img2[:] - img3[:])))

#形態學運算

#    scpy2.opencv.morphology_demo：示範OpenCV中的各種形態學運算。

#填充-floodFill

#%fig=示範floodFill()的填充效果
img = cv2.imread("coins.png")
seed1 = 344, 188
seed2 = 152, 126
diff = (13, 13, 13)
h, w = img.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
cv2.floodFill(img, mask, seed1, (0, 0, 0), diff, diff, cv2.FLOODFILL_MASK_ONLY)
cv2.floodFill(img, None, seed2, (0, 0, 255), diff, diff)

fig, axes = pl.subplots(1, 2, figsize=(9, 4))
axes[0].imshow(~mask, cmap="gray")
axes[1].imshow(img);

#    scpy2.opencv.floodfill_demo：示範填充函數floodFill()的各個參數的用法。

#去瑕疵-inpaint

#    scpy2.opencv.inpaint_demo：示範inpaint()的用法，使用者用滑鼠繪制需要去瑕疵的區域，程式實時顯示運算結果。


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個



