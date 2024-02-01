import sys

print("------------------------------------------------------------")  # 60個

x1 = 1
x2 = 11
x3 = 111
x4 = 1111
print("x= ", str(x1).rjust(4))
print("x= ", str(x2).rjust(4))
print("x= ", str(x3).rjust(4))
print("x= ", str(x4).rjust(4))

print("------------------------------------------------------------")  # 60個

x1 = 1
x2 = 11
x3 = 111
x4 = 1111
print("x= ", str(x1).rjust(4), end="\r", flush=True)
print("x= ", str(x2).rjust(4), end="\r", flush=True)
print("x= ", str(x3).rjust(4), end="\r", flush=True)
print("x= ", str(x4).rjust(4), end="\r", flush=True)

print("------------------------------------------------------------")  # 60個

# ch25_1.py
from twilio.rest import Client

# 你從twilio.com申請的帳號
accountSid='AC6fdc3efffd15cabcdee8b361e9d4e67'
# 你從twilio.com獲得的圖騰
authToken='9a6dfab51a342a480e7cf9c1f88d3e638'

client = Client(accountSid, authToken)
message = client.messages.create (
            from_ = "+12512548607",         # 這是twilio.com給你的號碼
            to = "+886952000000",           # 這是收簡訊方的號碼
            body = "Python王者歸來" )       # 發送的訊息


print("------------------------------------------------------------")  # 60個
from deep_translator import GoogleTranslator

# 要翻譯的文本
text = '早安'

# 翻譯成英文
translator = GoogleTranslator(source='auto', target='en')
translation_en = translator.translate(text)
print("英文:", translation_en)

# 翻譯成日文, 另一種寫法
translation_ja = GoogleTranslator(source='auto', target='ja').translate(text)
print("日文:", translation_ja)

# 翻譯成韓文
translation_ko = GoogleTranslator(source='auto', target='ko').translate(text)
print("韓文:", translation_ko)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

from pydub import AudioSegment

mywav = r'C:Windows\Media\notify.wav'
# 讀取.wav文件
wav_audio = AudioSegment.from_wav(mywav)

# 轉換為.mp3
wav_audio.export("notify.mp3", format="mp3")

print("------------------------------------------------------------")  # 60個

import speech_recognition as sr

r = sr.Recognizer()

# 設定錄音檔案的儲存路徑
audio_file_path = "out33_7.wav"

with sr.Microphone() as source:
    print("請說英文 ...")
    audio = r.listen(source)

    # 將聲音保存為 WAV 檔案
    with open(audio_file_path, "wb") as file:
        file.write(audio.get_wav_data())

    try:
        # 使用Google的語音識別API
        text = r.recognize_google(audio)  
        print("你說的英文是 : {}".format(text))
    except:
        print("抱歉無法聽懂你的語音")

print("------------------------------------------------------------")  # 60個

import speech_recognition as sr

r = sr.Recognizer()

# 設定錄音檔案的儲存路徑
audio_file_path = "out33_8.wav"

with sr.Microphone() as source:
    print("請說中文 ...")
    audio = r.listen(source)

    # 將聲音保存為 WAV 檔案
    with open(audio_file_path, "wb") as file:
        file.write(audio.get_wav_data())

    try:
        # 使用Google的語音識別API
        text = r.recognize_google(audio, language="zh-TW")  
        print("你說的中文是 : {}".format(text))
    except:
        print("抱歉無法聽懂你的語音")

print("------------------------------------------------------------")  # 60個

import sys
print("請輸入字串, 輸入完按Enter = ", end = "")
msg = sys.stdin.readline()
print(msg)

print("------------------------------------------------------------")  # 60個

import sys
print("請輸入字串, 輸入完按Enter = ", end = "")
msg = sys.stdin.readline(8)         # 讀8個字
print(msg)

print("------------------------------------------------------------")  # 60個

import sys

sys.stdout.write("I like Python")

print("------------------------------------------------------------")  # 60個

import sys
for dirpath in sys.path:
    print(dirpath)

print("------------------------------------------------------------")  # 60個

import sys
print("命令列參數 : ", sys.argv)

print("------------------------------------------------------------")  # 60個

import keyword

keywordLists = ['as', 'while', 'break', 'sse', 'Python']
for x in keywordLists:
    print(f"{x:>8s} {keyword.iskeyword(x)}")

print("------------------------------------------------------------")  # 60個

import sys
from pprint import pprint
print("使用print")
print(sys.path)
print("使用pprint")
pprint(sys.path)

print("------------------------------------------------------------")  # 60個

import string

def encrypt(text, encryDict):           # 加密文件
    cipher = []
    for i in text:                      # 執行每個字元加密
        v = encryDict[i]                # 加密
        cipher.append(v)                # 加密結果
    return ''.join(cipher)              # 將串列轉成字串
    
abc = string.printable[:-5]             # 取消不可列印字元
subText = abc[-3:] + abc[:-3]           # 加密字串
encry_dict = dict(zip(subText, abc))    # 建立字典
print("列印編碼字典\n", encry_dict)     # 列印字典

msg = 'If the implementation is easy to explain, it may be a good idea.'
ciphertext = encrypt(msg, encry_dict)

print("原始字串 ", msg)
print("加密字串 ", ciphertext)

print("------------------------------------------------------------")  # 60個

import sys
def wordsNum(filename):
    """適用英文文件, 輸入文章的檔案名稱,可以計算此文章的字數"""
    try:
        with open(filename) as file_Obj:  # 用預設"r"傳回檔案物件file_Obj
            data = file_Obj.read()  # 讀取檔案到變數data
    except FileNotFoundError:
        print("找不到 %s 檔案" % filename)
    else:
        wordList = data.split()     # 將文章轉成串列
        print(filename, " 文章的字數是 ", len(wordList))    # 列印文章字數

"""
files = []
for i in range(5):
    filename = input("請輸入檔案名稱 : ")
    files.append(filename)
    
for file in files:
    wordsNum(file)
"""

print("------------------------------------------------------------")  # 60個

def wordsNum(filename):
    """適用英文文件, 輸入文章的檔案名稱,可以計算此文章的字數"""
    try:
        with open(filename) as file_Obj:  # 用預設"r"傳回檔案物件file_Obj
            data = file_Obj.read()  # 讀取檔案到變數data
    except FileNotFoundError:
        print("找不到 %s 檔案" % filename)
    else:
        wordList = data.split()     # 將文章轉成串列
        print(filename, " 文章的字數是 ", len(wordList))    # 列印文章字數
        return len(wordList)

def lenWord(filename):
    """檢查檔案長度必須是10到35個字元"""
    wdlen = wordsNum(filename)                              # 檔案長度
    if wdlen < 10:                                    # 檔案長度不足            
        raise Exception('檔案長度不足')
    if wdlen > 35:                                    # 檔案長度太長
        raise Exception('檔案長度太長')
    print('檔案長度正確')

for file in ("data/d1.txt","data/d2.txt","data/d3.txt","data/d4.txt","data/d5.txt"):  # 測試系列檔案
    try:
        lenWord(file)
    except Exception as err:
        print("檔案長度檢查異常發生: ", str(err))

print("------------------------------------------------------------")  # 60個

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

filename = 'data/ex16_2.txt'
with open(filename) as file_obj:      # 讀取ex21_2.txt
    data = file_obj.read()

"""
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
"""    

print("------------------------------------------------------------")  # 60個

import re
import os

files = os.listdir("data")
txtList = []
# 測試1
pattern = '(.*).txt'
print("列印*.txt")
for filename in files:
    #print(filename)
    fnresult = re.search(pattern,filename)      # 傳回搜尋結果
    if fnresult != None:
        txtList.append(filename)
print(txtList)

pyList = []  
# 測試2
print("列印ch14_10.py - ch14_19.py")
pattern = '(ch14_1(\d).py)'
for filename in files:
    fnresult = re.search(pattern,filename)      # 傳回搜尋結果
    if fnresult != None:
        pyList.append(filename)
print(pyList)


print("------------------------------------------------------------")  # 60個

import re

msg = """txt@deepwisdom.comyyy.twkkk,
         ser@deepmind.com.tw,
         hung@gmail.com
         aaa@gmail.comcomkk,
         kkk@gmail.com,
         abc@aa,
         service@deepwidsom.com
         mymail@yahoo.com
         de1988@kkk
         abcdefg"""
pattern = r"""(
    [a-zA-Z0-9_.]+                  # 使用者帳號
    @                               # @符號
    [a-zA-Z0-9-.]+                  # 主機域名domain
    [\.]                            # .符號
    [a-zA-Z]{2,4}\b                 # 可能是com或edu或其它
    ([\.])?                         # .符號, 也可能無特別是美國
    ([a-zA-Z]{2,4}\b)?              # 國別
    )"""
eMail = re.findall(pattern, msg, re.VERBOSE)     # 傳回搜尋結果
for mail in eMail:
    print(mail[0])

print("------------------------------------------------------------")  # 60個

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
worldMap.render_to_file('tmp_world_map.svg')                 # 儲存地圖檔案

print("------------------------------------------------------------")  # 60個

import webbrowser

address = "花蓮市中正路"
webbrowser.open('http://www.google.com.tw/maps/place/' + address)

print("------------------------------------------------------------")  # 60個

import bs4, requests
"""
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

import smtplib
from email.mime.text import MIMEText

from_addr = 'cshung1961@gmail.com'              # 設定發信帳號
pwd = input('請輸入 %s 的密碼 : ' % from_addr)  # 要求輸入發信帳號密碼
to_addr_list = ['cshung@deepwisdom.com.tw', 'jiinkwei@me.com']   # 設定收件人

with open('ex26_2.txt', 'rb') as filename:         # 讀取檔案內容
    mailContent = filename.read()
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
"""



print("------------------------------------------------------------")  # 60個

code1 = '洪'
print('洪')
print(hex(ord(code1)))     # 輸出字元'洪'的Unicode(16進位)碼值
code2 = '錦'
print('錦')
print(hex(ord(code2)))     # 輸出字元'錦'的Unicode(16進位)碼值
code3 = '魁'
print('魁')
print(hex(ord(code3)))     # 輸出字元'魁'的Unicode(16進位)碼值


print("------------------------------------------------------------")  # 60個

print(" 姓名    國文    英文    總分    平均")
print("%3s  %4d    %4d    %4d     %3.1f" % ("洪冰儒", 98, 90, 188, 188/2))
print("%3s  %4d    %4d    %4d     %3.1f" % ("洪雨星", 96, 95, 191, 191/2))
print("%3s  %4d    %4d    %4d     %3.1f" % ("洪冰雨", 92, 88, 180, 180/2))
print("%3s  %4d    %4d    %4d     %3.1f" % ("洪星宇", 93, 97, 190, 190/2))

print("------------------------------------------------------------")  # 60個

wd = """The Zen of Python, by Tim Peters

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
print("下列是Python之禪內文")
print(wd)
print("以分行符號將Python 之禪的行資料變成串列元素")
songlist = wd.split('\n')
print(songlist)

print("------------------------------------------------------------")  # 60個

abc = 'abcdefghijklmnopqrstuvwxyz'
front5 = abc[:5]
end21 = abc[5:]
subText = end21 + front5
print("abc     = ", abc)
print("subText = ", subText)

print("------------------------------------------------------------")  # 60個

cities = ['Taipei','Beijing','Tokyo','Chicago','Nanjing']
print(cities)
cities.append('London')
print(cities)
cities.insert(3,'Xian')
print(cities)
cities.remove('Tokyo')
print(cities)

print("------------------------------------------------------------")  # 60個

sc = [['洪錦魁', 80, 95, 88, 0, 0],
      ['洪冰儒', 98, 97, 96, 0, 0],
      ['洪雨星', 91, 93, 95, 0, 0],
      ['洪冰雨', 92, 94, 90, 0, 0],
      ['洪星宇', 92, 97, 90, 0, 0],
     ]      
sc[0][4] = sum(sc[0][1:4])
sc[1][4] = sum(sc[1][1:4])
sc[2][4] = sum(sc[2][1:4])
sc[3][4] = sum(sc[3][1:4])
sc[4][4] = sum(sc[4][1:4])
sc[0][5] = round((sc[0][4] / 3), 1)
sc[1][5] = round((sc[1][4] / 3), 1)
sc[2][5] = round((sc[2][4] / 3), 1)
sc[3][5] = round((sc[3][4] / 3), 1) 
sc[4][5] = round((sc[4][4] / 3), 1) 
print(sc[0])   
print(sc[1])
print(sc[2])
print(sc[3])
print(sc[4])

print("------------------------------------------------------------")  # 60個

site = input("請輸入網址 : ")
if site.startswith("http://") or site.startswith("https://"):
    print("網址格式正確")
else:
    print("網址格式錯誤")

print("------------------------------------------------------------")  # 60個

n = 10
for i in range(1,n):
    for j in range(1,n-i+1):
        print(j, end='')
    print()

print("------------------------------------------------------------")  # 60個

fruits1 = ['蘋果', '香蕉', '西瓜', '水蜜桃', '百香果']
fruits2 = ['香蕉', '芭樂', '西瓜']
print("目前fruits2串列 : ", fruits2)
for fruit in fruits2[:]:
    if fruit in fruits1:
        fruits2.remove(fruit)
        print(f"刪除 {fruit}")
print("最後fruits2串列 : ", fruits2)

print("------------------------------------------------------------")  # 60個

title = "9 * 9 Multiplication Table"
print("%s" % title.center(40))
for i in range(1,10):
    print(f"{i:4d}", end='')
print()                                 # 跳列輸出
for i in range(40):
    print("=", end='')                  # 列印分隔符號
print()                                 # 跳列輸出
for i in range(1, 10):
    print(i, '|', end='')
    for j in range(1, 10):
        print(f"{i*j:4d}", end='')      # 列印乘法值
    print()                             # 跳列輸出

print("------------------------------------------------------------")  # 60個

answer = 30                 # 正確數字
guess = 0                   # 設定所猜數字的初始值
index = 1                   # 猜測次數
while guess != answer:
    guess = int(input("請猜1-100間的數字 = "))
    if guess > answer:
        print("請猜小一點")
    elif guess < answer:
        print("請猜大一點")
    else:
        print("恭喜答對了")
        print(f"共猜 {index} 次")
    index += 1

print("------------------------------------------------------------")  # 60個

x1 = eval(input("請輸入數值 1 : "))
x2 = eval(input("請輸入數值 2 : "))

gcd = 1
n = 2
while n <= x1 and n <= x2:
    if x1 % n == 0 and x2 % n == 0:
        gcd = n
    n += 1

print(f"{x1} 和 {x2} 的最大公約數是 : {gcd}")

print("------------------------------------------------------------")  # 60個

names = ['洪錦魁','洪冰儒','東霞','大成']
lastname = []
for name in names:
    if name.startswith('洪'):    # 是否姓氏洪開頭
        lastname.append(name)    # 加入串列
print(lastname)

print("------------------------------------------------------------")  # 60個

sc = [[1, '洪錦魁', 80, 95, 88, 0, 0, 0],
      [2, '洪冰儒', 98, 97, 96, 0, 0, 0],
      [3, '洪雨星', 91, 93, 95, 0, 0, 0],
      [4, '洪冰雨', 92, 94, 90, 0, 0, 0],
      [5, '洪星宇', 92, 97, 90, 0, 0, 0],
     ]
# 計算總分與平均
print("原始成績單")
for i in range(len(sc)):
    print(sc[i])
    sc[i][5] = sum(sc[i][2:5])              # 填入總分
    sc[i][6] = round((sc[i][5] / 3), 1)     # 填入平均
sc.sort(key=lambda x:x[5],reverse=True)     # 依據總分高往低排序
# 以下填入名次
for i in range(len(sc)):                    # 填入名次
    sc[i][7] = i + 1
# 以下修正相同成績應該有相同名次
for i in range((len(sc)-1)):
    if sc[i][5] == sc[i+1][5]:              # 如果成績相同
        sc[i+1][7] = sc[i][7]               # 名次應該相同
# 以下依座號排序
sc.sort(key=lambda x:x[0])                  # 依據座號排序
print("最後成績單")
for i in range(len(sc)):
    print(sc[i])

print("------------------------------------------------------------")  # 60個

weight = 50              
increase = 1.2
n = 5
for i in range(int(n)):
    weight += increase
    print(f"第 {i+1} 年體重 : {weight:4.1f}")

print("------------------------------------------------------------")  # 60個

fahrenheit = [32, 77, 104]
celsius = [(x - 32) * 5 / 9 for x in fahrenheit]
print(celsius)

print("------------------------------------------------------------")  # 60個

n1 = [1,2,3,4,5]
n2 = [1,2,3,4,5]
result = [[x, y] for x in n1 for y in n2]
print(result)

print("------------------------------------------------------------")  # 60個

bookclub = ('John','Peter','Curry','Mike','Kevin')
print("讀書會成員")
for people in bookclub:
    print(people)
bookclub[0] = 'Johnnason'
for people in bookclub:
    print(people)

print("------------------------------------------------------------")  # 60個

tp = (1,2,3,4,5,2,3,1,4)
lst = list(tp)
newlst = []
for i in lst:
    if i not in newlst:
        newlst.append(i)
newtp = tuple(newlst)
print("新的元組內容 : ", newtp)    

print("------------------------------------------------------------")  # 60個

weatherH = (30, 28, 29, 31, 33, 35, 32)
weatherL = (20, 21, 19, 22, 23, 24, 20)
print(f"過去一周的最高溫度 {max(weatherH)}")
print(f"過去一周的最低溫度 {min(weatherH)}")

print("過去一周的平均溫度")     
for i in range(len(weatherH)):
    print(f"{((weatherH[i]+weatherL[i])/2):3.1f}  ", end="")

print("------------------------------------------------------------")  # 60個

abc = 'abcdefghijklmnopqrstuvwxyz'
encry_dict = {}
front3 = abc[:3]
end23 = abc[3:]
subText = end23 + front3
encry_dict = dict(zip(subText, abc))    # 建立字典
print("列印編碼字典\n", encry_dict)     # 列印字典

msgTest = 'python'                      # 測試字串
cipher = []
for i in msgTest:                       # 執行每個字元加密
    v = encry_dict[i]                   # 加密
    cipher.append(v)                    # 加密結果
ciphertext = ''.join(cipher)            # 將串列轉成字串

print("原始字串 ", msgTest)
print("加密字串 ", ciphertext)

print("------------------------------------------------------------")  # 60個

season = {'Spring':'春季',
          'Summer':'夏季',
          'Fall':'秋季',
          'Winter':'冬季'}

wd = input("請輸入欲查詢的單字 : ")
if wd in season:
    print(wd, " 中文字義是 : ", season[wd])
else:
    print("查無此單字")

print("------------------------------------------------------------")  # 60個

month = {'一月':'January','二月':'February','三月':'March',
         '四月':'April', '五月':'May','六月':'June',
         '七月':'July','八月':'August','九月':'September',
         '十月':'October','十一月':'November','十二月':'December'
        }
         
key = input("請輸入月份(例如:一月) : ")
if key in month:
    print(month[key])
else:
    print('輸入錯誤')

print("------------------------------------------------------------")  # 60個

noodles = {'牛肉麵':100, '肉絲麵':80, '陽春麵':60,
           '大滷麵':90, '麻醬麵':70}
print(noodles)
for noodle, price in sorted(noodles.items(), key=lambda item:item[1]):
    print(noodle,":",price)

print("------------------------------------------------------------")  # 60個

armys = []                      # 建立小兵空串列
# 建立50個小兵
for soldier_number in range(50):
    soldier = {'tag':'red', 'score':3, 'speed':'slow'}
    armys.append(soldier)
# 列印前3個小兵
print("前3名小兵資料")
for soldier in armys[:3]:
    print(soldier)
# 更改編號36到38的小兵
for soldier in armys[35:38]:
    if soldier['tag'] == 'red':
        soldier['tag'] = 'blue'
        soldier['score'] = 5
        soldier['speed'] = 'medium'
# 列印編號35到40的小兵
print("列印編號35到40小兵資料")
for soldier in armys[34:40]:
    print(soldier)
# 更改編號47到49的小兵
for soldier in armys[47:50]:
    if soldier['tag'] == 'red':
        soldier['tag'] = 'green'
        soldier['score'] = 10
        soldier['speed'] = 'fast'
# 列印編號47到49的小兵
print("列印編號47到49小兵資料")
for soldier in armys[47:50]:
    print(soldier)   

print("------------------------------------------------------------")  # 60個

song = """Are you sleeping, are you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong."""

# 以下是將歌曲大寫字母全部改成小寫
songLower = song.lower()            # 歌曲改為小寫

# 將歌曲的標點符號用空字元取代
for ch in songLower:                
        if ch in ".,?":
            songLower = songLower.replace(ch,'')

# 將歌曲字串轉成串列
songList = songLower.split()        

# 將歌曲串列處理成字典
dict = {wd:songList.count(wd) for wd in songList}
   
maxCount = max(dict.values())       # 出現最多次數
for key, count in dict.items():
    if count == maxCount:
        print(f"字串 {key} 出現最多次共出現 {count} 次")

print("------------------------------------------------------------")  # 60個

A = []
for i in range(1,100,2):
    A.append(i)
B = []
for i in range(0,101,5):
    B.append(i)
aSet = set(A)                   # 將串列A轉成集合aSet
bSet = set(B)                   # 將串列B轉成集合bSet

unionAB = aSet | bSet
print("聯集 : ", unionAB)
interAB = aSet & bSet
print("交集 : ", interAB)
A_B = aSet - bSet
print("A-B差集 : ", A_B)
B_A = bSet - aSet
print("B-A差集 : ", B_A)

print("------------------------------------------------------------")  # 60個

A = []
for i in range(1,100,2):
    A.append(i)

num = 2
B = []
primeNum = 0
while num < 100:
    if num == 2:                                # 2是質數所以直接輸出
        B.append(num)
        primeNum += 1
    else:
        for n in range(2, num):                 # 用2 .. num-1當除數測試
            if num % n == 0:                    # 如果整除則不是質數
                break                           # 離開迴圈
        else:                                   # 否則是質數
            primeNum += 1
            B.append(num)
    num += 1

aSet = set(A)                                   # 將串列A轉成集合aSet
bSet = set(B)                                   # 將串列B轉成集合bSet

unionAB = aSet | bSet
print("聯集 : ", unionAB)
interAB = aSet & bSet
print("交集 : ", interAB)
A_B = aSet - bSet
print("A-B差集 : ", A_B)
B_A = bSet - aSet
print("B-A差集 : ", B_A)
AsdB = aSet ^ bSet
print("AB對稱差集 : ", AsdB)

print("------------------------------------------------------------")  # 60個

aSet = {i for i in range(1,100,2)}
bSet = {i for i in range(0,101,5)}

unionAB = aSet | bSet
print("聯集 : ", unionAB)
interAB = aSet & bSet
print("交集 : ", interAB)
A_B = aSet - bSet
print("A-B差集 : ", A_B)
B_A = bSet - aSet
print("B-A差集 : ", B_A)

print("------------------------------------------------------------")  # 60個

def reverse(n):
    reverseN = 0
    while n != 0:
        r = n % 10
        reverseN = reverseN * 10 + r
        n //= 10
    return reverseN 

def isPalindrome(n):
    return n == reverse(n)
        
x = eval(input("請輸入1個數值 = "))
if isPalindrome(x):
    print("這是回文數")
else:
    print("這不是回文數")

print("------------------------------------------------------------")  # 60個

def isPalindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[len(s)-1]:
        return False
    else:
        return isPalindrome(s[1:len(s)-1])

string = input("請輸入字串 : ")
if isPalindrome(string):
    print(f"{string} 是回文字串")
else:
    print(f"{string} 不是回文字串")

print("------------------------------------------------------------")  # 60個

def mysum(nLst):
    if nLst == []:
        return 0
    return nLst[0] + mysum(nLst[1:])

data = [5, 7, 9, 15, 21, 6]
print(f'mysum = {mysum(data)}')

print("------------------------------------------------------------")  # 60個

def fun(n):
    if n == 1:
        return 1.0 / 2
    else:
        return fun(n - 1) + (n * 1.0) / (n + 1)

n = eval(input('請輸入整數 : '))
for i in range(1, n + 1):
    print(f"{i} = {fun(i):5.3f}")           

print("------------------------------------------------------------")  # 60個

mylist = [5, 10, 15, 20, 25, 30]

evenlist = list(filter(lambda x: (x % 2 == 0), mylist))

# 輸出偶數串列
print("偶數串列: ",evenlist)

print("------------------------------------------------------------")  # 60個

def mymax(n1, n2):
    """ 較大值設計 """
    if n1 > n2:
        print("較大值是 : ", n1)
    else:
        print("較大值是 : ", n2)
        
x1, x2 = eval(input("請輸入2個數值 = "))
mymax(x1, x2)

print("------------------------------------------------------------")  # 60個

def upper(func):                # 大寫裝飾器
    def newFunc(args):
        oldresult = func(args)
        newresult = oldresult.upper()
        return newresult
    return newFunc
def bold(func):                 # 加粗體字串裝飾器
    def wrapper(args):
        return 'bold' + func(args) + 'bold'
    return wrapper
def italic(func):               # 加斜體字串裝飾器
    def wrapper(args):
        return 'italic' + func(args) + 'italic'
    return wrapper
@italic
@bold                           # 設定加粗體字串裝飾器
@upper                          # 設定大寫裝飾器
def greeting(string):           # 問候函數
    return string

print(greeting('Hello! iPhone'))

print("------------------------------------------------------------")  # 60個

def factorial(n):
    """ 計算n的階乘, n 必須是正整數 """
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))

N = eval(input("請輸入城市的個數 : "))
times = 10000000000000          # 電腦每秒可處理數列數目
day_secs = 60 * 60 * 24         # 一天秒數
year_secs = 365 * day_secs      # 一年秒數
combinations = factorial(N)     # 組合方式
years = combinations / (times * year_secs)
print(f"城市個數 {N}, 路徑組合數 = {combinations}")
print(f"需要 {years} 年才可以獲得結果")

print("------------------------------------------------------------")  # 60個

def guest_info(firstname, middlename, lastname, gender):
    """ 整合客戶名字資料 """
    if gender == "M":
        welcome = 'Mr. ' + firstname + middlename + lastname + 'Welcome'
    else:
        welcome = 'Miss ' + firstname + middlename + lastname + 'Welcome'
    return welcome

info1 = guest_info('Ivan ', 'Carl ', 'Hung ', 'M')
info2 = guest_info('Mary ', 'Ice ', 'Hung ', 'F')
print(info1)
print(info2)

print("------------------------------------------------------------")  # 60個

def pi(n):
    p = 0
    for i in range(1,n+1, 1):
        p += 4 *((-1)**(i+1)/(2*i-1))
    return p

print("  i      PI ")
print("================")
for i in range(1, 10000, 1000):
    print("%5d   %7.5f" % (i, pi(i)))

print("------------------------------------------------------------")  # 60個

class Myschool():
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def msg(self):
        print("Hi!" + self.name.title() + "你的成績是" + str(self.score) + "分")

A = Myschool("kevin",80)
A.msg()

print("------------------------------------------------------------")  # 60個

class Banks():
    # 定義銀行類別

    def __init__(self, uname):              # 初始化方法
        self.__name = uname                 # 設定私有存款者名字
        self.__balance = 0                  # 設定私有開戶金額是0
        self.__bankname = "Taipei Bank"     # 設定私有銀行名稱
        self.__rate = 30                    # 預設美金與台幣換匯比例
        self.__service_charge = 0.01        # 換匯的服務費

    def save_money(self, money):            # 設計存款方法
        self.__balance += money             # 執行存款
        print("存款 ", money, " 完成")      # 列印存款完成

    def withdraw_money(self, money):        # 設計提款方法
        self.__balance -= money             # 執行提款
        print("提款 ", money, " 完成")      # 列印提款完成

    def get_balance(self):                  # 獲得存款餘額
        print(self.__name.title(), " 目前餘額: ", self.__balance)

    def usa_to_taiwan(self, usa_d):         # 美金兌換台幣方法
        self.result = self.__cal_rate(usa_d)
        return self.result
    def taiwan_to_usa(self, usa_d):
        self.result = self.__newcal_rate(usa_d)
        return self.result
    def __newcal_rate(self, usa_d):
        return int(usa_d * self.__rate * (1 + self.__service_charge))
    def __cal_rate(self,usa_d):             # 計算換匯這是私有方法
        return int(usa_d * self.__rate * (1 - self.__service_charge))
        
hungbank = Banks('hung')                    # 定義物件hungbank
hungbank.save_money(5000)
hungbank.get_balance()
hungbank.withdraw_money(3000)
hungbank.get_balance()
hungbank.save_money(1500)
hungbank.get_balance()
print("購買100元美金")
changedallor = hungbank.taiwan_to_usa(100)
hungbank.withdraw_money(changedallor)
hungbank.get_balance()

print("------------------------------------------------------------")  # 60個

class Animals():
    """Animals類別, 這是基底類別 """
    def __init__(self, animal_name, animal_age ):
        self.name = animal_name # 紀錄動物名稱
        self.age = animal_age   # 紀錄動物年齡

    def run(self):              # 輸出動物 is running
        print(self.name.title(), " is running")

class Dogs(Animals):
    """Dogs類別, 這是Animal的衍生類別 """
    def __init__(self, dog_name, dog_age):
        super().__init__('My pet ' + dog_name.title(), dog_age)

class Birds(Animals):
    """Birds類別, 這是Animal的衍生類別 """
    def __init__(self, bird_name, bird_age):
        super().__init__('My pet ' + bird_name.title(), bird_age)
    def run(self):
        print(self.name.title(), "is flying")

mycat = Animals('lucy', 5)      # 建立Animals物件以及測試
print(mycat.name.title(), ' is ', mycat.age, " years old.")
mycat.run()

mydog = Dogs('lily', 6)         # 建立Dogs物件以及測試
print(mydog.name.title(), ' is ', mydog.age, " years old.")
mydog.run()
        
mybird = Birds('Cici', 8)       # 建立Birds物件以及測試
print(mybird.name.title(), ' is ', mybird.age, " years old.")
mybird.run()      

print("------------------------------------------------------------")  # 60個

class Grandfather():
    """ 定義祖父類別 """
    def action1(self):
        print("Grandfather")
        
class Father(Grandfather):
    """ 定義父親類別 """
    def action2(self):      # 定義action2()
        print("Father")

class Uncle(Grandfather):
    """ 定義叔父類別 """
    def action2(self):      # 定義action2()
        print("Uncle")

class Aunt(Grandfather):
    """ 定義阿姨類別 """
    def action2(self):      # 定義action2()
        print("Aunt")
        
class Ivan(Father, Uncle, Aunt):
    """ 定義Ivan類別 """
    def action3(self):
        print("Ivan")

ivan = Ivan()
ivan.action3()              # 順序 Ivan
ivan.action2()              # 順序 Ivan -> Father
ivan.action1()              # 順序 Ivan -> Father -> Grandfather

print("------------------------------------------------------------")  # 60個

class Grandfather():
    """ 定義祖父類別 """
    def action1(self):
        print("Grandfather")
        
class Father(Grandfather):
    """ 定義父親類別 """
    def action2(self):      # 定義action2()
        print("Father")

class Uncle(Grandfather):
    """ 定義叔父類別 """
    def action2(self):      # 定義action2()
        print("Uncle")

class Aunt(Grandfather):
    """ 定義阿姨類別 """
    def action2(self):      # 定義action2()
        print("Aunt")
        
class Ivan(Father, Uncle, Aunt):
    """ 定義Ivan類別 """
    def action3(self):
        print("Ivan")

ivan = Ivan()
ivan.action3()              # 順序 Ivan
ivan.action2()              # 順序 Ivan -> Father
ivan.action1()              # 順序 Ivan -> Father -> Grandfather

print("------------------------------------------------------------")  # 60個

class Grandfather():
    """ 定義祖父類別 """
    def action1(self):
        print("Grandfather")
        
class Father(Grandfather):
    """ 定義父親類別 """
    def action2(self):      # 定義action2()
        print("Father")

class Uncle(Grandfather):
    """ 定義叔父類別 """
    def action2(self):      # 定義action2()
        print("Uncle")

class Aunt(Grandfather):
    """ 定義阿姨類別 """
    def action2(self):      # 定義action2()
        print("Aunt")
        
class Ivan(Uncle, Aunt, Father):
    """ 定義Ivan類別 """
    def action3(self):
        print("Ivan")

ivan = Ivan()
ivan.action3()              # 順序 Ivan
ivan.action2()              # 順序 Ivan -> Father
ivan.action1()              # 順序 Ivan -> Father -> Grandfather

print("------------------------------------------------------------")  # 60個

class Grandfather():
    """ 定義祖父類別 """
    def action1(self):
        print("Grandfather")
        
class Father(Grandfather):
    """ 定義父親類別 """
    def action2(self):      # 定義action2()
        print("Father")

class Uncle(Grandfather):
    """ 定義叔父類別 """
    def action2(self):      # 定義action2()
        print("Uncle")

class Aunt(Grandfather):
    """ 定義阿姨類別 """
    def action2(self):      # 定義action2()
        print("Aunt")
        
class Ivan(Aunt, Father, Uncle):
    """ 定義Ivan類別 """
    def action3(self):
        print("Ivan")

ivan = Ivan()
ivan.action3()              # 順序 Ivan
ivan.action2()              # 順序 Ivan -> Father
ivan.action1()              # 順序 Ivan -> Father -> Grandfather

print("------------------------------------------------------------")  # 60個









print("------------------------------------------------------------")  # 60個

import MyMath

# 使用者輸入
print("請輸入運算")
print("1:加法")
print("2:減法")
print("3:乘法")
print("4:除法")
op = int(input("輸入1/2/3/4: "))
a = int(input("a = "))
b = int(input("b = "))

# 程式運算
if op == 1:
    print("a + b = ", MyMath.add(a, b))   # 輸出a-b字串和結果
elif op == 2:
    print("a - b = ", MyMath.sub(a, b))   # 輸出a-b字串和結果
elif op == 3:
    print("a * b = ", MyMath.mul(a, b))   # 輸出a*b字串和結果
elif op == 4:
    print("a / b = ", MyMath.div(a, b))   # 輸出a/b字串和結果
else:
    print("運算方法輸入錯誤")

print("------------------------------------------------------------")  # 60個

import sys

print("目前Python版本是:     ", sys.version)
print("目前Python版本是:     ", sys.version_info)
print("目前Python平台是:     ", sys.platform)
print("目前Python視窗版本是: ", sys.getwindowsversion())
print("目前Python可執行檔路徑", sys.executable)








print("------------------------------------------------------------")  # 60個

secretcode = '112299'                                   # 設定密碼
codeNotFound = True                                     # 尚未找到密碼為True
for i1 in range(0, 10):                                 # 第一位數
    if codeNotFound:            # 檢查是否找到沒有找到才會往下執行
        for i2 in range(0, 10):                         # 第二位數
            if codeNotFound:    # 檢查是否找到沒有找到才會往下執行
                for i3 in range(0, 10):                 # 第三位數
                    if codeNotFound:
                        for i4 in range(0, 10):
                            if codeNotFound:
                                for i5 in range(0, 10):
                                    if codeNotFound:
                                        for i6 in range(0, 10):
                                            code = str(i1)+str(i2)+str(i3)+str(i4)+str(i5)+str(i6) # 組成密碼
                                            if code == secretcode:              # 比對密碼
                                                print('Bingo!', code)
                                                codeNotFound = False            # 註明已經比對成功
                                                break
                                            else:
                                                print(code)                     # 列印無效碼

print("------------------------------------------------------------")  # 60個
import sqlite3
conn = sqlite3.connect("data29_1.db")   # 資料庫連線
sql = """SELECT name, tel
        from students
        where gender = "F""""
results = conn.execute(sql)
allstudents = results.fetchall()        # 結果轉成元素是元組的串列
for student in allstudents:
    print(student)
conn.close()                            # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個

import threading, time

def wakeUp(mytime,note,job):
    print(job," 開始")
    starttime = int(time.time())
    while int(time.time()) - starttime < mytime:
        pass
    print(note)
    print(job," 結束")
    
print("程式階段1")
threadObj1 = threading.Thread(target=wakeUp,
                args=[30,'買機票去北京','threadJob1'])
threadObj1.start()              # threadObj1執行緒開始工作
time.sleep(1)                   # 主執行緒休息1秒

threadObj2 = threading.Thread(target=wakeUp,
                args=[60,'送花給女友', 'threadJob2'])
threadObj2.start()              # threadObj1執行緒開始工作
time.sleep(1)                   # 主執行緒休息1秒

print("程式階段2,正常工作")

print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




import csv

filename = 'data/csvReport.csv'
with open(filename) as csvFile:               # 開啟csv檔案
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

import json

filename = 'data/populations.json'
with open(filename) as fnObj:
    getDatas = json.load(fnObj)                     # 讀json檔案

i = 0
filename = "_tmp_population.json"
tmpdict = {}
with open(filename, 'w') as fnObj:
    for getData in getDatas:
        if getData['Year'] == '2000':               # 篩選2000年的數據
            tmpdict["Country Name"] = getData['Country Name']
            tmpdict["Country Code"] = getData['Country Code']
            tmpdict["Year"] = getData['Year']
            tmpdict["Numbers"] = getData['Numbers']
            json.dump(tmpdict, fnObj)

print("------------------------------------------------------------")  # 60個

import json

filename = 'data/aqi.json'
with open(filename) as fnObj:
    getDatas = json.load(fnObj)                         # 讀json檔案

for getData in getDatas:
    if getData['County'] == '臺北市':
        sitename = getData['SiteName']                  # 站台名稱
        siteid = getData['SiteId']                      # 站台ID
        pm25 = getData['PM2.5']                         # PM2.5值    
        print('站台ID =%3s  PM2.5值 =%3s  站台名稱 = %s ' %
              (siteid, pm25, sitename))

print("------------------------------------------------------------")  # 60個




