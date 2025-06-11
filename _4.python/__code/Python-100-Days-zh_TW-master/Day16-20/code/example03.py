import sys

print("------------------------------------------------------------")  # 60個

import glob
import os
import time

print("多線程建立縮圖")

from concurrent.futures import ThreadPoolExecutor
from threading import Thread

from PIL import Image

def gen_thumbnail(infile):
    file, ext = os.path.splitext(infile)
    filename = file[file.rfind('/') + 1:]
    for size in (32, 64, 128):
        outfile = f'thumbnails/{filename}_{size}_{size}.png'
        image = Image.open(infile)
        image.thumbnail((size, size))
        image.save(outfile, format='PNG')

pool = ThreadPoolExecutor(max_workers=30)
futures = []
for infile in glob.glob('images/*'):
    print(infile)
    # submit方法是非阻塞式的方法 
    # 即便工作线程数已经用完，submit方法也会接受提交的任务 
    future = pool.submit(gen_thumbnail, infile)
    futures.append(future)
for future in futures:
    # result方法是一个阻塞式的方法 如果线程还没有结束
    # 暂时取不到线程的执行结果 代码就会在此处阻塞
    future.result()
# shutdown也是非阻塞式的方法 但是如果已经提交的任务还没有执行完
# 线程池是不会停止工作的 shutdown之后再提交任务就不会执行而且会产生异常
pool.shutdown()

print("------------------------------------------------------------")  # 60個

from concurrent.futures import ThreadPoolExecutor
from random import randint
from time import sleep

import threading

class Account():
    """银行账户"""

    def __init__(self, balance=0):
        self.balance = balance
        lock = threading.Lock()
        self.condition = threading.Condition(lock)

    def withdraw(self, money):
        """取钱"""
        with self.condition:
            while money > self.balance:
                self.condition.wait()
            new_balance = self.balance - money
            sleep(0.001)
            self.balance = new_balance

    def deposit(self, money):
        """存钱"""
        with self.condition:
            new_balance = self.balance + money
            sleep(0.001)
            self.balance = new_balance
            self.condition.notify_all()


def add_money(account):
    while True:
        money = randint(5, 10)
        account.deposit(money)
        print(threading.current_thread().name,
              ':', money, '====>', account.balance)
        sleep(0.5)


def sub_money(account):
    while True:
        money = randint(10, 30)
        account.withdraw(money)
        print(threading.current_thread().name,
              ':', money, '<====', account.balance)
        sleep(1)


account = Account()
with ThreadPoolExecutor(max_workers=10) as pool:
    for _ in range(5):
        pool.submit(add_money, account)
        pool.submit(sub_money, account)

print("------------------------------------------------------------")  # 60個

"""
aiohttp - 异步HTTP网络访问
异步I/O（异步编程）- 只使用一个线程（单线程）来处理用户请求
用户请求一旦被接纳，剩下的都是I/O操作，通过多路I/O复用也可以达到并发的效果
这种做法与多线程相比可以让CPU利用率更高，因为没有线程切换的开销
Redis/Node.js - 单线程 + 异步I/O
Celery - 将要执行的耗时间的任务异步化处理
异步I/O事件循环 - uvloop
"""
import asyncio
import re
import aiohttp


async def fetch(session, url):
    async with session.get(url, ssl=False) as resp:
        return await resp.text()


async def main_task():
    pattern = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    async with aiohttp.ClientSession() as session:
        for url in urls:
            print('url xxxx ', url)
            html = await fetch(session, url)
            print('取得 :', pattern.search(html).group('title'))

print('異步訪問')
loop = asyncio.get_event_loop()
loop.run_until_complete(main_task())
loop.close()

print("------------------------------------------------------------")  # 60個


