# -*- coding:utf-8 -*-
# file: S_P_C.py
#
import stackless							# 匯入stackless模組
import queue								# 匯入Queue模組
def Producer(i):							# 定義生產者
	global queue							# 宣告為全局Queue物件
	queue.put(i)							# 向佇列中加入資料
	print('Producer',i, 'add',i)
def Consumer():								# 定義消費者
	global queue
	i = queue.get()							# 從佇列中取出資料
	print('Consumer',i, 'get',i)
queue = Queue.Queue()							# 產生佇列物件
for i in range(10):
	stackless.tasklet(Producer)(i)					# 加入生產者工作
for i in range(10):
	stackless.tasklet(Consumer)()					# 加入消費者工作
stackless.run()								# 執行工作

