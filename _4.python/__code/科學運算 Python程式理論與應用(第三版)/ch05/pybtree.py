# -*- coding:utf-8 -*-
# file: pybtree.py
#
class BTree:									# 二元樹節點
	def __init__(self, value):						# 起始化函數
		self.left = None						# 左兒子
		self.data = value						# 節點值
		self.right = None						# 右兒子
	def insertLeft(self, value):						# 向左子樹插入節點
		self.left = BTree(value)
		return self.left
	def insertRight(self, value):						# 向右子樹插入節點
		self.right = BTree(value)
		return self.right
	def show(self):								# 輸出節點資料
		print(self.data)
if __name__ == '__main__':
	Root = BTree('Root')							# 根節點
	A = Root.insertLeft('A')						# 向根節點中插入A節點
	C = A.insertLeft('C')							# 向A節點中插入C節點
	D = A.insertRight('D')							# 向A節點中插入D節點
	F = D.insertLeft('F')							# 向D節點中插入F節點
	G = D.insertRight('G')							# 向D節點中插入G節點
	B = Root.insertRight('B')						# 向根節點中插入B節點
	E = B.insertRight('E')							# 向B節點中插入E節點
	Root.show()								# 輸出節點資料
	Root.left.show()
	Root.right.show()
	A = Root.left
	A.left.show()
	Root.left.right.show()

