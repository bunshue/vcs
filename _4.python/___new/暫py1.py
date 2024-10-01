
指定安裝版本
pip install imageai==2.0.2


selenium模組 : 瀏覽器自動化操作
PyAutoGUI模組 : 鍵盤滑鼠自動化


print("欲搜尋字串")
findstr = "aaaa"
index = str_Obj.find(findstr)     # 搜尋findstr字串是否存在
if  index >= 0:             # 搜尋檔案是否有欲尋找字串
    print("搜尋 %s 字串存在 %s 檔案中" % (findstr, filename))
    print("在索引 %s 位置出現" % index)
else:
    print("搜尋 %s 字串不存在 %s 檔案中" % (findstr, filename))

print("------------------------------------------------------------")  # 60個

from os import path
import shutil

png_path = path.join(default_dest, "fonts/HTML-CSS/TeX/png")
shutil.rmtree(png_path)

print("------------------------------------------------------------")  # 60個

#留下錄影部分 比較之

record_filename = 'tmp_screen_recording1_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.avi'

#建立影像寫入器 out
out = cv2.VideoWriter(record_filename, cv2.VideoWriter_fourcc(*'XVID'), 1, ImageGrab.grab().size)  # 幀率為32，可以調節

        for _ in range(10)
            im = ImageGrab.grab()
            imm = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
            out.write(imm)

        out.release()
        cv2.destroyAllWindows()





莫煩 python
https://mofanpy.com/

https://github.com/MorvanZhou


from os import system

"""
import platform

os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


"""


turtle 指令
turtle.Screen().reset()


做一個完整版 TextEditor 大整理



import cv2

video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

cap = cv2.VideoCapture(video_filename)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("影格尺寸:", width, "x", height)

fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
codec = (chr(fourcc&0xFF)+chr((fourcc>>8)&0xFF)+
        chr((fourcc>>16)&0xFF)+chr((fourcc>>24)&0xFF))
print("Codec編碼:", codec)





def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    

expression = input("請輸入數學表達式 :")
print("結果是 : ", eval(expression))


import datetime
    today = datetime.date.today()
    print('Day is', today)

bmi = round(weight / pow(height, 2), 2)

print("------------------------------------------------------------")  # 60個

import os
import sys

def lll(dirname):
    for name in os.listdir(dirname):
        #print('a')
        if name not in (os.curdir, os.pardir):
            print('b')
            full = os.path.join(dirname, name)
            print(full)


foldername = 'C:/_git/vcs/_1.data/______test_files5'

lll(foldername)

bufsize = 8096
usage = """
usage: md5sum.py [-b] [-t] [-l] [-s bufsize] [file ...]
-b        : read files in binary mode (default)
-t        : read files in text mode (you almost certainly don't want this!)
-l        : print last pathname component only
-s bufsize: read buffer size (default %d)
file ...  : files to sum; '-' or no files means stdin
""" % bufsize

sys.stderr.write('%s: %s\n%s' % ('aaaa', 'bbbbb', usage))

---

# cv2 之讀檔 存檔 (轉換檔案格式) 直接改副檔名即可
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
cv2.imwrite("aaaa.png", img)



撈出一層時 若遇到資料夾 是如何處理的?!

print("------------------------------------------------------------")  # 60個



# Count each letter in the string 
def countLetters(line, counts): 
    for ch in line:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1

filename = 'data/engnews.txt'

infile = open(filename, "r") # Open the file, 格式要unicode轉ascii

counts = 26 * [0] # Create and initialize counts
for line in infile:
    # Invoke the countLetters function to count each letter
    countLetters(line.lower(), counts)
    
# Display results
for i in range(len(counts)):
    if counts[i] != 0:
        print(chr(ord('a') + i) + " appears " + str(counts[i])
          + (" time" if counts[i] == 1 else " times"))

infile.close() # Close file
  
print("------------------------------------------------------------")  # 60個

CVzone

OpenCV是一个开源计算机视觉库，可提供播放不同图像和视频流的权限，还有助于端到端项目，如对象检测、人脸检测、对象跟踪等。

CVzone是一个计算机视觉包，可以让我们轻松运行像人脸检测、手部跟踪、姿势估计等，以及图像处理和其他 AI 功能。
它的核心是使用 OpenCV 和 MediaPipe 库。请点击此处获取更多信息。

https://github.com/cvzone/cvzone

AttributeError: module 'PIL.Image' has no attribute 'ANTIALIAS'

Pillow 10.0.0後 將
Image.ANTIALIAS
刪除

改成
Image.LANCZOS
Image.Resampling.LANCZOS


python data



pypy
找出指定目錄下所有 空 資料夾
找出指定目錄下所有 空 檔案


檔案整理要考慮是否要搬含資料夾
像是s94的 不用看資料夾
有些也不用考慮 例如xxxx 因為資料夾名會和檔案名一樣
只需要改短檔名即可

fx內也可以建立fx

準備撈出所有 python pip install 相關

Dictionaries Set List Tuple

random模組的方法
seed()
random()	產生0~1之間的浮點數
choice(seq)	從串列中隨機挑一個
randint(a, b)	從a~b中產生一個整數亂數
randrange(st, sp [, step])	從st~sp中產生一個step遞增的亂數
sample(polulation, k) 隨機挑選k個元素並以串列回傳
shuffle() 將串列資料洗牌
uniform(a, b) 從a~b中 隨機生成一個浮點數



內建函式 進位轉換 進位轉換之函數
bin(int)	十進位 轉 二進位
oct(int)	十進位 轉 八進位
hex(int)	十進位 轉 16進位
int(s, base)	字串s根據base轉成十進位
int(s, base)	字串根據基底轉成十進位

數學模組
math之屬性與方法
pi
e
ceil(x)
floor(x)
exp(x)
sqrt(x)
pow(x, y)	x ^ y
fmod(x, y)	x % y
hypot(x, y)	sqrt(x^2+y^2)
gcd(x, y)	GCD
isnan(x, y)	是否NaN
isinf(x, y)	是否inf

ord() 查詢某個字元的ASCII值
chr() 將ASCII的值轉換成英文字母

安裝opencv

pip install opencv-python


C:\_git\vcs\_4.python\__code\高效率Python自動化工作術\chap10

PySimpleGUI	建立應用程式的函示庫
mutagen	讀取與存寫語音檔的函示庫

pip install mutagen


PySimpleGUI的零件一欄表
Text		文字
Input		輸入欄位
Button		按鈕
Multiline	多行文字
FileBrowse	選取檔案按鈕
FolderBrowse	選取資料夾按鈕

pypi網站可以看到目前套件的最新版本
https://pypi.org/project/requests/

pypi
https://pypi.org/project/requests/

Python資料型態
數值(Number)	-- 整數(Integers, int) 和 浮點數(Floats, float)
字串(String)
布林(Boolean)

字典(Dictionary){}
集合(Set){}
串列(List)[]
元組(Tuple)()
後四者為容器型態(container type)

新進文件要如何整理?

Python字串 不允許變更內容

python_install_faq.txt

1. python IDLE, anaconda, thonny
2. pip install
3. 處理模組不能使用問題
  1. 特殊版本安裝法
  2. 特殊安裝法
  3. 修改程式
  4. 修改模組

使用豆瓣源 安裝moviepy	ok in kilo	2024/1/20 12:08上午

 pip install moviepy==1.0.3 -i https://pypi.doubanio.com/simple

安装成功.......


py需求

撈出資料夾下所有檔案(多層)
檔案容量>一定大小才顯示

承上
找出這些大檔的影片格式 若大於小於特定格式 顯示出來


改名
資料夾下的檔案 符合條件的字串要改成別的字串

ex:

全部的 good 改成 nice
D:/.../.../.../.../.../folder/ABCD.good.EFG
改成
D:/.../.../.../.../.../folder/ABCD.nice.EFG

資料夾 副檔名皆不變

print("------------------------------------------------------------")  # 60個

標準化 info

PIL開啟圖檔
opencv開啟圖檔
opencv開啟影片
opencv開啟WebCam

print("------------------------------------------------------------")  # 60個

filename1 = 'C:/_git/vcs/_4.python/_data/picture_mix1.bmp'
filename2 = 'C:/_git/vcs/_4.python/_data/picture_mix2.bmp'

picture_add1.bmp
picture_add2.bmp


newimg.paste(img, mask=img)             # 將PNG檔壓在白底圖片上



    image.paste(icon, (0, 0), icon)  # 加入浮水印


paste 的兩個icon

image2 = image2.resize((w, h), resample=Image.NEAREST)


窗口显示方式，cv2.WINDOW_NORMAL为正常显示，可以调整大小
# cv2.WINDOW_AUTOSIZE显示原图片的大小，用户不能调整大小


移動檔案指標

seek 要以binary開檔 才會正確

seek(偏移量, 起算位置)

起算位置 0 從頭開始算
起算位置 1 從目前位置起算
起算位置 2 從尾開始算

f.seek(0, 0) 將指標移到檔案頭
f.seek(3, 1) 從現在位置往後移動3個字
f.seek(-5, 2) 從最後面往前移動5個字


OpenCV 的 cv2.imread 在讀取圖片時，可以在第二個參數指定圖片的格式，可用的選項有三種：


數值 1
cv2.IMREAD_COLOR
    此為預設值，這種格式會讀取 RGB 三個 channels 的彩色圖片，而忽略透明度的 channel。

數值 0
cv2.IMREAD_GRAYSCALE
    以灰階的格式來讀取圖片。
數值 -1
cv2.IMREAD_UNCHANGED
    讀取圖片中所有的 channels，包含透明度的 channel。 
    



py之字串處理
1.長度 len
2.子字串
3.搜尋 index find
4.去頭尾空白 lstrip rstrip strip
5.取代 replace
6.分割 split
7.特定開頭與結尾 startswith endswith
8.轉大小寫 upper lower capitalize 全大寫、全小寫、首字大寫

9.運算子 in


在程式尚未完成前 可以在函數內容放上pass
def my_function(xxx):
    pass
之後再來做

hotkey

UE
找下一個	F3
找上一個	ctrl + F3
搜尋		ctrl + F
取代		ctrl + R
前往列GotoLine	ctrl + G

.svg  .webimage是用什麼軟體打開?
python之 PIL或opencv可否讀進這種檔案

matplotlib之繪圖之順序 口訣
(一般)
plot		繪製折線圖
scatter		繪製散點圖
bar、barh	繪製長條圖
hist		繪製直方圖
imshow		繪製圖像

imread	讀圖
savefig	寫圖

座標軸設定
title label xlabel ylabel
axis
xlim ylim
xticks yticks
tickparameter
legend
text grid show
cla()#清除圖表



顏色 rgbcmykw
hist參數 bbss

(進階)


tk順序
建立視窗
Button
Label
Entry
Text
MessageBox
Scale

排版 pack place grid


opencv之paste
x_st,y_st,w,h

小圖先縮放至所需大小w,h
大圖之(y_st:y_st+h, x_st:x_st+w) = 小圖之全部


基本資料型態(4)
int float bool str

DSLT
D: keys() values() items()


orientation : 直方圖方向 'vertical'(垂直, 預設), 'horizontal'(水平)





字典長度
    print(len(c))
字典鍵
    print(list(c.keys()))
字典值
    print(list(c.values()))



# 圖片大小畫素算法
# figsize=(W, H), dpi=100
# 圖片大小 W X H 英吋, 分辨率為 100 px/inch，故圖大小為 W * 100 x H * 100 px


超過兩個\n 變成兩個\n


函數的前後為兩個\n


print('------------------------------------------------------------')	#60個

串列操作
        x[0] = x[num - 1]  # 上次結束x座標成新的起點x座標
        y[0] = y[num - 1]  # 上次結束y座標成新的起點y座標
        del x[1:]  # 刪除舊串列x座標元素
        del y[1:]  # 刪除舊串列y座標元素

print('------------------------------------------------------------')	#60個


C:\_git\vcs\_1.data\______test_files3\DrAP_test6

filename1.jpg
filename2.jpg
filename3.jpg
 
ffff
  filename4.jpg
  filename5.jpg
  filename6.jpg
 


後面還有一個參數
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB), "gray")


和C一樣，python也有 位元運算子 和 位移運算子


位元運算子
&(AND)
|(OR)
~(NOT)
^(XOR)

位移運算子
<<
>>

print 之
用%參數格式化
用format函數格式化



找適合alpha疊加的範例圖片


print("------------------------------------------------------------")  # 60個


opencv目前像是不能做到動畫功能
例如

gamma 由 0:0.01:1 變化

圖片連續顯示之




C:\Program Files\ImageMagick-7.1.1-Q16-HDRI

C:\Program Files\ImageMagick-7.1.1-Q16-HDRI/magick.exe
C:\Program Files\ImageMagick-7.1.1-Q16-HDRI





使用moviepy生成视频时，提示找不到ImageMagick

安裝 ImageMagick

https://imagemagick.org/script/download.php#google_vignette

在下面的官网地址下载软件：
https://imagemagick.org/script/download.php

x86
ImageMagick-7.1.1-26-Q16-HDRI-x86-dll.exe

x64
ImageMagick-7.1.1-26-Q16-HDRI-x64-dll.exe


修改moviepy的配置文件config_defaults.py
位置在安装目录下： 
D:\python3.8\Lib\site-packages\moviepy
C:\Users\david\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\moviepy
之 config_defaults.py

FFMPEG_BINARY = os.getenv('FFMPEG_BINARY', 'ffmpeg-imageio')
#IMAGEMAGICK_BINARY = os.getenv('IMAGEMAGICK_BINARY', 'auto-detect')
IMAGEMAGICK_BINARY = r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"

最后一行设置的环境变量是auto-detect，这个在windows机器上很不靠谱，所以看结果是没有找到环境变量；
考虑收到设置地址，精准导航到指定位置；
注释掉最后一行，然后再添加一行


Python 如何安裝 PIL 

PIL(Python Imaging Library)是Python一個强大方便的影像處理函式庫。只支援到 Python 2.7。
PIL官方網站連結已失效。 

Python 3.x 安裝 Pillow

Python 安裝 Pillow 方法如下，
在命列列下使用 PIP 安裝，
$ pip install Pillow

解決
AttributeError: module 'PIL.Image' has no attribute 'ANTIALIAS'

  將
  resized_pil = pilim.resize(newsize[::-1], Image.ANTIALIAS)
  改成
  resized_pil = pilim.resize(newsize[::-1], Image.LANCZOS)



# 更新pip程式
cmd > python.exe -m pip install --upgrade pip

Python風格樣式

PEP8 是 Python 社群共通的風格指南
PEP 8風格指南

PEP是Python Enhancement Proposal的縮寫，通常翻譯為“Python增強提案”。


每個PEP都是一份為Python社群提供的指導Python往更好的方向發展的技術文件，其中的第8號增提案即PEP 8是針對Pyth


使用雙引號
行頭註解為 #空格註解
行尾註解為 空格空格#空格註解


Black是GitHub上的一個開源項目，號稱自己是“決不妥協的代碼排版器（The Uncompromising Code Formatter）”。


Python有一個官方建議的排版規范，叫做PEP 8: Style Guide for Python Code，是Python社區內排版的慣例。Black完全遵循這個規范，包括但不限于：

    使用4個空格縮進（每一級）每一行代碼長度不超過79個字符用兩行空行分隔頂層的函數和類定義等等。

Black本身是用python寫的可執行腳本。安裝非常的簡單，用pip就可以
pip install black

安裝完成之后，對想要重新排版的文件使用如下命令
black source.py


uncompromising
    KK[ʌnˋkɑmprə͵maɪzɪŋ] DJ[ˋʌnˋkɔmprəmaiziŋ] 
美式
    adj.
    不妥協的，不讓步的；堅定的
    比較級：more uncompro


pip install pytube3
pip install jupyter

pip install -r requirements.txt

requirements.txt

azure-functions
requests
pandas
pymysql
PIL==1.1.7
greenlet==0.4.5
gunicorn==19.1.1
oauthlib==0.7.2
paho-mqtt==1.0
paramiko==1.15.1
psycopg2==2.5.4
pycrypto==2.6.1
pytz==2014.9
tzlocal==1.1.2
redis==2.10.3
requests==2.4.3
requests-oauthlib==0.4.2
whitenoise==1.0.3
openpyxl==2.1.5



《幸運的基督徒》
有15個基督徒和15個非基督徒在海上遇險，為了能讓一部分人活下來不得不將其中15個人扔到海里面去，有個人想了個辦法就是大家圍成一個圈，由某個人開始從1報數，報到9的人就扔到海里面，他後面的人接著從1開始報數，報到9的人繼續扔到海里面，直到扔掉15個人。由於上帝的保佑，15個基督徒都倖免於難，問這些人最開始是怎麼站的，哪些位置是基督徒哪些位置是非基督徒。
"""






Python機器學習
1. sklearn(scikit-learn)機器學習
2. TensorFlow深度學習
3. Keras深度學習






"""
python的日期當中分成
1. date(日期)
2. time(時間)
3. datetime(混合date跟time)
4. timedelta(計算歷時期間的型態)
5. timezone(處理時區資訊的型態)

"""


名称：Black
描述：毫不妥协的 Python 代码格式化工具

black風格

引數內的等號 兩邊不用空白

前# 直接#, 一空白後寫字
後# 兩空白後一#, 一空白後寫字



檔案之中最多兩行空白

檔尾不留空白


def前後留兩行空白


print(psutil.disk_usage("硬碟 device 名稱"))  # 指定硬碟資訊 這一行有問題 black過不了
print("檔案 :", filename)  這一行有問題 black過不了
雙引號內有中文?

for-迴圈內不能打印?!?!



randint 的差別


   random.randint(st, sp)    含頭尾, 一次只能產出一個
np.random.randint(st, sp, N) 不含尾, 一次可產出N個





opencv放xml的地方
C:\Users\070601\AppData\Local\Programs\Python\Python311\Lib\site-packages\cv2\data

# 設定 Haar 分類器檔案路徑
xml_filename = r'C:\_git\vcs\_4.python\_data\haarcascade_frontalface_default.xml'


串列運算子
+	連接兩個串列元素
*	複製串列元素
=	複製串列的記憶體位址
in	判斷資料是否在串列內
not in	判斷資料是否不在串列內



Surface.blit()		重新繪製一個圖像
Surface.convert()	將Surface物件作複製, 副本可以重設像素
Surface.convert_alpha()	將Surface物件作複製, 適用於去背的圖片
Surface.fill()		以單色填滿Surface物件
Surface.get_size()	取得Surface物件的大小
Surface.get_rect()	取得Surface物件的矩形區域

pygame之畫圖
draw.line()
draw.rect()
draw.polygon()
draw.circle()
draw.ellipse()
draw.arc()



tkinter除了本身的模組外 還有兩個擴充的模組
tkinter.tix
tkinter.ttk


tkinter元件
Button		按鈕
Canvas		畫布
Checkbutton	核取方塊
Entry		單行文字標籤
Frame		框 可將元件組成群組
Label		標籤 可顯示文字或圖片
Listbox		清單方塊
Menu		選單
Menubutton	選單元件
Message		對話方塊
Radiobutton	選項按鈕
Scale		滑桿
Scrolllbar	捲軸
Text		多行文字標籤
Toplevel	建立子視窗容器




本地安裝套件

下載 XXXX.whl
pip install XXXX.whl

套件(package) : 多個模組組合在一起
套件就是一個模組庫 函式庫



#用預設程式開啟檔案
os.system('Histogram.png')  #開啟柱狀圖Histogram.png圖片




Numpy 知識
1-0 建議閱讀書籍
1-1 陣列ndarray
1-2 Numpy的資料型態
1-3 使用array( )建立一維或多維陣列
1-4 使用zeros( )建立內容是0的多維陣列
1-5 使用ones( )建立內容是1的多維陣列
1-6 使用random.rantint( )建立隨機數陣列
1-7 使用arange( )函數建立陣列數據
1-8 使用linspace( )函數建立陣列
1-9 使用reshape( )函數更改陣列形式
 



Python對正則表達式的支持

Python提供了re模塊來支持正則表達式相關操作，下面是re模塊中的核心函數。
函數 	說明
compile(pattern, flags=0) 	編譯正則表達式返回正則表達式對象
match(pattern, string, flags=0) 	用正則表達式匹配字符串 成功返回匹配對象 否則返回None
search(pattern, string, flags=0) 	搜索字符串中第一次出現正則表達式的模式 成功返回匹配對象 否則返回None
split(pattern, string, maxsplit=0, flags=0) 	用正則表達式指定的模式分隔符拆分字符串 返回列表
sub(pattern, repl, string, count=0, flags=0) 	用指定的字符串替換原字符串中與正則表達式匹配的模式 可以用count指定替換的次數
fullmatch(pattern, string, flags=0) 	match函數的完全匹配（從字符串開頭到結尾）版本
findall(pattern, string, flags=0) 	查找字符串所有與正則表達式匹配的模式 返回字符串的列表
finditer(pattern, string, flags=0) 	查找字符串所有與正則表達式匹配的模式 返回一個迭代器
purge() 	清除隱式編譯的正則表達式的緩存
re.I / re.IGNORECASE 	忽略大小寫匹配標記
re.M / re.MULTILINE 	多行匹配標記








如何撈出目前已安裝之模組與其版本?以期在另一台電腦上一次安裝

webbrowser如何增加頁箋



import sys
print('目前python程式所在位置')
print(sys.executable)


cmd / where python	//了解目前電腦安裝多少版本

cmd / python --version	//了解目前命令提示字元視窗執行Python的版本





列出所安裝的模組
    可以使用list列出所安裝的模組，如果使用’-o’可列出有新版本的模組。
pip list		# 列出安裝的模組
pip list –o    # 列出有新版本的模組  		
E-5：安裝更新版模組
未來如果有更新版，可用下列方式更新至最新版模組。
pip install -U 模組名稱			# 更新至最新版模組



刪除模組
    安裝了模組之後，若是想刪除可以使用uninstall，例如：若是想刪除basemap，可以使用下列指令。
    pip uninstall basemap






Python IDLE設定

Options/Shell_Ed/
At Start of Run(F5) 改選 No Prompt	#預設直接存檔 直接執行
勾選 Show line numbers in new windows	#加列號



避免使用
from <module_name> import *

除非沒辦法


sum_ = 0    # sum是內建函數, 不適合當作變數, 所以加上 _ 

n = int(input("請輸入整數:"))
sum_ = sum(range(n + 1))
print(f"從1到{n}的總和是 = {sum_}")


python沒有字元資料結構 字元就是長度為1的字串

python_data_type
數值 (整數浮點數)
布林
"" 字串 ""	str
{} 字典 集合	D S
[] 串列		L
() 元組		T


python預設基本函數
range
int
float
str

檔案讀寫 jieba用


# - pandas学习参考： [十分钟搞定pandas](http://www.cnblogs.com/chaosimple/p/4153083.html)

print('------------------------------------------------------------')	#60個

pip install 套件名稱

pip uninstall 想移除的套件名稱

pip show 想查詢的套件名稱


pip list


pip語法

pip uninstall keras -y
pip uninstall keras-nightly -y
pip uninstall keras-Preprocessing -y
pip uninstall keras-vis -y
pip uninstall tensorflow -y
pip uninstall h5py -y

pip install tensorflow==1.13.1
pip install keras==2.0.8
pip install h5py==2.10.0


更新套件
pip install yfinance -U


標準list  由list組成的list

鼠牛虎兔龍蛇 馬羊猴雞狗豬
r g b k w y m c  

animals = {'鼠' : ('mouse', 3),
           '牛' : ('ox', 48),
           '虎' : ('tiger', 33),
           '兔' : ('rabbit', 8),
           '龍' : ('dragon', 38),
           '蛇' : ('snake', 16),
           '馬' : ('horse', 31),
           '羊' : ('goat', 29),
           '猴' : ('monkey', 22),
           '雞' : ('chicken', 5),
           '狗' : ('dog', 17),
           '豬' : ('pig', 42),
           }

animals = {'鼠' : 3, '牛' : 48, '虎' : 33, '兔' : 8, '龍' : 38}


'米老鼠',
'班尼牛',
'跳跳虎',
'彼得兔',
'豆豆龍',
'貪吃蛇',
'草泥馬',
'喜羊羊',
'山道猴',
'肯德雞',
'貴賓狗',
'佩佩豬'
中文名	英文名	體重	代表人物
鼠	mouse	3	米老鼠
牛	ox	48	班尼牛
虎	tiger	33	跳跳虎
兔	rabbit	8	彼得兔
龍	dragon	38	豆豆龍
蛇	snake	16	貪吃蛇
馬	horse	31	草泥馬
羊	goat	29	喜羊羊
猴	monkey	22	山道猴
雞	chicken	5	肯德雞
狗	dog	17	貴賓狗
豬	pig	42	佩佩豬

針對無法連線到官方直接使用MNIST資料集的用戶，可以根據下面步驟執行MNIST Demo

可以使用先從PC上下載MNIST資料集
https://s3.amazonaws.com/img-datasets/mnist.npz



''' & '''  可執行的 但不執行的

""" & """ 放不能執行的

這樣才可做到用 ''' 包圍 """, 可以簡易地跳過不要執行的程式


需先行下載
yolo.h5
https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5

resnet50_imagenet_tf.2.0.h5
https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/resnet50_imagenet_tf.2.0.h5


cur_path = os.path.dirname(__file__) # 取得目前路徑



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


'''
暫存資料 全

'''

----------------常用的程式片段 ST cccc----------------

foldername = 'C:/_git/vcs/_1.data/______test_files5'

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/SpongeBob.gif'

video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_word/python_docx1.docx'
filename = 'C:/_git/vcs/_1.data/______test_files2/output.avi'

filename1 = 'C:/_git/vcs/_4.python/_data/elephant.jpg'
filename2 = 'C:/_git/vcs/_4.python/_data/tiger.jpg'
filename3 = 'C:/_git/vcs/_4.python/_data/bear.jpg'

filenames = [filename1, filename2, filename3]

for filename in filenames:
    print(filename)

print('------------------------------------------------------------')	#60個

import datetime
now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print("現在時間 :", now)

print('-' * 60)	#60個

filename = 'C:/_git/vcs/_1.data/______test_files2/AQI_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.csv'
filename = 'Image_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.jpg'

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei	微軟正黑體
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

plt.show()  #將圖表呈現出來

plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  #也可設mingliu或DFKai-SB

'''
#import ast
import json
data = dict()
with open('data\password.txt','r', encoding = 'UTF-8-sig') as f:
   filedata = f.read()
   print(filedata)
#   filedata = filedata.replace("\'", "\"")
#   data = ast.literal_eval(filedata)
   data = json.loads(filedata)

print(type(data),data)

'''

格式化列印語法    
print("{}已被儲存完畢".format(sys.argv[1]))
score = int(input('請輸入第{}號的成績:(-1結束)'.format(no)))

    person1={"name":"Amy","phone":"049-1234567","age":20}
    person2={"name":"Jack","phone":"02-4455666","age":25}
    person3={"name":"Nacy","phone":"04-9876543","age":17}
    persons=[person1,person2,person3]


def submit():
    username = request.values['username']
    password = request.values['password']
    if username=='david' and password=='1234':
        return '歡迎光臨本網站！'
    else:
        return '帳號或密碼錯誤！'

#!/usr/bin/python
# -*- coding: UTF-8 -*-    #告訴Python直譯器檔案編碼為UTF-8


for p in photos:
        image = p['images'][0]
        filename = image['source'].split('/')[-1].split('?')[0]
        print(filename)
        fp = open('fb-images/'+filename, 'wb')
        pic = requests.get(image['source'], stream=True)
        shutil.copyfileobj(pic.raw, fp)
        fp.close()
	

print("有無錢號的差異")
print("無錢號 : " + "cos(x^2)")
print("有錢號 : " + "$cos(x^2)$")

print("------------------------------------------------------------")  # 60個
response = requests.post(xxxx)
result = response.json()
print(result[0]['translations'][0]['text'])
print(result)	#列印結果


fig = plt.figure()

x_st = 0.15
y_st = 0.60
w = 0.7
h = 0.3
pic1 = fig.add_axes([x_st, y_st, w, h])

pic1.set_ylabel('Voltage [V]')
pic1.set_title('A sine wave')



data = sp.find_all('span', {'id':'Showtd'})
rows = data[0].find_all('tr')



給class用
print("Python %s on %s\n%s\n(%s)\n" %
	(sys.version, sys.platform, cprt,
	self.__class__.__name__))



Firebase 專案是應用程式的容器

檢查key
def CkeckKey(no):
    key_id=""
    if datas != None:
        for key in datas:
            if no==datas[key]["no"]: # 找到鍵名稱
                key_id = key
                break
    return key_id


plt有此語法否?
plt.gcf().set_size_inches(12, 14)


    apiURL='%s/update?api_key=%s&field1=%s' %(host, api_key, value) 
    print(apiURL)

  
apiURL='%s/channels/%s/feeds.json?api_key=%s&results=%d' %(host,ChannelID, api_key,records) 
print(apiURL)

print("------------------------------------------------------------")  # 60個

sys.stdout = sys.stderr
print('usage: findlinksto pattern directory ...')

print("------------------------------------------------------------")  # 60個

#另存新檔
filename2 = 'C:/_git/vcs/_1.data/______test_files2/human_face.jpg'
cv2.imwrite(filename2, image)	#寫入本機圖片

cv2.imwrite("face_detection.jpg", image)

cv2.imwrite('7.jpg', image)

print("------------------------------------------------------------")  # 60個
sys.exit(main(sys.argv[1:], sys.stdout))

sys.stderr.write('%s: %s\n%s' % (sys.argv[0], msg, usage))
sys.stderr.write("%s: %s\n" % (sys.argv[0], msg))


print("%s:%d:%s" % (filename, row, line), end = '')


//xil_printf("david0217: %s:%s(%d) ST setup g_exposure = %d\r\n",__FILE__,__func__,__LINE__, g_exposure);

david1031: ../src/vid_io_intf.c:vid_io_intf_init(279) FMC IMAGEON card not exist

字串的用法
split replace
            lang, encoding = locale.split('.')[:2]
            encoding = encoding.replace('-', '')
            encoding = encoding.replace('_', '')
    if test_func_name.startswith("test_"):

print("------------------------------------------------------------")  # 60個

自定義版本 資料

__version__ = "1.1"

__author__ = 'Raymond Hettinger'

print("msgfmt.py", __version__)


print('msgid_plural not preceded by msgid on %s:%d' % (infile, lno), file=sys.stderr)
print('plural without msgid_plural on %s:%d' % (infile, lno), file=sys.stderr)
print('ERROR: %a -> %a != %a' % (k, locale.normalize(k), v), file=sys.stderr)

print('    %-40s%a,' % ('%a:' % k, v))
print('#    removed %a' % k)
print('#    updated %a -> %a to %a' % (k, olddata[k], data[k]))


print("------------------------------------------------------------")  # 60個

print(__doc__ % globals())

print("-"*70)

print("------------------------------------------------------------")  # 60個def chop(line):
    if line.endswith("\n"):
        return line[:-1]
    else:
        return line


def parse(filename):

    with open(filename, encoding='latin1') as f:
        lines = list(f)
    data = {}
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line[:1] == '#':
            continue
        locale, alias = line.split()
        
        # Fix non-standard locale names, e.g. ks_IN@devanagari.UTF-8
        if '@' in alias:
            alias_lang, _, alias_mod = alias.partition('@')
            if '.' in alias_mod:
                alias_mod, _, alias_enc = alias_mod.partition('.')
                alias = alias_lang + '.' + alias_enc + '@' + alias_mod
    return data

def parse_glibc_supported(filename):

    with open(filename, encoding='latin1') as f:
        lines = list(f)
    data = {}
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line[:1] == '#':
            continue
        line = line.replace('/', ' ').strip()
        line = line.rstrip('\\').rstrip()
        words = line.split()
        if len(words) != 2:
            continue

print("------------------------------------------------------------")  # 60個
bind的用法：控件.bind(event, handler),其中event是tkinter已經定義好的的事件，handler是處理器，可以是一個處理函數，如果相關事件發生, handler 函數會被觸發, 事件對象 event 會傳遞給 handler 函數
基本所有控件都能bind

常見event有：

鼠標單擊事件：
鼠標左鍵點擊為 <Button-1>,
鼠標中鍵點擊為 <Button-2>,
鼠標右鍵點擊為 <Button-3>,
向上滾動滑輪為 <Button-4>,
向下滾動滑輪為 <Button-5>.

鼠標雙擊事件.：
鼠標左鍵點擊為 <Double-Button-1>,
鼠標中鍵點擊為 <Double-Button-2>,
鼠標右鍵點擊為 <Double-Button-3>.

鼠標釋放事件：
鼠標左鍵點擊為 <ButtonRelease-1>,
鼠標中鍵點擊為 <ButtonRelease-2>,
鼠標右鍵點擊為 <ButtonRelease-3>.
鼠標相對當前控件的位置會被存儲在 event 對象中的 x 和 y 字段中傳遞給回調函數.

鼠標移入控件事件：<Enter>

獲得焦點事件：<FocusIn>

鼠標移出控件事件: <Leave>

失去焦點事件:<FocusOut>

鼠標按下移動事件：
鼠標左鍵點擊為 <B1-Motion>,
鼠標中鍵點擊為 <B2-Motion>,
鼠標右鍵點擊為 <B3-Motion>.
鼠標相對當前控件的位置會被存儲在 event 對象中的 x 和 y 字段中傳遞給回調函數.

鍵盤按下事件:<Key>，event中的keysym ,keycode,char都可以獲取按下的鍵【其他想要獲取值的也可以先看看event中有什么】
鍵位綁定事件：<Return>回車鍵，<BackSpace>,<Escape>,<Left>,<Up>,<Right>,<Down>…….
控件大小改變事件：<Configure>，新的控件大小會存儲在 event 對象中的 width 和 height 屬性傳遞. 有些平臺上該事件也可能代表控件位置改變.


    Event中的屬性：
        widget：產生事件的控件
        x, y：當前鼠標的位置
        x_root, y_root：當前鼠標相對于屏幕左上角的位置，以像素為單位。
        char：字符代碼（僅限鍵盤事件），作為字符串。
        keysym：關鍵符號（僅限鍵盤事件）。
        keycode：關鍵代碼（僅限鍵盤事件）。
        num：按鈕號碼（僅限鼠標按鈕事件）。
        width, height：小部件的新大小（以像素為單位）（僅限配置事件）。
        type：事件類型。




print("------------------------------------------------------------")  # 60個

 
#width 選項的單位是文字單位，而不是畫素

字串處理

#url = input("請輸入網址：")
url = 'https://www.google.com.tw/'
if url.startswith("http://") or url.startswith("https://"):
    print("輸入的網址格式正確！")
else:
    print("輸入的網址格式錯誤！")



#熊貓是python的excel

print("------------------------------------------------------------")  # 60個
啟用一個測試用的本地端伺服器
python -m http.server -d www

瀏覽器輸入
localhost:8000
就可以看到www資料夾下的檔案列表

DOM	Document Object Model



def make_backup(filename):
    import os, os.path
    backup = filename + '~'
    if os.path.lexists(backup):
        try:
            os.remove(backup)
        except OSError:
            print("Can't remove backup %r" % (backup,), file=sys.stderr)
        # end try
    # end if
    try:
        os.rename(filename, backup)
    except OSError:
        print("Can't rename %r to %r" % (filename, backup), file=sys.stderr)
    # end try
# end def make_backup



    fp = open(substfile, 'r')
    lineno = 0
    while 1:
        line = fp.readline()
        if not line: break
        lineno = lineno + 1
        try:
            i = line.index('#')
        except ValueError:
            i = -1          # Happens to delete trailing \n
        words = line[:i].split()
        if not words: continue
        if len(words) == 3 and words[0] == 'struct':
            words[:2] = [words[0] + ' ' + words[1]]
        elif len(words) != 2:
            err(substfile + '%s:%r: warning: bad line: %r' % (substfile, lineno, line))
            continue
        if Reverse:
            [value, key] = words
        else:
            [key, value] = words
        if value[0] == '*':
            value = value[1:]
        if key[0] == '*':
            key = key[1:]
            NotInComment[key] = value
        if key in Dict:
            err('%s:%r: warning: overriding: %r %r\n' % (substfile, lineno, key, value))
            err('%s:%r: warning: previous: %r\n' % (substfile, lineno, Dict[key]))
    fp.close()






        os.rename(filename, filename + '~')


    print("%d objects before, %d after" % (before, after))


    if os.path.isdir(file) and not os.path.islink(file):
        
        print("checking", file, "...", end=' ')
            print("%r lines %d-%d" % (file, s+1, e+1))
            if os.path.exists(bak):
                os.remove(bak)
            os.rename(file, bak)



            outfile = os.path.basename(filename)


def usage():
    sys.stderr.write(__doc__ % globals())

sys.stderr.write(msg)


print("------------------------------------------------------------")  # 60個

IFTTT	IF This Then That
網路自動連結工具

import PySimpleGUI as sg
import shutil
import os
import sys

layout = [[sg.Text('PyInstaller EXE Creator', font='Any 15')],
              [sg.Text('Source Python File'), sg.Input(key='-sourcefile-', size=(45, 1)),
               sg.FileBrowse(file_types=(("Python Files", "*.py"),))],
              [sg.Text('Icon File'), sg.Input(key='-iconfile-', size=(45, 1)),
               sg.FileBrowse(file_types=(("Icon Files", "*.ico"),))],
              [sg.Frame('Output', font='Any 15', layout=[
                        [sg.Output(size=(65, 15), font='Courier 10')]])],
              [sg.Button('Make EXE', bind_return_key=True),
               sg.Button('Quit', button_color=('white', 'firebrick3')) ],
              [sg.Text('Made with PySimpleGUI (www.PySimpleGUI.org)', auto_size_text=True, font='Courier 8')]]

window = sg.Window('PySimpleGUI EXE Maker', layout, auto_size_text=False, auto_size_buttons=False, default_element_size=(20,1), text_justification='right')



print("------------------------------------------------------------")  # 60個

@app.route('/user/<username>')
def show_user(username):
    return 'User Name is {}'.format(username)

if __name__ == '__main__':
    app.run()

encoding = 'utf-8-sig'	編碼設定為將BOM去除的的utf-8編碼

https://pythex.org/

print("------------------------------------------------------------")  # 60個
    simpleaudio：播放WAV文件和NumPy數組。
    winsound：播放WAV文件或鳴響您的系統揚聲器
    https://docs.python.org/3/library/winsound.html

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
OCR 破解驗證碼

因為驗證碼通常會有很多噪點，
我上網引用了大大寫好的降噪副程式，
先將驗證碼降噪後再進行 OCR 辨識，
會大大的提高成功率。

https://stackoverflow.max-everyday.com/2019/06/python-opencv-denoising/

print("------------------------------------------------------------")  # 60個

Python 以模組名稱 __name__ 分辨程式執行模式


print("------------------------------------------------------------")  # 60個
MapKeyboard 重設鍵盤按鍵功能、讓指定按鍵失效！（remap鍵盤、停用按鍵）
https://123.briian.com/forum.php?mod=viewthread&tid=3668
MapKeyboard v1.5 停用鍵盤按鍵、將按鍵指定其他功能 REMAP
https://123.briian.com/forum.php?mod=viewthread&tid=3668

reg add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve

on-line compiler
https://www.tutorialspoint.com/execute_python_online.php
https://www.tutorialspoint.com/codingground.htm

time
https://tw.piliapp.com/time-now/tw/taipei/+

同步不同台電腦的python套件之phthon程式

需安裝之套件做成一個list

檢查本機電腦是否有安裝此套件
若無 則安裝之

print("------------------------------------------------------------")  # 60個

http://the.earth.li/~sgtatham/putty/latest/x86/putty.exe

GET
將資料全部寫在URL中，就像你寫明信片一樣，傳遞上較不安全。

GET加上參數的格式：https://www.example.com/index.html?key1=value1&key2=value2

POST
將資料寫在內部，就像你寫信然後裝進信封袋一樣，傳遞上比較安全且傳遞的資訊可以比較多。

from machine import Pin, PWM

pitches = {
    'C':261, # D0
    'D':294, # Re
    'E':329, # Mi
    'F':349, # Fa
    'G':392, # So
    'A':440, # La
    'B':493, # Si
    'S':0    # Stop
}

music = (
    ('C',1),('C',1),('G',1),('G',1),('A',1),('A',1),('G',2),
    ('F',1),('F',1),('E',1),('E',1),('D',1),('D',1),('C',2),
    ('G',1),('G',1),('F',1),('F',1),('E',1),('E',1),('D',2),
    ('G',1),('G',1),('F',1),('F',1),('E',1),('E',1),('D',2),
    ('C',1),('C',1),('G',1),('G',1),('A',1),('A',1),('G',2),
    ('F',1),('F',1),('E',1),('E',1),('D',1),('D',1),('C',1)
)

speed=400 # 設定節拍速度
period=10 # 設定每拍停頓時間

buzzer = PWM(Pin(14, Pin.OUT), duty=1000) # D5
try:
    for tone,tempo in music:
        if (tone=="S"):
            buzzer.duty(0) # 靜音
        else:
            buzzer.duty(1000)
            buzzer.freq(pitches[tone])
        time.sleep_ms(tempo*speed)
        print(pitches[tone])
        #以靜音設定每拍間稍為停頓
        buzzer.duty(0)         # 靜音
        time.sleep_ms(period)  # 停頓時間
    buzzer.deinit()
except:  # CTRL + C 中斷
    buzzer.deinit()       


//print("------------------------------------------------------------")  # 60個


----------------import os 大集合----------------




----------------import time 大集合----------------


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

        print("%s:" % func.__name__.replace("pi_", ""))
        print("result: %s" % str(x))

print("------------------------------------------------------------")  # 60個


                "client001": {
                    "fee": 1000.0,
                    "expiration_date": datetime(2020, 1, 3),
            {"fee": 1000.0, "expiration_date": datetime(2020, 1, 3)},
            "client001", expiration_date=datetime(2020, 1, 4)
            {"fee": 1000.0, "expiration_date": datetime(2020, 1, 4)},

                    "expiration_date": datetime(2020, 1, 3),
            {"fee": 1000.0, "expiration_date": datetime(2020, 1, 3)},
            "client001", expiration_date=datetime(2020, 1, 4)
            {"fee": 1000.0, "expiration_date": datetime(2020, 1, 4)},

print("------------------------------------------------------------")  # 60個
#攔截ctrl-C
import math, time, sys, os

LINE_CHAR = chr(9608)  # Character 9608 is a solid block.
print(LINE_CHAR, end='', flush=False)


try:
    while True:

        print('Press Ctrl-C to quit.', end='', flush=True)

        print('a')

        time.sleep(1)  # Pause for a bit.

        # Clear the screen:
        if sys.platform == 'win32':
            os.system('cls')  # Windows uses the cls command.
        else:
            os.system('clear')  # macOS and Linux use the clear command.

except KeyboardInterrupt:
    print('Rotating Cube, by Al Sweigart al@inventwithpython.com')
    sys.exit()  # When Ctrl-C is pressed, end the program.



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個





----------------print 大集合 pppp----------------



title = "Ming-Chi Institute of Technology"
print(f"/{title.center(50)}/")
dt = "Department of ME"
print(f"/{dt.ljust(50)}/")
site = "JK Hung"
print(f"/{site.rjust(50)}/")
print(f"/{title.zfill(50)}/")



----------------字串處理 大集合----------------


return fullpath.endswith(".py") or fullpath.endswith(".pyw")




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

            f = open(path)
        while True:
            line = f.readline()
            if line.startswith("END"):
                break

            L = int(line.split()[1])
            key = f.read(L)
            result.append(key)
            f.readline()
            line = f.readline()
            assert line.startswith("V ")
            L = int(line.split()[1])
            value = f.read(L)
            f.readline()
        f.close()


print()

for i in range(30):
    print("webpage{}.png".format(i))

f.write("    '%s':\t%s,  \t# %s\n" % (name,charcode,comment))
f.write('\n}\n')

print("------------------------------------------------------------")  # 60個

				發送e-mail
				
				import requests
				
				def send_simple_message():
				    return requests.post(
				        "https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
				        auth=("api", "key-558f*******3227e7"),
				        data={"from": "Excited User <skynet.tw@gmail.com>",
				              "to": ["minhuang@nkust.edu.tw"],
				              "subject": "Test mail from mailgun",
				              "text": "這是一個測試郵件"})
				
				send_simple_message()

大專院校校別學生數 CSV格式
https://data.gov.tw/dataset/6231


農產品交易行情 CSV JSON XML格式
https://data.gov.tw/dataset/8066


首頁-行政院農業委員會資料開放平台
https://data.coa.gov.tw/
https://data.coa.gov.tw/index.aspx


高科大焦點新聞網頁
https://ccet.nkust.edu.tw/p/403-1135-1046-1.php



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("姓名   座號  國文  數學  英文")
print("%3s  %2d   %3d   %3d  %3d" % ("林大明", 1, 100, 87, 79))
print("%3s  %2d   %3d   %3d  %3d" % ("陳阿中", 2, 74, 88, 100))
print("%3s  %2d   %3d   %3d  %3d" % ("張小英", 11, 82, 65, 8))

score = [85, 79, 93]
print("國文成績：%d 分" % score[0])
print("數學成績：%d 分" % score[1])
print("英文成績：%d 分" % score[2])

print("------------------------------------------------------------")  # 60個

print("The pysource module is not le search will be done.", file=sys.stderr)

print("------------------------------------------------------------")  # 60個

https://www.dreamstime.com/free-images_pg1

https://www.dreamstime.com/free-images_pg1

print("------------------------------------------------------------")  # 60個

content='''Hello Python
中文字測試
Welcome
'''

f=open('file1aaa.txt','w')
f.write(content)
f.close()

print("------------------------------------------------------------")  # 60個

from urllib.parse import urlparse

print('用 urlparse 解析一個網址')

url = 'http://taqm.epa.gov.tw:80/pm25/tw/PM25A.aspx?area=1'
up = urlparse(url)
print(up) 

print("scheme={}".format(up.scheme)) # http
print("netloc={}".format(up.netloc)) # taqm.epa.gov.tw
print("port={}".format(up.port))     # 80
print("path={}".format(up.path))     # /pm25/tw/PM25A.aspx
print("query={}".format(up.query))   # area=1

print("------------------------------------------------------------")  # 60個

import requests,json

url="https://graph.facebook.com/v3.2/me/posts?fields=message%2Ccreated_time&until=2016-09-01&since=2016-01-01&access_token=EAADAqsBw2wsBAL9vAlc8YZBZBpIClS2c0xBs0CdCOK1wZBW8lZCISy2CY2qUyG6waEYTNQhSZB45zb5ky8B9mk4SdZC8qZBUUdHmJnpB1q7owbmOt0mIC0SGhAHBFEZBZAMqRvvTFfJcWSvkKjXiP3l9qZCrlPyadqO6JUYDpsTmEtPR59CtR9upr0HdHesJIEMLlCNg0xP5c04AZDZD"
data = json.loads(requests.get(url).text) # 讀取資料並轉成 json 

for d in data['data']: # 讀取 Key 名稱為 data 的定典資料 
    if 'message' in d: # 確認 message 存在
        print("message:{}".format(d['message']))
        print("created_time:{}".format(d['created_time']))
        print("id:{}".format(d['id']))
        print()
        

print("{0:<15s}{1:<15s}{2:<15s}{3:<15s}".format(
    "ASCII Code", "Character", "Frequency", "Code"))  
    
for i in range(10):
    print("{0:<15d}{1:<15s}{2:<15d}{3:<15s}".format(i, chr(i), 123, 'abc'))
 

MAXIMUM_CAPACITY = 2 ** 30 


'''
text = open('result.txt').read().strip()
print("驗證碼為 " + text)
'''
print("------------------------------------------------------------")  # 60個


        def print_three_column(lst):
            lst.sort(key=str.lower)
            # guarantee zip() doesn't drop anything
            while len(lst) % 3:
                lst.append("")
            for e, f, g in zip(lst[::3], lst[1::3], lst[2::3]):
                print("%-*s   %-*s   %-*s" % (longest, e, longest, f,
                                              longest, g))


            assert not self.inplace
            basename, tail = os.path.splitext(ext_filename)
            newname = basename + "_failed" + tail
            if os.path.exists(newname):
                os.remove(newname)
            os.rename(ext_filename, newname)


        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)
        ret = os.system(
            '%s -print-multiarch > %s 2> /dev/null' % (cc, tmpfile))

        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)
        ret = os.system(
            'dpkg-architecture %s -qDEB_HOST_MULTIARCH > %s 2> /dev/null' %
            (opt, tmpfile))

        ret = os.system('%s -E -v - </dev/null 2>%s 1>/dev/null' % (gcc, tmpfile))
        

            cmd = ("echo '' | %s -Wextra -Wno-missing-field-initializers -E - "
                   "> /dev/null 2>&1" % cc)
            ret = os.system(cmd)
            if ret >> 8 == 0:
                extra_compile_args.extend(['-Wextra',
                                           '-Wno-missing-field-initializers'])


                cmd = "cd %s && env CFLAGS='' '%s/configure' %s" \
                      % (ffi_builddir, ffi_srcdir, " ".join(config_args))

                res = os.system(cmd)
                if res or not os.path.exists(ffi_configfile):
                    print("Failed to configure _ctypes module")
                    return False

print("------------------------------------------------------------")  # 60個

HTML之註解
<!--
程式名稱：artwebsite.jsp
說明：美工網頁
開發者：chmei
開發日期：2013.12.22
修改者：syyu
修改日期：2016.9.5
版本：ver2.0
-->

webbrowser做讀取local_html_file

print('----------------------------------------------------------------------')	#70個

http://data.ntpc.gov.tw/od/data/api

text() 在Axes物件的任意位置增加文字

網站網頁

https://rate.bot.com.tw/
https://rate.bot.com.tw/xrt?Lang=zh-TW


(台銀牌告匯率)
https://rate.bot.com.tw/xrt?Lang=zh-TW


分析網頁原始碼:按滑鼠右鍵，點選檢視網頁原始碼按鈕


import requests
#帳號密碼登入
r = requests.get('https://irs.zuvio.com.tw/irs/login', auth=('jykuo@ntut.edu.tw', '????'))
print(r.status_code)
print(r.text)

import requests
#帳號密碼登入
r = requests.get('http://bbs-mychat.com/login.php', auth=('bunshue', 'jp6rmp4'))
print(r.status_code)
print(r.text)



import requests
# 資料
my_data = {'key1': 'value1', 'key2': 'value2'}
# 將資料加入POST 請求中
r = requests.post('http://httpbin.org/post', data = my_data)
print(r.text)
# 要上傳的檔案
my_files = {'my_filename': open('A.py', 'rb')}
# 將檔案加入POST 請求中
r = requests.post('http://httpbin.org/post', files = my_files)
print(r.status_code)


https://user.gamer.com.tw/login.php


不知道甚麼時候會用到
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(ChromeDriverManager().install())


from webdriver_manager.chrome import ChromeDriverManager
# Chromeの起動
driver =webdriver.Chrome(ChromeDriverManager().install())





http://the.earth.li/~sgtatham/putty/latest/x86/putty.exe



x=[4 3 9 -7 1 2 0 0]';
y=fft(x);


clear
t=0:1/50:6.28;
x=sin(2*pi*15*t);
y=fft(x);
m=abs(y);
%p=unwrap(angle(y));
f=(0:length(y)-1)'*50/length(y);
figure(1);plot(t,x),ylabel('Sin(x)'),grid on
figure(2);plot(f,m),ylabel('Abs.'),grid on
%figure(3);plot(f,p*180/pi),ylabel('Phase'),grid on


                        
'''
# 題問說明
question_description = "[1]牡羊座 [2]金牛座 [3]雙子座 [4]巨蟹座 [5]獅子座 [6]處女座 [7]天秤座 [8]天蠍座 [9]射手座 [10]摩羯座 [11]水瓶座 [12]雙魚座，請選擇星座(僅能填數字):"

# 限制填寫內容為數字
while True:
    ans_data = input(question_description)
    # ans_data為數字且數值介於1~12
    if ans_data.isdigit() == True and int(ans_data) > 0 and int(ans_data) < 13:
        break
    else:
        pass
'''


url = 'https://oldsiao.neocities.org/'

html_data = get_html_data1(url)
if html_data == None:
    print('無法取得網頁資料')
    sys.exit(1)	#立刻退出程式

html_data.encoding = 'UTF-8'    # 設定讀取編碼(預設 UTF-8)
soup = BeautifulSoup(html_data.text, 'html.parser')

print("使用 BeautifulSoup 分析網頁")
print("取得網頁標題", soup.title)
print("取得網頁標題", soup.title.text)

                       
                        

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

io與print + 1 * / ** int string length type 

if-else-for-while

function

tk做一個公版的離開按鈕
tk之button如何做到Enable = false?

for語法
    for rcs_dir in ('.svn', '.git', '.hg', 'build'):
        print('取得特定資料夾:', rcs_dir)

def pathdirs():
    """Convert sys.path into a list of absolute, existing, unique paths."""
    dirs = []
    normdirs = []
    for dir in sys.path:
        dir = os.path.abspath(dir or '.')
        normdir = os.path.normcase(dir)
        if normdir not in normdirs and os.path.isdir(dir):
            dirs.append(dir)
            normdirs.append(normdir)
    return dirs
    
print("------------------------------------------------------------")  # 60個    
系統參數
sys.path:
        scriptdir = os.path.dirname(sys.argv[0])
        if scriptdir in sys.path:
            sys.path.remove(scriptdir)
        sys.path.insert(0, '.')

def cli():
    """Command-line interface (looks at sys.argv to decide what to do)."""
    import getopt
    class BadUsage(Exception): pass

    # Scripts don't get the current directory in their path by default
    # unless they are run with the '-m' switch
    if '' not in sys.path:
        scriptdir = os.path.dirname(sys.argv[0])
        if scriptdir in sys.path:
            sys.path.remove(scriptdir)
        sys.path.insert(0, '.')


print("------------------------------------------------------------")  # 60個

    n = read_uint4(f)
    assert n >= 0
    if n > sys.maxsize:
        raise ValueError("unicodestring4 byte count > sys.maxsize: %d" % n)


    def _dbg(self, level, msg):
        """Write debugging output to sys.stderr.
        """
        if level <= self.debug:
            print(msg, file=sys.stderr)

        # default setting for prog
        if prog is None:
            prog = _os.path.basename(_sys.argv[0])

print("------------------------------------------------------------")  # 60個

if 'strxfrm' not in globals():

    import os
    lookup = os.environ.get
    for variable in envvars:
        localename = lookup(variable,None)
        if localename:
            if variable == 'LANGUAGE':
                localename = localename.split(':')[0]
            break



    outdir = os.path.join(WORKDIR, 'diskimage')
    if os.path.exists(outdir):
        shutil.rmtree(outdir)


要能夠讓自定義的函數放在固定資料夾  讓.py去引用


修改檔案的內容

    if not os.path.isfile(m32):
        return
    with open(m32) as fin:
        with open(makefile, 'w') as fout:
            for line in fin:
                line = line.replace("=tmp32", "=tmp64")
                line = line.replace("=out32", "=out64")
                line = line.replace("=inc32", "=inc64")
                # force 64 bit machine
                line = line.replace("MKLIB=lib", "MKLIB=lib /MACHINE:X64")
                line = line.replace("LFLAGS=", "LFLAGS=/MACHINE:X64 ")
                # don't link against the lib on 64bit systems
                line = line.replace("bufferoverflowu.lib", "")
                fout.write(line)
    os.unlink(m32)

print("------------------------------------------------------------")  # 60個

SQLite 和 Python 資料型別

None     <->     NULL
int      <->     INTEGER/INT
float    <->     REAL/FLOAT
str      <->     TEXT/VARCHAR(n)
bytes    <->     BLOB
                
                
print("------------------------------------------------------------")  # 60個

ord函數		給一個Unicode字符，返回該字符的Unicode數字代碼

例如，給定ord('a') 返回整數 97，ord('\u2020') 返回 8224。同chr相反。

print("------------------------------------------------------------")  # 60個

if __name__ == '__main__':
    if len(sys.argv) == 1:
        _print_tokens(shlex())
    else:
        fn = sys.argv[1]
        with open(fn) as f:
            _print_tokens(shlex(f, fn))

    print("%d: %s[%d]%s %s" % (lineno(), filename(), filelineno(),
                                   isfirstline() and "*" or "", line))
print("%d: %s[%d]" % (lineno(), filename(), filelineno()))

    d = {}

        self.con = sqlite.connect(":memory:")
        self.con.execute("create table test (value text)")
        self.con.execute("insert into test (value) values (?)", ("a\x00b",))

       row = self.con.execute("select value from test").fetchone()
        cur.execute("select 4+5 as foo")
        row = cur.fetchone()

        austria = "Österreich"
        germany = "Deutchland"
        a_row = self.con.execute("select ?", (austria,)).fetchone()
        d_row = self.con.execute("select ?", (germany,)).fetchone()
        
print("------------------------------------------------------------")  # 60個
            print("The latest version of {} on PyPI is {}, but ensurepip "
                  "has {}".format(project, upstream_version, version))

        sys.stderr.write("can't stat %r: %r\n" % (filename, msg))

print("------------------------------------------------------------")  # 60個
def usage(msg):
    sys.stderr.write("%s: %s\n" % (sys.argv[0], msg))
    sys.stderr.write("Usage: %s [-l] file ...\n" % sys.argv[0])
    sys.stderr.write("Try `%s -h' for more information.\n" % sys.argv[0])

                print("%s:%d:%s" % (filename, row, line), end=' ')

    list = []
        list.append((tsub, key))
    list.sort()
    list.reverse()
    width = len(repr(list[0][0]))


print("------------------------------------------------------------")  # 60個
import sys

print('format語法 字串填空')

print('直接打印字串Unknown benchmark: {}'.format('zzzzzzzz', file=sys.stderr))
print('保留單引號Unknown benchmark: {!r}'.format('zzzzzzzz', file=sys.stderr))

seconds = 1
seconds_plural = 's' if seconds > 1 else ''
repeat = 3
pattern = ('這個字串要填入資料 第一筆 {}, 第二筆 {}, 第三筆 {}\n'
          '第四筆 {}\n'
          '第五筆 {!r}\n')

print(pattern.format(3, 8, 3, 4, 'dddd'))


sys.stdout.flush()


print "%s.%s unknown bits %x" % (self.name, name, unk)
                print "%s.%sunknown integer type %d" % (self.name, name, size)
        return "CREATE TABLE %s (%s PRIMARY KEY %s)" % (self.name, fields, keys)

    v = db.OpenView("INSERT INTO _Streams (Name, Data) VALUES ('%s', ?)" % name)



_directories = sets.Set()
        while logical in _directories:
            logical = "%s%d" % (_logical, index)
            index += 1
        _directories.add(logical)

print("------------------------------------------------------------")  # 60個
import sys

prog = sys.argv[0]

sys.stderr.write("Unable to open %s.  " % 'aaaaa')
sys.stderr.write("Check for format or version mismatch.\n")

    def touch_pymods(self):
        # force a rebuild of all modules that use OpenSSL APIs
        for fname in self.module_files:
            os.utime(fname)


print("------------------------------------------------------------")  # 60個
def usage(code, msg=''):
    print(__doc__ % globals(), file=sys.stderr)
    if msg:
        print(msg, file=sys.stderr)
    sys.exit(code)


            print(_(
                '*** %(file)s:%(lineno)s: Seen unexpected token "%(token)s"'
                ) % {
                'token': tstring,
                'file': self.__curfile,
                'lineno': self.__lineno
                }, file=sys.stderr)



                        print(_(
                            '# File: %(filename)s, line: %(lineno)d') % d, file=fp)

print("------------------------------------------------------------")  # 60個
            print(_(
                "Can't read --exclude-file: %s") % options.excludefilename, file=sys.stderr)

            fp = sys.stdin.buffer

                print('%s: %s, line %d, column %d' % (
                    e.args[0], filename, e.args[1][0], e.args[1][1]),
                    file=sys.stderr)

        print(msg, file=sys.stderr)

print("------------------------------------------------------------")  # 60個

print('No input file given', file=sys.stderr)
print("Try `msgfmt --help' for more information.", file=sys.stderr)


def pprint(data):
    items = sorted(data.items())
    for k, v in items:
        print('    %-40s%a,' % ('%a:' % k, v))

def print_differences(data, olddata):
    items = sorted(olddata.items())
    for k, v in items:
        if k not in data:
            print('#    removed %a' % k)
        elif olddata[k] != data[k]:
            print('#    updated %a -> %a to %a' % \
                  (k, olddata[k], data[k]))
        # Additions are not mentioned

print("------------------------------------------------------------")  # 60個


---- sys.version ------------------------------------------------------------

import sys
print(sys.version)


py3 = sys.version_info >= (3, 0)


print("------------------------------------------------------------")  # 60個
    print("Python %s" % sys.version)
    if sys.version_info < (3, 3):
        xxxx
    else:
    xxxx


print("------------------------------------------------------------")  # 60個

import sys, os

version_suffix = "%r%r" % sys.version_info[:2]
print(version_suffix)
print("Python%s.dll" % version_suffix)

from _msi import *
import os, string, re, sys

AMD64 = "AMD64" in sys.version
Itanium = "Itanium" in sys.version
Win64 = AMD64 or Itanium

print(sys.version)
print(AMD64)
print(Itanium)
print(Win64)

print("------------------------------------------------------------")  # 60個


    def print_label(filename, func):
        name = re.split(r'[-.]', filename)[0]
        sys.stdout.write(
            ("[%s] %s... "
                % (name.center(7), func.__doc__.strip())
            ).ljust(52))
        sys.stdout.flush()



    def print_results(size, n, real, cpu):
        bw = n * float(size) / 1024 ** 2 / real
        bw = ("%4d MB/s" if bw > 100 else "%.3g MB/s") % bw
        sys.stdout.write(bw.rjust(12) + "\n")
        if cpu < 0.90 * real:
            sys.stdout.write("   warning: test above used only %d%% CPU, "
                "result may be flawed!\n" % (100.0 * cpu / real))

print("------------------------------------------------------------")  # 60個
data = ('abc', '123', '   ', '\u1234\u2345\u3456', '\uFFFF'*10)
data = ('abc', '123', '   ', '\xe4\xf6\xfc', '\xdf'*10)
len_data = len(data)

for i in range(self.rounds):
	s = data[i % len_data]

print("------------------------------------------------------------")  # 60個
return "%s:%s" % (self.filename, self.lineno)

def __repr__(self):
	return "<Frame filename=%r lineno=%r>" % (self.filename, self.lineno)

def _normalize_filename(filename):
    filename = os.path.normcase(filename)
    if filename.endswith(('.pyc', '.pyo')):
        filename = filename[:-1]
    return filename

print("------------------------------------------------------------")  # 60個

sys.stderr.write("WARNING: %s can not be found - standard extensions may not be found\n" % defaultMapName)
sys.stderr.write("No definition of module %s in any specified map file.\n" % (mod))
sys.stderr.write("%s: %s\n" % (dsp, msg))
sys.stderr.write('MARKER 1 never found\n')

sys.stderr.write(
    "Usage:  %s HOSTNAME:PORTNUMBER [, HOSTNAME:PORTNUMBER...]\n" %
    sys.argv[0])

unknown = 'ddddd'
sys.stderr.write('Warning: unknown modules remain: %s\n' %' '.join(unknown))

# Ring bell
sys.stderr.write('\007')

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

磁碟處理 os類, shutil類

1. 建立資料夾
2. 檔案複製
3. 資料夾複製
4. 刪除檔案
5. 刪除資料夾

print("------------------------------------------------------------")  # 60個

__version__ = 1, 7, 0

__version__ = '2.1'
print('PYTHON %s' % __version__)

LINE = 50
print('-' * LINE)

print("------------------------------------------------------------")  # 60個

def prdict(d):
    keys = sorted(d.keys())
    for key in keys:
        value = d[key]
        print("%-15s" % key, str(value))


    keys = sorted(makevars.keys())
    for key in keys:
        outfp.write("%s=%s\n" % (key, makevars[key]))
    outfp.write("\nall: %s\n\n" % target)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
pppp

print('溫度:{:.1f}, 濕度:{:.0f}%'.format(humi, temp))


print("------------------------------------------------------------")  # 60個
import sys

error = 'mkreal error'

BUFSIZE = 32*1024

sys.stdout = sys.stderr


print("------------------------------------------------------------")  # 60個

import timeit
import itertools
import operator
import re
import sys
import datetime
import optparse

VERSION = '2.0'

def p(*args):
    sys.stdout.write(' '.join(str(s) for s in args) + '\n')

if sys.version_info >= (3,):
    BYTES = bytes_from_str = lambda x: x.encode('ascii')
    UNICODE = unicode_from_str = lambda x: x
else:
    BYTES = bytes_from_str = lambda x: x
    UNICODE = unicode_from_str = lambda x: x.decode('ascii')

class UnsupportedType(TypeError):
    pass


p('stringbench v%s' % VERSION)
p(sys.version)

# Flush buffer before each group
sys.stdout.flush()


p("bytes\tunicode")
p("(in ms)\t(in ms)\t%\tcomment")

bytes_total = uni_total = 0.0


big_s = "A" + ("Z"*128*12)
print(big_s)

_RANGE_1000 = list(range(1000))
_RANGE_100 = list(range(100))
_RANGE_10 = list(range(10))


'''
try:
    average = bytes_time/uni_time
except (TypeError, ZeroDivisionError):
    average = 0.0
print("%s\t%s\t%.1f\t%s (*%d)" % (
    bytes_time_s, uni_time_s, 100.*average,
    v.comment, v.repeat_count))

p("%.2f\t%.2f\t%.1f\t%s" % (
1000*bytes_total, 1000*uni_total, 100.*ratio, "TOTAL"))


'''


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
self.chars = list(range(256))

print("------------------------------------------------------------")  # 60個
print(self.name+":", size*len(self.data), "bytes", file=sys.stderr)

print("%d+%d bins at shift %d; %d bytes" % (len(t1), len(t2), shift, bytes), file=sys.stderr)
print("Size of original table:", len(t)*getsize(t), "bytes", file=sys.stderr)

print("------------------------------------------------------------")  # 60個
    table = {}
    maxkey = 255
        for key in range(256):
            table[key] = (key, '')

    # Create table code
    maxchar = 0
    for key in range(256):
        if key not in table:
            mapvalue = MISSING_CODE
            mapcomment = 'UNDEFINED'
        else:
            mapvalue, mapcomment = table[key]
        if mapvalue == MISSING_CODE:
            mapchar = UNI_UNDEFINED
        else:
            if isinstance(mapvalue, tuple):
                # 1-n mappings not supported
                return None
            else:
                mapchar = chr(mapvalue)






print("------------------------------------------------------------")  # 60個mix

#Get a list of module files for a filename, a module or package name, or a directory.
def getFilesForName(name):
    if not os.path.exists(name):
        # check for glob chars
        if containsAny(name, "*?[]"):
            files = glob.glob(name)
            list = []
            for file in files:
                list.extend(getFilesForName(file))
            return list

        # try to find module or package
        name = _get_modpkg_path(name)
        if not name:
            return []

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
def wrong_user_display(user_metadata: dict = {"name": "John", "age": 30}):


print("------------------------------------------------------------")  # 60個
        words = (
            "Acquaintance", "Rendezvous",
            "Acquaintance", "House", "Trip", "House", "House")
        expected_count = {
            'Acquaintance': 2,
            'Rendezvous': 1,
            'House': 3,
            'Trip': 1,
        }


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個self.assertEqual(func(), X + Y)
self.assertEqual((cn.id_, cn.user, cn.location), (42, "root", "127.0.0.1"))
self.assertEqual(customer.resolve_customer_id, 1)
self.assertFalse(hasattr(cn, "extra"))
self.assertTrue(result["latency"] >= 0.1)
self.assertTrue(result["latency"] >= 0.1)

self.assertIsNone(process_account_1.__doc__)
self.assertDictEqual(process_account_1.__annotations__, {})
self.assertTrue(process_account_2.__doc__.startswith("Process"))
self.assertDictEqual(process_account_2.__annotations__, {"account_id": str})
self.assertDictEqual(obtained, {"x": DEFAULT_X, "y": DEFAULT_Y})
self.assertDictEqual(obtained, {"x": DEFAULT_X, "y": DEFAULT_Y})
self.assertNotEqual(end_line, "[clinic]*/[clinic]*/")

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
        for name, group in (
            ('y', -1), ('x', -1),
            ('ch', 0),
            ('attr', 1),
            ):
            p = function.parameters[name]


        for name, group in (
            ('y1', -2), ('y2', -2),
            ('x1', -1), ('x2', -1),
            ('ch', 0),
            ('attr1', 1), ('attr2', 1), ('attr3', 1),
            ('attr4', 2), ('attr5', 2), ('attr6', 2),
            ):
            p = function.parameters[name]
            self.assertEqual(p.group, group)
            self.assertEqual(p.kind, inspect.Parameter.POSITIONAL_ONLY)

        self.assertEqual(function.docstring.strip(), """
imaginary([[y1, y2,] x1, x2,] ch, [attr1, attr2, attr3, [attr4, attr5,
          attr6]])



print("------------------------------------------------------------")  # 60個
import unittest

#從另一個.py檔取得參數
from default_arguments import DEFAULT_X, DEFAULT_Y

'''
DEFAULT_X = 5
DEFAULT_Y = 2

'''

print(DEFAULT_X)
print(DEFAULT_Y)


class TestUnitTest(unittest.TestCase):
    print('UnitTest')
    print('UnitTest')
    print('UnitTest')


if __name__ == "__main__":
    unittest.main()


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
class BaseTokenizer:
    """
    >>> tk = BaseTokenizer("28a2320b-fd3f-4627-9792-a2b38e3c46b0")
    >>> list(tk)
    ['28a2320b', 'fd3f', '4627', '9792', 'a2b38e3c46b0']
    """

    def __init__(self, str_token):
        self.str_token = str_token

    def __iter__(self):
        yield from self.str_token.split("-")


class UpperIterableMixin:
    def __iter__(self):
        return map(str.upper, super().__iter__())


class Tokenizer(UpperIterableMixin, BaseTokenizer):


tk = Tokenizer("28a2320b-fd3f-4627-9792-a2b38e3c46b0")
dddd = list(tk)
print(dddd)
#    ['28A2320B', 'FD3F', '4627', '9792', 'A2B38E3C46B0']


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
import logging

logger = logging.getLogger("RefactoringTool")
logger = logging.getLogger("RefactoringTool")


logger=self.logger)

logger.info(msg)

            msg = msg % args
logger.debug(msg)


log_debug("Source: %s", line.rstrip("\n"))
log_error("Can't parse docstring in %s line %s: %s: %s",
                           filename, lineno, err.__class__.__name__, err)



    # Set up logging handler
    level = logging.DEBUG if options.verbose else logging.INFO
    logging.basicConfig(format='%(name)s: %(message)s', level=level)
    logger = logging.getLogger('lib2to3.main')

        logger.info('Output in %r will mirror the input directory %r layout.',
                    options.output_dir, input_base_dir)



print("------------------------------------------------------------")  # 60個
    _default_options = {"print_function" : False,
                        "write_unchanged_files" : False}



print("------------------------------------------------------------")  # 60個

# Map named tokens to the type value for a LeafPattern
TOKEN_MAP = {"NAME": token.NAME,
             "STRING": token.STRING,
             "NUMBER": token.NUMBER,
             "TOKEN": None}



print("------------------------------------------------------------")  # 60個
import sys
import os
import difflib
import shutil
import optparse

def diff_texts(a, b, filename):
    """Return a unified diff of two strings."""
    a = a.splitlines()
    b = b.splitlines()
    return difflib.unified_diff(a, b, filename, filename,
                                "(original)", "(refactored)",
                                lineterm="")
def warn(msg):
    print("WARNING: %s" % (msg,), file=sys.stderr)

filename1 = 'C:/_git/vcs/_1.data/______test_files1/poetrya.txt'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/poetryb.txt'
filename = 'ttttt.txt'

diff_lines = diff_texts(filename1, filename2, filename)
for line in diff_lines:
    print(line)
for line in diff_lines:
    print(line)

warn("couldn't encode %s's diff for your terminal" % (filename,))
warn("--write-unchanged-files/-W implies -w.")

print("At least one file or directory argument required.", file=sys.stderr)
print("Use --help to show usage.", file=sys.stderr)

print("Sorry, -j isn't supported on this platform.", file=sys.stderr)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
import sys
import ensurepip

version=ensurepip._PIP_VERSION
print(version)

EXPECTED_VERSION_OUTPUT = "pip " + ensurepip._PIP_VERSION

print(EXPECTED_VERSION_OUTPUT)

sentinel = object()
orig_pip = sys.modules.get("pip", sentinel)

print(orig_pip)

if orig_pip is sentinel:
    print('aaaaa')
else:
    print('bbbbb')

#print(ensurepip._main(["--version"]))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



def output(string = '', end = '\n'):
    sys.stdout.write(string + end)


def output(*strings):
    for s in strings:
        sys.stdout.write(str(s) + "\n")






print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


'''

json轉dict
'''
import os
import sys
import json
from urllib.request import urlopen
from html.entities import html5

entities_url = 'http://dev.w3.org/html5/spec/entities.json'

def get_json(url):
    """Download the json file from the url and returns a decoded object."""
    with urlopen(url) as f:
        data = f.read().decode('utf-8')
    return json.loads(data)

def create_dict(entities):
    """Create the html5 dict from the decoded json object."""
    new_html5 = {}
    for name, value in entities.items():
        new_html5[name.lstrip('&')] = value['characters']
    return new_html5

new_html5 = create_dict(get_json(entities_url))





print("------------------------------------------------------------")  # 60個

    print('# Generated by {}.  Do not edit manually.'.format(__file__))

print("------------------------------------------------------------")  # 60個
        try:
            # RFC 1952 requires the FNAME field to be Latin-1. Do not
            # include filenames that cannot be represented that way.
            fname = os.path.basename(self.name)
                fname = fname[:-3]

print("------------------------------------------------------------")  # 60個

import locale, copy, io, os, re, struct, sys


print("------------------------------------------------------------")  # 60個
    def __repr__(self):
        args = ", ".join(map(repr, self.args))
        keywords = ", ".join("{}={!r}".format(k, v)
                                 for k, v in self.keywords.items())
        format_string = "{module}.{cls}({func}, {args}, {keywords})"
        return format_string.format(module=self.__class__.__module__,
                                    cls=self.__class__.__name__,
                                    func=self.func,
                                    args=args,
                                    keywords=keywords)

print("------------------------------------------------------------")  # 60個    exe_dir, _ = os.path.split(os.path.abspath(executable))
    site_prefix = os.path.dirname(exe_dir)
            os.path.join(exe_dir, conf_basename),
            os.path.join(site_prefix, conf_basename)
        if os.path.isfile(conffile)
        here = os.path.dirname(os.__file__)
        dirs.extend([os.path.join(here, os.pardir), here, os.curdir])


print("------------------------------------------------------------")  # 60個
    ckeys = sorted(caps)
    for type in ckeys:
        print(type)
        entries = caps[type]
        for e in entries:
            keys = sorted(e)
            for k in keys:
                print("  %-15s" % k, e[k])
            print()



print("------------------------------------------------------------")  # 60個
import sys

for i in range(32):
    print(hex(i))


print(sys.hexversion)

if sys.hexversion >= 0x02020000:
    print('aaaaa')

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
def _recursion222(object):
    print(type(object))
    print(type(object).__name__)
    print(id(object))
    return ("<Recursion on %s with id=%s>"
            % (type(object).__name__, id(object)))

object = [("string", (1, 2), [3, 4], {5: 6, 7: 8})] * 100000
nnnn = _recursion222(object)
print(nnnn)

print("------------------------------------------------------------")  # 60個
warnings.warn('the formatter module is deprecated and will be removed in '
	'Python 3.6', PendingDeprecationWarning)

warnings.warn("This class is deprecated, use the netrc module instead",
	DeprecationWarning, 2)



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
import os
import sys

def errprint(*args):
    sep = ""
    for arg in args:
        sys.stderr.write(sep + str(arg))
        sep = " "
    sys.stderr.write("\n")


file = 'ffff'
msg = 'mmm'
errprint("%r: I/O Error: %s" % (file, msg))

msg = 'aaaaaa'

errprint('aaaa', 'bbbb', 'kkkk')
errprint("Usage:", sys.argv[0], "[-v] file_or_directory ...")

print("------------------------------------------------------------")  # 60個
def errprint(*args):
    strings = map(str, args)
    msg = ' '.join(strings)
    if msg[-1:] != '\n':
        msg += '\n'
    sys.stderr.write(msg)

msg = 'aaaaaaaaaaaaaa'
errprint(msg)
errprint("Usage:", __doc__)
errprint("Skipping file %r; can't parse line %d:\n%s" % (self.fname, srow, line))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
    with open(filename, encoding=encoding) as f:
        return f.read(), filename



print("------------------------------------------------------------")  # 60個import os, sys

PYTHONLIB = 'libpython'+sys.version[:3]+'.a'
PC_PYTHONLIB = 'Python'+sys.version[0]+sys.version[2]+'.dll'
NM = 'nm -p -g %s'                      # For Linux, use "nm -g %s"

print(PYTHONLIB)
print(PC_PYTHONLIB)
print(NM)

# Definition file template
DEF_TEMPLATE = """\
EXPORTS
%s
"""







print("------------------------------------------------------------")  # 60個

    def get_prog_name(self):
        if self.prog is None:
            return os.path.basename(sys.argv[0])
        else:
            return self.prog



print("------------------------------------------------------------")  # 60個
"""
Synopsis: %(prog)s [-h|-b|-g|-r|-a|-d] [ picklefile ] dbfile
Read the given picklefile as a series of key/value pairs and write to a new
hash or btree database using db2pickle.py and reconstitute it to a recno
database with %(prog)s unless your keys are integers.

"""
import sys

prog = sys.argv[0]

print(globals())    #印出記憶體內目前所有的變數名稱

print()
print(__doc__ % globals())  #__doc__的內容有%的, 用變數名稱替換
print()
print(__doc__)  #有%不替換

print("------------------------------------------------------------")  # 60個
import sys, re, os

        sys.stderr.write('Cannot open %s\n' % filename)

    base = os.path.basename(filename)
    if base[-3:] == '.py':
        base = base[:-3]
    s = base + '\t' + filename + '\t' + '1\n'
    tags.append(s)
    while 1:
        line = fp.readline()
        if not line:
            break


print("------------------------------------------------------------")  # 60個
USAGE = """\
Usage: mimetypes.py [options] type
Options:
More than one type argument may be given.
"""

def usage(code, msg=''):
    print(USAGE)
    if msg:
        print(msg)

msg = 'kkkk'
usage(1, msg)

usage(0)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
def _modname(path):
    """Return a plausible module name for the patch."""

    base = os.path.basename(path)
    filename, ext = os.path.splitext(base)
    return filename

    comparepath = os.path.normcase(path)
    longest = ""
    for dir in sys.path:
        dir = os.path.normcase(dir)
        if comparepath.startswith(dir) and comparepath[len(dir)] == os.sep:
            if len(dir) > len(longest):
                longest = dir

    if longest:
        base = path[len(longest) + 1:]
    else:
        base = path
    # the drive letter is never part of the module name
    drive, base = os.path.splitdrive(base)
    base = base.replace(os.sep, ".")
    if os.altsep:
        base = base.replace(os.altsep, ".")
    filename, ext = os.path.splitext(base)
    return filename.lstrip(".")



print("------------------------------------------------------------")  # 60個
            if filename.endswith((".pyc", ".pyo")):
                filename = filename[:-1]

            if coverdir is None:
                dir = os.path.dirname(os.path.abspath(filename))
                modulename = _modname(filename)
            else:
                dir = coverdir
                if not os.path.exists(dir):
                    os.makedirs(dir)
                modulename = _fullmodname(filename)


                s = os.path.expandvars(s)
                s = os.path.normpath(s)




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個print(sys.getwindowsversion()[:2])

#if sys.getwindowsversion()[:2] >= (6, 0):

sys.getwindowsversion()[3] >= 2)


if 'ce' in sys.builtin_module_names:
    defpath = '\\Windows'


drive = os.environ['HOMEDRIVE']


    if path is None:
        path = os.environ['PATH']

    paths = path.split(os.pathsep)
    base, ext = os.path.splitext(executable)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

        for n in range(7):
            values = [5*x-12 for x in range(n)]
            for r in range(n+2):

        for n in range(6):
            s = 'ABCDEFG'[:n]
            for r in range(8):
                print(r)

        ans = list('abc')
        long_ans = list(range(10000))




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

    if not isinstance(dt, datetime.datetime):
        time_str = "000000"
    else:
        time_str = "{0.hour:02d}{0.minute:02d}{0.second:02d}".format(dt)
    y = dt.year
    if legacy:
        y = y % 100
        date_str = "{0:02d}{1.month:02d}{1.day:02d}".format(y, dt)
    else:
        date_str = "{0:04d}{1.month:02d}{1.day:02d}".format(y, dt)
    return date_str, time_str



        cmd = 'NEWNEWS {0} {1} {2}'.format(group, date_str, time_str)
        return self._longcmdstring(cmd, file)


            self.sock = socket.create_connection((host, port), timeout)
            self.sock = _encrypt_on(self.sock, ssl_context, host)
            file = self.sock.makefile("rwb")
            _NNTPBase.__init__(self, file, host,
                               readermode=readermode, timeout=timeout)
            if user or usenetrc:
                self.login(user, password, usenetrc)

        def _close(self):
            try:
                _NNTPBase._close(self)
            finally:

                self.sock.close()


        self.host = host
        self.port = port
        self.sock = socket.create_connection((host, port), timeout)
        file = self.sock.makefile("rwb")
        _NNTPBase.__init__(self, file, host,
                           readermode, timeout)
        if user or usenetrc:
            self.login(user, password, usenetrc)

    def _close(self):
        try:
            _NNTPBase._close(self)
        finally:
            self.sock.close()


    def load_file(self, pathname):
        dir, name = os.path.split(pathname)
        name, ext = os.path.splitext(name)




        print()
        print("  %-25s %s" % ("Name", "File"))
        print("  %-25s %s" % ("----", "----"))


            if m.__path__:
                print("P", end=' ')
            else:
                print("m", end=' ')
            print("%-25s" % key, m.__file__ or "")


        new_filename = original_filename = os.path.normpath(co.co_filename)



    path[0] = os.path.dirname(script)


    print(type(sys.path))
    print(sys.path)


    if os.path.isabs(pathname):
        return '/' + '/'.join(components)
    else:
        return '/'.join(components)


print("------------------------------------------------------------")  # 60個            print(file=self.stream)
            print(file=self.stream)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
import os
import sys
import stat

def _get_sep(path):
    if isinstance(path, bytes):
        return b'/'
    else:
        return '/'

def splitdrive(p):
    """Split a pathname into drive and path. On Posix, drive is always
    empty."""
    return p[:0], p

def basename(p):
    """Returns the final component of a pathname"""
    sep = _get_sep(p)
    i = p.rfind(sep) + 1
    return p[i:]


filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
st = os.lstat(filename)
print(st)
isLink = stat.S_ISLNK(st.st_mode)
print(isLink)



aaa = splitdrive(filename)
print(aaa)

bbb = basename(filename)
print(bbb)




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
    def touch(self, mode=0o666, exist_ok=True):
        """
        Create this file with the given access mode, if it doesn't exist.
        """
        if self._closed:
            self._raise_closed()
        if exist_ok:
            # First try to bump modification time
            # Implementation note: GNU touch uses the UTIME_NOW option of
            # the utimensat() / futimens() functions.
            try:
                self._accessor.utime(self, None)
            except OSError:
                # Avoid exception chaining
                pass
            else:
                return
        flags = os.O_CREAT | os.O_WRONLY
        if not exist_ok:
            flags |= os.O_EXCL
        fd = self._raw_open(flags, mode)
        os.close(fd)



print("------------------------------------------------------------")  # 60個

import os
import sys
from stat import S_ISDIR, S_ISLNK, S_ISREG, S_ISSOCK, S_ISBLK, S_ISCHR, S_ISFIFO

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

print(os.lstat(filename))
print(os.lstat(filename).st_mode)
print(os.lstat(filename).st_gid)

reserved_names = (
    {'CON', 'PRN', 'AUX', 'NUL'} |
    {'COM%d' % i for i in range(1, 10)} |
    {'LPT%d' % i for i in range(1, 10)}
    )

for aaa in reserved_names:
    print(aaa, end = ' ')
print()

'''
S_ISSOCK(self.stat().st_mode)
S_ISFIFO(self.stat().st_mode)
S_ISCHR(self.stat().st_mode)
S_ISBLK(self.stat().st_mode)
S_ISLNK(self.lstat().st_mode)
S_ISDIR(self.stat().st_mode)
S_ISREG(self.stat().st_mode)


    def _iterate_directories(self, parent_path, is_dir, listdir):
        yield parent_path
        for name in listdir(parent_path):
            path = parent_path._make_child_relpath(name)
            if is_dir(path):
                for p in self._iterate_directories(path, is_dir, listdir):
                    yield p




    def _select_from(self, parent_path, is_dir, exists, listdir):
        if not is_dir(parent_path):
            return
        path = parent_path._make_child_relpath(self.name)
        if exists(path):
            for p in self.successor._select_from(path, is_dir, exists, listdir):
                yield p

    def _select_from(self, parent_path, is_dir, exists, listdir):
        if not is_dir(parent_path):
            return
        cf = parent_path._flavour.casefold
        for name in listdir(parent_path):
            casefolded = cf(name)
            if self.pat.match(casefolded):
                path = parent_path._make_child_relpath(name)
                for p in self.successor._select_from(path, is_dir, exists, listdir):
                    yield p

        path.is_absolute()

'''


print("------------------------------------------------------------")  # 60個
from collections.abc import MutableMapping
from collections import OrderedDict as _default_dict, ChainMap as _ChainMap
import functools
import io
import itertools
import re
import sys
import warnings

warnings.warn(
    "The 'filename' attribute will be removed in future versions.  "
    "Use 'source' instead.",
    DeprecationWarning, stacklevel=1
    )

'''
    def read(self, filenames, encoding=None):
        if isinstance(filenames, str):
            filenames = [filenames]
        read_ok = []
        for filename in filenames:
            try:
                with open(filename, encoding=encoding) as fp:
                    self._read(fp, filename)
            except OSError:
                continue
            read_ok.append(filename)
        return read_ok

    def read_file(self, f, source=None):
        """Like read() but the argument must be a file-like object.

        The `f' argument must be iterable, returning one line at a time.
        Optional second argument is the `source' specifying the name of the
        file being read. If not given, it is taken from f.name. If `f' has no
        `name' attribute, `<???>' is used.
        """
        if source is None:
            try:
                source = f.name
            except AttributeError:
                source = '<???>'
        self._read(f, source)




        elements_added = set()
        for section, keys in dictionary.items():
            section = str(section)

'''





print("------------------------------------------------------------")  # 60個




print
name = ['mouse', 'ox', 'tiger']
weight = [3, 48, 33]
print('名稱     編號  體重')
for i in range(0, 3):
    print(name[i].ljust(10),
          str(i+1).rjust(10),
          str(weight[i]).rjust(10))






print("------------------------------------------------------------")  # 60個
print('glob: {}'.format(foldername))
for fname in glob.glob(foldername, recursive=False):
    print("loading: {}".format(fname))


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print('Python之內建函數')
r = abs(-10)
print("abs(-10) = " + str(r))
r = abs(5)
print("abs(5) = " + str(r))
r = pow(8, 2)
print("pow(8, 2) = " + str(r))
r = pow(2, 3)
print("pow(2, 3) = " + str(r))
r = max(9, 3, 12, 32, 81, 92)
print("max(9, 3, 12, 32, 81, 92) = " + str(r))
r = min(9, 3, 12, 32, 81, 92)
print("min(9, 3, 12, 32, 81, 92) = " + str(r))
r = round(5.32)
print("round(5.32) = " + str(r))
r = round(5.52)
print("round(5.52) = " + str(r))
r = round(3.14568757, 3)
print("round(3.14568757, 3) = " + str(r))
r = round(3.14568757, 1)
print("round(3.14568757, 1) = " + str(r))

print("------------------------------------------------------------")  # 60個
print("D:\\Python\\ch08")
print("HEX: \x48\x45\x58")

print("------------------------------------------------------------")  # 60個
x, y = 10, 20
s = "Y= {1} X= {0}".format(x, y)
print(s)
s = "y = {a} x = {b}".format(b=x, a = y)
print(s)
print("整數: {0:5d}".format(456))
print("整數: {0:05d}".format(123))
print("浮點數: {0:6.3f}".format(123.45678))
print("二進位: {0:b}".format(200))
print("八進位: {0:o}".format(200))
print("十六進位: {0:x}".format(200))

print("------------------------------------------------------------")  # 60個
str1 = 'welcome to python'
s = str1.capitalize()
print("str1.capitalize() = " + s)
s = str1.title()
print("str1.title() = " + s)
s = str1.swapcase()
print("str1.swapcase() = " + s)

s = str1.replace('python', 'vcs')
print("str1.replace() = " + s)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
d1 = {x: x*x for x in range(10)}
print(d1)
d2 = {x: x*x for x in range(10) if x % 2 == 0}
print(d2)

lst1 = [x for x in range(10)]
print(lst1)
lst2 = [x+1 for x in range(10)]
print(lst2)
lst3 = [x for x in range(10) if x % 2 == 1]
print(lst3)
lst4 = [x*2 for x in range(10) if x %2 == 1]
print(lst4)


print("------------------------------------------------------------")  # 60個




# 字元函數
ch1 = "A"
print("ch1 = " + ch1)
a = ord(ch1)
print("ord(ch1) = " + str(a))
a = chr(97)
print("chr(97) = " + a)
a = ord('B')
print("ord('B') = " + str(a))


split的用法(3)
str1 = "This is a pen."
lst1 = str1.split()
print(lst1)
str2 = "Tom,Bob,Mary,Joe,John"
lst2 = str2.split(",")
print(lst2)
str3 = "23\n52\n44\n78"
lst3 = str3.splitlines()
print(lst3)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
#eval() 和 exec()，能夠將字串轉換成可以運作的程式碼

m = 10
eval("print('Python')")
eval("print(50 + 10)")
eval("print(55 / 13)")
eval("print( m  * 5)")
eval("print('m' * 5)")

a, b, c = 1, 2, 3
eval('print(a, b, c)')                            # 1, 2, 3
eval('print(a, b, c)', {'a':4, 'b':5, 'c':6})     # 4, 5, 6
eval('print(a, b, c)', {'a':4, 'b':5, 'c':6}, {'a':7, 'b':8, 'c':9})   # 7, 8, 9
eval('print(a, b, c)')   # 1, 2, 3

a = eval('x+y',{'x':1,'y':2})
print(a)       # 3

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
字串處理函數
msg = '''CIA Mark told CIA Linda that the secret USB had given to CIA Peter'''
print("字串開頭是CIA: ", msg.startswith("CIA"))
print("字串結尾是CIA: ", msg.endswith("CIA"))
print("CIA出現的次數: ",msg.count("CIA"))
msg = msg.replace('Linda','Lxx')
print("新的msg內容 : ", msg)

print("------------------------------------------------------------")  # 60個
import sys
import time

SYSTIMES_IMPLEMENTATION = None
USE_WIN32PROCESS_GETPROCESSTIMES = 'win32process.GetProcessTimes()'

import win32process
SYSTIMES_IMPLEMENTATION = USE_WIN32PROCESS_GETPROCESSTIMES

WIN32_PROCESS_TIMES_TICKS_PER_SECOND = 1e7
def win32process_getprocesstimes_systimes():
    d = win32process.GetProcessTimes(win32process.GetCurrentProcess())
    return (d['UserTime'] / WIN32_PROCESS_TIMES_TICKS_PER_SECOND,
            d['KernelTime'] / WIN32_PROCESS_TIMES_TICKS_PER_SECOND)

systimes = win32process_getprocesstimes_systimes

def processtime():
    user, system = systimes()
    return user + system

def some_workload1():
    x = 0
    for i in range(10000000):
        x = x + 1
    print(x)

def some_workload2():
    x = 0.0
    for i in range(10000000):
        x += i
    print(x)

if __name__ == '__main__':
    print('Using %s as timer' % SYSTIMES_IMPLEMENTATION)
    print()
    
    print('Testing systimes() under load conditions')
    t0 = systimes()
    some_workload1()
    t1 = systimes()
    print('before:', t0)
    print('after:', t1)
    print('differences:', (t1[0] - t0[0], t1[1] - t0[1]))


    print('Testing systimes() under load conditions')
    t0 = systimes()
    some_workload1()
    t1 = systimes()
    print('before:', t0)
    print('after:', t1)
    print('differences:', (t1[0] - t0[0], t1[1] - t0[1]))
    

    print('Testing systimes() under load conditions 2222')
    t0 = systimes()
    some_workload2()
    t1 = systimes()
    print('before:', t0)
    print('after:', t1)
    print('differences:', (t1[0] - t0[0], t1[1] - t0[1]))


    print('Testing systimes() under idle conditions')
    t0 = systimes()
    time.sleep(1)
    t1 = systimes()
    print('before:', t0)
    print('after:', t1)
    print('differences:', (t1[0] - t0[0], t1[1] - t0[1]))
    print()

    print(processtime())

print("------------------------------------------------------------")  # 60個

檢查touch

    mtime = None
    atime = None
    try:
        statbuf = os.stat(filename)
        mtime = statbuf.st_mtime
        atime = statbuf.st_atime
        os.chmod(tempname, statbuf[ST_MODE] & 0o7777)

    if preserve_timestamps:
        if atime and mtime:
            try:
                os.utime(filename, (atime, mtime))
            except OSError as msg:
                err('%s: reset of timestamp failed (%r)\n' % (filename, msg))
                return 1

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/poetry2.txt'

with open(filename, "rb") as f:
    data = f.read()
if b'\0' in data:
    print(filename, "\tBinary")
else:
    print(filename, "\tASCII")

print("------------------------------------------------------------")  # 60個

"""Reverse grep.
Usage: rgrep [-i] pattern file
"""

import sys

def usage(msg, code=2):
    sys.stdout = sys.stderr
    print(msg)
    print(__doc__)
    sys.exit(code)


usage("not enough arguments")

print("------------------------------------------------------------")  # 60個

print(__file__)
print(__file__.lower())
print(__file__.upper())

import os
print(os.path.dirname(__file__))

    pathlist = os.environ['PATH'].split(os.pathsep)
    print(pathlist)

print("------------------------------------------------------------")  # 60個

set

consuming_calls = {"sorted", "list", "set", "any", "all", "tuple", "sum",
                   "min", "max", "enumerate"}

print(type(consuming_calls))

print("------------------------------------------------------------")  # 60個


串的格式化	使用 format

Python 字串可以做一些格式化, 比如說...

message = "你好, 來自{}的{}!".format(bp, name)


"1 美金是 {:.2f} 台幣。".format(30.1077859)
print("平均 = {:.2f}".format(s/5))

list(range(10))
list(range(1,10))
list(range(3, 15))

print('------------------------------------------------------------')	#60個    

    factors = []
:
:
    factors = list(set(factors))


list 轉 set 轉 list

這樣可以把重複地排除掉

print('------------------------------------------------------------')	#60個


        textvars = dict(
            VER='aaaaa',
            FULLVER='bbbbb',
        )


print('------------------------------------------------------------')	#60個


s = "   this is a sample sentance. this is a cat\n "
print(s.capitalize())
print(s.upper())
print(s.upper().casefold())
print(s.count("a"))
print(s.endswith("ce."))
print(s.find("this"))
print(s.split())
print("#".join(s.split()))
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.rfind("is"))
print(s.zfill(50))

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



for name in sorted(players.keys( )):
    print(name)
    print(f"Hi! {name} 我喜歡看你在 {players[name]} 的表現")
    
    
for team in players.values( ):
    print(team)
    
    


print('------------------------------------------------------------')	#60個


height = eval(input("請輸入身高(公分)："))
weight = eval(input("請輸入體重(公斤)："))
BMI = weight / (height / 100) ** 2 
if BMI >= 18.5 and BMI < 24:
    print(f"{BMI = :5.2f}體重正常")
else:
    print(f"{BMI = :5.2f}體重不正常")
    
    
    
    print(f"{r1 = :6.4f},    {r2 = :6.4f}")
    

print('------------------------------------------------------------')	#60個    

cars = ['honda','bmw','toyota','ford']     
print(f"目前串列car內容 = {cars}")
print("使用sorted()由小排到大")
cars_sorted = sorted(cars)            
print(f"從小排到大的排序串列結果 = {cars_sorted}")
print("-"*60)
print(f"原先串列car內容 = {cars}")
cars_sorted = sorted(cars,reverse=True)            
print(f"從大排到小的排序串列結果 = {cars_sorted}")
print(f"原先串列car內容不變 = {cars}")
print("="*60)
nums = [5, 3, 9, 2]     
print(f"目前串列num內容 = {nums}")
print("使用sorted()由小排到大")
nums_sorted = sorted(nums)            
print(f"從小排到大的排序串列結果 = {nums_sorted}")
print("-"*60)
print(f"原先串列num內容 = {nums}")
nums_sorted = sorted(nums,reverse=True)            
print(f"從大排到小的排序串列結果 = {nums_sorted}")
print(f"原先串列num內容不變 = {nums}")

print('------------------------------------------------------------')	#60個

# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.

print('------------------------------------------------------------')	#60個

ans = 0                         # 讀者心中的數字
print("猜生日日期遊戲,請回答下列5個問題,這個程式即可列出你的生日")

truefalse = "輸入y或Y代表有, 其它代表無 : "
# 檢測2進位的第1位是否含1
q1 = "有沒有看到自己的生日日期 : \n" + \
     "1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31 \n"
num = input(q1 + truefalse)
print(num)
if num == "y" or num == "Y":
    ans += 1
# 檢測2進位的第2位是否含1
truefalse = "輸入y或Y代表有, 其它代表無 : "
q2 = "有沒有看到自己的生日日期 : \n" + \
     "2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31 \n"
num = input(q2 + truefalse)
if num == "y" or num == "Y":
    ans += 2
# 檢測2進位的第3位是否含1
truefalse = "輸入y或Y代表有, 其它代表無 : "
q3 = "有沒有看到自己的生日日期 : \n" + \
     "4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31 \n"
num = input(q3 + truefalse)
if num == "y" or num == "Y":
    ans += 4
# 檢測2進位的第4位是否含1
truefalse = "輸入y或Y代表有, 其它代表無 : "
q4 = "有沒有看到自己的生日日期 : \n" + \
     "8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31 \n"
num = input(q4 + truefalse)
if num == "y" or num == "Y":
    ans += 8
# 檢測2進位的第5位是否含1
truefalse = "輸入y或Y代表有, 其它代表無 : "
q5 = "有沒有看到自己的生日日期 : \n" + \
     "16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31 \n"
num = input(q5 + truefalse)
if num == "y" or num == "Y":
    ans += 16

print(f"讀者的生日日期是 : {ans}")


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

song = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# 以下是將單字大寫字母全部改成小寫
songLower = song.lower()            # 單字改為小寫

# 將段落的標點符號用空字元取代
for ch in songLower:                
    if ch in ".,?!-*":
        songLower = songLower.replace(ch,'')

# 將文字段落字串轉成串列
songList = songLower.split()        

# 將單字串列處理成字典 
mydict = {wd:songList.count(wd) for wd in songList}
for wd, count in sorted(mydict.items()):
    print(wd, ":", count)                 
    
print('------------------------------------------------------------')	#60個

song = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# 以下是將單字大寫字母全部改成小寫
songLower = song.lower()            # 單字改為小寫

# 將段落的標點符號用空字元取代
for ch in songLower:                
    if ch in ".,?!-*":
        songLower = songLower.replace(ch,'')

# 將文字段落字串轉成串列
songList = songLower.split()        

# 將單字串列處理成字典 
mydict = {wd:songList.count(wd) for wd in songList}
for wd, count in sorted(mydict.items()):
    print(wd, ":", count)                 
    
print('------------------------------------------------------------')	#60個    
    
def pi(n):
    p = 0
    for i in range(1,n+1, 1):
        p += 4 *((-1)**(i+1)/(2*i-1))
    return p

print("  i      PI ")
print("================")
for i in range(1, 10000, 1000):
    print("%5d   %7.5f" % (i, pi(i)))
    
print('------------------------------------------------------------')	#60個

sc = {'John':80, 'Tom':90, 'Kevin':77}
newsc1 = sorted(sc.items(), key = lambda x:x[0])  # 依照key排序
print("依照人名排序")
for i in range(len(newsc1)):
    print(f"{newsc1[i][0]:5s}:{newsc1[i][1]}")

print("依照分數排序")
newsc2 = sorted(sc.items(), key = lambda x:x[1])  # 依照value排序
for i in range(len(newsc2)):
    print(f"{newsc2[i][0]:5s}:{newsc2[i][1]}")
    
print('------------------------------------------------------------')	#60個

DATA = b'Jack is my hero'

f = open(self.fname1, 'wb')
f.write(self.DATA)
f.close()


f = open(self.fname1, 'rb')
finish = f.readline()
f.close()

self.assertEqual(self.DATA, finish)

print('------------------------------------------------------------')	#60個

        for k, v in dict.items():
            if k.endswith('_pre') or k.endswith('_post'):
                assert isinstance(v, function)
            elif isinstance(v, function):
                methods.append(k)
        for m in methods:
            pre = dict.get("%s_pre" % m)
            post = dict.get("%s_post" % m)
            if pre or post:
                dict[m] = cls.make_eiffel_method(dict[m], pre, post)

print('------------------------------------------------------------')	#60個

print('zip 測試')
def iterate_simul():
    xpts = [1, 5, 4, 2, 10, 7]
    ypts = [101, 78, 37, 15, 62, 99]
    for x, y in zip(xpts, ypts):
        print(x, y)

    a = [1, 2, 3]
    b = ['w', 'x', 'y', 'z']
    for i in zip(a,b):
        print(i)  # 默认是按最短长度

    headers = ['name', 'shares', 'price']
    values = ['ACME', 100, 490.1]
    s = dict(zip(headers,values))

    for name, val in zip(headers, values):
        print(name, '=', val)


if __name__ == '__main__':
    iterate_simul()



print('------------------------------------------------------------')	#60個


"""
字典转换成XML格式
"""
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring

def dict_to_xml(tag, d):
    """
    Turn a simple dict of key/value pairs into XML
    """
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem

if __name__ == '__main__':
    r = dict_to_xml('root', {'鼠':'mouse', '牛':'ox'})
    print(r)
    print(tostring(r))
    r.set('虎', 'tiger')
    print(tostring(r))

print('------------------------------------------------------------')	#60個

重新命名檔案

import os
os.rename('filename.txt', 'new_filename.txt')

import os
os.rename('/path/to/dir/filename.txt', '/path/to/dir/new_filename.txt')

import os
 
dir = '/path/to/dir'
old_file = os.path.join(dir, 'filename.txt')
new_file = os.path.join(dir, 'new_filename.txt')
 
os.rename(old_file, new_file)

print('------------------------------------------------------------')	#60個

print("------------------------------------------------------------")  # 60個

'''
list [] append
files = ['da1.c','da2.py','da3.py','da4.java']
py = []
squares = []                     # 建立空串列

'''


import requests

user_key = "你的氣象API授權碼"
doc_name = "F-C0032-001"

cities = ["臺北","新北","桃園","臺中","臺南","高雄","基隆","新竹","嘉義"]  #市
counties = ["苗栗","彰化","南投","雲林","嘉義","屏東","宜蘭","花蓮","臺東","澎湖","金門","連江"]  #縣

def sendLUIS(event, mtext):  #LUIS
    try:
        r = requests.get('https://westus.api.cognitive.microsoft.com/luis/prediction/v3.0/apps/be857f50-efbf-4487-a8bb-b1ab1e4819b0/slots/production/predict?subscription-key=b70c437cffee487b9ab2aa9ed6faaac6&verbose=true&show-all-intents=true&log=true&query=' + mtext)
        result = r.json()
        city = ''
        if result["prediction"]['topIntent'] == '縣市天氣':
            city = result["prediction"]['entities']['地點'][0]

        if city != '':  #天氣類地點存在
            flagcity = False  #檢查是否為縣市名稱
            city = city.replace('台', '臺')  #氣象局資料使用「臺」
            if city in cities:  #加上「市」
                city += '市'
                flagcity = True
            elif city in counties:  #加上「縣」
                city += '縣'
                flagcity = True
            if flagcity:  #是縣市名稱
                weather = city + '天氣資料：\n'             
                api_link = "https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/%s?Authorization=%s&downloadType=WEB&format=JSON" % (doc_name,user_key)
                datas = requests.get(api_link).json()
                column = ['天氣狀況','最高溫','最低溫','舒適度','降雨機率(%)']
                for data in datas['cwbopendata']['dataset']['location']:
                    if data['locationName'] == city:
                        for i in range(len(data['weatherElement'])):
                            weather += column[i] + ':'
                            weather += data['weatherElement'][i]['time'][0]['parameter']['parameterName'] + '\n'
                        weather = weather[:-1]  #移除最後一個換行
                        break                       
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=weather))
            else:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='無此地點天氣資料！'))
        else:  #其他未知輸入
            text = '無法了解你的意思，請重新輸入！'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))            
    except:
       line_bot_api.reply_message(event.reply_token, TextSendMessage(text='執行時產生錯誤！'))


print("------------------------------------------------------------")  # 60個

np.arange(10)

np.arange(3, 10)

np.arange(3, 10, 0.5)

A = np.arange(10)


pandas 可以說像是 Python 中的 Excel

不只 CSV 檔, 很多資料檔案, 像 Excel 檔都很容易在 pandas 完成。使用法是這樣:

df2 = pd.read_excel('filename.xls', 'sheetname')
其中 sheetname 那裡要放工作表的名稱, 如果是中文的最好改成英文。

Pandas 有兩個基本資料結構:
1. DataFrame: 可以想成一個表格。
2. Series: 表格的某一列、某一行, 基本上就是我們以前的 list 或 array

一個 DataFrame, 我們有 index (列的名稱), columns (行的名稱)。
series 大概就是一個 list, 一個 array。其實更精準的說, 其實是一個有 "index" 的 array。

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print 格式化

name = "炎龍"
job = "老師"

print(f"你好, 我叫{name}, 我的工作是{job}。")

name = 'A機台'
output = 3.124000000000001
print(f"在{name}, 我的輸出是 {output:.2f}。")

行家超愛的 list comprehension
[i**2 for i in range(10)]





print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



'''

        return "%s %s %2d %02d:%02d:%02d %04d" % (
            _DAYNAMES[weekday],
            _MONTHNAMES[self._month],
            self._day,
            self._hour, self._minute, self._second,
            self._year)




'''



print("------------------------------------------------------------")  # 60個
innum = 0
list1 = []
while(innum != -1):
    innum = int(input("請輸入正整數 (-1：結束)："))
    list1.append(innum)
list1.pop()
print("共輸入 %d 個數" % len(list1))
print("最大數為：%d" % max(list1))
print("最小數為：%d" % min(list1))
print("輸入數的總和為：%d" % sum(list1))
print("輸入數由大到小排序為：{}".format(sorted(list1, reverse=True)))



print("------------------------------------------------------------")  # 60個

------------------------------------ 
  
  

---
應該是pandas/data_frame才有的語法
df_sbike.median().plot(kind="bar")
weekday_counts.plot(kind='bar')


---

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

list的排列要指名欄位
sc.sort(key=lambda x:x[5],reverse=True)     # 依據總分高往低排序


# 以下依座號排序
sc.sort(key=lambda x:x[0])                  # 依據座號排序

print('------------------------------------------------------------')	#60個

字典
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8 # 修改資料
dict['School'] = "DPS School" # 新增資料

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

print('------------------------------------------------------------')	#60個

 Python列表：	//操作方式很像字串
 
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
list3 = ["a", "b", "c", "d"]

print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]
 
print('------------------------------------------------------------')	#60個

刪除列表中的元素：

要刪除列表的元素，可以使用del語句，如果知道哪些元素要刪除；或如果你不知道那麼使用remove()方法。例子：

list1 = ['physics', 'chemistry', 1997, 2000]
print list1
del list1[2]
print "After deleting value at index 2 : "
print list1

基本列表操作：
Python 表達式 	結果 				描述
len([1, 2, 3]) 	3 				長度
[1, 2, 3] + [4, 5, 6] 	[1, 2, 3, 4, 5, 6] 	串聯
['Hi!'] * 4 	['Hi!', 'Hi!', 'Hi!', 'Hi!'] 	重複
3 in [1, 2, 3] 	True 				成員
for x in [1, 2, 3]: print x, 	1 2 3 		迭代


print('------------------------------------------------------------')	#60個

# *args 與 **kwargs 選用性與關鍵字參數

def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)


foo('hello')

print('')

foo('hello', 1, 2, 3)

print('')

foo('hello', 1, 2, 3, key='value', key2=999)

print('------------------------------------------------------------')	#60個

# lambda: 只有單一運算式的匿名函式

add = lambda x, y: x + y

print(add(5, 3))

print((lambda x, y: x + y)(5, 3))

print('------------------------------------------------------------')	#60個

# 在 sorted() 使用 lambda 匿名函式

tuples_list = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]


print(sorted(tuples_list))

print(sorted(tuples_list, key=lambda x: x[1]))

print(sorted(range(-5, 6), key=lambda x: x ** 2))

print('------------------------------------------------------------')	#60個

import zipfile

with zipfile.ZipFile('檔案路徑.zip', 'w') as zipf:
    zipf.write('要壓縮的檔案路徑', arcname='壓縮檔案中的名稱')


import zipfile

with zipfile.ZipFile('檔案路徑.zip', 'r') as zip_ref:
    zip_ref.extractall('解壓縮目標資料夾')



"""
程式名稱：九九乘法表
"""
for x in range(1, 10):
    for y in range(1, 10):
        print("{0}*{1}={2: ^2}".format(y, x, x * y), end=" ")
    print()

print('------------------------------------------------------------')	#60個

資料產生大範例

range

linspace

random

meshgrid

print('------------------------------------------------------------')	#60個

#將一個google drive檔案存成本地檔案

import requests

fontfile = requests.get("https://drive.google.com/uc?id=1QdaqR8Setf4HEulrIW79UEV_Lg_fuoWz&export=download")

with open('taipei_sans_tc_beta.ttf', 'wb') as f:
  f.write(fontfile.content)

print('------------------------------------------------------------')	#60個





text = "這個是測試資料。"
word1 = "這個是"
word2 = "那個是"

print("置換前 :", text)
text = text.replace(word1, word2)
print("置換後 :", text)


plt.plot(x, y)
plt.plot(x, y, color='y')
#plt.plot(x, y, color=(1,1,0))  #RGB
#plt.plot(x, y, color='# FFFF00')  #HEX
#plt.plot(x, y, color='yellow')  #英文全名
#plt.plot(x, y, color='0.5')


x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[16800,20000,21600,25400,12800,20000,25000,14600,32800,25400,18000,10600]
plt.plot(x, y, marker='d',ms=10, mfc='r', mec='b')


x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[16800,20000,21600,25400,12800,20000,25000,14600,32800,25400,18000,10600]

plt.plot(x, y, marker='.')



x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[200000,180000,175000,215000,280000,320000,90000,365000,318000,198000,268000,348000]

plt.plot(x, y, marker='*')



x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[200000,180000,175000,215000,280000,320000,90000,365000,318000,198000,268000,348000]

plt.plot(x, y, lw=8, ls='-.')


x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[200000,180000,175000,215000,280000,320000,90000,365000,318000,198000,268000,348000]

plt.plot(x, y, marker='D',ms=10, mfc='y', mec='r')

os.chdir(r"D:\Python_book\19Case\19_1Bankcredit")


"""
fontfile = requests.get("https://drive.google.com/uc?id=1QdaqR8Setf4HEulrIW79UEV_Lg_fuoWz&export=download")
fontfile = "../taipei_sans_tc_beta.ttf"
with open('taipei_sans_tc_beta.ttf', 'wb') as f:
  f.write(fontfile.content)
"""





同一支小算盤程式(program)執行多次 成為多個獨立的處理程序(process)


iris資料
https://archive.ics.uci.edu/dataset/53/iris

kaggle網站上的iris資料
https://www.kaggle.com/datasets/uciml/iris


import pandas as pd
df = pd.read_csv('Iris.csv')
print(df.head())
print('將Id整欄刪除')
df = df.drop('Id', axis = 1)

print(df.head())


C:\_git\vcs\_4.python>python -m pdb test10_new11.py


ML(2)
監督式學習	supervised learning
		分類學習 classification learning
		回歸學習 regression learning
無監督學習	un-supervised learning
		分群 clustering


無監督式學習
1. 分群 clustering
2. 分布密度估計 density estimation
3. 維度約簡 dimensionality reduction

print("------------------------------------------------------------")  # 60個

"""
Python的内置函数
- 数学相关: abs / divmod / pow / round / min / max / sum
- 序列相关: len / range / next / filter / map / sorted / slice / reversed
- 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
- 数据结构: dict / list / set / tuple
- 其他函数: all / any / id / input / open / print / type
"""

"""
Python常用模块
- 运行时服务相关模块: copy / pickle / sys / ...
- 数学相关模块: decimal / math / random / ...
- 字符串处理模块: codecs / re / ...
- 文件处理相关模块: shutil / gzip / ...
- 操作系统服务相关模块: datetime / os / time / logging / io / ...
- 进程和线程相关模块: multiprocessing / threading / queue
- 网络应用相关模块: ftplib / http / smtplib / urllib / ...
- Web编程相关模块: cgi / webbrowser
- 数据处理和编码模块: base64 / csv / html.parser / json / xml / ...
"""







git指令
git.exe pull --progress -v --no-rebase "origin"





網路爬蟲（英語：web crawler）

高	網路類：request、bs4
	影像類：opencv、PIL、webcam、
	數據類：scipy、scikit-learn、、、、、、、、

中	tk、matplotlib、numpy、pandas、資料庫、各種套件(sys、os、random、time、serial、)、、、、、
	(turtle、pygame、、、)

基	開發環境、IO、資料型態、容器DSLT、流程控制、函數(內建、自訂)、類別、檔案讀寫、、、


Python套件之數據結構 numpy pandas之seris dataFrame
網頁資料四大資料結構 csv json xml html
常用儲存資料結構 csv json sqlite

使用webAPI取得網路資料
1. 公開API
2. 認證API -- API key

自己要會的: HTML、正規表示式、物件導向
外部配合: 虛擬環境 自動測試環境 flask Heroku AWS

Python開發環境
1. Python IDE
2. Anaconda Jupyter
3. Visual Studio


OpenCV之
1. 基本使用 open show info save
2. draw
3. cut resize rotate	不改變影像的
4. video + webcam
5. 影像處理1  blur dilate erode....
6. 影像處理2

df.loc["xxx", "yyyy"]	loc索引器
df.iloc[nnn, nnn]	iloc使用index來取資料

建立-讀取-儲存

10張以上的subplot要怎麼寫

ok 但是可以看看medium的英文網站
https://medium.com/py-tips-conceptes/%E6%9C%AC%E6%96%87%E7%B4%80%E9%8C%84python%E7%B9%AA%E5%9C%96%E7%9A%84%E6%96%B9%E6%B3%95-%E4%BD%BF%E7%94%A8-seaborn-255b0006eb3e


#cv2.imwrite('test.jpg',img) 偽寫入


use_pivot 看encoding
import pandas as pd
df = pd.read_csv("..\data\ordersList.csv",encoding="utf-8",header = 0)
print(df.pivot_table(index="品名",columns="客戶名稱", values="金額", fill_value=0, margins=True, aggfunc="sum"))

print(df.pivot_table(index="品名",columns="客戶名稱", values="金額", fill_value=0, margins=True ))



excel相關之python套件

openpyxl	讀寫.xlsx
xlrd		讀取.xls .xlsx
xlwt		寫入.xls
xlswrite	寫入.xlsx

openpyxl	讀寫.xlsx
openpyxl	讀寫.xlsx
openpyxl	讀寫.xlsx



read
    img = cv2.imread('car.jpg')             # 讀取圖片

resize
    img_small = cv2.resize(img, (300, 100))  # 改變尺寸

save
        cv2.imwrite('small.jpg', img_small)  # 儲存影像

plt.xticks([])  #隱藏x座標
plt.yticks([])  #隱藏y座標





df的方法


基本常用口訣 做成 python.doc 待印之口訣
python_密技.doc

Python之四大容器 DSLT

複合資料型態 compound data type
D  S  L  T
字 集 串 元
典 合 列 組
{} {} [] ()

Dict	大括號
Set	大
List	中
Tuple	小

#range()回傳整數皆不含尾
range(a)	#0, 1, 2, ..., a-1
range(a, b)	#a, a + 1, a + 2, ..., b-1
range(a, b, c)	#a, a + c, a + 2c, ..., b-1

x = np.arange(0, 2 * np.pi, 0.02)
x = np.linspace(0, 2 * np.pi, num = 100)	#頭, 尾, 點數(含頭尾)
logspace

pandas主要之資料型態:
1. Series	一維資料結構
2. DataFrame	二維資料結構


1.SVM-支持向量机

其实SVM最开始主要用于分类，在维基百科上的解释，Support Vector Machines are learning models used for classification



SVM = Support Vector Machine 是 支持向量机
SVC = Support Vector Classification就是 支持向量机 用于分类
SVR = Support Vector Regression.就是 支持向量机 用于回归分析


big
https://www.flag.com.tw/VIP/Bonus#class01
Python 幫幫忙！用程式思維解決現實世界問題
集成式學習：Python 實踐

 歡迎下載「集成式學習：Python 實踐！整合全部技術，打造最強模型」一書的範例程式。請先依照書籍內容，回答以下小問題：

請輸入本書 第 1-11 頁，第 1 個 中文字
答案(哪裡找？)：

https://www.flag.com.tw/bk/st/F2387


KNN(K Nearest Neighbor) 最近鄰居法 or K-近鄰算法

K-means K-平均算法

兩者沒關係

MLP multi-layer perceptron 多層感知器的類神經模型


.	點標記
,	逗號標記
o	圓圈標記
v^<>	三角形標記
1~4	三角形標記
s	方形標記
p	五角形標記
*	星號標記
hH	六角形標記
dD	鑽石標記
+x	加和叉標記
|_	直和橫標記
-	實線樣式
--	虛線樣式
-.	點劃線樣式
:	虛線樣式


Python網頁伺服器

python -m http.server 8888

http://127.0.0.1:8888/

try ch14
01-httpServer.py


xampp
https://www.apachefriends.org/zh_tw/download.html


df.shape 這個df有幾列有幾欄
df.columns 這個df的變數資訊
df.index 這個df的列索引資訊
df.info()這個df的詳細資訊
df.describe() 這個df各數值變數的描述統計

df其他常見的函數
df.count()
df.min()
df.max()
df.idxmin()
df.idxmax()
df.quantile(0.1)	10%分位數
df.sum()
df.mean()
df.median()
df.mode()	眾數
df.var()
df.std()
df.mad()	平均絕對偏差
df.skew()	偏度
df.kurt()	峰度





在RGB各區間的分量


"""



"""





            三维2D图
            文本
            分绘

線圖
Axes3D.plot()
散點圖
Axes3D.scatter()
線框圖
Axes3D.plot_wireframe()
曲面圖
Axes3D.plot_surface()
三面圖
Axes3D.plot_trisurf()
等高線圖
Axes3D.contour()
填充輪廓圖
Axes3D.contourf()
多邊形圖
Axes3D.add_collection3d()
條形圖
Axes3D.bar()
顫抖
Axes3D.quiver()
文本
Axes3D.text()
 
分繪


線圖	連線圖
巴圖	橫條圖
柱圖	
點圖	散點圖
箱圖	箱型圖



黑白影像	binary image
灰階影像	gray image
彩色影像	color image

GIF 採交錯圖顯示出現


colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
colorInd = 0
t.color(colorsList[(colorInd)%5]); colorInd += 1

colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
for i in [1,2,3,4,5,6,7]:
    t.color(colorsList[(i-1)%8])

colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
        t.color(colorsList[(i-1)%8])


print("顯示反斜線: " + '\\')
print("顯示單引號: " + '\'');
print("顯示雙引號: " + '\"');
print("顯示16進位數: " + '\u0068')
print("顯示8進位數: " + '\123')
print("顯示倒退一個字元: " + '\b' + "xyz")
print("顯示空字元: " + "xy\0z")
print("雙引號的應用->\n\"跳脫字元的綜合運用\"")




print("------------------------------------------------------------")  # 60個
基本用range

for i in range(1, 11): #定義for迴圈

for i in range(11, 21): 

for n in range(0, k, 1):
for i in range(1, 201, 2):

print("------------------------------------------------------------")  # 60個

    # Keys are (x, y) tuples of ints, values the character at that
    # position on the canvas:
    canvas = {}

                canvasX = dieLeft + dx
                canvasY = dieTop + dy
                # Note that in dieFace, a list of strings, the x and y
                # are swapped:
                canvas[(canvasX, canvasY)] = dieFace[dy][dx]

    for cy in range(CANVAS_HEIGHT):
        for cx in range(CANVAS_WIDTH):
            print(canvas.get((cx, cy), ' '), end='')
        print()  # Print a newline.

------
# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.


print("------------------------------------------------------------")  # 60個

x = [1, 2, 2, 3, 5, 2, 5]
x.count(2)
3
x.count(5)
2
x.count(4)
0


保留 -----------------------------------------


---

你可使用 os.path 和 os 函式庫，尤其是os.path.join()、os.mkdir() 和os.rename()。

### 20.4.1 ###

create path for zip file
create empty zipfile
for each file
    write into zipfile
    remove original file

### 20.4.2 ###

你可以改書中的範例程式碼，再加上目前月份與檔案月份的核對即可。

print("------------------------------------------------------------")  # 60個

#! /usr/bin/env python3 

#數字與英文的對應字典
_1to9dict = {'0': '', '1': 'one', '2': 'two', '3': 'three',  
             '4': 'four','5': 'five', '6': 'six', '7': 'seven',     
             '8': 'eight','9': 'nine'}
_10to19dict = {'0': 'ten', '1': 'eleven', '2': 'twelve',
               '3': 'thirteen', '4': 'fourteen', '5': 'fifteen',
               '6': 'sixteen', '7': 'seventeen', '8': 'eighteen',
               '9': 'nineteen'}
_20to90dict = {'2': 'twenty', '3': 'thirty', '4': 'forty', 
               '5': 'fifty','6': 'sixty', '7': 'seventy',  
               '8': 'eighty', '9': 'ninety'}

def num2words(num_string): 
    if num_string == '0': 
        return'zero'
    if len(num_string) > 2:  
        return "抱歉此程式只能處理0~99的2位整數"
    num_string = '0' + num_string 
 
    tens, ones = num_string[-2], num_string[-1] 

    if tens == '0':    
        return _1to9dict[ones]
    elif tens == '1':  
        return _10to19dict[ones]
    else:              
        return _20to90dict[tens] + ' ' + _1to9dict[ones]

#定義主控函式
def main():                        
    print(num2words(sys.argv[1]))

main() 

print("------------------------------------------------------------")  # 60個

import sys

def main():
    # initialze counts
    line_count = 0
    word_count = 0
    char_count = 0
    
    option = None
    params = sys.argv[1:]
    if len(params) > 1:
        # if more than one param, pop the first one as the option
        option = params.pop(0).lower().strip()
    filename = params[0]    # open the file
    with  open(filename) as infile:
        for line in infile:
            line_count += 1
            char_count += len(line)
            words = line.split()
            word_count += len(words)
    
    if option == "-c":
        print("File has {} characters".format(char_count))
    elif option == "-w":
        print("File has {} words".format(word_count))
    elif option == "-l":
        print("File has {} lines".format(line_count))
    else:
        # print the answers using the format() method
        print("File has {0} lines, {1} words, {2} characters".format(
           line_count, word_count, char_count))

if __name__ == '__main__':
    main() 

print("------------------------------------------------------------")  # 60個


>>> math.ceil(3.4)
>>> math.ceil(3.4)
>>> math.ceil(3.4)




08.3.4 enumerate function

x = [1, 3, -7, 4, 9, -5, 4]
for i, n in enumerate(x):                               #1
    if n < 0:                                           #2
        print("Found a negative number at index ", i)   #3

08.3.5 zip function 

>>> x = [1, 2, 3, 4]
>>> y = ['a', 'b', 'c']           #A 
>>> z = zip(x, y)
>>> list(z)
[(1, 'a'), (2, 'b'), (3, 'c')]    #B


>>> x = [1, 2, 2, 3, 5, 2, 5]
>>> x.count(2)
3
>>> x.count(5)
2
>>> x.count(4)
0

print("------------------------------------------------------------")  # 60個

13.9 Shelving objects

>>> import shelve
>>> book = shelve.open("addresses")

>>> book['flintstone'] = ('fred', '555-1234', '1233 Bedrock Place')
>>> book['rubble'] = ('barney', '555-4321', '1235 Bedrock Place') 


>>> book.close()

>>> import shelve
>>> book = shelve.open("addresses")

>>> book['flintstone']
('fred', '555-1234', '1233 Bedrock Place')




print("------------------------------------------------------------")  # 60個


https://github.com/yenlung
https://github.com/packtpublishing/python-deep-learning

05. SVM

前面線性迴歸的結果有點遜, 不過我們可能會覺得那是因為我們使用的方法不夠高級。現在我們來用個高級的 SVM。

支持向量機, 大家都用英文縮寫 SVM 稱呼。是一個用曲線把資料分隔的辦法。在高維度的時候自然就是曲面 (超曲面) 分隔資料的方法。



np檢查兩個陣列是否相等
na1 = np.range
na2 = np.linspace(-5, 5, 1000)
na3 = ....

np.array_equal(clf.labels_, clf.predict(x))
True

list(range(10))

print("------------------------------------------------------------")  # 60個



#2-4-2 走訪二維 list
fruits = [
  ['apple', 'red'],
  ['banana', 'yellow'],
  ['guava', 'green'],
  ]

for fruit in fruits:   #第一層 for 迴圈 (走訪 list)
  for item in fruit:    #第二層 for 迴圈 (走訪子 list)
    print(item)


#2-5-3 用 zip() 同時走訪多個 list
index_list = ['a', 'b', 'c', 'd', 'e']
animal_list = ['dog', 'cat', 'monkey', 'bird', 'elephant']
print(list(zip(index_list, animal_list)))


fruits = ['apple', 'peach', 'banana', 'guava', 'papaya']
colors = ['red', 'pink', 'yellow', 'green', 'orange']
for name, color in zip(fruits, colors):
  print(name, 'is', color)

print("------------------------------------------------------------")  # 60個

字串格式化：format()
fruits = [
  ['apple', 6],
  ['banana', 2],
  ['guava', 3],
  ]

for name, num in fruits:
  print('{} 有 {} 個'.format(name, num))

for name, num in fruits:
  print(f'{name} 有 {num} 個')

------------------------------------------

LinearRegression

print('查詢已安裝的 sklearn 版本')
print(sklearn.__version__)

print(sklearn.version.version)


要跳過的關鍵字
print('55')
filename = 'engnews.txt'
with open(filename, "r", encoding="utf-8") as f:
    data = f.read()
special_chars = list("(),.“”")

print(special_chars)
for char in special_chars:
    data = data.replace(char, "")
data = data.split()
print(data)

sys.exit()





------------------------

plt.plot(t, t, 'r--')
plt.plot( t, [2,4,6,8], 'bs')
plt.plot( t, [3,6,9,12], 'g^')
plt.plot( t, [4,8,12,16], 'k:')


# pip install open-python
# pip install opencv-contrib-python

import cv2
print(cv2.__version__)




Python 資料科學實戰教本：爬蟲、清理、資料庫、視覺化、探索式分析、機器學習建模，數據工程一次搞定！


Python 刷題鍛鍊班：老手都刷過的50道程式題，求職面試最給力(附 Jupyter Notebook / Python Tutor 範例程式及原作者177分鐘線上教學影片)
作者： Reuven M. Lerner  

https://www.youtube.com/playlist?list=PLA5TE2ITfeXSNSoqvV8u4QZjOqfK1L-_W








pip install "scikit_learn==0.22.2.post1"

pip show scikit-learn

pip install scikit-learn scipy matplotlib numpy
pip install scikit-learn scipy matplotlib numpy

#alternative if you get permissions error
pip install scikit-learn scipy matplotlib numpy --user



plt.title('$ y = sinc(x^2) $') #直接支援LaTeX超棒ㄝㄝ



x = np.arange(0, 10, 0.1)
y = np.exp(x)
plt.plot(x, y)
plt.title("exponential function: $ y = e^x $")
plt.ylim(0, 5000)  # yを0-5000の範囲に限定



xmin, xmax = -np.pi, np.pi
x = np.arange(xmin, xmax, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.hlines([-1, 1], xmin, xmax, linestyles="dashed")  # y=-1, 1に破線を描画
plt.title(r"$\sin(x)$ and $\cos(x)$")
plt.xlim(xmin, xmax)
plt.ylim(-1.3, 1.3)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



下載
https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
將檔案改名成
cifar-10-batches-py.tar.gz
放在C:/Users/070601/.keras\datasets/之下


https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz
https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz
https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz

    plt.imshow(image, 'gray')
    #plt.imshow(X_test[i].reshape((28,28)), "gray")


print('------------------------------------------------------------')	#60個

import sys
import numpy
import pandas as pd
import sklearn
import matplotlib
import keras
print("Python version:", sys.version)
print("Numpy version:", numpy.version.version)
print("Pandas version:", pd.__version__)
print("Scikit-learn version:", sklearn.__version__)
print("Matplotlib version:", matplotlib.__version__)
print("Keras version:", keras.__version__)




## 取得發票號碼
### 安裝
```
pip insall invoiceTW
```
### 含入模組
```
from invoiceTW import invoice
```
### 使用
```
invoice.get_current()
```
傳回值：
```
{'title': '109年11月、12月', '特別獎': '77815838', '特獎': '39993297', '頭獎': '59028801、02813820、06896234', '增開六獎': '011、427'}
```









def modifySong(songStr):            # 將歌曲的標點符號用空字元取代       
    for ch in songStr:
        if ch in ".,?":
            songStr = songStr.replace(ch,'')
    return songStr                  # 傳回取代結果


def wordCount(songCount):
    songList = songCount.split()    # 將歌曲字串轉成串列
    print("以下是歌曲串列")
    print(songList)
    for wd in songList:
        if wd in mydict:
            mydict[wd] += 1
        else:
            mydict[wd] = 1



mydict = {}                         # 空字典未來儲存單字計數結果

wordCount(song)                     # 執行歌曲單字計數
print("以下是最後執行結果")
print(mydict)                       # 列印字典



import string

    
abc = string.printable[:-3]             # 取消不可列印字元
subText = abc[-3:] + abc[:-3]           # 加密字串字串
encry_dict = dict(zip(subText, abc))    # 建立字典

print(encry_dict)




layer0 TPG

layer3 GUI








min_size = (20, 20)
image_scale = 2
haar_scale = 1.2
min_neighbors = 2
haar_flags = 0



        faces = cv2.HaarDetectObjects(small_img, cascade, cv2.CreateMemStorage(0),
                                     haar_scale, min_neighbors, haar_flags, min_size)



        if faces:
            for ((x, y, w, h), n) in faces:
                # the input to cv2.HaarDetectObjects was resized, so scale the
                # bounding box of each face and convert it to two CvPoints
                pt1 = (int(x * image_scale), int(y * image_scale))
                pt2 = (int((x + w) * image_scale), int((y + h) * image_scale))
                cv2.Rectangle(img, pt1, pt2, cv2.RGB(255, 0, 0), 3, 8, 0)




        t = cv.GetTickCount()
        faces = cv.HaarDetectObjects(small_img, cascade, cv.CreateMemStorage(0),
                                     haar_scale, min_neighbors, haar_flags, min_size)
        t = cv.GetTickCount() - t
        print "detection time = %gms" % (t/(cv.GetTickFrequency()*1000.))



--------


        template = (
            '  %r != %r\n'
            '  values differ by more than tol=%r and rel=%r\n'
            '  -> absolute error = %r\n'
            '  -> relative error = %r'
            )
        return template % (first, second, tol, rel, abs_err, rel_err)

class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)


if __name__ == "__main__":
    main()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python-100-Days-zh_TW-master\Day01-15\code\Day08\circle.py

"""
练习
修一个游泳池 半径(以米为单位)在程序运行时输入 游泳池外修一条3米宽的过道
过道的外侧修一圈围墙 已知过道的造价为25元每平米 围墙的造价为32.5元每米
输出围墙和过道的总造价分别是多少钱(精确到小数点后2位)

Version: 0.1
Author: 骆昊
Date: 2018-03-08
"""

import math


class Circle(object):

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius if radius > 0 else 0

    @property
    def perimeter(self):
        return 2 * math.pi * self._radius

    @property
    def area(self):
        return math.pi * self._radius * self._radius


if __name__ == '__main__':  
    radius = float(input('请输入游泳池的半径: '))
    small = Circle(radius)
    big = Circle(radius + 3)
    print('围墙的造价为: ￥%.1f元' % (big.perimeter * 115))
    print('过道的造价为: ￥%.1f元' % ((big.area - small.area) * 65))


print("------------------------------------------------------------")  # 60個

"""
另一种创建类的方式

Version: 0.1
Author: 骆昊
Date: 2018-03-08
"""


def bar(self, name):
    self._name = name


def foo(self, course_name):
    print('%s正在学习%s.' % (self._name, course_name))


def main():
    Student = type('Student', (object,), dict(__init__=bar, study=foo))
    stu1 = Student('骆昊')
    stu1.study('Python程序设计')


if __name__ == '__main__':
    main()  

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python-100-Days-zh_TW-master\Day01-15\code\Day08\rect.py

"""
定义和使用矩形类

Version: 0.1
Author: 骆昊
Date: 2018-03-08
"""


class Rect(object):
    """矩形类"""

    def __init__(self, width=0, height=0):
        """初始化方法"""
        self.__width = width
        self.__height = height

    def perimeter(self):
        """计算周长"""
        return (self.__width + self.__height) * 2

    def area(self):
        """计算面积"""
        return self.__width * self.__height

    def __str__(self):
        """矩形对象的字符串表达式"""
        return '矩形[%f,%f]' % (self.__width, self.__height)

    def __del__(self):
        """析构器"""
        print('销毁矩形对象')


if __name__ == '__main__':
    rect1 = Rect()
    print(rect1)
    print(rect1.perimeter())
    print(rect1.area())
    rect2 = Rect(3.5, 4.5)
    print(rect2)
    print(rect2.perimeter())
    print(rect2.area())

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python-100-Days-zh_TW-master\Day01-15\code\Day08\student.py

"""
定义和使用学生类

Version: 0.1
Author: 骆昊
Date: 2018-03-08
"""


def _foo():
    print('test')


class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是很多程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_av(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国大电影.' % self.name)


def main():
    stu1 = Student('骆昊', 38)
    stu1.study('Python程序设计')
    stu1.watch_av()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_av()


if __name__ == '__main__':
    main()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

字串的方法
.replace()
.reverse()
.sort()
.split()


seq = [333, 555, 888]                # 年度
plt.xticks(seq)                         # 設定x軸刻度


lineBenz, = plt.plot(seq, Benz, '-*', label='Benz')
lineBMW, = plt.plot(seq, BMW, '-o', label='BMW')
lineLexus, = plt.plot(seq, Lexus, '-^', label='Lexus')

plt.legend(handles=[lineBenz, lineBMW, lineLexus], loc=0)
plt.tick_params(axis='both', labelsize=12, color='red')



seq = [2018, 2019, 2020]                # 年度
plt.xticks(seq)                         # 設定x軸刻度
lineBenz, = plt.plot(seq, Benz, '-*', label='Benz')
lineBMW, = plt.plot(seq, BMW, '-o', label='BMW')
lineLexus, = plt.plot(seq, Lexus, '-^', label='Lexus')

plt.legend(handles=[lineBenz, lineBMW, lineLexus], loc='best')

plt.tick_params(axis='both', labelsize=12, color='red')


lineBenz, = plt.plot(seq, Benz, '-*', label='Benz')
lineBMW, = plt.plot(seq, BMW, '-o', label='BMW')
lineLexus, = plt.plot(seq, Lexus, '-^', label='Lexus')

plt.legend(handles=[lineBenz, lineBMW, lineLexus], loc='upper right')
plt.tick_params(axis='both', labelsize=12, color='red')


seq = [2018, 2019, 2020]                # 年度
plt.xticks(seq)                         # 設定x軸刻度
lineBenz, = plt.plot(seq, Benz, '-*', label='Benz')
lineBMW, = plt.plot(seq, BMW, '-o', label='BMW')
lineLexus, = plt.plot(seq, Lexus, '-^', label='Lexus')

plt.legend(handles=[lineBenz, lineBMW, lineLexus], loc='upper left',
           bbox_to_anchor=(1,1))
plt.tick_params(axis='both', labelsize=12, color='red')


seq = [2018, 2019, 2020]                # 年度
plt.xticks(seq)                         # 設定x軸刻度
lineBenz, = plt.plot(seq, Benz, '-*', label='Benz')
lineBMW, = plt.plot(seq, BMW, '-o', label='BMW')
lineLexus, = plt.plot(seq, Lexus, '-^', label='Lexus')
plt.legend(handles=[lineBenz, lineBMW, lineLexus], loc='upper left',
           bbox_to_anchor=(1,1))
plt.tight_layout(pad=7)

plt.tick_params(axis='both', labelsize=12, color='red')


seq = [2018, 2019, 2020]                            # 年度
plt.xticks(seq)                                     # 設定x軸刻度
lineBenz, = plt.plot(seq, Benz, '-*', label='Benz')
lineBMW, = plt.plot(seq, BMW, '-o', label='BMW')
lineLexus, = plt.plot(seq, Lexus, '-^', label='Lexus')

plt.legend(handles=[lineBenz, lineBMW, lineLexus])

plt.tick_params(axis='both', labelsize=12, color='red')
#plt.savefig('out20_13.jpg', bbox_inches='tight')    # 存檔

seq = [2018, 2019, 2020]                # 年度
plt.xticks(seq)                         # 設定x軸刻度
lineBenz, = plt.plot(seq, Benz, '-*', label='Benz')
lineBMW, = plt.plot(seq, BMW, '-o', label='BMW')
lineLexus, = plt.plot(seq, Lexus, '-^', label='Lexus')

plt.legend(handles=[lineBenz, lineBMW, lineLexus])

plt.tick_params(axis='both', labelsize=12, color='red')



seq = [2018, 2019, 2020]                # 年度
plt.xticks(seq)                         # 設定x軸刻度
lineBenz, = plt.plot(seq, Benz, '-*', label='Benz')
lineBMW, = plt.plot(seq, BMW, '-o', label='BMW')
lineLexus, = plt.plot(seq, Lexus, '-^', label='Lexus')

plt.legend(handles=[lineBenz, lineBMW, lineLexus], loc=6)
plt.tick_params(axis='both', labelsize=12, color='red')



plt.scatter(xpt, ypt1, color=(0, 1, 0)) # 綠色
plt.scatter(xpt, ypt, c=(0, 1, 0))  # 綠色
plt.scatter(xpt, ypt, color='y')

plt.tick_params(axis='both', labelsize=12, color='red')





while True:
    do_something

    yORn = input("是否繼續 ?(y/n) ")            # 詢問是否繼續
    if yORn == 'n' or yORn == 'N':              # 輸入n或N則程式結束
        break
    
with open(fn) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
    data = file_Obj.read()  # 讀取檔案到變數data
    print(data)                 # 輸出變數data相當於輸出檔案





print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

# 將字串反轉
def reverse_str(s):
    return s[::-1]

print("------------------------------------------------------------")  # 60個

# 計算一個字串中指定字符的出現次數
def count_char(s, c):
    count = 0
    for char in s:
        if char == c:
            count += 1
    return count

print("------------------------------------------------------------")  # 60個

sigma=0
k = 30
for n in range(0,k,1):
    if n & 1: #如果n是奇數
        sigma += float(-1/(2*n+1))
    else: #如果n是偶數
        sigma += float(1/(2*n+1))
print("PI = %f" %(sigma*4))


print("總銷售業績{},應付獎金：{}".format(e1, e2))

print("------------------------------------------------------------")  # 60個


ticks寫法
plt.xticks([-2*np.pi,-np.pi,0, np.pi, 2*np.pi],['-$2\pi$', '-$\pi$','0', '$\pi$', '$2\pi$'])

legend寫法
plt.legend(['sin','cos'],loc=3,fontsize='xx-large',edgecolor='y',facecolor='r')


依次設定兩個串列 / numpy.ndarray
x = np.linspace(-2*np.pi, 2*np.pi, 100)
s, c=np.sin(x), np.cos(x)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

OpenCV / PIL 整理 pillow

opencv01

0類 基本顯示類
opencv0	顯示 info
PIL0

1類 不修圖處理類
opencv1	顯示 裁剪 複製 剪貼 縮放 旋轉 鏡像 存檔
PIL1


2類 畫圖類
opencv2	顯示 畫圖

3類 影像處理類
opencv3	顯示 影像處理

4類 Video處理類
資料夾 opencv4_video

8類 其他
opencv8_other

9類 新進
資料夾 opencv9_new	



----
# Set up the constants:
SUSPECTS = ['DUKE HAUTDOG', 'MAXIMUM POWERS', 'BILL MONOPOLIS', 'SENATOR SCHMEAR', 'MRS. FEATHERTOSS', 'DR. JEAN SPLICER', 'RAFFLES THE CLOWN', 'ESPRESSA TOFFEEPOT', 'CECIL EDGAR VANDERTON']
ITEMS = ['FLASHLIGHT', 'CANDLESTICK', 'RAINBOW FLAG', 'HAMSTER WHEEL', 'ANIME VHS TAPE', 'JAR OF PICKLES', 'ONE COWBOY BOOT', 'CLEAN UNDERPANTS', '5 DOLLAR GIFT CARD']
PLACES = ['ZOO', 'OLD BARN', 'DUCK POND', 'CITY HALL', 'HIPSTER CAFE', 'BOWLING ALLEY', 'VIDEO GAME MUSEUM', 'UNIVERSITY LIBRARY', 'ALBINO ALLIGATOR PIT']
TIME_TO_SOLVE = 300  # 300 seconds (5 minutes) to solve the game.

# First letters and longest length of places are needed for menu display:
PLACE_FIRST_LETTERS = {}
LONGEST_PLACE_NAME_LENGTH = 0
for place in PLACES:
    PLACE_FIRST_LETTERS[place[0]] = place
    if len(place) > LONGEST_PLACE_NAME_LENGTH:
        LONGEST_PLACE_NAME_LENGTH = len(place)

# Basic sanity checks of the constants:
assert len(SUSPECTS) == 9
assert len(ITEMS) == 9
assert len(PLACES) == 9
# First letters must be unique:
assert len(PLACE_FIRST_LETTERS.keys()) == len(PLACES)



----




"""
print('請輸入密碼 :')
response = input('> ').upper().strip()
  action = input('> ').upper().strip()
print('----------------')
print(response)
print('----------------')
"""



# Colab 使用，本機環境請刪除
from flask_ngrok import run_with_ngrok

# import os
# os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用


print("------------------------------------------------------------")  # 60個



import os
os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除


vcs待尋找
目前用webbrowser顯示pdf檔案, 無法用程式的方法得知此時看到第幾頁 也無法得知目前頁面顯示比例



tk參數最齊全

lblShow = Label(root, text = 'Hello Python!!',
    width = 20, height = 4, fg = 'white', bg = 'gray')


# 設定標籤的顯示文字(text)、背景(bg)和前景(fg)顏色
lbla = Label(root, text = 'Gray', bg = 'gray',
        fg = 'white').pack(side = 'right')#加入版面

lblb = Label(root, text = 'Yellow',
        bg = 'yellow', fg = 'gray').pack(
        side = 'right', padx = 5, pady = 10)

lblc = Label(root, text = 'Orange', bg = 'orange', fg = 'gray').pack(side = 'right')


# 設定標籤的顯示文字(text)、背景(bg)和前景(fg)顏色
lbla = Label(root, text = 'Gray', bg = 'gray', fg = 'white').pack()#加入版面

lblb = Label(root, text = 'Yellow', bg = 'yellow', fg = 'gray').pack()

lblc = Label(root, text = 'Orange', bg = 'orange', fg = 'gray').pack()


photo = PhotoImage(file = '001.png')#建立圖片

#標籤 - bg 設背景色
t1 = Label(wnd, text = 'Hello\n Python', bg = '#78A', 
    fg = '#FF0', relief = 'groove', bd = 2, 
    width = 15, height = 3, justify = 'right')

t2 = Label(wnd, text = '世界', width = 6, height = 3,
    relief = RIDGE, bg = 'pink', font = ('標楷體', 16))

#在第3個標籤載入圖片
t3 = Label(wnd, image = photo, relief = 'sunken',
    bd = 5, width = 180, height = 150)

t1.grid(row = 0, column = 0)
t2.grid(row = 0, column = 1)
t3.grid(columnspan = 2)


print("------------------------------------------------------------")  # 60個



             /* info
            richTextBox1.Text += "aaa: " + pfc.Families.Length.ToString() + "\n";
            for (int i = 0; i < pfc.Families.Length; i++)
            {
                richTextBox1.Text += "aaa: " + pfc.Families[i].Name + "\n";
            }

            richTextBox1.Text += "\n";
            richTextBox1.Text += f.FontFamily.ToString() + "\n";
            richTextBox1.Text += "字型名稱: " + f.FontFamily.Name + "\n";
            //richTextBox1.Text += "字型名稱: " + f.Name + "\n";    same
            */

 



with open(filename, encoding='utf-8-sig') as file_Obj: # utf-8-sig





指定 ZIP 檔名的編碼方式
・cp932　…日文
・cp950　…繁體中文
・cp936　…簡體中文
・cp874　…泰文
・utf-8  　…UTF-8

GB2312是中国规定的汉字编码，也可以说是简体中文的字符集编码

GBK 是 GB2312的扩展 ,除了兼容GB2312外，它还能显示繁体中文，还有日文的假名

cp936：中文本地系统是Windows中的cmd，默认codepage是CP936，cp936就是指系统里第936号编码格式，即GB2312的编码。
(当然有其它编码格式：cp950 繁体中文、cp932 日语、cp1250 中欧语言。。。)

Unicode是国际组织制定的可以容纳世界上所有文字和符号的字符编码方案。UTF-8、UTF-16、UTF-32都是将数字转换到程序数据的编码方案。

UTF-8 （8-bit Unicode Transformation Format）是最流行的一种对 Unicode 进行传播和存储的编码方式。它用不同的 bytes 来表示每一个代码点。ASCII 字符每个只需要用一个 byte ，与 ASCII 的编码是一样的。所以说 ASCII 是 UTF-8 的一个子集。

chardet模块

 chardet是一个非常优秀的编码识别模块。

通过pip 安装：

>pip install chardet



import this

#網頁連線https://xkcd.com/353/
import antigravity

print("------------------------------------------------------------")  # 60個







----------------tkinter ST tktk----------------




----------------tkinter SP tktk----------------

