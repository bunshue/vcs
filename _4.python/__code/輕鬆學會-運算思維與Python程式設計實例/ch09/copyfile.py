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
