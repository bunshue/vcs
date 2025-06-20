------------------------------------------------------------
snippet 片段
Code Snippet
------------------------------------------------------------

------------------------------------------------------------

# PIL

from PIL import Image, ImageOps
import numpy as np

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

image = Image.open(filename)

size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

# display the resized image
image.show()
------------------------------------------------------------

# 設定中文字型及負號正確顯示
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei

也可以

# 設定中文字型及負號正確顯示
plt.rcParams["font.sans-serif"] = "mingliu"


------------------------------------------------------------

pip freeze > requirements.txt


from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent







# plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 也可設mingliu或DFKai-SB
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 也可設 mingliu 或 DFKai-SB

一個df可以將多筆資料畫在多圖
一個df可以將多筆資料畫在一圖

目前不能畫多個df至一圖



plt.rcParams['figure.figsize'] = [10, 10]
plt.rcParams['figure.dpi'] = 72

print('打印 plt 參數')
cc = plt.rcParams.keys
print(cc)



一大圖上畫上各小圖
plt.figure(figsize=[8, 4])
plt.axes([0, 0, 0.8, 1])
plt.title(label="Chart 1")
plt.plot([1, 2, 3], "r:o")

plt.axes([0.55, 0.1, 0.2, 0.2])
plt.title(label="Chart 2")
plt.plot([1, 2, 3], "g--o")

plt.show()



------------------------------------------------------------


print("姓名   座號  國文  數學  英文")
print("%3s  %2d   %3d   %3d  %3d" % ("林大明", 1, 100, 87, 79))
print("%3s  %2d   %3d   %3d  %3d" % ("陳阿中", 2, 74, 88, 100))
print("%3s  %2d   %3d   %3d  %3d" % ("張小英", 11, 82, 65, 8))

# print("本班總成績：%d 分，平均成績：%5.2f 分" % (total, average))
# print("本班總成績：%d 分，平均成績：%5.2f 分" % (total, average))



------------------------------------------------------------
------------------------------------------------------------

edge_x[edge_x > 255] = 255
edge_y[edge_y > 255] = 255
edge_x = edge_x.astype(np.uint8)
edge_y = edge_y.astype(np.uint8)

edge[edge > 255] = 255


------------------------------------------------------------

------------------------------------------------------------


------------------------------------------------------------


------------------------------------------------------------


------------------------------------------------------------
