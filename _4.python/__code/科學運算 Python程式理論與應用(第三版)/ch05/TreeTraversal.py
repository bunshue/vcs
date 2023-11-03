# -*- coding:utf-8 -*-
# file: TreeTraversal.py
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
def preorder(node):								# 先序檢查
	if node.data:
		node.show()
		if node.left:
			preorder(node.left)
		if node.right:
			preorder(node.right)
def inorder(node):								# 中序檢查
	if node.data:
		if node.left:
			inorder(node.left)
		node.show()
		if node.right:
			inorder(node.right)
def postorder(node):								# 後序檢查
	if node.data:
		if node.left:
			postorder(node.left)
		if node.right:
			postorder(node.right)
		node.show()
if __name__ == '__main__':
	Root = BTree('Root')							# 建構樹
	A = Root.insertLeft('A')
	C = A.insertLeft('C')
	D = A.insertRight('D')
	F = D.insertLeft('F')
	G = D.insertRight('G')
	B = Root.insertRight('B')
	E = B.insertRight('E')
	print('*************************')
	print('Binary Tree Pre-Traversal')
	print('*************************')
	preorder(Root)								# 對樹進行先序檢查
	print('*************************')
	print('Binary Tree In-Traversal')
	print('*************************')
	inorder(Root)								# 對樹進行中序檢查
	print('*************************')
	print('Binary Tree Post-Traversal')
	print('*************************')
	postorder(Root)								# 對樹進行後序檢查
