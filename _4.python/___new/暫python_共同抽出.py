
linewidth == lw


plt.bar(x1, df1["測試資料"], width=0.4, ec="none", fc="#e63946")
plt.bar(x2, df1["預測結果"], width=0.4, ec="none", fc="#7fb069")




# plt.plot([1, 9],[1, 9],'r', lw = 10)




#下載台北思源黑體並命名 taipei_sans_tc_beta.ttf
https://drive.google.com/uc?id=1eGAsTN1HBpJAkeVM57_C7ccp7hbgSz3_&export=download
https://drive.google.com/uc?id=1eGAsTN1HBpJAkeVM57_C7ccp7hbgSz3_

# 將字型加入 matplotlib
from matplotlib.font_manager import fontManager
fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')

plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta'] #輸入中文




from pylab import mpl
mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
# 指定默認字形：解決plot不能顯示中文問題
mpl.rcParams["axes.unicode_minus"] = False


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
圖形大小和分辨率
plt.figure(figsize=(width, height), dpi=dpi)：設定圖形大小和分辨率。
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

plt.title("使用kdeplot()函數繪製常態分布 " + r"$\mu=0, \sigma=1$")

plt.xlabel("日期", fontsize=12, color="b")
plt.ylabel("時數", fontsize=12, color="b")
plt.title("繪製一週工作和玩手機的時間", fontsize=16, color="b")

plt 之 字型設定 字體 大小 顏色 font fontsize fontcolor

plt.xlabel('程式課程', fontsize="10") # 設定 x 軸標題內容及大小
plt.ylabel('選修人數', fontsize="10") # 設定 y 軸標題標題內容及大小
plt.title('資訊程式課程選修人數', fontsize="18") # 設定圖表標題內容及大小
plt.title("2025年1月臺北天氣報告", fontsize=24)
plt.ylabel(r"溫度 $C^{o}$", fontsize=14)

plt.title("Sales Report", fontsize=24)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Number of Sales", fontsize=14)

plt.title('五月份國外旅遊調查表',fontsize=16,color='b')


#文字顯示問題

from os import path
from matplotlib.font_manager import fontManager

print('顯示所有字型')
for i in fontManager.ttflist:
    print(i.fname, i.name)

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

#plt.figure(figsize=(7,2),facecolor='yellow')

print("------------------------------------------------------------")	#60個

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

print("------------------------------------------------------------")	#60個

一樣的意思
plt.imshow(image0[:, :, ::-1])  # 原圖 # same
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))  # 原圖

print("------------------------------------------------------------")	#60個

# cv2 儲存檔案 存圖 cv2.imwrite
# cv2.imwrite 可透過圖片的副檔名來指定輸出的圖檔格式

cv2.imwrite('filename.jpg', image)  # 存成 jpg
cv2.imwrite('filename.png', image)  # 存成 png
cv2.imwrite('filename.tiff', image)  # 存成 tiff

# 部分圖片寫入圖檔
# cv2.imwrite(filename, image[y:y + h, x:x + w])

print('存圖')
filename = 'C:/_git/vcs/_1.data/______test_files2/image_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.bmp'
cv2.imwrite(filename, image)

#輸出圖片檔案時，也可以調整圖片的品質或壓縮率：

# 設定 JPEG 圖片品質為 90（可用值為 0 ~ 100）
cv2.imwrite('filename.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, 90])

print('存圖, 質量為5')
cv2.imwrite("./1.jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY), 5])
print('存圖, 質量為100')
cv2.imwrite("./2.jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

cv2.imwrite(filename2b, image2, [int(cv2.IMWRITE_JPEG_QUALITY), 50])

cv2.imwrite('tmp_image_2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 80])

# 設定 PNG 壓縮層級為 5（可用值為 0 ~ 9）
cv2.imwrite('filename.png', image, [cv2.IMWRITE_PNG_COMPRESSION, 5])
print('存圖, 壓縮為0')
cv2.imwrite("./3.png", image, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
print('存圖, 壓縮為9')
cv2.imwrite("./4.png", image, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])

---------------- 共同抽出 matplotlib plt----------------

"""
plt
另法顯示中文
font = {"family": "DFKai-SB"}  # 設定柱狀圖可以顯示中文
plt.rc("font", **font)
"""




#plt.xticks(np.arange(-5,6))

font_filename = 'C:/Windows/Fonts/mingliu.ttc'  #中英文字型
font = FontProperties(fname = font_filename, size = 20)

plt.xlabel('Time(s)', fontproperties = font)
plt.ylabel('Amplitude', fontproperties = font)
plt.title('三角函數', fontproperties = font, fontsize = 24)

#ax.get_xaxis().set_visible(False)
#ax.get_yaxis().set_visible(False)
#plt.axis('off') #座標軸關閉

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#中文字型的用法
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=font_filename, size=18)
title(u'原始图像', fontproperties=font)

#畫點
plt.plot(1,0,'bo')


plt.plot(seq, data1, '-*', seq, data2, '-o', seq, data3, '-^', seq, data4, '-s')   
plt.plot(seq, data1, 'g--', seq, data2, 'r-.', seq, data3, 'y:', seq, data4, 'k.')   


seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)                         # 設定x軸刻度

plt.plot(seq, Benz, '-*', label='Benz')
plt.plot(seq, BMW, '-o', label='BMW')
plt.plot(seq, Lexus, '-^', label='Lexus')


#plt.plot(x, y, lw=8, ls='-.')
#plt.plot(x, y, marker='*')
#plt.plot(x, y, marker='D',ms=10, mfc='y', mec='r')
#plt.plot(x, y, color='y')
#plt.plot(x, y, color=(1,1,0))  #RGB
#plt.plot(x, y, color='# FFFF00')  #HEX
#plt.plot(x, y, color='yellow')  #英文全名
#plt.plot(x, y, color='0.5')

plt.xticks(range(0,5500,500))
plt.tick_params(axis = 'both', labelsize = 10, color = 'red')
plt.bar(listx, listy, width = 0.5, color = 'r')
plt.barh(listy, listx, height = 0.5, color = 'r')


製作數據
xpt = list(range(1,101))    # 建立1-100序列x座標點
ypt = [x**2 for x in xpt]   # 以x平方方式建立y座標點
ypt = [math.sin(x/10) for x in xpt]   # 以x平方方式建立y座標點

xpt = np.linspace(0, 10, 500)   # 建立含500個元素的陣列
ypt1 = np.sin(xpt)              # y陣列的變化
ypt2 = np.cos(xpt)


x1 = np.linspace(0, 10, num=11)     # 使用linspace()產生陣列
print(type(x1), x1)
x2 = np.arange(0,11,1)              # 使用arange()產生陣列
print(type(x2), x2)
x3 = np.arange(11)                  # 簡化語法產生陣列
print(type(x3), x3)

畫圖資料
plt.legend([ 'y=sin(x)', 'y=cos(x)'])
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

weight = np.array([10, 14, 18, 20, 18, 16, 17, 18, 20, 17])
plt.ylim([0, weight.max()+1])   
plt.plot(days, weight, marker='o', markerfacecolor='gray') 

plt.ylim([0, weight.max()+1])

plt.plot(days, weight, marker='o', markerfacecolor='red',
         linestyle='--', linewidth=2.5, color='green')  

print('載入字型範例')

翰字鑄造 臺北黑體 regular 版本
TaipeiSansTCBeta-Regular.ttf 
https://drive.google.com/uc?id=1eGAsTN1HBpJAkeVM57_C7ccp7hbgSz3_&export=download
TaipeiSansTCBeta-Regular.ttf'


plt.title(r'衰減數列 cos($3\pi x * e^{x})$',fontsize=20)


from matplotlib.font_manager import FontProperties as font

# 連結中文字體
zhfont1 = font(fname = font_filename)
plt.title("連結中文字體", fontproperties=zhfont1)
plt.title("連結中文字體2222")

x = np.linspace(-2 * np.pi, 2 * np.pi, 100) #共100個點
x = np.linspace(-2 * np.pi, 2 * np.pi)   #預設為50個點

s, c = np.sin(x), np.cos(x) #一次做兩個運算

#自訂座標軸的刻度及標籤–xticks()、yticks()
#x座標
ticks = [-2*np.pi, -1.5*np.pi, -1*np.pi, -0.5*np.pi, 0, np.pi * 0.5, np.pi, np.pi * 1.5, np.pi * 2]
#要在x座標寫上的標籤
labels = ['-360°', '-270°', '-180°', '-90°', '0°', '90°', '180°', '270°', '360°']
plt.xticks(ticks, labels)

#x軸刻度 5個點 分別用pi表示
#plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi],['-$2\pi$', '-$\pi$','0', '$\pi$', '$2\pi$'])

plt.legend(['sin','cos'])
plt.legend(['sin','cos'],loc=3,fontsize='xx-large',edgecolor='y',facecolor='r')

plt.ylabel(r'溫度 $C^{o}$')


hist參數
plt.hist(minutes, bins=4, edgecolor='white', linewidth=1.2)
plt.hist(scores, bins=4, color='red', edgecolor='white', linewidth=1.2)

#h = plt.hist(dice,sides,rwidth=0.8)     # 繪製hist圖
h = plt.hist(dice,sides,rwidth=0.5,cumulative=True) # 繪製hist圖

.bar


pie圖參數
labels = ['<100', '100~149', '>=150']

plt.pie(toyota, radius=1.2, labels=labels, shadow=True)
plt.pie(lexus, radius=1.2, labels=labels, shadow=True)
plt.pie(mazda, radius=1.2, labels=labels, shadow=True)
plt.pie(subaru, radius=1.2, labels=labels, shadow=True)

plt.plot(listx1, listy1, color="black", linewidth=1.0, linestyle="-", label="Boys")
plt.plot(listx2, listy2, color="black", linewidth=1.0, linestyle="-.", label="Girls")

----------------------------------------------------------------

#scatter 顏色
#plt.scatter(xpt, ypt1, color=(0, 1, 0)) # 綠色
#plt.scatter(xpt, ypt2)                  # 預設顏色

plt.tick_params(axis='both', labelsize=12, color='red')


#中文字型設定

import matplotlib as mpl
from matplotlib.font_manager import fontManager

fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')

fontManager.addfont('msjhl.ttc')
mpl.rc('font', family='Microsoft JhengHei')

fontManager.addfont('NotoSansTC-Bold.otf')
mpl.rc('font', family='Noto Sans TC')

----------------------------------------------------------------

matplotlib: 畫圖的標準套件
matplotlib.pyplot 是用來畫圖的


matplotlib放font的地方
C:\Users\070601\AppData\Local\Programs\Python\Python311\Lib\site-packages\matplotlib\mpl-data\fonts\ttf

import matplotlib.pyplot as plt
import matplotlib.image as img

fig = img.imread('out20_12.jpg')
plt.imshow(fig)
plt.show()

print('---- plt.figure ST--------------------------------------------------------')	#60個

# 建立第一張圖，若直接 plt.plot 隱含自動建立 figure 並建立 subplot(111)
plt.figure(1)


# plt.figure()參數

plt.figure()  #開新圖片
plt.figure("Figure_1")
plt.figure(figsize=[10,5])
plt.figure(figsize=(10,10))    # 改變圖表尺寸 單位是英吋
plt.figure(frameon=False)
plt.figure(num = '股票分析', figsize=(10,10)) # 設定圖表區寬高

print('---- plt.figure SP--------------------------------------------------------')	#60個







---------------- 共同抽出 opencv cv2----------------


cv
#cv2.waitKey(2000)       # 等待兩秒 ( 2000 毫秒 ) 後關閉圖片視窗




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

print("------------------------------------------------------------")	#60個









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



