# coding:utf-8
#
# file:traverse.py

import os,os.path

def traverse(pathname):	
	for item in os.listdir(pathname):
		fullitem = os.path.join(pathname,item)
		print(fullitem)
		if os.path.isdir(fullitem): #判斷是否為目錄
			traverse(fullitem)
	
traverse("c:/python32")
