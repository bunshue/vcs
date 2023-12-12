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

print('用np建立一個影像陣列')

W = 640
H = 480
D = 3

#建立陣列
image = np.ones([H, W, D], dtype = np.uint8) * 128  # 填滿 128

#改變陣列內容
image[:, :, 0] = 0;     #第0通道 B
image[:, :, 1] = 255;   #第1通道 G
image[:, :, 2] = 255;   #第2通道 R

#做resize
size = H, W
print(size)
rst = cv2.resize(image, size)

print("image.shape = ", image.shape)
#print("image = \n", image)

print("rst.shape = ", rst.shape)
#print("rst = \n", rst)

plt.figure('用np建立一個影像陣列', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖 640X480')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('resize 480X640')
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))

plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
print('讀取圖檔 :', filename)
image = cv2.imread(filename)

H, W, D = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)
print('D = ', D)

size = (int(W * 0.9), int(H * 1.1))#變瘦變高
rst = cv2.resize(image, size)

print("image.shape = ", image.shape)
print("rst.shape = ", rst.shape)

plt.figure('resize', figsize = (16, 12))
plt.subplot(221)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title('resize 變瘦1成變高1成')
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
print('讀取圖檔 :', filename)
image = cv2.imread(filename)

rst = cv2.resize(image, None, fx = 2, fy = 0.5)
print("image.shape =", image.shape)
print("rst.shape =", rst.shape)

plt.subplot(223)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title('resize x變2倍, y變一半')
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))

plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
image = cv2.imread(filename)

H, W, D = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)
print('D = ', D)

x = 100
y = 100
M = np.float32([[1, 0, x], [0, 1, y]])
move = cv2.warpAffine(image, M, (W, H))

plt.figure('影像處理 move', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('move')
plt.imshow(cv2.cvtColor(move, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
image = cv2.imread(filename)

H, W, D = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)
print('D = ', D)

M = cv2.getRotationMatrix2D((W / 2, H / 2), 45, 0.6)
rotate = cv2.warpAffine(image, M, (W, H))

plt.figure('rotate', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('rotate')
plt.imshow(cv2.cvtColor(rotate, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
image = cv2.imread(filename)

H, W, D = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)
print('D = ', D)

p1 = np.float32([[0, 0], [W - 1, 0], [0, H - 1]])
p2 = np.float32([[0, H * 0.33], [W * 0.85, H * 0.25], [W * 0.15, H * 0.7]])
M = cv2.getAffineTransform(p1, p2)
dst = cv2.warpAffine(image, M, (W, H))

plt.figure('xxxxxx1', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/demo.bmp'
print('讀取圖檔 :', filename)
image = cv2.imread(filename)

H, W, D = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)
print('D = ', D)

pts1 = np.float32([[150, 50], [400, 50], [60, 450], [310, 450]])
pts2 = np.float32([[50, 50], [H - 50, 50], [50, W - 50], [H - 50, W - 50]])
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(image, M, (W, H))

plt.figure('xxxxxx2', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

print('用np建立一個隨機影像陣列')
image = np.random.randint(0, 256, size = [4, 5], dtype = np.uint8)

H, W = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)

mapx = np.zeros(image.shape,np.float32)
mapy = np.zeros(image.shape,np.float32)
for i in range(H):
    for j in range(W):
        mapx.itemset((i, j), j)
        mapy.itemset((i, j), i)
rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)
print("image = \n", image)
print("mapx = \n",mapx)
print("mapy = \n",mapy)
print("rst = \n",rst)

plt.figure('xxxxxx3', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

print('用np建立一個隨機影像陣列')
image = np.random.randint(0, 256, size = [4, 5], dtype = np.uint8)

H, W = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)

mapx = np.zeros(image.shape, np.float32)
mapy = np.zeros(image.shape, np.float32)
for i in range(H):
    for j in range(W):
        mapx.itemset((i, j), j)
        mapy.itemset((i, j), i)
rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)
print("image = \n", image)
print("mapx = \n", mapx)
print("mapy = \n", mapy)
print("rst = \n", rst)

plt.figure('xxxxxx4', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
image = cv2.imread(filename)

H, W, D = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)
print('D = ', D)

mapx = np.zeros(image.shape[:2], np.float32)
mapy = np.zeros(image.shape[:2], np.float32)
for i in range(H):
    for j in range(W):
        mapx.itemset((i, j), j)
        mapy.itemset((i, j), i)
rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)

plt.figure('xxxxxx5', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

print('用np建立一個隨機影像陣列')
image = np.random.randint(0, 256, size = [4, 5], dtype = np.uint8)

H, W = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)

mapx = np.zeros(image.shape, np.float32)
mapy = np.zeros(image.shape, np.float32)
for i in range(H):
    for j in range(W):
        mapx.itemset((i, j), j)
        mapy.itemset((i, j), H - 1 - i)
rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)
print("image = \n", image)
print("mapx = \n", mapx)
print("mapy = \n", mapy)
print("rst = \n", rst)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
image = cv2.imread(filename)

H, W, D = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)
print('D = ', D)

mapx = np.zeros(image.shape[:2], np.float32)
mapy = np.zeros(image.shape[:2], np.float32)
for i in range(H):
    for j in range(W):
        mapx.itemset((i, j), j)
        mapy.itemset((i, j), H - 1 - i)
rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)

plt.figure('xxxxxx6', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

print('用np建立一個隨機影像陣列')
image = np.random.randint(0, 256, size = [4, 5], dtype = np.uint8)

H, W = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)

mapx = np.zeros(image.shape, np.float32)
mapy = np.zeros(image.shape, np.float32)
for i in range(H):
    for j in range(W):
            mapx.itemset((i, j), W - 1 - j)
            mapy.itemset((i, j), i)
rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)
print("image = \n", image)
print("mapx = \n", mapx)
print("mapy = \n", mapy)
print("rst = \n", rst)

plt.figure('xxxxxx7', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
image = cv2.imread(filename)

H, W, D = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)
print('D = ', D)

mapx = np.zeros(image.shape[:2], np.float32)
mapy = np.zeros(image.shape[:2], np.float32)
for i in range(H):
    for j in range(W):
            mapx.itemset((i, j), W - 1 - j)
            mapy.itemset((i, j), i)
rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)

plt.figure('xxxxxx8', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

print('用np建立一個隨機影像陣列')
image = np.random.randint(0, 256, size = [4, 5], dtype = np.uint8)

H, W = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)

mapx = np.zeros(image.shape, np.float32)
mapy = np.zeros(image.shape, np.float32)
for i in range(H):
    for j in range(W):
            mapx.itemset((i, j), W - 1 - j)
            mapy.itemset((i, j), H - 1 - i)
rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)
print("image = \n", image)
print("mapx = \n", mapx)
print("mapy = \n", mapy)
print("rst = \n", rst)

plt.figure('xxxxxx9', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
image = cv2.imread(filename)

H, W, D = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)
print('D = ', D)

mapx = np.zeros(image.shape[:2], np.float32)
mapy = np.zeros(image.shape[:2], np.float32)
for i in range(H):
    for j in range(W):
            mapx.itemset((i, j), W - 1 - j)
            mapy.itemset((i, j), H - 1 - i)
rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)

plt.figure('xxxxxxa', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

print('用np建立一個隨機影像陣列')
image = np.random.randint(0, 256, size = [4, 6], dtype = np.uint8)

H, W = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)

mapx = np.zeros(image.shape, np.float32)
mapy = np.zeros(image.shape, np.float32)
for i in range(H):
    for j in range(W):
            mapx.itemset((i, j), i)
            mapy.itemset((i, j), j)
rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)
print("image = \n", image)
print("mapx = \n", mapx)
print("mapy = \n", mapy)
print("rst = \n", rst)

plt.figure('xxxxxxb', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
image = cv2.imread(filename)

H, W, D = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)
print('D = ', D)

mapx = np.zeros(image.shape[:2], np.float32)
mapy = np.zeros(image.shape[:2], np.float32)
for i in range(H):
    for j in range(W):
            mapx.itemset((i, j), W - 1 - j)
            mapy.itemset((i, j), H - 1 - i)
rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)

plt.figure('xxxxxxc', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('上下顛倒')
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
image = cv2.imread(filename)

H, W, D = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)
print('D = ', D)

mapx = np.zeros(image.shape[:2], np.float32)
mapy = np.zeros(image.shape[:2], np.float32)
for i in range(H):
    for j in range(W):
        if 0.25 * W < i < 0.75 * W and 0.25 * H < j < 0.75 * H:
                mapx.itemset((i, j), 2 * (j - W * 0.25 ) + 0.5)
                mapy.itemset((i, j), 2 * (i - H * 0.25 ) + 0.5)
        else:     
                mapx.itemset((i, j), 0)
                mapy.itemset((i, j), 0)
rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)

plt.figure('xxxxxxd', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('縮小圖')
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個
