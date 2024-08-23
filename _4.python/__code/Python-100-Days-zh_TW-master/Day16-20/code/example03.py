import sys

print("------------------------------------------------------------")  # 60個

from functools import wraps
from random import randint
from time import time, sleep

import pymysql

def record(output):

    def decorate(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            ret_value = func(*args, **kwargs)
            output(func.__name__, time() - start)
            return ret_value

        return wrapper

    return decorate


def output_to_console(fname, duration):
    print('%s: %.3f秒' % (fname, duration))


def output_to_file(fname, duration):
    with open('log.txt', 'a') as file_stream:
        file_stream.write('%s: %.3f秒\n' % (fname, duration))


def output_to_db(fname, duration):
    con = pymysql.connect(host='localhost', port=3306,
                          database='test', charset='utf8',
                          user='root', password='123456',
                          autocommit=True)
    try:
        with con.cursor() as cursor:
            cursor.execute('insert into tb_record values (default, %s, %s)',
                           (fname, '%.3f' % duration))
    finally:
        con.close()


@record(output_to_console)
def random_delay(min, max):
    sleep(randint(min, max))


for _ in range(3):
    # print(random_delay.__name__)
    random_delay(3, 5)
# for _ in range(3):
#     # 取消掉装饰器
#     random_delay.__wrapped__(3, 5)

print("------------------------------------------------------------")  # 60個

"""
面向对象的三大支柱：封装、继承、多态
面向对象的设计原则：SOLID原则
面向对象的设计模式：GoF设计模式（单例、工厂、代理、策略、迭代器）
月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成
"""
from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """员工(抽象类)"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """结算月薪(抽象方法)"""
        pass


class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """程序员"""

    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)

    def get_salary(self):
        return 200.0 * self.working_hour


class Salesman(Employee):
    """销售员"""

    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return 1800.0 + self.sales * 0.05


class EmployeeFactory():
    """创建员工的工厂（工厂模式 - 通过工厂实现对象使用者和对象之间的解耦合）"""

    @staticmethod
    def create(emp_type, *args, **kwargs):
        """创建员工"""
        emp_type = emp_type.upper()
        emp = None
        if emp_type == 'M':
            emp = Manager(*args, **kwargs)
        elif emp_type == 'P':
            emp = Programmer(*args, **kwargs)
        elif emp_type == 'S':
            emp = Salesman(*args, **kwargs)
        return emp

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


