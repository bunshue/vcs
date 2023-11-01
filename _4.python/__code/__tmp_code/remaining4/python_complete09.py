import os
import sys
import time
import random


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('編碼錯誤')
obj=open('test_encode.txt','r', encoding='cp950')  #開啟檔案
for line in obj:
	print(line)
obj.close()

print('編碼正確')

obj=open('test_encode.txt','r', encoding='UTF-8')  #開啟檔案
for line in obj:
	print(line)
obj.close()


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個




obj='''五福臨門
十全十美
'''
#建立新檔
fn = open('phrase.txt', 'w')   
fn.write(obj)#將字串寫入檔案   
fn.close()#關閉檔案



file1=open("phrase.txt",'r')
for line in file1:
    print(line,end='')
file1.close()


import os.path #匯入os.path
import sys #匯入sys

if os.path.isfile('phrase_new.txt'): #如果檔案存在則取消複製
    print('此檔案已存在,不要複製')
    sys.exit()
else:
    file1=open('phrase.txt','r')#讀取模式
    file2=open('phrase_new.txt','w')#寫入模式
    text=file1.read() #以逐字元的方式讀取檔案
    text=file2.write(text) #寫入檔案
    print('檔案複製成功')
    file1.close() 
    file2.close() 




print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個

