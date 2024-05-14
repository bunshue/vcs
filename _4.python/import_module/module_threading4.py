import threading
import time
import random

print("多執行緒")

print("------------------------------------------------------------")  # 60個

import threading


def job(num):
    print("子執行緒", num)


threads = []
for i in range(3):
    threads.append(threading.Thread(target=job, args=(i,)))
    threads[i].start()

for i in range(3):
    print("主程式", i)

for i in threads:
    i.join()

print("結束")


print("------------------------------------------------------------")  # 60個

from concurrent.futures import ThreadPoolExecutor

a = True  # 定義 a 為 True


def run():
    global a  # 定義 a 是全域變數
    while a:  # 如果 a 為 True
        print(123)  # 不斷顯示 123
        time.sleep(1)  # 每隔一秒


def keyin():
    global a  # 定義 a 是全域變數
    if input() == "a":
        a = False  # 如果輸入的是 a，就讓 a 為 False，停止 run 函式中的迴圈


executor = ThreadPoolExecutor()
e1 = executor.submit(run)
e2 = executor.submit(keyin)
executor.shutdown()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
