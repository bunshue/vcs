import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


# 2-5-1 Python 舊式字串格式化

errno = 50159747054
name = '鮑勃'

print('嘿, %s, 有錯誤 0x%x 發生了!' % (name, errno))

print('嘿, %(name)s, 有錯誤 0x%(errno)x 發生了!' % {'name': name, 'errno': errno})

# 2-5-2 Python 新式字串格式化

errno = 50159747054
name = '鮑勃'

print('嘿, {}, 有錯誤 0x{:x} 發生了!'.format(name, errno))

print('嘿, {name:s}, 有錯誤 0x{errno:x} 發生了!'.format(name=name, errno=errno))


# 2-5-3 f-string 字串格式化 (Python 3.6+)

errno = 50159747054
name = '鮑勃'

print(f'嘿, {name:s}, 有錯誤 0x{errno:x} 發生了!')

a = 5
b = 10

print(f'5 加 10 等於 {a + b} 而非 {2 * (a + b)}')



# 2-5-4 樣板字串格式化

from string import Template

errno = 50159747054
name = '鮑勃'

templ_string = '嘿 $name, 有錯誤 $error 發生了!'
print(Template(templ_string).substitute(name=name, error=hex(errno)))



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\__tmp_code\remaining1\5-2-2.py

# 5-2-2 array.array - C 語言格式數值陣列

import array

arr = array.array('f', (1.0, 1.5, 2.0, 2.5))

print(arr)

print(arr[1])

arr[1] = 23.0

print(arr)

del arr[1]

print(arr)

arr.append(42.0)

print(arr)

#arr[1] = 'hello'

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\__tmp_code\remaining1\5-2-3.py

# 5-2-3 str - 不可變 Unicode 字元陣列

arr = 'abcd'

print(arr)

print(arr[1])

print(type(arr))

print(type(arr[1]))

arr_list = list(arr)

print(arr_list)

print(''.join(arr_list))

#arr[1] = 'e'

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\__tmp_code\remaining1\5-2-4.py

# 5-2-4 bytes - 不可變位元組陣列

arr = bytes((0, 1, 2, 3))

print(type(arr))

print(arr)

print(arr[1])

data = 'this is data'
arr = str.encode(data)

print(arr)
print(bytes.decode(arr))

#arr = bytes((0, 300))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\__tmp_code\remaining1\5-2-5.py

# 5-2-5 bytearray - 可變位元組陣列

arr = bytearray((0, 1, 2, 3))

print(arr)

print(arr[1])

arr[1] = 23

print(arr)

del arr[1]

print(arr)

arr.append(42)

print(arr)

print(bytes(arr))

#arr[1] = 300

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\__tmp_code\remaining1\5-5-4.py

# 5-5-4 LifoQueue - 可用於多執行緒的堆疊 (2)

import threading, queue, time

source = ['吃飯', '睡覺', '寫程式', '散步', '聽音樂', '打牌', '玩電動']
threads_num = 3

q = queue.LifoQueue()
for item in source:
    q.put(item)

def worker():
    print('執行緒開始')
    while True:
        item = q.get()
        if item == 'STOP':
            print('執行緒結束')
            break
        print('處理資料:', item)
        time.sleep(0.01)
        q.task_done()


threads = []
for _ in range(threads_num):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

q.join()

for _ in range(threads_num):
    q.put('STOP')

for t in threads:
    t.join()

print('主程式結束')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\__tmp_code\remaining1\5-6-2.py

# 5-6-2 Queue - 可用於多執行緒的佇列

import threading, queue, time

source = ['吃飯', '睡覺', '寫程式', '散步', '聽音樂', '打牌', '玩電動']
threads_num = 3

q = queue.Queue()
for item in source:
    q.put(item)

def worker():
    print('執行緒開始')
    while True:
        item = q.get()
        if item == 'STOP':
            print('執行緒結束')
            break
        print('處理資料:', item)
        time.sleep(0.01)
        q.task_done()


threads = []
for _ in range(threads_num):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

q.join()

for _ in range(threads_num):
    q.put('STOP')

for t in threads:
    t.join()

print('主程式結束')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\__tmp_code\remaining1\5-6-3.py

# 5-6-3 multiprocessing.Queue - 給多核運算用的佇列

import multiprocessing, time


def worker(queue):
    print('process 開始')
    while True:
        item = queue.get()
        if item == 'STOP':
            print('process 結束')
            break
        print('處理資料:', item)
        time.sleep(0.01)


if __name__ == '__main__':
    
    source = ['吃飯', '睡覺', '寫程式', '散步', '聽音樂', '打牌', '玩電動']
    process_num = 3
    
    q = multiprocessing.Queue()
    for item in source:
        q.put(item)
    
    processes = []
    for _ in range(process_num):
        p = multiprocessing.Process(target=worker, args=(q,))
        p.start()
        processes.append(p)
    
    for _ in range(process_num):
        q.put('STOP')
    
    for p in processes:
        p.join()
    
    print('主程式結束')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\__tmp_code\remaining1\5-7-3.py

# 5-7-3 PriorityQueue - 可用於多執行緒的 heapq

import threading, queue, time

source = ['2-吃飯', '1-睡覺', '3-寫程式', '7-散步', '5-聽音樂', '6-打牌', '4-玩電動']
threads_num = 3

q = queue.PriorityQueue()
for item in source:
    q.put(item)

def worker():
    print('執行緒開始')
    while True:
        item = q.get()
        if item == 'STOP':
            print('執行緒結束')
            break
        print('處理資料:', item)
        time.sleep(0.01)
        q.task_done()


threads = []
for _ in range(threads_num):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

q.join()

for _ in range(threads_num):
    q.put('STOP')

for t in threads:
    t.join()

print('主程式結束')

print("------------------------------------------------------------")  # 60個

import requests #滙入requests套件

addr = 'https://www.books.com.tw/'
res = requests.get(addr)

#檢查狀態碼
if res.status_code == 200:
    res.encoding='utf-8'
    print(res.text)
else:
    print(res.status_code)
    
print('------------------------------------------------------------')	#60個

import urllib.request
#設定欲請求的網址
addr = 'http://www.grandtech.info/'
#以with/as敘述來取得網址，離開之後也能釋放資源
with urllib.request.urlopen(addr) as response:
    print('網頁網址',response.geturl())
    print('伺服器狀態碼',response.getcode())
    print('網頁表頭',response.getheaders())
    zct_str = response.read().decode('UTF-8')
print('將網頁資料轉成字串格式',zct_str)

print('------------------------------------------------------------')	#60個

from urllib.parse import urlparse

addr = 'https://www.zct.com.tw/hot_sale.php?act=goods&hash=5717321f978f1'

result = urlparse(addr)
print('回傳的 ParseResult 物件:')
print(result)
print('通訊協定:'+result.scheme)
print('網站網址:', result.netloc)
print('路徑:', result.path)
print('查詢字串:', result.query)



print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個




#政府資料開放平臺 XML格式資料擷取與應用

url="https://apiservice.mol.gov.tw/OdService/download/A17000000J-000007-yrg"

import urllib.request as ur

with ur.urlopen(url) as response:
    get_xml=response.read()
    

from bs4 import BeautifulSoup

data = BeautifulSoup(get_xml,'xml')
HandlingUnit = data.find_all('辦理單位')
ContactPerson = data.find_all('聯絡人')
DuringTraining = data.find_all('訓練期間')
ContactNumber = data.find_all('聯絡電話')
CourseTitle = data.find_all('課程名稱')


csv_str = ""
for i in range(0, len(HandlingUnit)):
    csv_str += "{},{},{},{},{}\n".\
                format(HandlingUnit[i].get_text(),\
                       ContactPerson[i].get_text(),\
                       ContactNumber[i].get_text(),\
                       DuringTraining[i].get_text(),\
                       CourseTitle[i].get_text())

with open("course_xml.csv", "w") as f:
    story=f.write(csv_str)    #寫入檔案
    
print("XML格式資料擷取與應用,已將資料寫入course_xml.csv")



print('------------------------------------------------------------')	#60個

#以BeautifulSoup套件進行網頁解析
from bs4 import BeautifulSoup
content="""
<!DOCTYPE html>
<html lang="zh-TW">
<head>
<title>BeautifulSoup套件進行網頁解析</title>
<meta charset="utf-8">
</head>
<body>
<h1 style="background-color:red; color:white; font-family:Segoe Script; border:3px #000000 solid;">Python is funny</h1>
Python簡單易學又有趣
<h1 style="color:rgb(255, 99, 71);">程式設計網站推薦</h1>
<a href="https://www.python.org/">Python官方網站</a>
</body>
</html>
"""
bs = BeautifulSoup(content,'html.parser') 
print('網頁標題屬性：') #網頁標題屬性
print(bs.title) #網頁標題屬性
print('--------------------------------------------------------')
print('網頁html語法區塊：') 
print(bs.find('html')) #<html>標籤
print('--------------------------------------------------------')
print('網頁表頭範圍：') 
print(bs.find('head')) #<head>標籤
print('--------------------------------------------------------')
print('網頁身體範圍：') 
print(bs.find('body')) #<body>標籤
print('--------------------------------------------------------')
print('第1個超連結：')
print(bs.find("a",{"href":"https://www.python.org/"}))
print('--------------------------------------------------------')

print('------------------------------------------------------------')	#60個


from bs4 import BeautifulSoup
import requests

addr = 'https://tw.stock.yahoo.com/s/list.php?\
c=%A8%E4%A5%A6%B9q%A4l&rr=0.84235400%201556957344'

#取得網頁原始程式碼
res = requests.get(addr).text 
#以html.parser解析程式解析程式碼
bs = BeautifulSoup(res, 'html.parser')
#以<tr>並配合屬性取得表格中每列內容
rows = bs.find_all('tr', {'height':'30'})

#印出要查詢資料各欄位名稱
print('代號 名稱  時間  成交  買進   賣出  漲跌   張數   昨收   開盤  最高  最低')
#讀取每列的內容，找出<td>
for row in rows:
    if row.find('td'):
        #屬性stripped_strings去餘每欄中字串的空白符號
        cols =[item for item in row.stripped_strings]
        #讀取List物件的元素
        for item in range(0,len(cols)):
            print(cols[item], end = ' ')
        print() #換行
print('------------------------------------------------------------')	#60個




import requests
from bs4 import BeautifulSoup

# 獲取網頁內容
game_ranking_html = requests.get('https://acg.gamer.com.tw/billboard.php?t=2&p=iOS')

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(game_ranking_html.text, "html.parser")

# 找到所有遊戲排名標題的標籤
games = soup.find_all('div', {'class': 'APP-LI-NAME'})

# 顯示遊戲排名標題
for i, game in enumerate(games, 1):
    print(f"{i}. {game.text.strip()}")



print("------------------------------------------------------------")  # 60個






"""
双色球随机选号程序
"""

from random import randrange, randint, sample


def display(balls):
    """
    输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print("|", end=" ")
        print("%02d" % ball, end=" ")
    print()


def random_select():
    """
    随机选择一组号码
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    for _ in range(6):
        index = randrange(len(red_balls))
        selected_balls.append(red_balls[index])
        del red_balls[index]
    # 上面的for循环也可以写成下面这行代码
    # sample函数是random模块下的函数
    # selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    n = int(input("机选几注: "))
    for _ in range(n):
        display(random_select())


if __name__ == "__main__":
    main()

print("------------------------------------------------------------")  # 60個


import random           # 導入模組random

n = 3
for i in range(n):
    print("1-100     : ", random.randint(1, 100))

for i in range(n):
    print("500-1000  : ", random.randint(500, 1000))

for i in range(n):
    print("2000-3000 : ", random.randint(2000, 3000))

print("------------------------------------------------------------")  # 60個

import random                       # 導入模組random

min, max = 1, 100                   # 隨機數最小與最大值設定
num = random.randint(min, max)  # 產生是否讓玩家答對的隨機數
print(num)

print("------------------------------------------------------------")  # 60個

import random                       # 導入模組random

fruits = ['蘋果', '香蕉', '西瓜', '水蜜桃', '百香果']
print(random.choice(fruits))

print("------------------------------------------------------------")  # 60個

import random                       # 導入模組random

porker = ['2', '3', '4', '5', '6', '7', '8',
          '9', '10', 'J', 'Q', 'K', 'A']
random.shuffle(porker)              # 將次序打亂重新排列
print(porker)

print("------------------------------------------------------------")  # 60個


import random                       # 導入模組random

min, max = 1, 10
ans = random.randint(min, max)      # 隨機數產生答案
print(ans)


print("------------------------------------------------------------")  # 60個


for _ in range(10):
    aa = random.randint(1,10)
    print(aa)

import random

val=0
data=[0]*80
for i in range(80):
    data[i]=random.randint(1,150)
while val!=-1:
    find=0
    val=int(input('請輸入搜尋鍵值(1-150)，輸入-1離開：'))
    for i in range(80):
        if data[i]==val:
            print('在第 %3d個位置找到鍵值 [%3d]' %(i+1,data[i]))
            find+=1
    if find==0 and val !=-1 :
        print('######沒有找到 [%3d]######' %val)
print('資料內容：')
for i in range(10):
    for j in range(8):
        print('%2d[%3d]  ' %(i*8+j+1,data[i*8+j]),end='')
    print('')

print("------------------------------------------------------------")  # 60個

import random
name = ["小明", "小黃", "小紅", "小綠", "小白"]

print("抽取一個元素：", random.choice(name))

print("抽取三個元素：", random.sample(name, 3))

print("抽取三個元素：", random.shuffle(name))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch08\ExRandrange.py

import random

print("任一整數", random.randrange(100))

print("任一整數", random.randrange(52, 100))

print("奇數", random.randrange(1, 100, 2))

print("偶數", random.randrange(0, 100, 2))




import random

for i in range(5):
    a = random.randint(1,10) #隨機取得整數
    print(a,end=' ')
print()
#給定items數列的初始值
word = ['apple','bird','tiger','happy','quick']
random.shuffle(word)  #使用shuffle函數打亂字的順序
print(word)#將打亂後字依序輸出



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



