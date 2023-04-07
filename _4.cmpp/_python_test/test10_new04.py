x = 2
y = 0.5

print("x**y = "+str(x**y))


lst = [3, 2, 1, 5, 9, 0]
sorted(lst)
print(lst)


print('處理網址資料')

url = "https://www.nkust.edu.tw/p/403-1000-12-{}.php?Lang=zh-tw"
for pg in range(1, 11):
    print(url.format(pg))


url = "https://tw.stock.yahoo.com/news_list/url/d/e/N{}.html?q=&pg={}"
for cate in [1, 4]:
    for pg in range(1, 6):
        print(url.format(cate, pg))



def hexToDecimal(hex):
    decimalValue = 0
    for i in range(len(hex)):
        ch = hex[i]
        if 'A' <= ch <= 'F' or '0' <= ch <= '9':
            decimalValue = decimalValue * 16 + \
                hexCharToDecimal(ch)
        else:
            return None

    return decimalValue

def hexCharToDecimal(ch):
    if 'A' <= ch <= 'F':
        return 10 + ord(ch) - ord('A')
    else:
        return ord(ch) - ord('0')

hex = 'aa'
decimal = hexToDecimal(hex.upper())

if decimal == None:
    print("Incorrect hex number")
else:
    print("The decimal value for hex number", hex, "is", decimal) 



import random
import time

n = 10
lst = list(range(n))
print(lst)
random.shuffle(lst)
print(lst)
startTime = time.time()
lst.sort()
print("Sort time in Python is", int(time.time() - startTime), "seconds")

print(lst)


items = "03/11/2006".split("/")
print(items)




import time
def get_time():
    return time.strftime("%Y/%m/%d %A %H:%M:%S", time.localtime(time.time()))

localtime = get_time()
print('現在時間 : ' + localtime)


import time
print("現在時間")
localtime = time.strftime("%Y/%m/%d %A %H:%M:%S", time.localtime(time.time()))
print('現在時間 : ' + localtime)



print(__name__)
#print(__name__._version)



'''
import requests

r=requests.get("http://www.e-happy.com.tw")
r.encoding='utf-8'
print("下載完畢!")
if (r.status_code==200):
    print(1111)
    print(r.text)
    print(r.raw.read(100))
'''


username = 'david'
password = '1234'
if username=='david' and password=='1234':
    print('歡迎光臨本網站！')
else:
    print('帳號或密碼錯誤！')


filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/human2.jpg'

name = filename.split('/')
print(len(name))
print(name)
print(type(name))

ccc = name.reverse()
print(ccc)







