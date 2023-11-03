# -*- coding:utf-8 -*-
# file: threaddaemon.py
# 
import threading							# 匯入threading模組
import time								# 匯入time模組
class mythread(threading.Thread):					# 透過繼承建立類別
	def __init__(self,threadname):					# 起始化方法
		threading.Thread.__init__(self,name = threadname)	# 呼叫父類別的起始化方法
	def run(self):							# 多載run方法
		time.sleep(5)						# 呼叫time模組中的sleep函數，讓執行緒休眠5秒	
		print(self.getName())
def func1():								# 定義函數func1
	t1.start()						
	print('func1 done')
def func2():								# 定義函數func2
	t2.start()
	print('func2 done')
t1 = mythread('t1')							# 類別案例化
t2 = mythread('t2')							# 類別案例化
#t2.setDaemon(True)							# 設定t2的Daemon標志
t2.daemon=True



func1()									# 呼叫函數func1
func2()									# 呼叫函數func2

