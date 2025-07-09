


------------------------------------------------------------




------------------------------------------------------------



------------------------------------------------------------


linewidth == lw


plt.bar(x1, df1["測試資料"], width=0.4, ec="none", fc="#e63946")
plt.bar(x2, df1["預測結果"], width=0.4, ec="none", fc="#7fb069")




# plt.plot([1, 9],[1, 9],'r', lw = 10)






plt.plot(X, Y, color="black")
plt.plot(X, Y, linestyle="--")
plt.plot(X, Y, linewidth=5)
plt.plot(X, Y, marker="o")



# 繪製折線圖並自定義參數
plt.plot(x, y, color='b', linestyle='--', linewidth=2.0, marker='o', markersize=8, markerfacecolor='red', markeredgecolor='blue', label='數據1')

# 設定刻度標籤
plt.xticks([1, 2, 3, 4, 5])
plt.yticks([2, 3, 5, 7, 11])

"""
參數說明
顏色和樣式
color：設定折線的顏色，例如 'r'（紅色），'#00FF00'（綠色）。
linestyle：設定折線的樣式，例如 '-'（實線），'--'（虛線），'-.'（點劃線），':'（點線）。
linewidth：設定折線的寬度，例如 2.0。
標記
marker：設定數據點的標記樣式，例如 'o'（圓點），'s'（正方形），'^'（三角形）。
markersize：設定標記的大小，例如 8。
markerfacecolor：設定標記內部顏色。
markeredgecolor：設定標記邊緣顏色。
刻度和網格
plt.xticks() 和 plt.yticks()：設定刻度標籤。
plt.grid()：顯示或隱藏網格線。

"""

"""
儲存圖表
plt.savefig('tmp_plot.png')
"""

plt.xlabel("X軸", loc="left")
plt.ylabel("Y軸", loc="top")
plt.legend(loc=1)
plt.xlabel("X軸", loc="center")


plt.plot(..., 'yx' )
plt.plot(..., 'gx' )
plt.plot(..., 'b--' )


建立資料 共同抽出

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)  # 共100個點
x = np.linspace(-2 * np.pi, 2 * np.pi)  # 預設為50個點



# 讓年月轉成30度的直書格式，才更方便閱讀
plt.xticks(rotation=30)

plot標記

plt.plot(x, y**2, "b--")
plt.plot(x, 0.5 * y, "go")
plt.plot(x, y, "m+")


x = np.linspace(0, 2 * np.pi, 300)
y = np.sin(x**2)

x = np.linspace(0, 2 * np.pi, num=100, endpoint=True)

# plt.subplot(n_rows, n_cols, plot_num)
# plt.subplot(n_rows, n_cols, plot_num)

plt.subplot(2, 2, 1)
plt.subplot(221)


設定x y 軸 之刻度值
plt.xticks(x, ("2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"))
plt.yticks(np.arange(0, 150, 15))

print("------------------------------------------------------------")  # 60個

#image.save("xxxx.jpg")
#image.save("xxxx.png")

#img1.save("tmp_blue.jpg")
#print(img1.shape)

#img2.save("tmp_alpha.png")
#print(img2.shape)


print('字串轉日期格式')
from datetime import datetime
date_string = "2024/7/3"
date_datetime = datetime.strptime(date_string, "%Y/%m/%d")
print(date_datetime)



"""
import matplotlib.pyplot as plt


fig.autofmt_xdate()  # 預設最佳化角度旋轉

fig.autofmt_xdate(rotation=60)  # 日期旋轉60度

"""

------------------------------------------------------------

plt.legend(loc="upper right")

字串值 整數值 說明
best           0  最佳位置
upper right    1  右上
upper left     2  左上
lower left     3  左下
lower right    4  右下
right          5  右
center left    6  中左
center right   7  中右
lower center   8  中下
upper center   9  中上
center         10 正中

------------------------------------------------------------


------------------------------------------------------------


---------------- 共同抽出 matplotlib plt----------------


----------------------------------------------------------------

#scatter 顏色
#plt.scatter(xpt, ypt1, color=(0, 1, 0)) # 綠色
#plt.scatter(xpt, ypt2)                  # 預設顏色

----------------------------------------------------------------

matplotlib: 畫圖的標準套件
matplotlib.pyplot 是用來畫圖的

---------------- 共同抽出 opencv cv2----------------


---------------- 共同抽出 pillow PIL ----------------

"""
共用抽出

#顯示
#image.show()

"""

PIL opencv之內容區分

1. 作畫的
2. PIL 無圖處理
3. PIL 圖片相關的處理
   3.0 PIL 基本使用 顯示圖片 顯示圖片訊息
   3.1 無 影像處理 縮放 裁剪 複製 合成 旋轉 鏡射
          圖片無影像處理的 放大縮小 裁剪 旋轉  影像不變的
   3.2 有 影像處理 圖片有影像處理的 濾鏡 找輪廓


要小心注意的地方是，讀取進來的模式我們必須選擇二進制的 “rb”。畢竟 Python 預設是使用 Unicode 讀取的，故這樣一個我們無法判斷編碼的文件，若冒然直接讀取，常常是會報錯的。

然後我們可以看到，這個文件屬於『簡體中文』，畢竟其編碼為簡中著名的 “GB2312〃。另外很方便的是， “chardet” 套件會給予一個 “confident” 作為信心度，正如同我上方所說的，這個套件並不是一個可以完美解決所有問題的方法，所以我們也許可以參考 “chardet” 分析結果的信心程度。

----------------------------------------------------------------

取得現在工作中 axes*

我們有時要設 axes 的背景啦等等的資訊。這時就要取得現在工作中的 axes。這一般有兩種方式, 第一種是設 subplot 時可以取得:

fig, ax = plt.subplot()

另一種是用 gca 函數:

ax = plt.gca()

----------------------------------------------------------------

ax.imshow(volume[ax.index, :, :], cMap, vmin=cMin, vmax=cMax)


print('ピクセル(pixel)の情報をそのまま数値として利用する')

from PIL import Image
import numpy as np

image = Image.open('mlzukan-img.png').convert('L')
width, height = image.size
print(image.size)

image_pixels = []
for y in range(height):
    for x in range(width):
        # getpixelで指定した位置のピクセル(pixel)値を取得.
        image_pixels.append(image.getpixel((x,y)))

print(image_pixels)

sys.exit()

------------------------------------------------------------

●----P5-10頁----

from PIL import Image


●----P5-11頁----

image = Image.open('flower.jpg')
image.show()


●----P5-12頁----

red, green, blue = image.split()
convert_image = Image.merge("RGB", (blue, green, red))
convert_image.show()
convert_image.save('rgb_to_bgr.jpg')


●----P5-13頁----

image.split()

type(image.split())


●----P5-14頁----

使用 Pillow 套件，要怎麼把一張圖片從藍色變紅色 ?


●----P5-15頁----

使用 Pillow 套件，要怎麼把一張圖片從藍色變紅色
--- 先不用提供詳細的解決，可以只列出可以用哪些函式，列出 5 點就好


用 split() 怎麼做，請提供我範例程式


●----P5-17頁----

black_and_white = image.convert('1')
black_and_white.show()
black_and_white.save('b_and_w.jpg')


●----P5-18頁----

gray_image = image.convert('L')
gray_image.show()
gray_image.save('gray_image.jpg')

image.transpose(Image.ROTATE_90).show()
image.transpose(Image.ROTATE_90).save('rotate_90.jpg')

#PIL 存圖
print('圖片另存新檔')
image.save('tmp_image1.jpg')
image.save('tmp_image2.jpg', 'JPEG')
image.save('tmp_image4.png', 'PNG')
image2.save("tmp_filename.png")
image2.save("tmp_filename.jpg")

image.transpose(Image.FLIP_LEFT_RIGHT).show()
image.filter(ImageFilter.GaussianBlur(4)).show()
image.filter(ImageFilter.xxxxxx).show()
image.thumbnail((width // 4, height // 4))
image.show()
"""

#另存新檔
image.save("tmp_pic_01.png")
#image.show()
img1.save("aaa.jpg")


print('PIL之另存新檔')

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'
infile = filename
savefile = "tmp_savePNG1.png"

img = Image.open(infile)      #載入圖片檔
img.save(savefile, format="PNG")    #PNG轉存檔案

image = Image.open(filename)
image.save("tmp_pic_quality95.jpg", quality=95 )
image.close()

image = Image.open(filename)
image.save('tmp_pic_normal.jpg')
image.close()

"""
newImage.save("tmp_pic24.png")
img.save("tmp_pic20.png")  # 儲存為 png
newImage.save("tmp_pic26.png")

newImage.save("tmp_pic27.png")

newImage.save("tmp_pic25.png")

"""

savefile = "tmp_redline.png"
image.save(savefile, format="PNG")

newImage.save("tmp_pic_6.jpg")
image.save("tmp_house.png")

---------------- 共同抽出 readwrite file ----------------




---------------- 共同抽出 其他 ----------------



