# coding:utf-8
#
# file:trav_walk.py

import os,os.path

def trav_walk(pathname):
	for root,dirs,files in os.walk(pathname):
		for fil in files:
			fname=os.path.abspath(os.path.join(root,fil))
			print(fname)

trav_walk("c:/python32")