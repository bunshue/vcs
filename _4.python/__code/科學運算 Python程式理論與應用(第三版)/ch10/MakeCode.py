# -*- coding:utf-8 -*-
# file: MakeCode.py
# 
import os
import sys
import datetime
# python指令稿範本
py = '''#-----------------------------------------------------
# TO:        
#-----------------------------------------------------
# BY: 
#-----------------------------------------------------
'''
# c範本
c = ''' *-----------------------------------------------------
 * TO:        
 *-----------------------------------------------------
 * BY: 
 *-----------------------------------------------------
'''
if os.path.isfile(sys.argv[1]):				# 判斷要建立的檔案是否存在，若果存在則離開指令稿
	print('%s already exist!' % sys.argv[1])
	sys.exit()
file = open(sys.argv[1], 'w')				# 建立檔案
today = datetime.date.today()				# 獲得目前日期，並格式化為xxxx-xx-xx的形式
date = today.strftime('%Y')+'-'+today.strftime('%m')+'-'+today.strftime('%d')
filetypes = str.split(sys.argv[1],'.')			# 判斷將建立的檔案是什麼型態以便對其分別處理
length = len(filetypes)
filetype = filetypes[length - 1]
if filetype == 'py':
	print('use python mode')
	file.writelines('# -*- coding:utf-8 -*-')
	file.write('\n')
	file.writelines('# File: ' + sys.argv[1])
	file.write('\n')
	file.write(py)
	file.write('# Date: ' + date)
	file.write('\n')
	file.write('#-----------------------------------------------------')
elif filetype == 'c' or filetype == 'cpp':
	print('use c mode')
	file.writelines('/*')
	file.write('\n')
	file.writelines(' *-----------------------------------------------------')
	file.write('\n')
	file.writelines(' * File: ' + sys.argv[1]) 
	file.write('\n')
	file.write(c)
	file.write(' * Date: ' + date)
	file.write('\n')
	file.write(' *-----------------------------------------------------')
	file.write('\n')
	file.write(' */ \n')
else:
	print('just create %s' % sys.argv[1])
file.close()								# 關閉檔案
