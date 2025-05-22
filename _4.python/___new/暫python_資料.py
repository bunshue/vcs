/**********************************************************
 * Filename	:	data_python.c
 * Description	:	python 相關資料
 **********************************************************/
Jupyter Notebook 是 Python 的前端界面

Jupyter 前身叫做 IPython
Jupyter。名稱的由來是
    Julia-Python-R 三種開放式的程式語言混合
    發音就是「木星」 (Jupiter), 取伽利略當時觀察木星衛星, 筆記完全開放那種精神。



------------------------------------------------------------



------------------------------------------------------------




------------------------------------------------------------



------------------------------------------------------------


------------------------------------------------------------

匿名函式 lambda
lambda 函式是「只有一行」的函式，可以用來處理一些小型函式，就可以不用為了一小段程式碼，額外新增一個有名稱的函式，這篇教學將會介紹 Python 的匿名函式。


python運算
/：除法
//：整除法
**：次方


------------------------------------------------------------


Python - 知名

Jieba 中文斷詞工具  結巴中文分詞

------------------------------------------------------------



完整的Python教學網站

Python教學
http://tw.gitbook.net/python/index.html



http://tw.gitbook.net/index.html

https://matplotlib.org/

----------------wwww----------------

百度搜索語法範例
https://dict.baidu.com/s?wd=python
https://dict.baidu.com/s?wd=python

帶參數的GET請求
html_data = requests.get(url, headers = headers)	自訂請求表頭
html_data = requests.get(url, params = params)		增加 URL 查詢參數
html_data = requests.get(url, verify = False)		不合格憑證
html_data = requests.get(url, cookies = cookies)
html_data = requests.get(url = url, params = params)
html_data = requests.get(url = url, cookies={'over18': '1'})
html_data = requests.get(url, headers = header, timeout = timeout)

共13種參數
params	data		json	headers	cookies	files	auth
timeout	allow_redirects	proxies	verify	stream	cert

timeout	等待逾時
# 等待 3 秒無回應則放棄
requests.get('http://github.com/', timeout = 3)

data 讓使用者填入資料
verify 不合格憑證
requests 遇到這種伺服器就容易會出現 requests.exceptions.SSLError 這樣的錯誤，解決的方式就是加上 verify=False，關閉 requests 的憑證檢查功能：
# 關閉憑證檢查
r = requests.get('https://my.server.com/', verify = False)

auth 指定帳號與密碼

# 需要帳號登入的網頁
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))

files 上傳檔案

若要將自己設定的 cookies 放進 GET 請求中送給伺服器，可以這樣寫：
# 設定 cookie
my_cookies = dict(my_cookie_name='G. T. Wang')
# 將 cookie 加入 GET 請求
r = requests.get("http://httpbin.org/cookies", cookies = my_cookies)

Response 物件 		說明
url 			資源的 URL 位址。
content 		回應訊息的內容 ( bytes )。
text 			回應訊息的內容字串 ( str )。
raw 			原始回應訊息串流 ( bytes )。
status_code 		回應的狀態 ( int )。
encoding 		回應訊息的編碼。
headers 		回應訊息的標頭 ( dict )。
cookies 		回應訊息的 cookies ( dict )。
history 		請求歷史 ( list )。
json() 			將回應訊息進行 JSON 解碼後回傳 ( dict )。
rasise_for_status()	檢查是否有例外發生，如果有就拋出例外。


取得response後, 透過parser轉換成BeautifulSoup比較好處理的格式:
soup = BeautifulSoup(resp.text, 'html.parser')
soup是獲得的文件物件, html.parser是支援的parser.
關於parser, 比較常見的parser有這些:
html.parser
html5lib
lxml

----------------wwww----------------

postman使用
https://ithelp.ithome.com.tw/articles/10275113

# 一種可以在網路上自動抓取資料的工具，又稱「網路爬蟲」(Web Crawler)

BeautifulSoup有提供兩種解析器，一種是html.parser，另一種是xml，因為現在抓到的是HTML，所以選html.parser。
解析原始碼後，會返回一個DOM tree的物件，初始位置在文件的root，之後就是對這個物件去操作。
prettify()這個函數可以將DOM tree以比較美觀的方式印出。



資料型態轉換 (Casting)

將變數強制轉成我們要的變數型態。
int()：將任何的資料型態轉為int
float()：將任何的資料型態轉為float
str()：將任何的資料型態轉為string

------------------------------------------------------------

字串長度

使用len()得到字串的長度，回傳的是一個數字。
第n個字元

將字串視為一個由字元所組成的列表(明天就會講)，每個數字都有索引值，索引值從0開始。

如果要取得第n個字元的話，就是str[n-1]。
切割字串

str[n:m]可以切割從n到m-1的子字串。
取代字串

str.replace("A", "B")將字串中所有的"A"都取代成"B"。
分割字串

str.split(",")用逗號將字串分割成好幾個小區塊，並回傳一個字串的陣列。
連接字串

------------------------------------------------------------




matplotlib.pyplot.figure(num=None, figsize=None, dpi=None, *, facecolor=None, edgecolor=None, frameon=True, FigureClass=<class 'matplotlib.figure.Figure'>, clear=False, **kwargs)



matplotlib.pyplot.figure
無法全螢幕
無法指定視窗顯示位置

#設定圖表在整個視窗的位置與大小
x_st = 0.15
y_st = 0.10
w = 0.7
h = 0.3
pic2 = fig.add_axes([x_st, y_st, w, h])
#pic2.set_xlabel('Time [s]')

------------------------------------------------------------

# The function for finding a key in the list 
def linearSearch(lst, key):
    for i in range(len(lst)): 
        if key == lst[i]:
            return i
  
    return -1
    
    
    
try:
    number = eval(input("Enter a number: "))
    print("The number entered is", number)
except NameError as ex:
    print("Exception:", ex)


------------------------------------------------------------

 [第 16 天] 網頁解析 
https://ithelp.ithome.com.tw/articles/10186119

完美解決爬蟲時遇到的'NoneType' object has no attribute 'find'或'NoneType' object has no attribute 'find_all'問題
https://www.twblogs.net/a/5eeff4821e58dca42b87ccf1

 
 
matplotlib.pyplot.figure(num=None, figsize=None, dpi=None, *, facecolor=None, edgecolor=None, frameon=True, FigureClass=<class 'matplotlib.figure.Figure'>, clear=False, **kwargs)



matplotlib.pyplot.figure
無法全螢幕
無法指定視窗顯示位置



#設定圖表在整個視窗的位置與大小
x_st = 0.15
y_st = 0.10
w = 0.7
h = 0.3
pic2 = fig.add_axes([x_st, y_st, w, h])
#pic2.set_xlabel('Time [s]')


subplots設定
plt.subplots(ncols=2, figsize=(12, 8))


Matplotlib官網
https://matplotlib.org/stable/index.html
https://matplotlib.org/stable/plot_types/index.html
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#examples-using-matplotlib-pyplot-imshow


------------------------------------------------------------

一些python網頁

https://www.runoob.com/w3cnote/python-pip-install-usage.html

https://learn.microsoft.com/zh-tw/visualstudio/python/tutorial-working-with-python-in-visual-studio-step-05-installing-packages?view=vs-2022

https://fynn90.github.io/2018/02/01/PIL%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B/

https://www.runoob.com/matplotlib/matplotlib-install.html

------------------------------------------------------------


四種定位方法
find()
find()函數可以定位符合標籤的第一個節點。

find_all()
find_all()定位符合標籤的所有節點，回傳的是一個列表。

select_one()
select_one()使用CSS選擇器的語法來定位節點。

select()
select()其實就是使用CSS選擇器語法的find_all()。回傳是一個列表。




.py IDLE 只能吃unicode / utf-8  不能吃big5



ssss
https://www.python.org/downloads/


Download the latest version for Windows
Download Python 3.11.1
這是64位的

Download Windows installer (32-bit)


python 机器学习 sklearn——一起识别数字吧
https://blog.csdn.net/weixin_52521533/article/details/123802259?spm=1001.2100.3001.7377&utm_medium=distribute.pc_feed_blog.none-task-blog-hot_rank_bottoming-20.nonecase&depth_1-utm_source=distribute.pc_feed_blog.none-task-blog-hot_rank_bottoming-20.nonecase

Python绘制世界疫情地图

https://blog.csdn.net/wxfighting/article/details/123802999?spm=1001.2100.3001.7377&utm_medium=distribute.pc_feed_blog.none-task-blog-hot_rank_bottoming-3.nonecase&depth_1-utm_source=distribute.pc_feed_blog.none-task-blog-hot_rank_bottoming-3.nonecase



Code . Arts . Travel
python
http://www.jysblog.com/category/coding/python/



https://www.kancloud.cn/thinkphp/python-guide/39428

http://www.codedata.com.tw/python/python-tutorial-the-1st-class-4-unicode-support-basic-input-output/
http://www.runoob.com/python/python-chinese-encoding.html

	
------------------------------------------------------------

from PIL import Image, ImageFilter

kitten = Image.open("ABP238.jpg")       #開啟檔案
kitten.show()                           #顯示檔案

blurryKitten = kitten.filter(ImageFilter.GaussianBlur)  #過濾波器
blurryKitten.save("ABP238222.jpg")      #存檔
blurryKitten.show()                     #顯示檔案

------------------------------------------------------------



Python 傳送 email 的三種方式

https://www.itread01.com/content/1541896623.html

http://pythonscraping.com/pages/page1.html
http://www.pythonscraping.com/pages/page3.html

Web Scraping with Python - Collecting Data from the Modern Web
https://github.com/REMitchell/python-scraping/tree/master/v1/chapter5
https://github.com/REMitchell/python-scraping/tree/master/v1/chapter6
https://github.com/REMitchell/python-scraping/tree/master/v1

------------------------------------------------------------

網站擷取：使用Python（二版）

目錄
前言

第一部 建構擷取程序
第一章 你的第一個擷取程序
第二章 進階HTML解析
第三章 撰寫網站爬行程序
第四章 網站爬行模型
第五章 Scrapy
第六章 儲存資料

第二部 儲存資料
第七章 讀取文件
第八章 清理髒資料
第九章 讀寫自然語言
第十章 表單與登入
第十一章 與擷取相關的JavaScript
第十二章 透過API 爬行
第十三章 影像處理與文字辨識
第十四章 避開擷取陷阱
第十五章 以爬行程序測試你的網站
第十六章 平行擷取網站
第十七章 遠端擷取
第十八章 網站擷取的法規與道德

索引
收回


------------------------------------------------------------

有关Matplotlib的一些技巧

http://www.yeolar.com/note/2011/04/28/matplotlib-tips/

------------------------------------------------------------

import之用法	用前兩個就好
一、	讀一個套件
import numpy
y = numpy.sin(2*numpy.pi*t)


二、	讀一個套件、給個簡單的代號
import numpy as np


三、	單獨要某一個函數
from numpy import sin

四、	某個套件庫的函數全要
from numpy import *


#從0到10,很均勻的找出100個點。

x = np.linspace(0, 10, 100)


A = np.arange(10)
輸出:array([1, 2, …, 10])


>>> type(data)
<class 'str'>
>>> 
>>> type(a)
<class 'int'>

------------------------------------------------------------

內置函數列表及方法：

Python中包括下面的列表函數功能：
SN 	函數及描述
1 	cmp(list1, list2)	比較兩個列表的元素
2 	len(list)		給出列表的總長度
3 	max(list)		從列表中，項目的最大值
4 	min(list)		從列表中，項目的最小值
5 	list(seq)		一個元組到列表的轉換

Python中包括下面的列表的方法
SN 	方法及描述
1 	list.append(obj)	添加obj對象到列表
2 	list.count(obj)		計算返回obj出現在列表的次數
3 	list.extend(seq)	附加序列seq內容到列表
4 	list.index(obj)		返回列表中出現obj的最小索引
5 	list.insert(index, obj)	插入obj對象在列表偏移索引位置
6 	list.pop(obj=list[-1])	移除並返回列表最後一個對象或obj
7 	list.remove(obj)	從列表中移除obj對象
8 	list.reverse()		反轉列表的對象
9 	list.sort([func])	排序列表中的對象，使用func比較（如果給定）



數據類型轉換：
函數 			描述
int(x [,base])		將x轉換為一個整數。基數指定為base，如果x是一個字符串。
long(x [,base] )	將x轉換為一個長整數。基數指定為base，如果x是一個字符串。
float(x)		將x轉換到一個浮點數。
complex(real [,imag])	創建一個複數。
str(x)			轉換對象x為字符串表示形式。
chr(x)			整數轉換為一個字符。
unichr(x)		整數轉換為一個Unicode字符。
hex(x)			將整數轉換為十六進製字符串。

內建轉換函式
str
int
float


int("1010", 2)
int("A0A0", 16)


Python包括以下執行數學計算的函數。
函數 		返回（描述）
abs(x)		x的絕對值：x和零之間的（正極）的距離。
ceil(x)		x的上限：最小整數不小於x
cmp(x, y)	-1 if x < y, 0 if x == y, 或1 if x > y
exp(x)		x的指數: ex
fabs(x) 	x的絕對值
floor(x) 	x的地板：最大的整數不大於x
log(x)		x的自然對數，對於x> 0時
log10(x) 	以10為底的對數，X>0。
max(x1, x2,...) 它最大的參數：值最接近正無窮大
min(x1, x2,...) 它的最小參數：值最接近負無窮大
modf(x) 	x的兩個項元組的整數和小數部分。這兩個元素具有相同的x符號。整數部分返回一個浮點數。
pow(x, y) 	x**y 的值
round(x [,n]) 	x在小數點四舍五入到n位數字。 Python遠離零點決定：round(0.5) 是1.0 而round(0.5) 為-1.0。
sqrt(x) 	x的平方根（x>0）

Random 模組
函數 		描述
choice(seq) 	從列表，元組或字符串隨機項。
randrange ([start,] stop [,step]) 	從範圍隨機選擇的元素（啟動，停止，步驟）
random() 	隨機產生一個介於0與1之間小數
seed([x]) 	設置生成隨機數使用整數開始值。調用任何其他隨機模塊函數之前調用這個函數。返回None。
shuffle(lst) 	隨機化代替列表中的項。返回None。
uniform(x, y) 	隨機浮點數r，使得x小於或等於r，r小於y

seed()				亂數產生器，以目前的系統時間為預設值
random()			亂數產生0~1之間的浮點數
choice(seq)			從序列項目中隨機挑選一個
randint(a, b)			從a到b之間產生隨機整數值
randrange(st, sp[, step])	在指定範圍內，依step遞增獲取一個隨機數
sample(polulation, k)		序列項目隨機挑選k個元素並以list回傳
shuffle(x[, random))		將序列項目重新洗排(shuffle)
uniform(a, b)			指定範圍內隨機生成一個浮點數




degrees(x) 	從弧度到度角 x 的轉換
radians(x) 	從角度到弧度角 x 的轉換




python特有的運算             

** 	指數冪- 執行運算符的指數（冪）計算 	a**b = 10 的 20 次冪
// 	Floor Division - Floor除法 - 操作數相除，其結果的小數點後的數字將被刪除。 	9//2 = 4 ， 9.0//2.0 = 4.0

指數
地板除

**=
//=


a = 0011 1100

b = 0000 1101

-----------------

a&b = 0000 1100

a|b = 0011 1101

a^b = 0011 0001

~a  = 1100 0011


             
而中文的處理，我們可以透過unicode的編解碼來處理

!!!注意中文的檔案要加上# encoding: utf-8

單行註解為#,多行註解則用"""開頭與結尾
"""
這是一個簡單的python程式
介紹基本的語法
"""

Python - 十分鐘入門 
http://tech-marsw.logdown.com/blog/2014/09/03/getting-started-with-python-in-ten-minute

http://tech-marsw.logdown.com/blog/2016/01/10/crawler-index


python

使用matplotlib繪圖
http://me1237guy.pixnet.net/blog/post/64496047
http://me1237guy.pixnet.net/blog/post/64496047

https://matplotlib.org/index.html

https://matplotlib.org/gallery/index.html

https://matplotlib.org/api/cbook_api.html#matplotlib.cbook.get_sample_data

https://matplotlib.org/api/cbook_api.html#matplotlib.cbook.get_sample_data




https://matplotlib.org/gallery/lines_bars_and_markers/simple_plot.html#sphx-glr-gallery-lines-bars-and-markers-simple-plot-py



有关Matplotlib的一些技巧

http://www.yeolar.com/note/2011/04/28/matplotlib-tips/




matplotlib

https://medium.com/jameslearningnote/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90-%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E7%AC%AC2-5%E8%AC%9B-%E8%B3%87%E6%96%99%E8%A6%96%E8%A6%BA%E5%8C%96-matplotlib-seaborn-plotly-75cd353d6d3f



/**********************************************************
 * Filename	:	python_data.c
 * Description	:	python相關資料與片段程式
 **********************************************************/



測試有沒有裝tkinter
>>> import tkinter
>>> tkinter._test()
>>> 

[第 18 天] 資料視覺化 matplotlib
https://ithelp.ithome.com.tw/articles/10186484

tkinter教學
http://effbot.org/tkinterbook/
http://effbot.org/tkinterbook/tkinter-index.htm

python教學

https://sites.google.com/site/ezpythoncolorcourse/


http://www.runoob.com/python/python-tutorial.html
http://www.runoob.com/python/python-tutorial.html

http://tw.gitbook.net/python/index.html

C:\Users\user>python
Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import tkinter
>>> tkinter._test()
>>> tkinter._test()

各種python簡易說明

Firebase 即時資料庫
即時資料庫並進行 CRUD (Create, Retrieve, Update, Delete) 操作


溝通網頁的利器 requests 模組

要用 matplotlib 顯示圖片，要先透過 matplotlib.image 模組中的
imread() 方法讀取圖片，讀取後使用 imshow() 在圖表中繪製圖片，最後透過 plt.show() 顯示圖表。


Sympy 這是 Python 用來繪製數學公式與進行符號運算的套件
requests：用於請求伺服器回傳資料，可用正則表達式篩選所需的資料。
BeautifulSoup：方便對特定的目標加以分析、擷取的強大模組。

Python的網頁解析套件 -- BeautifulSoup

------------------------------------------------------------

Windows 7 安裝 Python @ kilo	2023/3/3 11:44下午

需要安裝Windows 7 Service Pack 1

KB2533623丁(Win7Win2008 R2)
windows6.1-kb976932-x86_c3516bc5c9e69fee6d9ac4f981f5b95977a8a2fa
windows6.1-kb2533552-x86_f2061d1c40b34f88efbe55adf6803d278aa67064

https://www.python.org/downloads/

官網下載最新版
python-3.11.2-amd64.exe

----------------pypy python test SP----------------

python待新增


python待尋找
python目前不會做的事情：
1. timer
2.
3.
4.

Python 與 OpenCV 基本讀取、顯示與儲存圖片教學
https://blog.gtwang.org/programming/opencv-basic-image-read-and-write-tutorial/

Python 使用 OpenCV、Dlib 實作即時人臉偵測程式教學
https://blog.gtwang.org/programming/python-opencv-dlib-face-detection-implementation-tutorial/

https://steam.oxxostudio.tw/category/python/ai/opencv.html
https://steam.oxxostudio.tw/category/python/ai/opencv-index.html

OpenCV播放影片

應該無法做到倒轉、快轉慢轉....

PIL有九种不同模式: 1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。

1 : 为二值图像，非黑即白。每个像素用8个bit表示，0表示黑，255表示白。

L : 为灰度图像，每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
　　 转换公式：L = R * 299/1000 + G * 587/1000+ B * 114/1000。





----------------Python Reserved 暫存 候用 ST----------------
pygame
pySimpleGUI
turtle

turtle --- 海龜繪圖
https://docs.python.org/zh-cn/3/library/turtle.html

pySimpleGUI
https://github.com/PySimpleGUI/PySimpleGUI/tree/master/DemoPrograms

The PySimpleGUI Cookbook
https://www.pysimplegui.org/en/latest/cookbook/

DICOM in Python 
https://github.com/pydicom
https://pydicom.github.io/pydicom/dev/auto_examples/index.html
https://pydicom.github.io/pydicom/dev/old/pydicom_user_guide.html


----------------Python Reserved 暫存 候用 SP----------------

單底線 _ : 無名暫時變數
for _ in range(10):
	do_something()

抽象基礎類別
Abstract Base Class, ABC
