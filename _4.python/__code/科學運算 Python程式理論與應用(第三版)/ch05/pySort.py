# -*- coding:utf-8 -*-
# file: pySort.py
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
def inorder(node):								# 中序檢查
	if node.data:
		if node.left:
			inorder(node.left)
		node.show()
		if node.right:
			inorder(node.right)
def rinorder(node):								# 中序檢查,先檢查右子樹
	if node.data:
		if node.right:
			rinorder(node.right)
		node.show()
		if node.left:
			rinorder(node.left)
def insert(node, value):
	if value > node.data:
		if node.right:
			insert(node.right, value)
		else:
			node.insertRight(value)
	else:
		if node.left:
			insert(node.left, value)
		else:
			node.insertLeft(value)
if __name__ == '__main__':
	l = [3, 5 , 7, 20, 43, 2, 15, 30]
	Root = BTree(l[0])							# 根節點
	node = Root
	for i in range(1, len(l)):
		insert(Root, l[i])
	print('*****************************')
	print('        從小到大')
	print('*****************************')
	inorder(Root)
	print('*****************************')
	print('        從大到小')
	print('*****************************')
	rinorder(Root)
