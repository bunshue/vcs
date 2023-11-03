# -*- coding:utf-8 -*-
# file: syn.py
#
import threading							# 匯入threading模組
import time								# 匯入time模組
class mythread(threading.Thread):					# 透過繼承建立類別
	def __init__(self,threadname):					# 起始化方法
		threading.Thread.__init__(self,name = threadname)	# 呼叫父類別的起始化方法
	def run(self):							# 多載run方法
		global x						# 使用global表明x為全局變數
		lock.acquire()						# 呼叫lock的acquire方法
		for i in range(3):
			x = x + 1
		time.sleep(2)						# 呼叫sleep函數，讓執行緒休眠5秒
		print(x)
		lock.release()						# 呼叫lock的release方法
lock = threading.RLock()						# 類別案例化	
tl = []									# 定義清單
for i in range(10):
	t = mythread(str(i))						# 類別案例化
	tl.append(t)							# 將類別物件新增到清單中
	
x=0									# 將x給予值為0
for i in tl:
	i.start()							# 依次執行執行緒


