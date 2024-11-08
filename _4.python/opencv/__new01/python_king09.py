"""
OpenCV

OpenCV-圖形處理和電腦視覺


"""

print("------------------------------------------------------------")  # 60個

import cv2
import pylab as pl

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
filename = "data/lena.jpg"
img = cv2.imread( filename ) #❶
print(type(img), img.shape, img.dtype)
cv2.namedWindow("demo1")     #❷
cv2.imshow("demo1", img)     #❸
cv2.waitKey(0)  #❹;

print("------------------------------------------------------------")  # 60個

filename = "data/lena.jpg"
img = cv2.imread( filename )
cv2.namedWindow("demo1")
cv2.imshow("demo1", img)
cv2.waitKey(0)

print("------------------------------------------------------------")  # 60個

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img_gray.shape)

print("------------------------------------------------------------")  # 60個

#圖形型態

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
    fn = "tmp_{}_{}.png".format(dtype, nchannel)
    cv2.imwrite(fn, img)

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

img = cv2.imread("data/lena.jpg")
for quality in [90, 60, 30]:
    cv2.imwrite("tmp_lena_q{:02d}.jpg".format(quality), img, 
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
cv2.imwrite("tmp_img_8bit.jpg", img_8bit)
cv2.imwrite("tmp_img_16bit.jpg", img_16bit)
cv2.imwrite("tmp_img_8bit.png", img_8bit)
cv2.imwrite("tmp_img_16bit.png", img_16bit);

#位元組序列與圖形相互轉換

with open("tmp_img_8bit.png", "rb") as f:
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
    fn = "tmp_x264_q{:02d}.avi".format(quantizer)
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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#圖形處理
#二維卷冊積

#%fig=使用filter2D()製作的各種圖形處理效果
src = cv2.imread("data/lena.jpg")

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

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#形態學運算

#    scpy2.opencv.morphology_demo：示範OpenCV中的各種形態學運算。

#填充-floodFill

#%fig=示範floodFill()的填充效果
img = cv2.imread("data/coins.png")
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

plt.show()

#    scpy2.opencv.floodfill_demo：示範填充函數floodFill()的各個參數的用法。

#去瑕疵-inpaint

#    scpy2.opencv.inpaint_demo：示範inpaint()的用法，使用者用滑鼠繪制需要去瑕疵的區域，程式實時顯示運算結果。

print("------------------------------------------------------------")  # 60個

from numpy import fft

#圖形變換
#幾何變換

#%fig=對圖形進行仿射變換
img = cv2.imread("data/lena.jpg")
h, w = img.shape[:2]
src = np.array([[0, 0], [w - 1, 0], [0, h - 1]], dtype=np.float32)  #❶
dst = np.array([[300, 300], [873, 78], [161, 923]], dtype=np.float32)  #❷

m = cv2.getAffineTransform(src, dst)  #❸
result = cv2.warpAffine(
    img, m, (2 * w, 2 * h), borderValue=(255, 255, 255, 255))  #❹

fig, ax = pl.subplots(figsize=(8, 8))
fig.subplots_adjust(0, 0, 1, 1)
ax.set_xlim(-5, w * 2 + 5)
ax.set_ylim(h * 2 + 5, -5)
ax.axis("off")
ax.imshow(result[:, :, ::-1])
ax.imshow(img[:, :, ::-1], alpha=0.4)
p = np.vstack((src, src[:1]))
ax.plot(p[:, 0], p[:, 1], "-o", alpha=0.5)
from matplotlib.patches import FancyArrowPatch
for p1, p2 in zip(src, dst):
    arrow = FancyArrowPatch(p1, p2, transform=ax.transData,
                            color="gray", mutation_scale=10)
    ax.add_artist(arrow)

plt.show()

print("------------------------------")  # 30個

#%fig=對圖形進行透視變換
src = np.array(
    [[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]], dtype=np.float32)
dst = np.array(
    [[300, 350], [800, 300], [900, 923], [161, 923]], dtype=np.float32)

m = cv2.getPerspectiveTransform(src, dst)
result = cv2.warpPerspective(
    img, m, (2 * w, 2 * h), borderValue=(255, 255, 255, 255))

fig, ax = pl.subplots(figsize=(8, 8))
fig.subplots_adjust(0, 0, 1, 1)
ax.set_xlim(-5, w * 2 + 5)
ax.set_ylim(h * 2 + 5, -5)
ax.axis("off")
ax.imshow(result[:, :, ::-1])
ax.imshow(img[:, :, ::-1], alpha=0.4)
p = np.vstack((src, src[:1]))
ax.plot(p[:, 0], p[:, 1], "-o", alpha=0.5)
from matplotlib.patches import FancyArrowPatch
for p1, p2 in zip(src, dst):
    arrow = FancyArrowPatch(p1, p2, transform=ax.transData,
                            color="gray", mutation_scale=10)
    ax.add_artist(arrow)

plt.show()

print("------------------------------------------------------------")  # 60個

"""
    SOURCE
    scpy2.opencv.warp_demo：仿射變換和透視變換的示範程式，
    可以透過滑鼠拖曳圖中藍色三角形和四邊形的頂點，
    進一步決定原始圖形各個頂角經由變換之後的座標。

"""

#%exec_python -m scpy2.opencv.warp_demo

"""
#重映射-remap

mapy, mapx = np.mgrid[0:h * 3:3, 0:w * 2:2]
img2 = cv2.remap(img, mapx.astype("f32"), mapy.astype("f32"), cv2.INTER_LINEAR)
x, y = 12, 40 #用於驗證映射公式的座標點
assert np.all(img[mapy[y, x], mapx[y, x]] == img2[y, x])

#%fig=使用3D曲面和remap()對圖片進行變形
def make_surf_map(func, r, w, h, d0):
    #計算曲面函數func在[-r:r]範圍之上的值，並進行透視投影。
    #視點高度為曲面高度的d0倍+1
    y, x = np.ogrid[-r:r:h * 1j, -r:r:w * 1j]
    z = func(x, y) + 0 * (x + y)  # ❶
    d = d0 * np.ptp(z) + 1.0  # ❷
    map1 = x * (d - z) / d  # ❸
    map2 = y * (d - z) / d
    return (map1 / (2 * r) + 0.5) * w, (map2 / (2 * r) + 0.5) * h  # ❹

def make_func(expr_str):
    def f(x, y):
        return eval(expr_str, np.__dict__, locals())
    return f

def get_latex(expr_str):
    import sympy
    x, y = sympy.symbols("x, y")
    env = {"x": x, "y": y}
    expr = eval(expr_str, sympy.__dict__, env)
    return sympy.latex(expr)

settings = [
    ("sqrt(8 - x**2 - y**2)", 2, 1),
    ("sin(6*sqrt(x**2+y**2))", 10, 10),
    ("sin(sqrt(x**2+y**2))/sqrt(x**2+y**2)", 20, 0.5)
]
fig, axes = pl.subplots(1, len(settings), figsize=(12, 12.0 / len(settings)))

for ax, (expr, r, height) in zip(axes, settings):
    mapx, mapy = make_surf_map(make_func(expr), r, w, h, height)
    img2 = cv2.remap(
        img, mapx.astype("f32"), mapy.astype("f32"), cv2.INTER_LINEAR)
    ax.imshow(img2[:, :, ::-1])
    ax.axis("off")
    ax.set_title("${}$".format(get_latex(expr)))

fig.subplots_adjust(0, 0, 1, 1, 0.02, 0)

plt.show()
"""
print("------------------------------------------------------------")  # 60個

"""
    SOURCE

    scpy2.opencv.remap_demo：示範remap()的拖曳效果。在圖形上按住滑鼠左鍵進行拖曳，每次拖曳完成之後，都將修改原始圖形，可以按滑鼠右鍵取消上次的拖曳動作。
"""

#%fig=使用remap()實現圖形拖曳效果
img = cv2.imread("data/lena.jpg")
h, w = img.shape[:2]
gridy, gridx = np.mgrid[:h, :w]  # ❶
tx, ty = 313, 316
sx, sy = 340, 332
r = 40.0
sigma = 20

mask = ((gridx - sx) ** 2 + (gridy - sy) ** 2) < r ** 2  # ❷
offsetx = np.zeros((h, w))
offsety = np.zeros((h, w))
offsetx[mask] = tx - sx  # ❸
offsety[mask] = ty - sy
offsetx_blur = cv2.GaussianBlur(offsetx, (0, 0), sigma)  # ❹
offsety_blur = cv2.GaussianBlur(offsety, (0, 0), sigma)
img2 = cv2.remap(img,
                 (offsetx_blur + gridx).astype("f4"),
                 (offsety_blur + gridy).astype("f4"), cv2.INTER_LINEAR)

fig, ax = pl.subplots(1, 1, figsize=(8, 8))
fig.subplots_adjust(0, 0, 1, 1, 0, 0)
ax.imshow(img2[:, :, ::-1])
circle = pl.Circle((tx, ty), r, fill=None, alpha=0.5, lw=2, ls="dashed")
ax.add_artist(circle)
circle = pl.Circle((sx, sy), r, fill=None, alpha=0.5, lw=2, color="black")
ax.add_artist(circle)
ax.axis("off")

plt.show()

print("------------------------------------------------------------")  # 60個

#%exec_python -m scpy2.opencv.remap_demo

#直方圖

#%fig=`data/lena.jpg`的三個通道的直方圖統計、通道0和通道2的二維直方圖統計
img = cv2.imread("data/lena.jpg")
fig, ax = pl.subplots(1, 2, figsize=(12, 5))
colors = ["blue", "green", "red"]

for i in range(3):
    hist, x = np.histogram(img[:,:, i].ravel(), bins=256, range=(0, 256)) #❶
    ax[0].plot(0.5 * (x[:-1] + x[1:]), hist, label=colors[i], color=colors[i])

ax[0].legend(loc="upper left")
ax[0].set_xlim(0, 256)
hist2, x2, y2 = np.histogram2d(  # ❷
    img[:,:, 0].ravel(), img[:,:, 2].ravel(), 
    bins=(100, 100), range=[(0, 256), (0, 256)])
ax[1].imshow(hist2, extent=(0, 256, 0, 256), origin="lower", cmap="gray")
ax[1].set_ylabel("blue")
ax[1].set_xlabel("red");

plt.show()

print("------------------------------")  # 30個

result = cv2.calcHist([img],
                      channels=(0, 1, 2),
                      mask = None,
                      histSize = (30, 20, 10),
                      ranges = (0, 256, 0, 256, 0, 256))
cc = result.shape
print(cc)

#(30, 20, 10)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#直方圖反向映射

#%fig=使用calcBackProject()尋找圖形中橙子部分
img = cv2.imread("data/fruits_section.jpg")  # ❶
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

result = cv2.calcHist([img_hsv], [0, 1], None,  # ❷
                      [40, 40], [0, 256, 0, 256])

result /= np.max(result) / 255  # ❸

img2 = cv2.imread("data/fruits.jpg")  # ❹
img_hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

img_bp = cv2.calcBackProject([img_hsv2],  # ❺
                             channels=[0, 1],
                             hist=result,
                             ranges=[0, 256, 0, 256],
                             scale=1)
_, img_th = cv2.threshold(img_bp, 180, 255, cv2.THRESH_BINARY)  # ❻
struct = np.ones((3, 3), np.uint8)
img_mp = cv2.morphologyEx(img_th, cv2.MORPH_CLOSE, struct, iterations=5)  # ❼

fig, axes = pl.subplots(2, 3, figsize=(9, 6))
fig.subplots_adjust(0, 0, 1, 1, 0.01, 0.01)
axes[0, 0].imshow(img[:, :, ::-1])
axes[0, 1].imshow(img2[:, :, ::-1])
axes[0, 2].imshow(result[:], cmap="gray")
axes[1, 0].imshow(img_bp[:], cmap="gray")
axes[1, 1].imshow(img_th[:], cmap="gray")
axes[1, 2].imshow(img_mp[:], cmap="gray")

for axe in axes.flat:
    axe.axis("off")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#直方圖比對

def histogram_match(src, dst):
    res = np.zeros_like(dst)
    cdf_src = np.zeros((3, 256))
    cdf_dst = np.zeros((3, 256))
    cdf_res = np.zeros((3, 256))
    kw = dict(bins=256, range=(0, 256), normed=True)

    for ch in (0, 1, 2):
        hist_src, _ = np.histogram(src[:, :, ch], **kw)  # ❶
        hist_dst, _ = np.histogram(dst[:, :, ch], **kw)
        cdf_src[ch] = np.cumsum(hist_src)  # ❷
        cdf_dst[ch] = np.cumsum(hist_dst)
        index = np.searchsorted(cdf_src[ch], cdf_dst[ch], side="left")  # ❸
        np.clip(index, 0, 255, out=index)  # ❹
        res[:, :, ch] = index[dst[:, :, ch]]  # ❺
        hist_res, _ = np.histogram(res[:, :, ch], **kw)
        cdf_res[ch] = np.cumsum(hist_res)

    return res, (cdf_src, cdf_dst, cdf_res)

src = cv2.imread("data/autumn.jpg")
dst = cv2.imread("data/summer.jpg")

res, cdfs = histogram_match(src, dst)

#%figonly=直方圖比對結果
fig = pl.figure(figsize=(10, 6))
fig.subplots_adjust(0, 0, 1, 1, 0, 0)
ax1 = pl.subplot2grid((5, 6), (0, 0), 3, 3)
ax2 = pl.subplot2grid((5, 6), (0, 3), 3, 3)
ax1.imshow(dst[:,:,::-1])
ax2.imshow(res[:,:,::-1])
ax1.axis("off")
ax2.axis("off")
axb = pl.subplot2grid((5, 6), (3, 0), 2, 2)
axg = pl.subplot2grid((5, 6), (3, 2), 2, 2)
axr = pl.subplot2grid((5, 6), (3, 4), 2, 2)

axg.set_yticklabels([])
axr.set_yticklabels([])

for ax, cdf in zip((axb, axg, axr), zip(*cdfs)):
    ax.plot(cdf[0], alpha=0.6, label="src", ls="--")
    ax.plot(cdf[1], alpha=0.6, label="dst", ls=":")
    ax.plot(cdf[2], alpha=0.6, label="res")
    ax.set_xlim(0, 256)
    ax.set_ylim(0, 1.1)

plt.show()
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
#二維離散傅立葉變換

from numpy import fft

x = np.random.rand(8, 8)
X = fft.fft2(x)
print(np.allclose(X[1:, 1:], X[7:0:-1, 7:0:-1].conj()))  # 共軛復數
print(X[::4, ::4]) # 虛數為零

"""
True
[[ 31.48765415+0.j  -2.80563949+0.j]
 [  0.75758598+0.j  -0.53147589+0.j]]
"""

x2 = fft.ifft2(X) # 將頻域訊號轉換回空域訊號
np.allclose(x, x2) # 和原始訊號進行比較

#True

#%fig=（左上）用fft2()計算的頻域訊號，
#（中上）使用fftshift()移位之後的頻域訊號，
#（其它）各個領域所對應的空域訊號

N = 256
img = cv2.imread("data/lena.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (N, N))
img_freq = fft.fft2(img)
img_mag = np.log10(np.abs(img_freq))
img_mag_shift = fft.fftshift(img_mag)

rects = [(80, 125, 85, 130), (90, 90, 95, 95),
         (150, 10, 250, 250), (110, 110, 146, 146)]

"""
    SOURCE

    scpy2.opencv.fft2d_demo：示範二維離散傅立葉變換，
    使用者在左側的頻域模值圖形上用滑鼠繪制隱藏區域，
    右側的圖形為頻域訊號經由隱藏處理之後所轉換成的空域訊號。
"""

#%fig=(左上)用fft2()計算的頻域訊號，(中上)使用fftshift()移位之後的頻域訊號，(其它)各個領域所對應的空域訊號
filtered_results = []
for i, (x0, y0, x1, y1) in enumerate(rects):
    mask = np.zeros((N, N), dtype=np.bool)  # ❶
    mask[x0:x1 + 1, y0:y1 + 1] = True  # ❷
    mask[N - x1:N - x0 + 1, N - y1:N - y0 + 1] = True  # ❸
    mask = fft.fftshift(mask)  # ❹
    img_freq2 = img_freq * mask  # ❺
    img_filtered = fft.ifft2(img_freq).real  # ❻
    filtered_results.append(img_filtered)

fig, axes = pl.subplots(2, 3, figsize=(9, 6))
axes = axes.ravel()
axes[0].imshow(img_mag, cmap=pl.cm.gray)
axes[1].imshow(img_mag_shift, cmap=pl.cm.gray)

ax = axes[1]
for i, (x0, y0, x1, y1) in enumerate(rects):
    r = pl.Rectangle((x0, y0), x1 - x0, y1 - y0, alpha=0.2)
    ax.add_artist(r)
    pl.text((x0 + x1) / 2, (y0 + y1) / 2, str(i + 1), color="white",
            transform=ax.transData, ha="center", va="center", alpha=0.8)

for ax, result in zip(axes[2:], filtered_results):
    ax.imshow(result, cmap=pl.cm.gray)

for ax in axes:
    ax.set_axis_off()

fig.subplots_adjust(0.01, 0.01, 0.99, 0.99, 0.02, 0.02)

plt.show()
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
#用二元視覺圖形計算深度訊息

img_left = cv2.pyrDown(cv2.imread('data/aloeL.jpg'))
img_right = cv2.pyrDown(cv2.imread('data/aloeR.jpg'))

img_left = cv2.cvtColor(img_left, cv2.COLOR_BGR2RGB)
img_right = cv2.cvtColor(img_right, cv2.COLOR_BGR2RGB)

stereo_parameters = dict(
    SADWindowSize = 5,
    numDisparities = 192,
    preFilterCap = 4,
    minDisparity = -24,
    uniquenessRatio = 1,
    speckleWindowSize = 150,
    speckleRange = 2,
    disp12MaxDiff = 10,
    fullDP = False,
    P1 = 600,
    P2 = 2400)

stereo = cv2.StereoSGBM(**stereo_parameters)
# NG disparity = stereo.compute(img_left, img_right).astype(np.float32) / 16

#%fig=用remap重疊左右兩幅圖形
h, w = img_left.shape[:2]
ygrid, xgrid = np.mgrid[:h, :w]
ygrid = ygrid.astype(np.float32)
xgrid = xgrid.astype(np.float32)
# NG res = cv2.remap(img_right, xgrid - disparity, ygrid, cv2.INTER_LINEAR)

fig, axes = pl.subplots(1, 3, figsize=(9, 3))
axes[0].imshow(img_left)
axes[0].imshow(img_right, alpha=0.5)
#axes[1].imshow(disparity, cmap="gray")
axes[2].imshow(img_left)
#axes[2].imshow(res, alpha=0.5)
for ax in axes:
    ax.axis("off")
fig.subplots_adjust(0, 0, 1, 1, 0, 0);

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#圖形識別
#用Hough變換檢驗直線和圓

"""
    SOURCE
    scpy2.opencv.hough_demo：霍夫變換示範程式，可透過界面調節函數的所有參數。
"""
#檢驗線段

#%figonly=用r和θ表示的直線
    
x = [-2, 5]
y = [5, -1]

from sympy import Point, Line
from sympy import Point, Line

line = Line(Point(x[0], y[0]), Point(x[1], y[1]))
seg = line.perpendicular_segment(Point(0, 0))

plt.plot([seg.p1.x, seg.p2.x], [seg.p1.y, seg.p2.y], "--o", color="gray")

from matplotlib.patches import Wedge

angle = np.rad2deg(np.arctan2(float(seg.p2.y), float(seg.p2.x)))
theta = Wedge((0, 0), 1, 0, angle, alpha=0.3)
#plt.add_patch(theta)
plt.text(1, 0.5, r"$\theta$", fontsize="large")
plt.text(0.8, 1.1, r"$r$", fontsize="large");

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#%figonly=霍夫變換示意圖
k = 1.2
b = 3

xn, yn = 4, 3

fig, (ax1, ax2) = pl.subplots(1, 2, figsize=(8, 3))
xs = np.linspace(0, 5, 4)
ys = xs * k + b

for x0, y0 in zip(xs, ys):
    ax1.plot(x0, y0, "o")

ax1.plot(xn, yn, ">")
ax1.margins(0.1, 0.1)

theta = np.linspace(0, np.pi, 100)
for x0, y0 in zip(xs, ys):
    r = x0 * np.cos(theta) + y0 * np.sin(theta)
    ax2.plot(theta, r)

r = xn * np.cos(theta) + yn * np.sin(theta)
ax2.plot(theta, r, "--")
ax2.set_xlim(0, np.max(theta));

plt.show()
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

'''
#%fig=使用HoughLinesP()檢驗圖形中的直線
img = cv2.imread("data/building.jpg", cv2.IMREAD_GRAYSCALE)
img_binary = cv2.Canny(img, 100, 255)
lines = cv2.HoughLinesP(img_binary, rho=1, theta=np.deg2rad(0.1),
                        threshold=96, minLineLength=33,
                        maxLineGap=4)

fig, ax = pl.subplots(figsize=(8, 6))
pl.imshow(img, cmap="gray")
from matplotlib.collections import LineCollection
lc = LineCollection(lines.reshape(-1, 2, 2))
ax.add_collection(lc)
ax.axis("off");

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#檢驗圓形

#%fig=使用HoughCircles()檢驗圖形中的圓形
img = cv2.imread("data/coins.png", cv2.IMREAD_GRAYSCALE)
img_blur = cv2.GaussianBlur(img, (0, 0), 1.8) #❶
circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT, dp=2.0, minDist=20.0,
                 param1=170, param2=44, minRadius=16, maxRadius=40)

x, y, r = circles[0].T

fig, ax = pl.subplots(figsize=(8, 6))
pl.imshow(img, cmap="gray")
from matplotlib.collections import EllipseCollection
ec = EllipseCollection(widths=2*r, heights=2*r, angles=0, units="xy", # ❷
                       facecolors="none", edgecolors="red",
                       transOffset=ax.transData, offsets=np.c_[x, y])
ax.add_collection(ec)
ax.axis("off");

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#圖形分割
#Mean-Shift法

#%fig=使用pyrMeanShiftFiltering()進行圖形分割，從左到右參數sr分別為20, 40, 80
fig, axes = pl.subplots(1, 3, figsize=(9, 3))

img = cv2.imread("data/fruits.jpg")

srs = [20, 40, 80]
for ax, sr in zip(axes, srs):
    img2 = cv2.pyrMeanShiftFiltering(img, sp=20, sr=sr, maxLevel=1)
    ax.imshow(img2[:,:,::-1])
    ax.set_axis_off()
    ax.set_title("sr = {}".format(sr))
    
fig.subplots_adjust(0.02, 0, 0.98, 1, 0.02, 0) 

plt.show()
'''
print("------------------------------------------------------------")  # 60個
'''
#分水嶺算法

img = cv2.imread("data/pills.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray = cv2.blur(img_gray, (15, 15)) #❶
_, img_binary = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY) #❷
peaks = img_gray == cv2.dilate(img_gray, np.ones((7, 7)), 1) #❸

# NG peaks &= img_binary
peaks[1, 1] = True  #❹

from scipy.ndimage import label
markers, count = label(peaks) #❺
cv2.watershed(img, markers)

"""
    SOURCE
scpy2.opencv.watershed_demo：分水嶺算法的示範程式。
用滑鼠在圖形上繪制起始區域，起始區域將使用“目前標簽”填充，
按滑鼠右鍵切換到下一個標簽。每次繪制起始區域之後，將顯示分割的結果。
"""

print("------------------------------")  # 30個

#%figonly=使用watershed分割藥丸
fig, axes = pl.subplots(1, 2, figsize=(10, 3))
axes[0].imshow(img[:, :, ::-1])
peaks_img = np.zeros(img.shape[:2] + (4,), np.uint8)
peaks_img[peaks, 2] = 255
peaks_img[peaks, -1] = 255
axes[0].imshow(peaks_img)

colors = np.random.randint(64, 200, (count+2, 3)).astype(np.uint8)
colors[markers[1, 1]] = 255, 255, 255
colors[-1] = 0
axes[1].imshow(colors[markers])
for ax in axes:
    ax.axis("off")
fig.subplots_adjust(0, 0, 1, 1, 0, 0);

plt.show()
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
# 無 SURF() 函數
#SURF特征比對

#%fig=SURF()找到的關鍵點和每個關鍵點的局部圖形
img_gray1 = cv2.imread("data/lena.jpg", cv2.IMREAD_GRAYSCALE) #❶
surf = cv2.SURF(2000, 2)  #❷
key_points1 = surf.detect(img_gray1) #❸
key_points1.sort(key=lambda kp:kp.size, reverse=True) #❹

img_color1 = cv2.cvtColor(img_gray1, cv2.COLOR_GRAY2RGB)
cv2.drawKeypoints(img_color1, key_points1[:25], img_color1, color=(255, 0, 0),  #❺
                  flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

from scpy2.utils.image import concat_keypoints

img_keypoints = concat_keypoints(img_gray1, key_points1[:25], 5, 5, scale=2)
#%array_image img_color1; img_keypoints

print("------------------------------")  # 30個

_, features1 = surf.compute(img_gray1, key_points1)
cc = features1.shape
print(cc)

#(145, 128)

img_gray2 = cv2.imread("dat/lena2.jpg", cv2.IMREAD_GRAYSCALE)
img_color2 = cv2.cvtColor(img_gray2, cv2.COLOR_GRAY2RGB)
surf2 = cv2.SURF(2000, 2)  
key_points2, features2 = surf2.detectAndCompute(img_gray2, None)

FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=100)   

fbm = cv2.FlannBasedMatcher(index_params, search_params) #❶
match_list = fbm.knnMatch(features1, features2, k=1) #❷

m = match_list[0][0]

#%C m.distance; m.queryIdx; m.trainIdx

#請讀者思考如何利用下面程式得到的matrix矩陣將變形之後的圖形復原成原始圖形。

key_positions1 = np.array([kp.pt for kp in key_points1])
key_positions2 = np.array([kp.pt for kp in key_points2])

index1 = np.array([m[0].queryIdx for m in match_list])
index2 = np.array([m[0].trainIdx for m in match_list])

distances = np.array([m[0].distance for m in match_list])

best_index = np.argsort(distances)[:50] #❶
matched_positions1 = key_positions1[index1[best_index]]
matched_positions2 = key_positions2[index2[best_index]]

matrix, mask = cv2.findHomography(matched_positions1, matched_positions2, cv2.RANSAC) #❷

#scpy2.opencv.surf_demo：SURF圖形比對示範程式。
#用滑鼠修改右側圖形的四個角的位置計算出透視變換之後的圖形，
#然後在原始圖形和變換之後的圖形之間搜尋比對點，並計算透視變換的矩陣。
"""

""" no module
#%figonly=顯示特征比對的關鍵點
from matplotlib.collections import LineCollection
from scpy2.utils.image import concat_images

COLORS = np.array([[0, 0.0, 0.5], [1, 0, 0]])

img_color1 = cv2.cvtColor(img_gray1, cv2.COLOR_GRAY2RGB)
merged_img = concat_images([img_color1, img_color2], margin=0)

fig, ax = pl.subplots(figsize=(12, 6))
ax.axis("off")
pl.imshow(merged_img)
lines = np.concatenate([matched_positions1, matched_positions2], axis=1)
lines[:, 2] += img_color2.shape[1]
line_collection = LineCollection(lines.reshape(-1, 2, 2), 
                                 colors=COLORS[mask.ravel()], lw=1, alpha=0.5)
ax.add_collection(line_collection);

plt.show()

"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
from numpy import fft

#形狀與結構分析
#輪廓檢驗

#%exec_python -m scpy2.opencv.findcontours_demo

img_coin = cv2.imread("data/coins.png", cv2.IMREAD_COLOR)
img_coin_gray = cv2.cvtColor(img_coin, cv2.COLOR_BGR2GRAY)
img_coin_blur = cv2.GaussianBlur(img_coin_gray, (0, 0), 1.5, 1.5)
img_coin_binary = cv2.Canny(img_coin_blur.copy(), 60, 60)
img_coin_binary = cv2.morphologyEx(img_coin_binary, cv2.MORPH_CLOSE, 
                                   np.ones((3, 3), "uint8"))

for approx in ["NONE", "SIMPLE", "TC89_KCOS", "TC89_L1"]:
    approx_flag = getattr(cv2, "CHAIN_APPROX_{}".format(approx))
    coin_contours, hierarchy = cv2.findContours(img_coin_binary.copy(), 
                           cv2.RETR_EXTERNAL, approx_flag)
    print("{}: {}  ".format(approx, sum(contour.shape[0] for contour in coin_contours)))

#NONE: 3179   SIMPLE: 1579   TC89_KCOS: 849   TC89_L1: 802  

#%fig=顯示所有圓度在0.8到1.2之間的輪廓
def circularity(contour):
    perimeter = cv2.arcLength(contour, True)
    area = cv2.contourArea(contour) + 1e-6
    return perimeter * perimeter / (4 * np.pi * area)

coin_contours = [contour for contour in coin_contours 
                 if 0.8 < circularity(contour) < 1.2]
cv2.drawContours(img_coin, coin_contours, -1, (255, 0, 0))

cv2.imshow("demo1", img_coin)
cv2.waitKey(0)
'''

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
img_pattern = cv2.imread("data/nested_patterns.png")
img_pattern_gray = cv2.cvtColor(img_pattern, cv2.COLOR_BGR2GRAY)
_, img_pattern_binary = cv2.threshold(img_pattern_gray, 100, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(img_pattern_binary.copy(),
        cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_L1)
hierarchy.shape = -1, 4

root_index = [i for i in range(len(hierarchy)) if hierarchy[i, 3] < 0]
print(root_index)

#[0, 7, 19]

def get_children(hierarchy, index):
    first_child = hierarchy.item(index, 2)
    if first_child >= 0:
        yield first_child
        brother = hierarchy.item(first_child, 0)
        while brother >= 0:
            yield brother
            brother = hierarchy.item(brother, 0)
            
def get_descendant(hierarchy, index, level=1):
    for child in get_children(hierarchy, index):
        yield level, child
        for item in get_descendant(hierarchy, child, level + 1):
            yield item
            
print(list(get_descendant(hierarchy, 0)))

#[(1, 1), (2, 2), (3, 3), (2, 4), (3, 5), (3, 6)]

#%figonly=顯示輪廓的階層結構
root_index = [i for i in range(len(hierarchy)) if hierarchy[i, 3] < 0]

lines = []
levels = []

for index in root_index:
    items = zip(*get_descendant(hierarchy, index))
    if items:
        children_level, children_index = items
        lines.extend([contours[i] for i in children_index])
        levels.extend(children_level)
    lines.append(contours[index])
    levels.append(0)
    
lines = [line[:, 0, :] for line in lines]
    
from matplotlib.collections import LineCollection, PolyCollection
fig, ax = pl.subplots(figsize=(8, 8))
ax.set_aspect("equal")
polys = PolyCollection(lines, array=np.array(levels), facecolors="none")
ax.add_collection(polys)
ax.set_xlim(0, img_pattern.shape[1])
ax.set_ylim(img_pattern.shape[0], 0);

plt.show()
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#輪廓比對

img_patterns = cv2.imread("data/patterns.png", cv2.IMREAD_GRAYSCALE)
patterns, _ = cv2.findContours(img_patterns, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
img_targets = cv2.imread("data/targets.png", cv2.IMREAD_GRAYSCALE)
targets, _ = cv2.findContours(img_targets, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

patterns = [pattern - np.min(pattern, 0, keepdims=True) for pattern in patterns] #❶
targets = [target - np.min(target, 0, keepdims=True) for target in targets]

patterns_simple = [cv2.approxPolyDP(pattern, 5, True) for pattern in patterns] #❷
targets_simple = [cv2.approxPolyDP(target, 8, True) for target in targets]


for method in [1, 2, 3]:
    method_str = "CONTOURS_MATCH_I{}".format(method)
    method = getattr(cv2, method_str)
    scores = [cv2.matchShapes(targets_simple[0], patterns_simple[pidx], method, 0)
                  for pidx in range(5)]
    print(method_str, ", ".join("{: 8.4f}".format(score) for score in scores))

"""
CV_CONTOURS_MATCH_I1  11.3737,   0.3456,   0.0289,   1.0495,   0.0020
CV_CONTOURS_MATCH_I2   4.8051,   2.2220,   0.0179,   0.3624,   0.0013
CV_CONTOURS_MATCH_I3   0.9164,   0.4778,   0.0225,   0.4552,   0.0016
"""


#%figonly=使用`matchShapes()`比較由`approxPolyDP()`近似之後的輪廓
fig, ax = pl.subplots(figsize=(8, 8))
ax.set_aspect("equal")

width = 180
for tidx, (target, target_simple) in enumerate(zip(targets, targets_simple)): 
    scores = []
    texts = []
    for pidx, (pattern, pattern_simple) in enumerate(zip(patterns, patterns_simple)):
        index = np.s_[:, 0, :]
        pattern2 = pattern[index]
        target2 = target[index]
        pattern_simple2 = pattern_simple[index]
        target_simple2 = target_simple[index]
        
        x0 = pidx * width + width
        y0 = tidx * width + width
        
        if tidx == 0:
            pattern_poly = pl.Polygon(pattern2 + [x0, 0], color="black", alpha=0.6)
            ax.add_patch(pattern_poly)
            text = ax.text(x0 + width * 0.3, -50, str(pidx), fontsize=14, ha="center")
        if pidx == 0:
            target_poly = pl.Polygon(target2 + [0, y0], color="green", alpha=0.6)
            ax.add_patch(target_poly)
            text = ax.text(-50, y0 + width * 0.3, str(tidx), fontsize=14, ha="center")

        pattern_simple_poly = pl.Polygon(pattern_simple2 + [x0, 0], facecolor="none", alpha=0.6)
        ax.add_patch(pattern_simple_poly)
        target_simple_poly = pl.Polygon(target_simple2 + [0, y0], facecolor="none", alpha=0.6)
        ax.add_patch(target_simple_poly)
        
        score = cv2.matchShapes(target_simple, pattern_simple, cv2.CONTOURS_MATCH_I3, 0)
        text = ax.text(x0 + width * 0.3, y0 + width * 0.2, "{:5.4f}".format(score), 
                ha="center", va="center", fontsize=16)
        scores.append(score)
        texts.append(text)
    best_index = np.argmin(scores)
    texts[best_index].set_color("red")
    
ax.relim()
ax.set_axis_off()
ax.autoscale();

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


"""
型態轉換
"""

points = np.random.rand(20, 2).astype(np.float32)
(x, y), (w, h), angle = cv2.minAreaRect(points)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




