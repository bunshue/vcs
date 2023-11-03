# -*- coding:utf-8 -*-
# file: P_C.py
#
import threading							# 匯入threading模組
class Producer(threading.Thread):					# 定義生產者類別
	def __init__(self,threadname):
		threading.Thread.__init__(self,name = threadname)
	def run(self):
		global x
		con.acquire()						# 呼叫con的acquire方法				
		if x == 1000000:
			con.wait()					# 呼叫con的wait方法
			pass
		else:
			for i in range(1000000):
				x = x + 1
			con.notify()					# 呼叫con的notify方法
		print(x)
		con.release()						# 呼叫con的release方法
class Consumer(threading.Thread):					# 定義生產者類別
	def __init__(self,threadname):
		threading.Thread.__init__(self,name = threadname)
	def run(self):
		global x
		con.acquire()
		if x == 0:
			con.wait()	
			pass
		else:
			for i in range(1000000):
				x = x - 1
			con.notify()
		print(x)
		con.release()
con = threading.Condition()						# 類別案例化
x=0
p = Producer('Producer')						# 產生生產者物件
c = Consumer('Consumer')						# 產生消費者物件
p.start()								# 執行執行緒
c.start()
p.join()								# 等待執行緒結束
c.join()
print(x)
