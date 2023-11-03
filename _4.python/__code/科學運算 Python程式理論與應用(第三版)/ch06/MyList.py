# -*- coding:utf-8 -*-
# file: MyList.py
#
class MyList:									# 定義MyList類別
	#__mylist = []									# 定義__mylist屬性
	def __init__(self, *args):							# 多載__init__方法
		self.__mylist = []					# 此處相當於__mylist起始化，避免多個案例物件資料混合
		for arg in args:
			self.__mylist.append(arg)
	def __add__(self,n):								# 多載“+”運算符
		for i in range(0,len(self.__mylist)):
			self.__mylist[i] = self.__mylist[i] + n
	def __sub__(self,n):								# 多載“-”運算符
		for i in range(0,len(self.__mylist)):
			self.__mylist[i] = self.__mylist[i] - n
	def __mul__(self,n):								# 多載“*”運算符
		for i in range(0,len(self.__mylist)):
			self.__mylist[i] = self.__mylist[i] * n
	def __div__(self,n):								# 多載“/”運算符
		for i in range(0,len(self.__mylist)):
			self.__mylist[i] = self.__mylist[i] / n
	def __mod__(self,n):								# 多載“%”運算符
		for i in range(0,len(self.__mylist)):
			self.__mylist[i] = self.__mylist[i] % n
	def __pow__(self,n):								# 多載“**”運算符
		for i in range(0,len(self.__mylist)):
			self.__mylist[i] = self.__mylist[i] ** n
	def __len__(self):								# 多載len方法
		return len(self.__mylist)
	def show(self):									# 定義show方法
		print(self.__mylist)
		


