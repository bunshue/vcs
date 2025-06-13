
------------------------------------------------------------



------------------------------------------------------------




------------------------------------------------------------



------------------------------------------------------------



滑鼠 event 與 flag 列表

當滑鼠在指定視窗中滑動進行某些行為，都會觸發一些事件，相關事件列表如下：
代號 	事件 	說明
0 	cv2.EVENT_MOUSEMOVE 	滑動
1 	cv2.EVENT_LBUTTONDOWN 	左鍵點擊
2 	cv2.EVENT_RBUTTONDOWN 	右鍵點擊
3 	cv2.EVENT_MBUTTONDOWN 	中鍵點擊
4 	cv2.EVENT_LBUTTONUP 	左鍵放開
5 	cv2.EVENT_RBUTTONUP 	右鍵放開
6 	cv2.EVENT_MBUTTONUP 	中鍵放開
7 	cv2.EVENT_LBUTTONDBLCLK 	左鍵雙擊
8 	cv2.EVENT_RBUTTONDBLCLK 	右鍵雙擊
9 	cv2.EVENT_MBUTTONDBLCLK 	中鍵雙擊

除了事件，滑鼠的行為也會觸發一些 flag，相關 flag 列表如下：
代號 	flag 	說明
1 	cv2.EVENT_FLAG_LBUTTON 	左鍵拖曳
2 	cv2.EVENT_FLAG_RBUTTON 	右鍵拖曳
4 	cv2.EVENT_FLAG_MBUTTON 	中鍵拖曳
8～15 	cv2.EVENT_FLAG_CTRLKEY 	按 Ctrl 不放事件
16～31 	cv2.EVENT_FLAG_SHIFTKEY 	按 Shift 不放事件
32～39 	cv2.EVENT_FLAG_ALTKEY 	按 Alt 不放事件


"""
**Source** Kevin Markham https://github.com/justmarkham/python-reference

"""

在 python2.x 中，使用 python3.x 的寫法:

from __future__ import print_function
from __future__ import division
from __future__ import with_statement
from __future__ import absolute_import
from __future__ import unicode_literals

------------------------------------------------------------

#useless
mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
mpl.rcParams["axes.unicode_minus"] = False


df.to_excel('closeprice.xls')

pandas.plot是matplotlib.pyplot.plot的简单包装

.ix is deprecated. Please use
.loc for label based indexing or   <= 用這個 
.iloc for positional indexing


#np算4分位數
print("25th percentile =", np.percentile(height, 25))
print("Median =", np.median(height))
print("75th percentile =", np.percentile(height, 75))

import matplotlib.pyplot as plt
也就是說，我們繪圖實際上用的是matplotlib包的pyplot模塊。


print("字串處理 技巧")

print("教育部統計處資料 很多")
url = "https://stats.moe.gov.tw/files/detail/{}/{}_student.csv"
for year in range(106, 110):
    print(url.format(year, year))


 
        mode = os.lstat(long_filename).st_mode
        if stat.S_ISDIR(mode):
            print('folder')
        elif stat.S_ISREG(mode):
            print('file')
        else:
            # Unknown file type, print a message
            print("Skipping %s" % long_filename)



1. 撈出指定資料夾下所有檔案
2. + 分辨檔案型態
3. + 過濾檔案大小
4. + 過濾影片格式 > 1080p, < 720p 者

搜尋模式:
'全部', '檔案大小', '影像大小', '影片時長', '相似檔名', '零容量檔案'



"""
python / vcs 暫存片段程式

"""


turtle --- 龜圖學

源码： Lib/turtle.py
https://docs.python.org/zh-tw/3.8/library/turtle.html
https://docs.python.org/zh-tw/3.8/library/turtle.html




for i in [9.4, 9.5, 9.6, 9.7]:
    j= round(i)
    print(j)


    j= round(i, 0)
    j= round(i, 1)
    j= round(i, 1)
    j= round(i, 1)
    j= round(i, 2)
    j= round(i, 2)
    j= round(i, 1)




color('red', 'yellow')

tu.home()

tu.ht()


------------------------------------------------------------

print(dir(random))

------------------------------------------------------------



------------------------------------------------------------


------------------------------------------------------------

# post 與 payload的寫法 目前不能用
import requests
url = 'http://www.ibon.com.tw/retail_inquiry_ajax.aspx'
payload = {'strTargetField': 'COUNTY', 'strKeyWords': '南投縣'}
html = requests.post(url, data=payload)
html.encoding='utf-8'

url = 'http://www.ibon.com.tw/retail_inquiry.aspx#gsc.tab=0'
r = requests.get(url)
r.encoding = 'utf-8'
html = BeautifulSoup(r.text, 'html.parser')





------------------------------------------------------------



------------------------------------------------------------

用 hist 與 boxplot畫 常態分佈

------------------------------------------------------------

------------------------------------------------------------

Seaborn常见图形绘制（kdeplot、distplot）

seaborn是基于matplotlib的Python可视化库，在matplotlib的基础上进行了更高级的API封装，从而使得作图更加容易，不需要经过大量的调整就能让图变得精致好看。

一、kdeplot（核密度估计图）

核密度估计（kernel density estimation）是在概率论中用来估计未知的密度函数，属于非参数检验的方法之一。通过核密度估计图可以比较直观地看出数据样本本身的分布特征。

通过一些具体的例子来学习kdeplot的参数用法：

在这里插入图片描述

cut参数：表示绘制的时候，切除带宽往数轴极限值的多少（默认为3）

在这里插入图片描述

cumulative参数：是否绘制累积分布

在这里插入图片描述

shade参数：若为True，则在kde曲线下面的区域进行阴影处理，color空值曲线和阴影的颜色

在这里插入图片描述

vertical参数：表示以X轴进行绘制还是以Y轴进行绘制

在这里插入图片描述
二元kde图像

在这里插入图片描述

cbar参数：添加一个颜色棒（颜色棒在二元kde图像中才有）

在这里插入图片描述
二、displot

distplot()集合了matplotlib的hist()与核密度函数kdeplot()的功能，增加了rugplot分布观察条显示与利用scipy库fit拟合参数分布的新颖用途。具体用法如下：

hist()表示直方图，又叫做质量分布图。通过表示沿数据范围形成封箱，然后绘制条形以显示落入每个分箱贯彻的次数的数据分布。

在这里插入图片描述

可以通过hist和kde参数调节是否显示直方图及和密度估计（默认hist，kde均为True）

在这里插入图片描述

bins：int或list，控制直方图的划分

在这里插入图片描述

rug：控制是否生成观测数值的小细条

在这里插入图片描述

fit：控制拟合的参数分布图形，能够直观地评估它与观察数据的对应关系（黑色线条为确定的分布）

在这里插入图片描述

hist_kws,kde_kws,rug_kws,fit_kws参数接收字典类型，可以自行定义更多高级样式

在这里插入图片描述

norm_hist：若为True，则直方图高度显示密度而非计数（含有KDE图形中默认为True）




------------------------------------------------------------


取子字符串有两种方法，使用[]索引或者切片运算法[:]，这两个方法使用面非常广



bunshue <noreply@github.com>

RE: [bunshue/vcs] fb02f3: david modify vcs code


生策會 <ibmi@ibmi.org.tw>

NVIDIA Developer Relations <news@nvidia.com>


Synology Newsletter <noreply@news.synology.com>





下載本書客製化Python套件的超連結
Google Drive:

https://drive.google.com/file/d/1EkUZPiNGmCNxzEPtDNkffyz5ngmLWa3M/view?usp=sharing

MEGA Drive:

https://mega.nz/file/KQVlRAhR#c7-tWIJ6Kzz7tcTkYHd1kmr8oDAicupkSCO9tO4O470



------------------------------------------------------------

Day 1_Data_Preprocessing python版本适配问题 #109 
 
enc.get_feature_names在python3版本上跑不通，可以替换成 enc.get_feature_names_out





接下來四天是一個小單元，我們做一個簡單的小練習，要做一個可以辨識貓狗的模型，用於訓練的資料集是由Kaggle所提供，一個資料分析辨識的競賽平台，不過在Microsoft網站有提供下載，內有解析度不定的貓狗圖片各12500張，請下載然後解壓縮出來，跟你的ipynb檔案放在一起。

----------------暫存文字雲 ST----------------

Qtime

用comport知道ims相機有接上 但 USB無ims影像
若能做到 將ims主機軟體重置 看會不會有效 此時 PC軟體要重抓USB影像

安裝驗證(IQ)、操作驗證(OQ)、性能驗證(PQ)

距今多久程式

晴空匯火災	2024/5/27


----------------暫存文字雲 SP----------------


主程式持續進行，開啟thread做一些事，thread做事時，主程式依舊不耽擱

thread工作型態
1. 建立一個thread，讓他無限迴圈地等待做一件事，直到外面叫他停止		印表機、
2. 建立一個thread，只做一件事，做完即結束				去搬便當、

停止 thread 的3個方法
1. 強制停止 .Abort()
2. 使用 flag 讓 thread 中斷運行
3. 事情做完 thread即停止

//無限迴圈
richTextBox1.Text += "0";
Thread.Sleep(500);


//建立一個Thread 到 偵錯/視窗/即時運算 看結果

System.Diagnostics.Debug.Print("即時運算視窗輸出除錯訊息 測試訊息！！！Form1！！！ title = " + title + "  " + aa.ToString());


plt.title("軸範圍: " + str(plt.axis()))

#marker
plt.plot(days, celsius_min, "r-o",
         days, celsius_max, "g--o")

plt.savefig("Celsius.svg")

plt.savefig("Celsius.pdf")

# x 軸刻度用文字
labels = ["鼠", "牛", "虎", "兔", "龍", "蛇"]
index = np.arange(len(labels))
plt.xticks(index, labels)

# 指定刻度數值
plt.xticks(range(0, 25, 2))
plt.yticks(range(15, 35, 3))


locs1, labels = plt.xticks()
locs2, labels = plt.yticks()
plt.title(str(locs1) + "\n" + str(locs2))

------------------------------------------------------------

面板上三類 Button LED燈號

1. 僅Button : Start / Smart / Brighten / Darken / Metering
2. GPIO控制LED亮暗 : RED / 亮度1~5 / CEN / AVG / AUTO
3. 恆亮LED : Start / Smart / Brighten / Darken / Metering



18+
https://garageplay.tw/plus/news/2?cp=setn7d&tk=st-cpc-gpm-lk-2407191-vod




"""
from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組

mp3_filename = 'C:/_git/vcs/_1.data/______test_files1/_mp3/16.監獄風雲.mp3'
song = AudioSegment.from_mp3(mp3_filename)  # 讀取 mp3 檔案
song.export("aaaa.wav", format="wav")  # 轉換並儲存為 wav
"""








chrome://version/

Google Chrome	127.0.6533.73 (正式版本) (64 位元) (cohort: Stable) 
修訂版本	b59f345ebd6c6bd0b5eb2a715334e912b514773d-refs/branch-heads/6533@{#1761}
作業系統	Windows 10 Version 22H2 (Build 19045.4651)
JavaScript	V8 12.7.224.16
使用者代理程式	Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36
命令列	"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --disable-features=RendererCodeIntegrity --flag-switches-begin --flag-switches-end
可執行檔的路徑	C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
設定檔路徑	C:\Users\070601\AppData\Local\Google\Chrome\User Data\Default
使用中的變化版本	e61eae14-ca7d8d80
bb437d9a-377be55a
f69863c5-ca7d8d80
45bb09c-ca7d8d80
f6c95bed-f5e2d583


        self.text = tkinter.Text(root)
        self.text.place(y=220)

    #text = self.text.get(1.0, tkinter.END)  # 取得信件內容


self.text.insert(tkinter.END, "傳送錯誤\n")

        self.entryPass = tkinter.Entry(root, show="*")


        self.entryPort = tkinter.Entry(root)
        self.entryPort.insert(tkinter.END, "25")


i = 1
for path in os.sys.path:  # 使用os模組
    print(i, " ", path)
    print("<br>")
    i = i + 1


製作不一樣權重的 random

        weight = 40
        weight = 60
        if random.randint(1,100) > weight:
            canvas.move(item2, 5, 0)  # item2 x軸移動5像素, y軸移動0像素
            item2Loc += 1
        else:
            canvas.move(item1, 5, 0)  # item1 x軸移動5像素, y軸移動0像素
            item1Loc += 1


print('裁剪資料成字典')

std_data = dict()
    lines = f.readlines()
    for line in lines:
        no, name = line.rstrip('\n').split(',')
        std_data[no] = name
print(std_data)




from selenium import webdriver

driver = webdriver.Chrome()

tk
window.minsize(600, 480)	# 可拉大 不可縮小

tk.Label(window, text = "標準版顯示訊息").pack()

print("------------------------------------------------------------")  # 60­э

img_url = "https://upload.wikimedia.org/wikipedia/commons/8/8b/%E8%A5%BF%E8%9E%BA%E5%A4%A7%E6%A9%8B_%28cropped%29.jpg"

    # csv 轉 html
    # 將資料轉成data字典物件
    f = open("tmp_Masks.csv", encoding="utf-8")
    data = csv.DictReader(f)

    # 若有 tmp_Masks.html 網頁即刪除
    if os.path.exists("tmp_Masks.html"):
        os.remove("tmp_Masks.html")

    # 使用附加模式建立tmp_Masks.html網頁
    fH = open("tmp_Masks.html", "a", encoding="utf-8")
    # 寫入網頁表格標題
    fH.write('<meta charset="utf-8" /><table border="1">')
    fH.write(
        "<tr>\
                 <th>醫事機構名稱</th>\
                 <th>醫事機構地址</th>\
                 <th>醫事機構電話</th>\
                 <th>成人口罩剩餘數</th>\
                 <th>兒童口罩剩餘數</th>\
                 <th>路線規劃</th>\
              </tr>"
    )
    # 印出查詢的健保特約機構口罩剩餘數量明細資料
    for row in data:
        address = row["醫事機構地址"]
        # 判斷地址與搜尋地址是否吻合
        if search in address:
            # 不顯示成人以及兒童口罩賣完的診所
            if row["成人口罩剩餘數"] != 0 and row["兒童口罩剩餘數"] != 0:
                print("藥局名稱:", row["醫事機構名稱"])
                print("藥局地址:", row["醫事機構地址"])
                print("藥局電話:", row["醫事機構電話"])
                print("成人口罩剩餘數:", row["成人口罩剩餘數"])
                print("兒童口罩剩餘數:", row["兒童口罩剩餘數"])
                print("=" * 50)
                # 將資料寫入 tmp_Masks.html
                fH.write("<tr>")
                fH.write("<td>" + row["醫事機構名稱"] + "</td>")
                fH.write("<td>" + row["醫事機構地址"] + "</td>")
                fH.write("<td>" + row["醫事機構電話"] + "</td>")
                fH.write("<td>" + row["成人口罩剩餘數"] + "</td>")
                fH.write("<td>" + row["兒童口罩剩餘數"] + "</td>")
                fH.write(
                    '<td><a href="https://www.google.com/'
                    + "maps/search/"
                    + row["醫事機構地址"]
                    + '">路線規劃</a></td>'
                )
                fH.write("</tr>")
    fH.write("</table>")
    # 關閉檔案
    fH.close()
    f.close()

-----

import shutil
    
image_foldername = 'tmp_images'
filename = 'tmp_countryfood2222.html'
print('存檔檔案 :', filename)
if os.path.exists(filename):  
    os.remove(filename)     # 若有 tmp_countryfood.html 網頁即刪除
if os.path.exists(image_foldername): 
    shutil.rmtree(image_foldername)    # 若有images目錄即刪除
else:
    os.mkdir(image_foldername)        # 若無images目錄即刪除


    #從網址取得檔名
    imgUrl=col['PicURL']
    print(cnt)
    #網址用'/'分隔取最後一筆資料 => *.jpg
    filename = imgUrl.split('/')[-1] #擷取圖片名稱
    print('圖片網址：', imgUrl)
    print('圖片檔名：', filename)

    #網址用'/'分隔取最後一筆資料 => *.jpg
    picName=row['PicURL'].split('/')[-1]
    print('圖片網址：', row['PicURL'])
    print('圖片檔名：', picName)
    

        #建立取得圖片的 response 物件
        response=requests.get(imgUrl) 
        f=open((image_foldername+'/'+filename),'wb')    #開啟圖片檔案                    
        f.write(response.content)  # 將response.content二進位內容寫入檔案
        print(filename,'下載完畢')



filename = 'aaaaa.html'

print("%s 網頁建置完成" % (filename))

------------------------------------------------------------


def checkpassword(password):
    #檢查密碼長度必須是5到10個字元
    length = len(password)  # 密碼長度
    if length < 5:  # 密碼長度不足
        raise Exception("密碼長度不足")
    if length > 10:  # 密碼長度太長
        raise Exception("密碼長度太長")
    print("密碼長度正確")

print('測試 raise Exception')

password = "lion-mouse"

try:
    checkpassword(password)
except Exception as err:
    print("密碼檢查異常發生: ", str(err))


------------------------------------------------------------


def passWord(pwd):
    # 檢查密碼長度必須是5到8個字元
    pwdlen = len(pwd)  # 密碼長度
    if pwdlen < 5:  # 密碼長度不足
        raise Exception("密碼長度不足")
    if pwdlen > 8:  # 密碼長度太長
        raise Exception("密碼長度太長")
    print("密碼長度正確")


for pwd in ("aaabbbccc", "aaa", "aaabbb"):  # 測試系列密碼值
    try:
        passWord(pwd)
    except Exception as err:
        print("密碼長度檢查異常發生: ", str(err))






python套件分類

數學		SciPy, NumPy
數據分析	Pandas
圖形處理	matplotlib, seaborn
編輯器		Spyder Jupyter Notebook
網路		Bokeh
機器學習	scikit-learn
自然語言	NLTK


print ('姓名','國文','數學','平均',sep='\t')

print("BMI is", format(bmi, ".2f"))




ims_qc_database
zip	41MB


序號格式(13碼, 1英7數1英4數)
Ex: N2201001A0001


\\192.168.1.231\\ims_qc_database\\ims_qc_database.exe


M:\ims_qc_database\QC\csv

giphy10-ezgif.com-optimize.gif


命令 pyinstaller -F ims_qc_database.py

資料表欄位型別(4)

INTEGER	整數
REAL	浮點數
TEXT	字串
BLOB	多媒體物件 ex : 圖片 音樂

UNIQUE 唯一
NOT NULL	不能空白

------------------------------------------------------------


    elif k == ord('r'):
        draw = np.zeros((h,w,4), dtype='uint8')

GET  爬蟲，取得網站的靜態資料
POST 爬蟲，提出要求向對方索取資料



       X0 1 2 3
      Y+-+-+-+-+
      0| | | | |
       +-+-+-+-+
      1| | | | |
       +-+-+-+-+
      2| | | | |
       +-+-+-+-+
      3| | | | |
       +-+-+-+-+"""


 X0 1 2 3
Y+-+-+-+-+
0| | | | |
 +-+-+-+-+
1| | | | |
 +-+-+-+-+
2| | | | |
 +-+-+-+-+
3| | | | |
 +-+-+-+-+
 
 


--------------------------

--------------------------

# 取出檔案副檔名，統一轉小寫並去除開頭的'.'字元
ext = os.path.splitext(ffname)[-1].lower().replace('.', '')
print('副檔名', ext)


--------------------------


------------------------------------------------------------

集合的方法：
交集		a.intersection(b)		a&b
聯集		a.union(b)			a|b
差集		a.difference(b)			a-b
對稱差集	a.symmetric_difference(b)	a^b



常用的檔案操作方法

read(size)
readline(size)
readlines(size)
readable()	檔案是否可讀取，回傳TF
writable()	檔案是否可寫入，回傳TF
write(文字內容)
writelines(文字內容串列)
tell()
seek(偏移量, 起始位置)
close()






opencv PIL 之一些CCRR操作，不用顯示出來，文字寫出來就好

是否任意matplotlib之圖皆可化為海生?



python
https://medium.com/seaniap/matplotlib%E8%B3%87%E6%96%99%E8%A6%96%E8%A6%BA%E5%8C%96-2-%E6%9F%B1%E7%8B%80%E5%9C%96%E8%88%87%E7%9B%B4%E6%96%B9%E5%9C%96-316c7f17f199




目前電腦語音有問題
win10 可播放中英文
win7 僅可播放英文
python / vcs 都一樣

python+webcam+win10 OK

python+webcam+win7 fail



------------------------------------------------------------




------------------------------------------------------------




------------------------------------------------------------



------------------------------------------------------------



------------------------------------------------------------


pygame.mixer.music.rewind() #重新啟動音樂
#將當前音樂的播放重新設置為一開始
 
pygame.mixer.music.stop() #停止音樂播放


pygame.mixer.music.pause() #暫時停止音樂播放
pygame.mixer.music.unpause()   #恢復暫停音樂


print('音量0.5')
pygame.mixer.music.set_volume(0.5)  #調節音樂音量
#設置音樂播放的音量。值參數在0.0和1.0之間。當加載新音樂時，音量就會重置
time.sleep(30)
print('音量1')
pygame.mixer.music.set_volume(1)
time.sleep(30)
print('音量0.3')
pygame.mixer.music.set_volume(0.3)
 

b=pygame.mixer.music.get_volume() #返回當前音量
#值將在0.0和1.0之間
 

b=pygame.mixer.music.get_busy()   #檢查音樂流是否在播放
#當音樂流在積極播放時，就會返回True。當音樂空閑時，返回False
#暫停相當于在播放，返回True
 




b=pygame.mixer.get_init()  #測試混音器是否初始化
#如果混音器已初始化，則返回正在使用的播放參數。如果混音器尚未初始化，則返回None
#get_init() -> (frequency, format, channels)
#(22050, -16, 2)
 

------------------------------------------------------------

sql

CREATE TABLE 範例

CREATE TABLE "Orders" 
(
  "Id" INTEGER PRIMARY KEY, 
  "CustomerId" VARCHAR(8000) NULL, 
  "EmployeesId" INTEGER NOT NULL, 
  "orderdate" VARCHAR(8000) NULL, 
  "RequiredDate" VARCHAR(8000) NULL, 
  "ShippedDate" VARCHAR(8000) NULL, 
  "ShipVia" INTEGER NULL, 
  "Freight" DECIMAL NOT NULL, 
  "ShipName" VARCHAR(8000) NULL, 
  "ShipAddress" VARCHAR(8000) NULL, 
  "ShipCity" VARCHAR(8000) NULL, 
  "ShipRegion" VARCHAR(8000) NULL, 
  "ShipPostalCode" VARCHAR(8000) NULL, 
  "ShipCountry" VARCHAR(8000) NULL 
);

CREATE TABLE "Orders" 
(
  "Id" INTEGER PRIMARY KEY, 
  "CustomerId" VARCHAR(8000) NULL, 
  "EmployeesId" INTEGER NOT NULL, 
  "orderdate" VARCHAR(8000) NULL, 
  "RequiredDate" VARCHAR(8000) NULL, 
  "ShippedDate" VARCHAR(8000) NULL, 
  "ShipVia" INTEGER NULL, 
  "Freight" DECIMAL NOT NULL, 
  "ShipName" VARCHAR(8000) NULL, 
  "ShipAddress" VARCHAR(8000) NULL, 
  "ShipCity" VARCHAR(8000) NULL, 
  "ShipRegion" VARCHAR(8000) NULL, 
  "ShipPostalCode" VARCHAR(8000) NULL, 
  "ShipCountry" VARCHAR(8000) NULL 
);
CREATE TABLE "OrderDetails" 
(
  "Id" VARCHAR(8000) PRIMARY KEY, 
  "OrderId" INTEGER NOT NULL, 
  "ProductId" INTEGER NOT NULL, 
  "UnitPrice" DECIMAL NOT NULL, 
  "Quantity" INTEGER NOT NULL, 
  "Discount" DOUBLE NOT NULL 
);
CREATE TABLE "Customers" 
(
  "Id" VARCHAR(8000) PRIMARY KEY, 
  "CompanyName" VARCHAR(8000) NULL, 
  "ContactName" VARCHAR(8000) NULL, 
  "ContactTitle" VARCHAR(8000) NULL, 
  "Address" VARCHAR(8000) NULL, 
  "City" VARCHAR(8000) NULL, 
  "Region" VARCHAR(8000) NULL, 
  "PostalCode" VARCHAR(8000) NULL, 
  "Country" VARCHAR(8000) NULL, 
  "Phone" VARCHAR(8000) NULL, 
  "Fax" VARCHAR(8000) NULL 
);


------------------------------------------------------------




------------------------------------------------------------



------------------------------------------------------------






