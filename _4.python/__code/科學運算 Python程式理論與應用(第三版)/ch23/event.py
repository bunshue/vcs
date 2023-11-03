# -*- coding:utf-8 -*-
# file: event.py
#
import threading			# 匯入threading模組
class mythread(threading.Thread):
	def __init__(self,threadname):
		threading.Thread.__init__(self,name = threadname)
	def run(self):
		global event		# 使用全局Event物件
		if event.isSet():	# 判斷Event物件內定訊號標志
			event.clear()	# 若已設定標志則清除
			event.wait()	# 呼叫wait方法
			print(self.getName())
		else:
			print(self.getName())
			event.set()	# 設定Event物件內定訊號標志
event = threading.Event()		# 產生Event物件
event.set()				# 設定Event物件內定訊號標志
tl = []
for i in range(10):
	t = mythread(str(i))
	tl.append(t)			# 產生執行緒清單
	
for i in tl:
	i.start()			# 執行執行緒
