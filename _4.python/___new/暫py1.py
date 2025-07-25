
程式內不能用 \　Backslash (反斜線)
在 檔案路徑, 要改用 \\ 或 /
在註解內 black會報錯

vcs抓打鼓節奏

opencv目前像是不能做到動畫功能
例如

gamma 由 0:0.01:1 變化

圖片連續顯示之


------------------------------------------------------------

"""
HSV簡單介紹分別為：
色相(H)：色彩的顏色名稱，如紅色、黃色等。
飽和度(S)：色彩的純度，越高色彩越純，低則逐漸變灰，數值為0-100%。
明度(V)：亮度，數值為0-100%。
"""

------------------------------------------------------------


------------------------------------------------------------



------------------------------------------------------------

----------------一句話說明python模組 ST----------------

pickle --- Python 物件序列化

Selenium	瀏覽器自動化操操作
PyAutoGUI	鍵盤滑鼠自動化
gradio		神奇網頁互動介面
schedule	定時執行任務
tqdm		進度條
cnlunardate	農曆日期


selenium模組 : 瀏覽器自動化操作
PyAutoGUI模組 : 鍵盤滑鼠自動化


開放原碼專案名稱	簡述
TensorFlow		機器學習框架
OpenCV			電腦視覺工具
PyTorch			機器學習函式庫
Keras			機器學習函式庫
Stable Diffusion	文字轉圖像的擴散模型
DeepFaceLab		比DeepFaake更強大的AI偽造技術
Theano			函式庫與最佳化編譯器
YOLOv7			即時物件偵測模型



----------------一句話說明python模組 SP----------------


----------------Colab ST----------------

"""
# 選取檔案的寫法
from google.colab import files
uploaded = files.upload()
print(uploaded)
"""

print('aaa')
cc = os.listdir("/content/drive/My Drive/Colab Notebooks")
print(cc)

print('bbb')

df = pd.read_csv("/content/drive/MyDrive/CSV/iris_sample.csv")
cc = df.head()
print(cc)

print('ccc')

import matplotlib
import matplotlib.font_manager as fm
!wget -O MicrosoftJhengHei.ttf https://github.com/a7532ariel/ms-web/raw/master/Microsoft-JhengHei.ttf
!wget -O ArialUnicodeMS.ttf https://github.com/texttechnologylab/DHd2019BoA/raw/master/fonts/Arial%20Unicode%20MS.TTF
 
fm.fontManager.addfont('MicrosoftJhengHei.ttf')
matplotlib.rc('font', family='Microsoft Jheng Hei')
 
fm.fontManager.addfont('ArialUnicodeMS.ttf')
matplotlib.rc('font', family='Arial Unicode MS')

------------------------------------------------------------
# colab
------------------------------------------------------------

"""
os.chdir("/content/")
"""

from google.colab import drive
drive.mount("/content/drive")
# drive.mount("/content/drive", force_remount=True)

os.chdir("/content/drive/MyDrive/data/ch08")  # 使用 Colab 要換路徑使用，本機環境可以刪除
filenames = os.listdir()  # 轉出一層, 指定目錄, 若無參數, 就是當前目錄
print("4轉出一層(資料夾+檔案)\n", filenames)
print("當前目錄下共有 :", len(filenames), "個項目(資料夾+檔案)")

if os.path.isfile("img3.jpg"):
  print('有')
else:
  print('無')

if os.path.isfile("/content/yolo.h5"):
  print('有')
else:
  print('無')



colab執行Shell命令 !
!pip install pytube
!pip list
!pwd
!ls

魔術指令 %
%lsmagic	顯示所有可用的魔術指令
#cd
## writefile filename 寫檔
#run filename
 
jupyter 命令
!cat /proc/cpuinfo
!bash



import os
from google.colab import drive
drive.mount("/content/drive")

# 此時在目錄/content/drive下
filenames = os.listdir()  # 轉出一層, 指定目錄, 若無參數, 就是當前目錄
print("1轉出一層(資料夾+檔案)\n", filenames)
print("當前目錄下共有 :", len(filenames), "個項目(資料夾+檔案)")

# 至我的雲端硬碟根目錄MyDrive
os.chdir("/content/drive/MyDrive")  # 使用 Colab 要換路徑使用，本機環境可以刪除
filenames = os.listdir()  # 轉出一層, 指定目錄, 若無參數, 就是當前目錄
print("2轉出一層(資料夾+檔案)\n", filenames)
print("當前目錄下共有 :", len(filenames), "個項目(資料夾+檔案)")

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除
filenames = os.listdir()  # 轉出一層, 指定目錄, 若無參數, 就是當前目錄
print("3轉出一層(資料夾+檔案)\n", filenames)
print("當前目錄下共有 :", len(filenames), "個項目(資料夾+檔案)")

os.chdir("/content/drive/MyDrive/CSV")  # 使用 Colab 要換路徑使用，本機環境可以刪除
filenames = os.listdir()  # 轉出一層, 指定目錄, 若無參數, 就是當前目錄
print("4轉出一層(資料夾+檔案)\n", filenames)
print("當前目錄下共有 :", len(filenames), "個項目(資料夾+檔案)")



colab通用之

一開始的ls

寫檔案是寫在哪裡? 會永久留存嗎?



檔案/在GitHub中儲存副本 / 或使用colab編輯GitHub上的檔案，按儲存

存放區
bunshue/vcs

檔案路徑
_4.python/ipynb/ddd0529.ipynb

記得打勾加入Colab連結

------------------------------

編輯/筆記本設定/選GPU

------------------------------

"""
GPU
1.安裝: pip install nvidia-ml-py3
2.#常用的指令：
import pynvml
pynvml.nvmlInit()
# 這裏的0是GPU id
handle = pynvml.nvmlDeviceGetHandleByIndex(0)
meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)
print(meminfo.used)
3. 指令參考網址:https://docs.nvidia.com/deploy/nvml-api/group__nvmlDeviceQueries.html#group__nvmlDeviceQueries
"""

------------------------------------------------------------

#!cp  /content/db.sqlite3          "/content/drive/MyDrive/Colab Notebooks/package/tchinese_db.sqlite3"
#!cp "/content/drive/MyDrive/Colab Notebooks/package/tchinese_db.sqlite3" /content/db.sqlite3

------------------------------------------------------------

#Colab資料夾設定方法
!pip install google.colab 
!pip install google.colab
!pip install google.colab

"""
!mkdir -p /drive
#umount /drive
!mount --bind /content/drive/My\ Drive /drive
!mkdir -p /drive/ngrok-ssh
!mkdir -p ~/.ssh

----

!mkdir -p /drive/ngrok-ssh
%cd /drive/ngrok-ssh
!wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip -O ngrok-stable-linux-amd64.zip
!unzip -u ngrok-stable-linux-amd64.zip
!cp /drive/ngrok-ssh/ngrok /ngrok
!chmod +x /ngrok
"""

------------------------------------------------------------

"""
!mkdir -p /drive
!mount --bind /content/drive/My\ Drive /drive
!mkdir -p /drive/ngrok-ssh
!mkdir -p ~/.ssh

------------------------------------------------------------

!mkdir -p /drive/ngrok-ssh
%cd /drive/ngrok-ssh
!wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip -O ngrok-stable-linux-amd64.zip
!unzip -u ngrok-stable-linux-amd64.zip
!cp /drive/ngrok-ssh/ngrok /ngrok
!chmod +x /ngrok
"""

------------------------------------------------------------


----------------Colab SP----------------


python 之 ''' 與  ''' 內, 不可以存在 \

程式內不允許有 \ 反切


在tk內顯示opencv

np.meshgrid為numpy之函數

用scatter 用3d表示之


唐三藏 Tang
孫悟空 Monkey
豬八戒 Pig
沙悟淨 Sand
白龍馬 Horse

二郎神
千里眼 Eye
順風耳 Ear

牛魔王 Ox
紅孩兒 Child
白骨精 Bone
蜘蛛精 Spider


還是應該要有一個vcs螢幕截圖的常駐程式  隨時要用 例如 看yt時


[, , , , , 
, , 87, 98, 97, 87, 79, 74, 79, 82, 79, 73, 87, 90, 71, 82, 92, 92, 86, 94, 85
, 94, 76, 87, 75, , 89, 85, 82, 87, 88, 78, 94, 93, 92, 87, 72, 95, 99, 83, 89, 85
, 93, 90, 72, 91, 75, 97, 77, 84, 94, 98, 71, 80, 87, 93, 77, 93, 83, 85, 99, 79, 79, 82, 78, 71
, 91, 82, 74, 78, 83, 90, 75, 76, 96, 94, 81, 74, 96, 73, 84, 72, 99, 97, 95, 87, 89, 99, 75, 88



Python的應用領域

目前Python在Web應用開發、雲基礎設施、DevOps、網絡爬蟲開發、數據分析挖掘、機器學習等領域都有著廣泛的應用，因此也產生了Web後端開發、數據接口開發、自動化運維、自動化測試、科學計算和可視化、數據分析、量化交易、機器人開發、圖像識別和處理等一系列的職位。


OK
《Python Cookbook in Chinese》 3rd Edition 翻译

《Python Cookbook》3rd 中文版3.0.0正式发布

在线阅读地址：http://python3-cookbook.readthedocs.org/zh_CN/latest/

最新版(3.0.0)下载

    中文简体版PDF下载地址：https://pan.baidu.com/s/1pL1cI9d
    中文繁体版PDF下载地址：https://pan.baidu.com/s/1qX97VJI



《Python 神乎其技》免費教學文章整理
https://haosquare.com/python-tricks/



python
https://pythonziliao.com/post/826.html


MediaPipe 解決方案指南
https://ai.google.dev/edge/mediapipe/solutions/guide?hl=zh-tw


安裝MediaPipe執行環境
https://sites.google.com/view/zsgititit/home/ji-qi-xue-xi/%E5%AE%89%E8%A3%9Dmediapipe%E5%9F%B7%E8%A1%8C%E7%92%B0%E5%A2%83

使用 MediaPipe ( 舊版 )
https://steam.oxxostudio.tw/category/python/ai/ai-mediapipe.html#google_vignette

Python的串口使用，自
https://fantasyhh.github.io/2019/08/01/Arduino-Serial/


Matplotlib 立體圖
https://openhome.cc/Gossip/DCHardWay/Axes3D.html


matplotlib的二维作图及三维作图 ax.plot_wireframe， scatter
https://www.cnblogs.com/tangjunjun/articles/10854423.html


標準化py文件

ABC.txt
poem.txt
article.txt
big5 gb2312... formats
	animals.csv

sqlite之簡易版範例 for animals
簡易之資料庫增刪查改範例

MyDictionary

csv檔 => 字典 = > 資料庫

資料庫增刪改查搜尋

增刪查改	CDRU
CRUD

CRUD (新增:Create , 讀取:Read, 更新: Update, 刪除:Delete)
增	新增:Create	POST
查	讀取:Read	GET
改	更新:Update	PUT
刪	刪除:Delete

增刪查改（英語：CRUD）
增加（Create，意為「建立」）
刪除（Delete）
查詢（Read，意為「讀取」）
改正（Update，意為「更新」）
在電腦程式語言中是一連串常見的動作行為
而其行為通常是為了針對某個特定資源所作出的舉動（例如：建立資料、讀取資料等）

莫煩 python
https://mofanpy.com/

https://github.com/MorvanZhou

turtle 指令
turtle.Screen().reset()

做一個完整版 TextEditor 大整理



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


C:\_git\vcs\_4.python\__code\高效率Python自動化工作術\chap10

PySimpleGUI	建立應用程式的函示庫
mutagen	讀取與存寫語音檔的函示庫


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

------------------------------------------------------------


------------------------------------------------------------

filename1 = 'C:/_git/vcs/_4.python/_data/picture_mix1.bmp'
filename2 = 'C:/_git/vcs/_4.python/_data/picture_mix2.bmp'

picture_add1.bmp
picture_add2.bmp

newimg.paste(img, mask=img)             # 將PNG檔壓在白底圖片上

image.paste(icon, (0, 0), icon)  # 加入浮水印

移動檔案指標

seek 要以binary開檔 才會正確

seek(偏移量, 起算位置)

起算位置 0 從頭開始算
起算位置 1 從目前位置起算
起算位置 2 從尾開始算

f.seek(0, 0) 將指標移到檔案頭
f.seek(3, 1) 從現在位置往後移動3個字
f.seek(-5, 2) 從最後面往前移動5個字




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


------------------------------------------------------------

串列操作
        x[0] = x[num - 1]  # 上次結束x座標成新的起點x座標
        y[0] = y[num - 1]  # 上次結束y座標成新的起點y座標
        del x[1:]  # 刪除舊串列x座標元素
        del y[1:]  # 刪除舊串列y座標元素

------------------------------------------------------------

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


------------------------------------------------------------




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



《幸運的基督徒》
有15個基督徒和15個非基督徒在海上遇險，為了能讓一部分人活下來不得不將其中15個人扔到海里面去，有個人想了個辦法就是大家圍成一個圈，由某個人開始從1報數，報到9的人就扔到海里面，他後面的人接著從1開始報數，報到9的人繼續扔到海里面，直到扔掉15個人。由於上帝的保佑，15個基督徒都倖免於難，問這些人最開始是怎麼站的，哪些位置是基督徒哪些位置是非基督徒。


Python機器學習
1. sklearn(scikit-learn)機器學習
2. TensorFlow深度學習
3. Keras深度學習


python的日期當中分成
1. date(日期)
2. time(時間)
3. datetime(混合date跟time)
4. timedelta(計算歷時期間的型態)
5. timezone(處理時區資訊的型態)


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



套件(package) : 多個模組組合在一起
套件就是一個模組庫 函式庫


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

cmd / where python	//了解目前電腦安裝多少版本

cmd / python --version	//了解目前命令提示字元視窗執行Python的版本


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

------------------------------------------------------------

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


''' & '''  可執行的 但不執行的

""" & """ 放不能執行的

這樣才可做到用 ''' 包圍 """, 可以簡易地跳過不要執行的程式

cur_path = os.path.dirname(__file__) # 取得目前路徑

------------------------------------------------------------


------------------------------------------------------------


------------------------------------------------------------


'''
暫存資料 全

'''

----------------常用的程式片段 ST cccc----------------

import datetime
print(f"現在時刻 : {datetime.datetime.now()}")

foldername = 'C:/_git/vcs/_1.data/______test_files5'

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/SpongeBob.gif'

video_filename = "C:/_git/vcs/_4.python/opencv/data/_video/spiderman.mp4"

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_word/python_docx1.docx'
filename = 'C:/_git/vcs/_1.data/______test_files2/output.avi'

filename1 = 'C:/_git/vcs/_4.python/_data/elephant.jpg'
filename2 = 'C:/_git/vcs/_4.python/_data/tiger.jpg'
filename3 = 'C:/_git/vcs/_4.python/_data/bear.jpg'

filenames = [filename1, filename2, filename3]

for filename in filenames:
    print(filename)

print("------------------------------------------------------------")	#60個

用兩連線分隔主題
print("------------------------------------------------------------")	#60個
print("------------------------------------------------------------")	#60個

用半連線分隔主題內之分支
print("------------------------------")	#30個



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
  
------------------------------------------------------------

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

------------------------------------------------------------

sys.stdout = sys.stderr
print('usage: findlinksto pattern directory ...')

------------------------------------------------------------

------------------------------------------------------------

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

------------------------------------------------------------

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

------------------------------------------------------------

print(__doc__ % globals())

print("-"*70)

------------------------------------------------------------def chop(line):

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

------------------------------------------------------------
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

------------------------------------------------------------
 
#width 選項的單位是文字單位，而不是畫素

字串處理

#url = input("請輸入網址：")
url = 'https://www.google.com.tw/'
if url.startswith("http://") or url.startswith("https://"):
    print("輸入的網址格式正確！")
else:
    print("輸入的網址格式錯誤！")



#熊貓是python的excel

------------------------------------------------------------

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

------------------------------------------------------------

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

------------------------------------------------------------

@app.route('/user/<username>')
def show_user(username):
    return 'User Name is {}'.format(username)

if __name__ == '__main__':
    app.run()

encoding = 'utf-8-sig'	編碼設定為將BOM去除的的utf-8編碼

https://pythex.org/

------------------------------------------------------------

    simpleaudio：播放WAV文件和NumPy數組。
    winsound：播放WAV文件或鳴響您的系統揚聲器
    https://docs.python.org/3/library/winsound.html

------------------------------------------------------------

OCR 破解驗證碼

因為驗證碼通常會有很多噪點，
我上網引用了大大寫好的降噪副程式，
先將驗證碼降噪後再進行 OCR 辨識，
會大大的提高成功率。

https://stackoverflow.max-everyday.com/2019/06/python-opencv-denoising/

------------------------------------------------------------

Python 以模組名稱 __name__ 分辨程式執行模式


------------------------------------------------------------

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

------------------------------------------------------------

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


------------------------------------------------------------


----------------import os 大集合----------------




----------------import time 大集合----------------


------------------------------------------------------------

------------------------------------------------------------

        print("%s:" % func.__name__.replace("pi_", ""))
        print("result: %s" % str(x))

------------------------------------------------------------


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

------------------------------------------------------------
#攔截ctrl-C
import math, time, sys, os

LINE_CHAR = chr(9608)  # Character 9608 is a solid block.
print(LINE_CHAR, end='', flush=False)


try:
    while True:

        print('Press Ctrl-C to quit.', end='', flush=True)

        print('a')

        time.sleep(1)  # Pause for a bit.

except KeyboardInterrupt:
    print('Rotating Cube, by Al Sweigart al@inventwithpython.com')
    sys.exit()  # When Ctrl-C is pressed, end the program.

------------------------------------------------------------

------------------------------------------------------------

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




------------------------------------------------------------



------------------------------------------------------------

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

------------------------------------------------------------

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



------------------------------------------------------------



print("The pysource module is not le search will be done.", file=sys.stderr)

------------------------------------------------------------

https://www.dreamstime.com/free-images_pg1

https://www.dreamstime.com/free-images_pg1

------------------------------------------------------------

content='''Hello Python
中文字測試
Welcome
'''

f=open('file1aaa.txt','w')
f.write(content)
f.close()

------------------------------------------------------------

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

------------------------------------------------------------

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
------------------------------------------------------------


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

------------------------------------------------------------

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
                     
                        

------------------------------------------------------------


------------------------------------------------------------

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


------------------------------------------------------------

np.arange(10)

np.arange(3, 10)

np.arange(3, 10, 0.5)

A = np.arange(10)

------------------------------------------------------------

print 格式化

name = "炎龍"
job = "老師"

print(f"你好, 我叫{name}, 我的工作是{job}。")

name = 'A機台'
output = 3.124000000000001
print(f"在{name}, 我的輸出是 {output:.2f}。")

行家超愛的 list comprehension
[i**2 for i in range(10)]

------------------------------------------------------------

        return "%s %s %2d %02d:%02d:%02d %04d" % (
            _DAYNAMES[weekday],
            _MONTHNAMES[self._month],
            self._day,
            self._hour, self._minute, self._second,
            self._year)

------------------------------------------------------------

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

------------------------------------------------------------

list的排列要指名欄位
sc.sort(key=lambda x:x[5],reverse=True)     # 依據總分高往低排序


# 以下依座號排序
sc.sort(key=lambda x:x[0])                  # 依據座號排序

------------------------------------------------------------

字典
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8 # 修改資料
dict['School'] = "DPS School" # 新增資料

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

------------------------------------------------------------

 Python列表：	//操作方式很像字串
 
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
list3 = ["a", "b", "c", "d"]

print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]
 
------------------------------------------------------------

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

------------------------------------------------------------

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

------------------------------------------------------------

# lambda: 只有單一運算式的匿名函式

add = lambda x, y: x + y

print(add(5, 3))

print((lambda x, y: x + y)(5, 3))

------------------------------------------------------------

# 在 sorted() 使用 lambda 匿名函式

tuples_list = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]


print(sorted(tuples_list))

print(sorted(tuples_list, key=lambda x: x[1]))

print(sorted(range(-5, 6), key=lambda x: x ** 2))

------------------------------------------------------------

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

------------------------------------------------------------

資料產生大範例

range

linspace

random

meshgrid

------------------------------------------------------------

#將一個google drive檔案存成本地檔案

import requests

fontfile = requests.get("https://drive.google.com/uc?id=1QdaqR8Setf4HEulrIW79UEV_Lg_fuoWz&export=download")

with open('taipei_sans_tc_beta.ttf', 'wb') as f:
  f.write(fontfile.content)

------------------------------------------------------------

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

C:\_git\vcs\_4.python>python -m pdb test10_new11.py

------------------------------------------------------------

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

ok 但是可以看看medium的英文網站
https://medium.com/py-tips-conceptes/%E6%9C%AC%E6%96%87%E7%B4%80%E9%8C%84python%E7%B9%AA%E5%9C%96%E7%9A%84%E6%96%B9%E6%B3%95-%E4%BD%BF%E7%94%A8-seaborn-255b0006eb3e

excel相關之python套件

openpyxl	讀寫.xlsx
xlrd		讀取.xls .xlsx
xlwt		寫入.xls
xlswrite	寫入.xlsx

openpyxl	讀寫.xlsx
openpyxl	讀寫.xlsx
openpyxl	讀寫.xlsx

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


            三维2D图

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

------------------------------------------------------------
基本用range

for i in range(1, 11): #定義for迴圈

for i in range(11, 21): 

for n in range(0, k, 1):
for i in range(1, 201, 2):

------------------------------------------------------------

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


------------------------------------------------------------

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

------------------------------------------------------------

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

------------------------------------------------------------

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

------------------------------------------------------------


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

------------------------------------------------------------

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




------------------------------------------------------------


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

------------------------------------------------------------



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

------------------------------------------------------------

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

------------------------

plt.plot(t, t, 'r--')
plt.plot( t, [2,4,6,8], 'bs')
plt.plot( t, [3,6,9,12], 'g^')
plt.plot( t, [4,8,12,16], 'k:')


# pip install open-python
# pip install opencv-contrib-python

Python 資料科學實戰教本：爬蟲、清理、資料庫、視覺化、探索式分析、機器學習建模，數據工程一次搞定！


Python 刷題鍛鍊班：老手都刷過的50道程式題，求職面試最給力(附 Jupyter Notebook / Python Tutor 範例程式及原作者177分鐘線上教學影片)
作者： Reuven M. Lerner  

https://www.youtube.com/playlist?list=PLA5TE2ITfeXSNSoqvV8u4QZjOqfK1L-_W



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

------------------------------------------------------------

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





--------


        template = (
            '  %r != %r\n'
            '  values differ by more than tol=%r and rel=%r\n'
            '  -> absolute error = %r\n'
            '  -> relative error = %r'
            )
        return template % (first, second, tol, rel, abs_err, rel_err)

------------------------------------------------------------

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





------------------------------------------------------------

------------------------------------------------------------

# 將字串反轉
def reverse_str(s):
    return s[::-1]

------------------------------------------------------------

# 計算一個字串中指定字符的出現次數
def count_char(s, c):
    count = 0
    for char in s:
        if char == c:
            count += 1
    return count

------------------------------------------------------------

sigma=0
k = 30
for n in range(0,k,1):
    if n & 1: #如果n是奇數
        sigma += float(-1/(2*n+1))
    else: #如果n是偶數
        sigma += float(1/(2*n+1))
print("PI = %f" %(sigma*4))


print("總銷售業績{},應付獎金：{}".format(e1, e2))

------------------------------------------------------------


ticks寫法
plt.xticks([-2*np.pi,-np.pi,0, np.pi, 2*np.pi],['-$2\pi$', '-$\pi$','0', '$\pi$', '$2\pi$'])

legend寫法
plt.legend(['sin','cos'],loc=3,fontsize='xx-large',edgecolor='y',facecolor='r')


依次設定兩個串列 / numpy.ndarray
x = np.linspace(-2*np.pi, 2*np.pi, 100)
s, c=np.sin(x), np.cos(x)

------------------------------------------------------------

------------------------------------------------------------

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

------------------------------------------------------------

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

------------------------------------------------------------

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

------------------------------------------------------------







----------------tkinter ST tktk----------------




----------------tkinter SP tktk----------------






python_install_faq.txt

1. python IDLE, anaconda, thonny
2. pip install
3. 處理模組不能使用問題
  1. 特殊版本安裝法
  2. 特殊安裝法
  3. 修改程式
  4. 修改模組





目前 sugar 的 python 版本

C:\Users\070601\Desktop>python --version
Python 3.11.2

---------------- Python PIP 使用 requirements.txt 管理套件相依性 ----------------

如何使用 pip 一次安裝多個套件
將安裝過的套件建立成 requirements.txt 套件清單：
pip freeze > requirements_sugar.txt

安裝 requirements.txt 內的套件清單：

pip install -r requirements.txt


安裝又更新所有套件
pip install -U -r requirements.txt

----------------安裝 反安裝 更新----------------

更新pip程式
python.exe -m pip install --upgrade pip

更新套件
pip install package_name --upgrade

指定安裝版本
pip install package_name==2.0.2

指定版本安裝套件

pip install urllib3==1.26.6


C:\Users\david>python -m pip install -U scipy==1.9.1
C:\Users\david>python -m pip install -U scikit-image==0.19.3
C:\Users\david>python -m pip install -U scikit-learn==1.1.1

更新套件
pip install -U XXXXXXX

pip install xlrd==1.2.0

C:\Users\070601>pip install xlrd==1.2.0
Collecting xlrd==1.2.0
Uninstalling xlrd-2.0.1:
Successfully uninstalled xlrd-2.0.1
Successfully installed xlrd-1.2.0

----------------list----------------

列出所安裝的模組
    可以使用list列出所安裝的模組，如果使用’-o’可列出有新版本的模組。
pip list		# 列出安裝的模組
pip list –o    # 列出有新版本的模組  		
E-5：安裝更新版模組
未來如果有更新版，可用下列方式更新至最新版模組。
pip install -U 模組名稱			# 更新至最新版模組

pip show sklearn命令查看sklearn包的路径

使用 SimpleGUICS2Pygame 替換 simplegui

C:\Users\070601>pip install SimpleGUICS2Pygame
pip install SimpleGUICS2Pygame
pip install SimpleGUICS2Pygame --upgrade

python -m pip install SimpleGUICS2Pygame --user --upgrade


import simplegui

改成
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


刪除模組
    安裝了模組之後，若是想刪除可以使用uninstall，例如：若是想刪除basemap，可以使用下列指令。
    pip uninstall basemap

pip list	#看目前已經安裝的套件

把所有要安裝的套件條列式的寫在一張txt檔案裡面

beautifulsoup4
requests
html5lib
matplotlib
selenium
jieba
wordcloud
Pillow==4.0.0

再來使用以下指令一次安裝所有套件:
$ pip install -r [txt_file_name]

安裝pySimpleGUI
	C:\Users\user>pip install pysimplegui

安裝pySerial
	C:\Users\user>pip install pyserial


C:\Users\david>pip install pillow
Collecting pillow

#PIL：Python Imaging Library
安裝Pillow
>pip install pillow


----------------pypy python test ST 安裝與升級 pip----------------

Python的套件管理程式	PIP

python -m pip install -U matplotlib	//Windows
pip install -U matplotlib		//Linux

在Windows下安裝Python套件:
用windows command line安裝 BeautifulSoup
C:\Users\david>pip3 install beautifulsoup4

windows command line下:

>pip list	//查看目前有安裝的Python套件
>pip3 install matplotlib	//安裝matplotlib

升級pip
python -m pip install -U pip
python -m pip install -U matplotlib
C:\Users\david>python -m pip install -U pip
安装 matplotlib 库：
C:\Users\david>python -m pip install -U matplotlib

重裝Pillow套件
pip uninstall PIL
pip uninstall Pillow
pip install Pillow

C:\Users\david\AppData\Local\Programs\Python\Python38-32>python.exe -m pip install opencv-python


pip : the package installer for Python



安裝 python-3.7.7.exe


C:\Users\david>python --version
Python 3.7.7


C:\Users\david>pip --version
C:\Users\david>pip3 --version

安裝 matplotlib
C:\Users\david>pip install matplotlib

安裝 requests
C:\Users\david>pip install requests
C:\Users\david>pip install BeautifulSoup	有問題 kilo/sugar不可用
C:\Users\david>pip install beautifulsoup4	 kilo/sugar 可用
C:\Users\david>pip install opencv-python

sugar 的 python 的位置

C:\Users\070601\AppData\Local\Programs\Python\Python311>python

Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

sugar 的 pip 的位置

C:\Users\070601\AppData\Local\Programs\Python\Python311\Scripts>pip --version
pip 22.3.1 from C:\Users\070601\AppData\Local\Programs\Python\Python311\Lib\site-packages\pip (python 3.11)

sugar 安裝 matplotlib
C:\Users\070601\AppData\Local\Programs\Python\Python311\Scripts>pip install matplotlib

sugar 安裝 serial
C:\Users\070601\AppData\Local\Programs\Python\Python311\Scripts>pip install serial

sugar 安裝 PySimpleGUI

sugar 安裝 requests
C:\Users\070601\AppData\Local\Programs\Python\Python311\Scripts>pip install requests

pip install flask

pip install twstock

pip install plotly

twstock 台灣股市股票價格擷取
https://pypi.org/project/twstock/

以 Python Imaging Library 進行影像資料處理
需先 pip install pillow

C:\Users\070601\AppData\Local\Programs\Python\Python311\Scripts>pip install lxml



ModuleNotFoundError: No module named matplotlib 问题解决方案
解决方案：
打开cmd ,切换到python的安装路径下，然后输入：python -m pip install matplotlib  
稍等片刻，成功！
C:\Users\david\AppData\Local\Programs\Python\Python38-32>
C:\Users\david\AppData\Local\Programs\Python\Python38-32>python -m pip install matplotlib







C:\Users\070601>pip show scikit-learn
C:\Users\070601>pip show pytube
C:\Users\070601>python --version
C:\Users\070601>pip --version


也可以針對特定套件顯示更詳細的套件資訊
pip show <package-name>
pip show pytube

檢查所有套件有無更新版本
pip list --outdated

安裝opencv
pip install opencv-python

pip install pytube3
pip install jupyter



本地安裝套件

下載 XXXX.whl
pip install XXXX.whl


pip install "scikit_learn==0.22.2.post1"

pip show scikit-learn

pip install scikit-learn scipy matplotlib numpy
pip install scikit-learn scipy matplotlib numpy

#alternative if you get permissions error
pip install scikit-learn scipy matplotlib numpy --user





本書各章pip安裝的套件清單

第9章: Python 3.9
pip install pywin32==303
第10章: Python 3.9
pip install opencv-python==4.5.4.60
pip install imutils==0.5.4
第12章: Python 3.9
pip install mediapipe==0.8.9.1
pip install cvzone==1.5.3
pip install <下載的Dlib的.whl檔>
pip install face-recognition==1.3.0
第15章: Python 3.9
pip install https://github.com/google-coral/pycoral/releases/download/v2.0.0/tflite_runtime-2.5.0.post1-cp39-cp39-win_amd64.whl
pip install pytesseract==0.3.8
第16章: Python 3.9
pip install torch==1.10.2
pip install torchvision==0.11.3
pip install torchaudio==0.10.2




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



# 一次安裝多個，並指定版本

pip install cython pillow>=7.0.0 numpy>=1.18.1 opencv-python>=4.1.2 torch>=1.9.0 --extra-index-url https://download.pytorch.org/whl/cpu torchvision>=0.10.0 --extra-index-url https://download.pytorch.org/whl/cpu pytest==7.1.3 tqdm==4.64.1 scipy>=1.7.3 matplotlib>=3.4.3 mock==4.0.3

pip install 
cython pillow>=7.0.0
numpy>=1.18.1
opencv-python>=4.1.2
torch>=1.9.0 --extra-index-url https://download.pytorch.org/whl/cpu
torchvision>=0.10.0 --extra-index-url https://download.pytorch.org/whl/cpu
pytest==7.1.3
tqdm==4.64.1
scipy>=1.7.3
matplotlib>=3.4.3
mock==4.0.3

