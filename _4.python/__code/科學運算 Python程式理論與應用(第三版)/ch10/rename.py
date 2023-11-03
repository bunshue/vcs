# -*- coding:utf-8 -*-
# file: rename.py
#
import os
perfix = 'Python'						# perfix 為更名後的檔案起始字元
length = 2 							# length 為除去perfix後，檔名要達到的長度
base = 1								# 檔名的起始數
format = 'mdb'							# 檔案的副檔名
# 函數PadLeft將檔名補全到指定長度
# str 為要補全的字元
# num 為要達到的長度
# padstr 為達到長度所加入的字元
def PadLeft(str , num , padstr):
	stringlength = len (str)
	n = num - stringlength
	if n >=0 :
		str=padstr * n + str
	return str
# 為了避免誤動作，這裡先提示使用者
print('the files in %s will be renamed' % os.getcwd())
input = input('press y to continue\n')		# 取得使用者輸入
if input.lower() != 'y':							# 判斷使用者輸入，以決定是否執行更名動作
	exit()
filenames = os.listdir(os.curdir)				# 獲得目前目錄中的內容
# 從基數減1，為了是下邊 i = i + 1在第一次執行時等於基數
i = base - 1
for filename in filenames:					# 檢查目錄中內容，進行更名動作
	i = i+1
	# 判斷目前路徑是否為檔案，並且不是“rename.py”
	if filename != "rename.py" and os.path.isfile(filename):
		name = str(i)					# 將i轉換成字元
		name = PadLeft(name,length,'0')	# 將name補全到指定長度
		t = filename.split('.')				# 分割檔名，以檢查其是否是所要修改的型態
		m = len(t)
		if format == '':					# 若果未指定檔案型態，則變更目前目錄中所有檔案
			os.rename(filename,perfix+name+'.'+t[m-1])
		else:							# 否則只修改指定型態
			if t[m-1] == format:
				os.rename(filename,perfix+name+'.'+t[m-1])
			else:
				i = i - 1				# 確保i連續
	else:
		i = i - 1						# 確保i連續

