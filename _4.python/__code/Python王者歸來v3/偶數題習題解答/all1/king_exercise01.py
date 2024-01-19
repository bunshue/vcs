# ex15_2.py
def wordsNum(fn):
    """適用英文文件, 輸入文章的檔案名稱,可以計算此文章的字數"""
    try:
        with open(fn) as file_Obj:  # 用預設"r"傳回檔案物件file_Obj
            data = file_Obj.read()  # 讀取檔案到變數data
    except FileNotFoundError:
        print("找不到 %s 檔案" % fn)
    else:
        wordList = data.split()     # 將文章轉成串列
        print(fn, " 文章的字數是 ", len(wordList))    # 列印文章字數

files = []
for i in range(5):
    fn = input("請輸入檔案名稱 : ")
    files.append(fn)
    
for file in files:
    wordsNum(file)




#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex15_4.py

# ex15_4.py
def division(x, y):
    try:                        # try - except指令
        x = int(x)
        y = int(y)
        return x / y
    except Exception:          # 除法的資料型態不符
        print("資料輸入錯誤")

op1 = input("請輸入第1個數字 : ")
op2 = input("請輸入第2個數字 : ")
print(division(op1, op2))          






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex15_6.py

# ex15_6.py
def wordsNum(fn):
    """適用英文文件, 輸入文章的檔案名稱,可以計算此文章的字數"""
    try:
        with open(fn) as file_Obj:  # 用預設"r"傳回檔案物件file_Obj
            data = file_Obj.read()  # 讀取檔案到變數data
    except FileNotFoundError:
        print("找不到 %s 檔案" % fn)
    else:
        wordList = data.split()     # 將文章轉成串列
        print(fn, " 文章的字數是 ", len(wordList))    # 列印文章字數
        return len(wordList)

def lenWord(fn):
    """檢查檔案長度必須是10到35個字元"""
    wdlen = wordsNum(fn)                              # 檔案長度
    if wdlen < 10:                                    # 檔案長度不足            
        raise Exception('檔案長度不足')
    if wdlen > 35:                                    # 檔案長度太長
        raise Exception('檔案長度太長')
    print('檔案長度正確')

for file in ("d1.txt","d2.txt","d3.txt","d4.txt","d5.txt"):  # 測試系列檔案
    try:
        lenWord(file)
    except Exception as err:
        print("檔案長度檢查異常發生: ", str(err))



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex15_8.py

# ex15_8.py
class Banks():
    # 定義銀行類別
    title = 'Taipei Bank'                   # 定義屬性
    def __init__(self, uname, money):       # 初始化方法
        self.name = uname                   # 設定存款者名字
        assert money >= 100, '開戶金額必需大於或等於100'
        self.balance = money                # 設定所存的錢

    def save_money(self, money):            # 設計存款方法
        assert money > 0, '存款money必需大於0'
        self.balance += money               # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        assert money > 0, '提款money必需大於0'
        assert money <= self.balance, '存款金額不足'
        self.balance -= money               # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.name.title(), " 目前餘額: ", self.balance)

hungbank = Banks('hung', 100)               # 定義物件hungbank
hungbank.get_balance()                      # 獲得存款餘額                
hungbank.save_money(300)                    # 存款300元
hungbank.get_balance()                      # 獲得存款餘額
chenbank = Banks('chen', -100)
chenbank.get_balance()                      # 獲得存款餘額





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex16_2.py

# ch16_2.py
def compareString(string):
    """檢查是否是搜尋的字串"""
    if string == searchStr:
        return True
    else:
        return False

def parseString(string):
    global num
    # notFoundSignal = True     # 註記沒有找到電話號碼為True
    for i in range(len(data)):  # 用迴圈逐步抽取字串長度做測試
        msg = data[i:i+len(string)]
        if compareString(msg):
            num += 1

fn = 'ex16_2.txt'
with open(fn) as file_obj:      # 讀取ex21_2.txt
    data = file_obj.read()

while True:
    searchStr = input("請輸入與搜尋字串 : ")
    num = 0
    parseString(searchStr)
    print("所搜尋字串 %s 共出現 %d 次" % (searchStr, num))
    print("\n是否繼續,輸入Y或y則程式繼續")
    again = input("= ")       # 讀取使用者輸入
    if again == 'Y' or again == 'y':    # 若輸入Y或y
        pass
    else:
        break
    
    



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex16_4.py

# ex16_4.py
import re
import os

files = os.listdir("D:\\Python\\ch14")
txtList = []
# 測試1
pattern = '(.*).txt'
print("列印*.txt")
for fn in files:
    #print(fn)
    fnresult = re.search(pattern,fn)      # 傳回搜尋結果
    if fnresult != None:
        txtList.append(fn)
print(txtList)

pyList = []  
# 測試2
print("列印ch14_10.py - ch14_19.py")
pattern = '(ch14_1(\d).py)'
for fn in files:
    fnresult = re.search(pattern,fn)      # 傳回搜尋結果
    if fnresult != None:
        pyList.append(fn)
print(pyList)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex16_6.py

# ex16_6.py
import re

msg = '''txt@deepwisdom.comyyy.twkkk,
         ser@deepmind.com.tw,
         hung@gmail.com
         aaa@gmail.comcomkk,
         kkk@gmail.com,
         abc@aa,
         service@deepwidsom.com
         mymail@yahoo.com
         de1988@kkk
         abcdefg'''
pattern = r'''(
    [a-zA-Z0-9_.]+                  # 使用者帳號
    @                               # @符號
    [a-zA-Z0-9-.]+                  # 主機域名domain
    [\.]                            # .符號
    [a-zA-Z]{2,4}\b                 # 可能是com或edu或其它
    ([\.])?                         # .符號, 也可能無特別是美國
    ([a-zA-Z]{2,4}\b)?              # 國別
    )'''
eMail = re.findall(pattern, msg, re.VERBOSE)     # 傳回搜尋結果
for mail in eMail:
    print(mail[0])




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex18_2.py

# ex18_2.py
from tkinter import *

window = Tk()
window.title("ex18_2")              # 視窗標題
lab1 = Label(window,text="Peter",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = Label(window,text="John",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = Label(window,text="Notron",
              bg="lightblue",       # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab4 = Label(window,text="Kevin",
              bg="lightgreen",      # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab5 = Label(window,text="Tommy",
              bg="lightblue",       # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab6 = Label(window,text="Mary",
              bg="lightyellow",     # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab7 = Label(window,text="Tracy",
              bg="lightblue",       # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab8 = Label(window,text="Mike",
              bg="lightyellow",     # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab9 = Label(window,text="Vicent",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15

lab1.grid(row=0,column=0)           # 格狀包裝
lab2.grid(row=0,column=1)           # 格狀包裝
lab3.grid(row=0,column=2)           # 格狀包裝
lab4.grid(row=1,column=0)           # 格狀包裝
lab5.grid(row=1,column=1)           # 格狀包裝
lab6.grid(row=1,column=2)           # 格狀包裝
lab7.grid(row=2,column=0)           # 格狀包裝
lab8.grid(row=2,column=1)           # 格狀包裝
lab9.grid(row=2,column=2)           # 格狀包裝
window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex18_4.py

# ex18_4.py
from tkinter import *

def myfun():
    monthrate = interest.get() / (12*100)
    loan = loanmoney.get()
    molecules = loan * monthrate
    denominator = 1-(1/(1+monthrate) ** (years.get() * 12))
    monthpaid = int(molecules / denominator)
    monthpayment.set(monthpaid)
    totalpaid = int(monthpaid * 12 * years.get())
    totalpayment.set(totalpaid)
        
window = Tk()
window.title("ex18_4")                  # 視窗標題

Interest = Label(window, text="利率")
Years = Label(window, text="貸款年數")
LoanMoney = Label(window, text="貸款金額")
MonthPayment = Label(window, text="每月支付金額")
TotalPayment = Label(window, text="總支付金額")

interest = DoubleVar()
years = IntVar()
loanmoney = IntVar()
monthpayment = IntVar()
totalpayment = IntVar()

interestE = Entry(window, textvariable=interest)
yearsE = Entry(window, textvariable=years)
loanmoneyE = Entry(window, textvariable=loanmoney)
monthpaymentL = Label(window, textvariable=monthpayment, bg='lightyellow')
totalpaymentL = Label(window, textvariable=totalpayment, bg='lightyellow')

Interest.grid(row=0, column=0)
Years.grid(row=1, column=0)
LoanMoney.grid(row=2, column=0)
MonthPayment.grid(row=3, column=0)
TotalPayment.grid(row=4, column=0)

interestE.grid(row=0, column=1, padx=2)
yearsE.grid(row=1, column=1, padx=2)
loanmoneyE.grid(row=2, column=1, padx=2)
monthpaymentL.grid(row=3, column=1, padx=2)
totalpaymentL.grid(row=4, column=1, padx=2)

btnExec = Button(window, text="計算", command=myfun)
btnExec.grid(row=5, column=1, pady=2)

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex18_6.py

# ex18_6.py
from tkinter import *

def printInfo():
    selection = ''
    for i in checkboxes:                    # 檢查此字典
        if checkboxes[i].get() == True:     # 被選取則執行
            selection = selection + sports[i] + " "
    x.set(selection)

window = Tk()
window.title("ex18_6")                     # 視窗標題

Label(window,text="請選擇喜歡的運動",
      fg="blue",bg="lightyellow",width=30).grid(row=0)

sports = {0:"美式足球",1:"棒球",2:"籃球",3:"網球",
          4:"桌球", 5:"排球"}               # 運動字典
checkboxes = {}                             # 字典存放被選取項目
for i in range(len(sports)):                # 將運動字典轉成核取方塊
    checkboxes[i] = BooleanVar()            # 布林變數物件
    Checkbutton(window,text=sports[i],
                variable=checkboxes[i]).grid(row=i+1,sticky=W)
  
Button(window,text="確定",width=10,command=printInfo).grid(row=i+2)

x = StringVar()
display = Label(window,textvariable=x, bg="lightgreen",width=30)
display.grid(row=i+3)

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex18_8.py

# ex18_8.py
from tkinter import *
    
window = Tk()
window.title("ex18_8")         # 視窗標題

sselogo = PhotoImage(file="hung.gif")
lab1 = Label(window,image=sselogo).pack(side="right")

sseText = """Python作者:洪錦魁
喜歡旅遊
曾經留學University of Mississippi和University of Kentucky"""
lab2 = Label(window,text=sseText,bg="lightyellow",
             justify=LEFT,padx=10).pack(side="left")

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex20_10.py

# ex20_10.py
import numpy as np
import matplotlib.pyplot as plt
from random import randint


def dice_generator(times, sides):
    ''' 處理隨機數 '''
    for i in range(times):              
        ranNum1 = randint(1, sides)             # 產生1-6隨機數
        ranNum2 = randint(1, sides)             # 產生1-6隨機數
        dice.append(ranNum1+ranNum2)
def dice_count(sides):
    '''計算2-11個出現次數'''
    for i in range(2, 13):
        frequency = dice.count(i)               # 計算i出現在dice串列的次數
        frequencies.append(frequency)
plt.rcParams["font.family"] = ["Microsoft JhengHei"]          
times = 1000                                    # 擲骰子次數
sides = 6                                       # 骰子有幾面
dice = []                                       # 建立擲骰子的串列
frequencies = []                                # 儲存每一面骰子出現次數串列
dice_generator(times, sides)                    # 產生擲骰子的串列
dice_count(sides)                               # 將骰子串列轉成次數串列
N = len(frequencies)
x = np.arange(N)                                # 長條圖x軸座標
width = 0.35                                    # 長條圖寬度
plt.bar(x, frequencies, width, color='g')       # 繪製長條圖
plt.ylabel('出現次數')
plt.title('測試 1000 次', fontsize=16)
plt.xticks(x, ('2','3','4','5','6','7','8','9','10','11','12'))
plt.yticks(np.arange(0, 150, 15))
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex20_12.py

# ex20_12.py
import matplotlib.pyplot as plt
from pylab import mpl

plt.rcParams["font.family"] = ["Microsoft JhengHei"] 

country = ["美國","澳洲","日本","歐洲","英國"]
pou = [10543, 2105, 1190, 3346, 980]
          
plt.pie(pou,labels=country,explode=(0,0,0.2,0,0),
        autopct="%1.2f%%")                          # 繪製圓餅圖
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex20_14.py

# ex20_14.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x)
fig = plt.figure()
ax1 = fig.add_subplot(121,projection='polar')
ax1.plot(x, y)
ax1.set_title("極座標 Sin 圖",fontsize=12)
ax2 = fig.add_subplot(122)
ax2.plot(x, y)
ax2.set_title('一般座標 Sin 圖',fontsize=12)
ax2.set_aspect(2)
plt.tight_layout()                      # 緊縮佈局
plt.show()




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex20_16.py

# ex20_16.py
import matplotlib.pyplot as plt
import numpy as np

def f1(x, y):                                # 左邊曲面函數
    return (np.power(x,2) + np.power(y, 2))
def f2(x, y):                                # 右邊曲面函數
    r = np.sqrt(np.power(x,2) + np.power(y, 2))
    return (np.sin(r))

X = np.arange(-3, 3, 0.1)                   # 曲面 X 區間
Y = np.arange(-3, 3, 0.1)                   # 曲面 Y 區間
X, Y = np.meshgrid(X, Y)                    # 建立 XY 座標
# 建立子圖
fig,ax = plt.subplots(1,2,figsize=(8,4),subplot_kw={'projection':'3d'})
# 左邊子圖乎叫 f1
ax[0].plot_surface(X, Y, f1(X,Y), cmap='hsv')   # 繪製 3D 圖
# 左邊子圖乎叫 f2
ax[1].plot_surface(X, Y, f2(X,Y), cmap='hsv')   # 繪製 3D 圖
plt.show()



      

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex20_2.py

# ex20_2.py
import matplotlib.pyplot as plt
import numpy as np

left = -2 * np.pi
right = 2 * np.pi
x = np.linspace(left, right, 50)

f1 = 3 * np.sin(x)                  # y陣列的變化
f2 = np.sin(x)
f3 = 0.2 * np.sin(x)

plt.plot(x, f1) 
plt.plot(x, f2, '-x')
plt.plot(x, f3)
plt.plot(x, f1, 'go')
plt.show()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex20_4.py

# ex20_4.py
import matplotlib.pyplot as plt
import numpy as np

left = -np.pi
right = np.pi
x = np.linspace(left, right, 100)
y = np.sin(2*x)                  # y陣列的變化

plt.plot(x, y) 
plt.fill_between(x, 1, y, alpha=0.1)
plt.show()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex20_6.py

# ex20_6.py
import matplotlib.pyplot as plt
import numpy as np

# 函數的係數
a = -1
b = 2
# 繪製區間圖形
x = np.linspace(-2, 4, 1000)
y = a*x**2 + b*x
plt.plot(x, y, color='b')
plt.fill_between(x, y1=y, y2=0, where=(x>=-2)&(x<=5),
                 facecolor='lightgreen')

plt.grid()
plt.show()















print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex20_8.py

# ex20_8.py
import matplotlib.pyplot as plt

data1 = [1, 2, 3, 4, 5, 6, 7, 8]                # data1線條
data2 = [1, 4, 9, 16, 25, 36, 49, 64]           # data2線條
data3 = [1, 3, 6, 10, 15, 21, 28, 36]           # data3線條
data4 = [1, 7, 15, 26, 40, 57, 77, 100]         # data4線條

seq = [1, 2, 3, 4, 5, 6, 7, 8]

plt.subplot(2, 2, 1)
plt.plot(seq, data1, '-*')

plt.subplot(2, 2, 2)
plt.plot(seq, data2, '-o')

plt.subplot(2, 2, 3)
plt.plot(seq, data3, '-^')

plt.subplot(2, 2, 4)
plt.plot(seq, data4, '-s')

plt.show()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex21_2.py

# ex21_2.py
import json

fn = 'populations.json'
with open(fn) as fnObj:
    getDatas = json.load(fnObj)                     # 讀json檔案

i = 0
fn = "out21_2.json"
tmpdict = {}
with open(fn, 'w') as fnObj:
    for getData in getDatas:
        if getData['Year'] == '2000':               # 篩選2000年的數據
            tmpdict["Country Name"] = getData['Country Name']
            tmpdict["Country Code"] = getData['Country Code']
            tmpdict["Year"] = getData['Year']
            tmpdict["Numbers"] = getData['Numbers']
            json.dump(tmpdict, fnObj)




        







        


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex21_4.py

# ex21_4.py
import pygal.maps.world

worldMap = pygal.maps.world.World()                     # 建立世界地圖物件
worldMap.title = 'Populations in China/Japan/Thailand'  # 世界地圖標題
worldMap.add('Asia',{'cn':1262645000,
                     'jp':126870000,
                     'th':63155029})                    # 標記人口資訊
worldMap.add('Europe',{'fr':60762406,
                     'se':1011781,
                     'sz':7184798})                    # 標記人口資訊
worldMap.add('Africa',{'cd':49626496,
                     'eg':67649043,
                     'za':44000833})                    # 標記人口資訊
worldMap.add('North America',{'us':282162848,
                     'mx':99959895,
                     'ca':30770661})                    # 標記人口資訊
worldMap.render_to_file('out21_4.svg')                 # 儲存地圖檔案



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex21_6.py

# ex21_6.py
import json

fn = 'aqi.json'
with open(fn) as fnObj:
    getDatas = json.load(fnObj)                         # 讀json檔案

for getData in getDatas:
    if getData['County'] == '臺北市':
        sitename = getData['SiteName']                  # 站台名稱
        siteid = getData['SiteId']                      # 站台ID
        pm25 = getData['PM2.5']                         # PM2.5值    
        print('站台ID =%3s  PM2.5值 =%3s  站台名稱 = %s ' %
              (siteid, pm25, sitename))




        


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex22_2.py

# ex22_2.py
import csv

fn = 'csvReport.csv'
with open(fn) as csvFile:               # 開啟csv檔案
    csvReader = csv.reader(csvFile)     # 讀檔案建立Reader物件
    listReport = list(csvReader)        # 將資料轉成串列
total2025 = 0
total2026 = 0
for row in listReport:
    if row[0] == 'Steve':
        if row[1] == '2025':
            total2025 += int(row[5])
        if row[1] == '2026':
            total2026 += int(row[5])

print("Steve's Total Revenue of 2025 = ", total2025)
print("Steveis Total Revenue of 2026 = ", total2026)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex22_4.py

# ex22_4.py
import csv
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
fn = 'TaipeiWeatherJan.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)          # 讀取文件下一列
    highTemps, meanTemps, lowTemps = [], [], []                       
    for row in csvReader:
        highTemps.append(int(row[1]))    # 儲存最高溫
        meanTemps.append(int(row[2]))    # 儲存均溫
        lowTemps.append(int(row[3]))     # 儲存最低溫

seq = range(1,32)
plt.plot(seq,highTemps,seq,meanTemps,seq,lowTemps)

plt.title("2025年1月台北天氣報告", fontsize=24)
plt.xlabel("", fontsize=14)
plt.ylabel(r'溫度 $C^{o}$', fontsize=14)
plt.show()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex22_6.py

# ex22_6.py
import csv
import matplotlib.pyplot as plt
from datetime import datetime

def convert_tw_date_to_ad(tw_date):
    # 分割日期為年、月、日
    year, month, day = map(int, tw_date.split('/'))
    # 將民國年轉換為西元年
    year += 1911
    # 重組日期並返回
    return f"{year}-{month:02d}-{day:02d}"

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
fn = 'ST43_3479_202310.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    for _ in range(5):                              # 跳過前5列
        next(csvReader)
    all_rows = list(csvReader)
    data_without_last_row = all_rows[:-1]           # 跳過最後一列
    
    mydates, openPrices, highPrices, lowPrices, closePrices = [], [], [], [], []   
    
    for row in data_without_last_row:
        try:
            # 將日期轉換為西元年格式
            converted_date = convert_tw_date_to_ad(row[0])
            # 使用 strptime 解析轉換後的日期字串
            parseDate = datetime.strptime(converted_date, "%Y-%m-%d")
            currentDate = parseDate.strftime("%Y-%m-%d") # 轉換後日期
            openPrice = eval(row[3])
            highPrice = eval(row[4])                # 設定最高價
            lowPrice = eval(row[5])                 # 設定最低價
            closePrice = eval(row[6])               # 設定收盤價
        except Exception:
            print(f'有缺值 {row}')
        else:
            openPrices.append(openPrice)            # 儲存開盤價
            highPrices.append(highPrice)            # 儲存最高價
            lowPrices.append(lowPrice)              # 儲存最低價
            closePrices.append(closePrice)          # 儲存收盤價
            mydates.append(currentDate)             # 儲存日期

fig = plt.figure(figsize=(12, 8))                   # 設定繪圖區大小
plt.plot(mydates, openPrices, '-p', label='開盤價')    # 繪製開盤價
plt.plot(mydates, highPrices, '-*', label='最高價')    # 繪製最高價
plt.plot(mydates, lowPrices, '-o', label='最低價')     # 繪製最低價
plt.plot(mydates, closePrices, '-^', label='收盤價')   # 繪製收盤價
plt.legend()
fig.autofmt_xdate()                                 # 日期旋轉
plt.title("2023年10月安勤公司日線圖", fontsize=24)
plt.ylabel('價格', fontsize=14)
plt.show()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex23_2.py

# ex23_2.py
import webbrowser

address = input("請輸入地址 : ")
webbrowser.open('http://www.google.com.tw/maps/place/' + address)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex23_4.py

# ex23_4.py
import bs4, requests

url = 'http://www.taiwanlottery.com.tw'
html = requests.get(url)

objSoup = bs4.BeautifulSoup(html.text, 'lxml')      # 建立BeautifulSoup物件

dataTag = objSoup.select('.contents_box02')         # 尋找class是contents_box02
        
# 找尋開出順序與大小順序的球
balls = dataTag[2].find_all('div', {'class':'ball_tx ball_yellow'})
print("開出順序 : ", end='')
for i in range(6):                                  # 前6球是開出順序
    print(balls[i].text, end='   ')

print("\n大小順序 : ", end='')
for i in range(6,len(balls)):                       # 第7球以後是大小順序
    print(balls[i].text, end='   ')

# 找出第二區的紅球                   
redball = dataTag[2].find_all('div', {'class':'ball_red'})
print("\n特別號   :", redball[0].text)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex24_2.py

# ex24_2.py
from selenium import webdriver
import time

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
url = 'https://www.wikipedia.org/'
browser.get(url)                    # 網頁下載至瀏覽器

txtBox = browser.find_element_by_id('searchInput')
txtBox.send_keys('Artificial Intelligence')          # 輸入表單資料
time.sleep(5)                       # 暫停5秒
txtBox.submit()                     # 送出表單

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex25_2.py

# ex25_2.py
from twilio.rest import Client

# 你從twilio.com申請的帳號
accountSid='AC308f91e9dc748a01538feb9d74ed993a'
# 你從twilio.com獲得的圖騰
authToken='f513161b63f71720f62118e4d33ca8ac'

client = Client(accountSid, authToken)
message = client.messages.create (
            from_ = "+15052070000",         # 這是twilio.com給你的號碼
            to = "+886952xxxxxx",           # 填上老師的號碼
            body = "感謝老師,我們學會了Python" )   # 發送的訊息




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\偶數題習題解答\all1\ex26_2.py

# ex26_2.py
import smtplib
from email.mime.text import MIMEText

from_addr = 'cshung1961@gmail.com'              # 設定發信帳號
pwd = input('請輸入 %s 的密碼 : ' % from_addr)  # 要求輸入發信帳號密碼
to_addr_list = ['cshung@deepwisdom.com.tw', 'jiinkwei@me.com']   # 設定收件人

with open('ex26_2.txt', 'rb') as fn:         # 讀取檔案內容
    mailContent = fn.read()
msg = MIMEText(mailContent, 'base64', 'utf-8')
msg['Content-Type'] = 'application/octet-stream'
msg['Content-Disposition'] = 'attachment; filename="ex26_2.txt"'
msg['Subject'] = '傳送Python學習心得附加檔案'
msg['From'] = '學生'
msg['To'] = 'cshung@deepwisdom.com.tw'
msg['Cc'] = 'jiinkwei@me.com'

mySMTP = smtplib.SMTP('smtp.gmail.com', 587)    # 執行連線
mySMTP.ehlo()                                   # 啟動對話
mySMTP.starttls()                               # 執行TLS加密               
mySMTP.login(from_addr, pwd)                    # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg.as_string())  # 執行發送信件
if status == {}:                                # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()                                   # 結束連線


print("------------------------------------------------------------")  # 60個

