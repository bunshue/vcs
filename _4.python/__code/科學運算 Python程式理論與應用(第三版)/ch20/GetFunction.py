# -*- coding:utf-8 -*-
# file : GetFunction.py
# 
import re
import sys
def DealWithFunc(s):
	r = re.compile(r'''
		(?<=def\s)	# 前邊必須含有def且def後跟一個空格
		\w+		# 比對函數明
		\(.*?\)		# 比對參數
		(?=:)		# 後邊必須跟一個“:”
		''',re.X | re.U)	# 設定編譯選項，忽略模式中的注解
	return r.findall(s)
def DealWithVar(s):
	vars = []		# 定義一個清單，因為這裡分兩種情況處理
	r = re.compile(r'''
		\b		# 比對單字開始
		\w+		# 比對變數名
		(?=\s=)		# 處理為為變數給予值的情況
		''',re.X | re.U)
	vars.extend(r.findall(s))
	r = re.compile(r'''
		(?<=for\s)	# 處理變數位於for敘述中的情況
		\w+		# 比對變數名
		\s		# 比對空格
		(?=in)		# 比對in
		''',re.X | re.U)	# 設定編譯選項，忽略模式中的注解
	vars.extend(r.findall(s))
	return vars
# 判斷指令行是否有輸入，沒有則要求輸入要處理的檔案
if len(sys.argv) == 1:
	sour = input('請輸入要處理的檔案路徑')
else:
	sour = sys.argv[1]
file = open(sour,encoding="utf-8")		# 開啟檔案
s = file.readlines()		# 將檔案內容以行讀入的s中
file.close()			# 關閉檔案
print('********************************')
print(sour,'中的函數有：')
print('********************************')
i = 0				# i為函數所在的行號
# 循環處理每一行，比對其中的函數並輸出函數所在的行號，以及函數的原型
for line in s:
	i = i + 1
	function = DealWithFunc(line)
	if len(function) == 1:
		print('Line: ',i,'\t',function[0])
print('********************************')
print(sour,'中的變數有：')
print('********************************')
i = 0				# 此處i為變數所在的行號
# 循環處理每一行，比對其中的變數，輸出變數所在的行號，以及變數名
for line in s:
	i = i + 1
	var = DealWithVar(line)
	if len(var) == 1:
		print('Line: ',i,'\t',var[0])
