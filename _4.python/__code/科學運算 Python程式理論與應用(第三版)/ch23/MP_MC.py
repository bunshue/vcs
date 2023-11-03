# -*- coding:utf-8 -*-
# file: MP_MC.py
#
import threading		# 匯入threading模組
import time			# 匯入time模組
import queue			# 匯入Queue模組
class Producer(threading.Thread):# 定義生產者類別
	def __init__(self,threadname):
		threading.Thread.__init__(self,name = threadname)
	def run(self):
		global queue	# 宣告queue為全局變數
		queue.put(self.getName())	# 呼叫put方法將執行緒名新增到佇列中
		print(self.getName(),'put ',self.getName(),' to queue')
class Consumer(threading.Thread):# 定義消費者類別
	def __init__(self,threadname):
		threading.Thread.__init__(self,name = threadname)
	def run(self):
		global queue
		print(self.getName(),'get ',queue.get(),'from queue')#呼叫get方法取得佇列中內容
queue = queue.Queue()	# 產生佇列物件
plist = []		# 產生者物件清單
clist = []		# 消費者物件清單
for i in range(10):
	p = Producer('Producer' + str(i))
	plist.append(p)		# 新增到生產者物件清單
for i in range(10):
	c = Consumer('Consumer' + str(i))
	clist.append(c)		# 新增到消費者物件清單
for i in plist:
	i.start()		# 執行生產者執行緒
	i.join()
for i in clist:
	i.start()		# 執行消費者執行緒
	i.join()

