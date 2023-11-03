# -*- coding:utf-8 -*-
# file: pystack.py
#
class PyStack:									# 堆堆疊類別
	def __init__(self, size = 20):
		self.stack = []							# 堆堆疊清單
		self.size = size						# 堆堆疊大小
		self.top = -1							# 堆疊頂位置
	def setSize(self, size):						# 設定堆堆疊大小
		self.size = size
	def push(self, element):						# 元素進堆疊
		if self.isFull():
			raise StackException('PyStackOverflow')		# 若果堆疊滿則引發例外
		else:
			self.stack.append(element)
			self.top = self.top + 1
	def pop(self):								# 元素出堆疊
		if self.isEmpty():
			raise StackException('PyStackUnderflow')		# 若果堆疊為空則引發例外
		else:
			element = self.stack[-1]
			self.top = self.top - 1
			del self.stack[-1]
			return element
	def Top(self):								# 取得堆疊頂位置
		return self.top
	def empty(self):							# 清理堆疊
		self.stack = []
		self.top = -1
	def isEmpty(self):							# 是否為空堆疊
		if self.top == -1:
			return True
		else:
			return False
	def isFull(self):							# 是否為滿堆疊
		if self.top == self.size - 1:
			return True
		else:
			return False
		
class StackException(Exception):				#自訂例外類別
	def __init__(self,data):
		self.data=data
	def __str__(self):
		return self.data
	
if __name__ == '__main__':
	stack = PyStack()							# 建立堆疊
	for i in range(10):
		stack.push(i)							# 元素進堆疊
	print(stack.Top())							# 輸出堆疊頂位置
	for i in range(10):
		print(stack.pop())						# 元素出堆疊
	stack.empty()								# 清理堆疊
	for i in range(21):
		stack.push(i)							# 此處將引發例外
