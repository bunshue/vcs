# -*- coding:utf-8 -*-
# file: pyqueue.py
#
class PyQueue:									# 建立隊
	def __init__(self, size = 20):
		self.queue = []							# 隊
		self.size = size						# 隊大小
		self.end = -1							# 佇列尾
	def setSize(self, size):						# 設定隊大小
		self.size = size
	def In(self, element):							# 加入佇列
		if self.end < self.size - 1:
			self.queue.append(element)
			self.end = self.end + 1
		else:
			raise QueueException('PyQueueFull')	# 若果隊滿則引發例外
	def Out(self):								# 出隊
		if self.end != -1:
			element = self.queue[0]
			self.queue = self.queue[1:]
			self.end = self.end - 1
			return element
		else:
			raise QueueException('PyQueueEmpty')	# 若果對為空則引發例外
	def End(self):								# 輸出佇列尾
		return self.end
	def empty(self):							# 清楚隊
		self.queue = []
		self.end = -1

class QueueException(Exception):				#自訂例外類別
	def __init__(self,data):
		self.data=data
	def __str__(self):
		return self.data
	
if __name__ == '__main__':
	queue = PyQueue()
	for i in range(10):
		queue.In(i)							# 元素加入佇列
	print(queue.End())
	for i in range(10):
		print(queue.Out())						# 元素出隊
	for i in range(20):
		queue.In(i)							# 元素加入佇列
	queue.empty()								# 清理隊
	for i in range(20):
		print(queue.Out())						# 此處將引發例外
