import sys

print("------------------------------------------------------------")  # 60個

import threading, time

def wakeUp():
    print("threadObj執行緒開始")
    time.sleep(10)              # threadObj執行緒休息10秒
    print("女朋友生日")
    print("threadObj執行緒結束")
    
print("程式階段1")
threadObj = threading.Thread(target=wakeUp)
threadObj.start()               # threadObj執行緒開始工作
time.sleep(1)                   # 主執行緒休息1秒
print("程式階段2")

print("------------------------------------------------------------")  # 60個

import threading, time

def wakeUp(name, blessingWord):
    print("threadObj執行緒開始")
    time.sleep(10)              # threadObj執行緒休息10秒
    print(name, " ", blessingWord)
    print("threadObj執行緒結束")
    
print("程式階段1")
threadObj = threading.Thread(target=wakeUp, args=['NaNa','生日快樂'])
threadObj.start()               # threadObj執行緒開始工作
time.sleep(1)                   # 主執行緒休息1秒
print("程式階段2")

print("------------------------------------------------------------")  # 60個

import threading
import time

def worker():
    print(threading.current_thread().name, 'Starting')
    time.sleep(2)
    print(threading.current_thread().name, 'Exiting')

def manager():
    print(threading.current_thread().name, 'Starting')
    time.sleep(3)
    print(threading.current_thread().name, 'Exiting')

m = threading.Thread(target=manager)
w = threading.Thread(target=worker)
m.start()
w.start()

print("------------------------------------------------------------")  # 60個

import threading
import time

def worker():
    print(threading.current_thread().name, 'Starting')
    time.sleep(2)
    print(threading.current_thread().name, 'Exiting')
def manager():
    print(threading.current_thread().name, 'Starting')
    time.sleep(3)
    print(threading.current_thread().name, 'Exiting')

m = threading.Thread(target=manager)
w = threading.Thread(target=worker)
w2 = threading.Thread(name='Manager',target=worker)
m.start()
w.start()
w2.start()

print("------------------------------------------------------------")  # 60個


""" many
import requests
import os
import threading

# XKCD 漫畫的基本 URL
base_url = 'https://xkcd.com/'

# 定義下載漫畫的函數
def download_xkcd(start_comic, end_comic):
    for comic_number in range(start_comic, end_comic):
        # 跳過編號為 0 的漫畫，因為它不存在
        if comic_number == 0:
            continue

        url = f'{base_url}{comic_number}/info.0.json'   # 建立API URL來獲取漫畫資訊
        try:
            response = requests.get(url)
            response.raise_for_status()                 # 確保請求成功

            comic_json = response.json()
            comic_url = comic_json['img']               # 從JSON響應中提取圖片 URL
            print(f'\n圖片下載中 : {comic_url}...')

            # 向圖片 URL 發送請求並下載圖片
            res = requests.get(comic_url)
            res.raise_for_status()

            # 保存圖片到本地資料夾
            with open(os.path.join('xkcd_comics', os.path.basename(comic_url)), 'wb') as image_file:
                for chunk in res.iter_content(100000):
                    image_file.write(chunk)             # 寫入圖片數據
        except requests.exceptions.HTTPError as err:
            print(f'Failed to download comic {comic_number}: {err}')  # 輸出錯誤訊息

# 建立並啟動多個執行緒
thread_count = 10                                       # 執行緒的數量
comic_range = 10                                        # 每個執行緒負責下載的漫畫數量

# 如果不存在, 建立一個目錄來存儲下載的漫畫
if not os.path.exists('xkcd_comics'):
    os.makedirs('xkcd_comics')

# 建立執行緒並將它們添加到執行緒串列表
threads = []
for i in range(1, thread_count * comic_range, comic_range):         # 漫畫編號從 1 開始
    start = i
    end = i + comic_range
    thread = threading.Thread(target=download_xkcd, args=(start, end))
    threads.append(thread)
    thread.start()                                      # 啟動執行緒

# 等待所有執行緒完成
for thread in threads:
    thread.join()

print('漫畫圖片下載完成')

"""

print("------------------------------------------------------------")  # 60個

import subprocess

calcPro = subprocess.Popen('calc.exe')      # 傳回值是子行程
notePro = subprocess.Popen('notepad.exe')   # 傳回值是子行程
writePro = subprocess.Popen('write.exe')    # 傳回值是子行程
print(f"資料型態     = {type(calcPro)}")
print(f"列印calcPro  = {calcPro}")
print(f"列印notePro  = {notePro}")
print(f"列印writePro = {writePro}")

print("------------------------------------------------------------")  # 60個

import subprocess

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

paintPro = subprocess.Popen(['mspaint.exe', filename])
print(paintPro)

print("------------------------------------------------------------")  # 60個

import subprocess

path = r'C:\Users\User\AppData\Local\Programs\Python\Python311\python.exe'
pyPro = subprocess.Popen([path, 'ch30_12.py'])
print(pyPro)

print("------------------------------------------------------------")  # 60個

import subprocess

filename1 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/poetry.txt'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

textPro = subprocess.Popen(['start', filename1], shell=True)
pictPro = subprocess.Popen(['start', filename2], shell=True)
print("文字檔案子行程 = ", textPro)
print("圖片檔案子行程 = ", pictPro)

print("------------------------------------------------------------")  # 60個

import subprocess

calcPro = subprocess.run('calc.exe')      
print(f"資料型態     = {type(calcPro)}")
print(f"列印calcPro  = {calcPro}")

print("------------------------------------------------------------")  # 60個

import subprocess

ret = subprocess.run('echo %time%', shell=True, stdout=subprocess.PIPE)
print(f"資料型態       = {type(ret)}")
print(f"列印ret        = {ret}")
print(f"列印ret.stdout = {ret.stdout}")

print("------------------------------------------------------------")  # 60個
