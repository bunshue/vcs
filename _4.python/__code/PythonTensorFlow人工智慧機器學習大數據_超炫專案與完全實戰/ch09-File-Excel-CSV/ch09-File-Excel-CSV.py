import sys

fr = open('workfile.txt', 'w')
fr.write('This is a test\n')
fr.close()

fw = open('workfile.txt', 'r')
for line in fw:
    print(line)
fw.close()

print('------------------------------------------------------------')	#60個

import os
import os.path
import shutil

FileName1='workfile.txt'
FileName2='workfileCopy.txt'
FileName3='workfileRename.txt'

def FunListAllFiles(iMeg):
	allFiles = os.listdir('.')
	print(iMeg)
	print(allFiles)

FunListAllFiles("1.")
if os.path.isfile(FileName1) and os.access(FileName1, os.R_OK):
    shutil.copy(FileName1, FileName2)   


FunListAllFiles("2.")
if os.path.isfile(FileName2) and os.access(FileName2, os.R_OK):
    os.rename(FileName2, FileName3)   


FunListAllFiles("3.")
if os.path.isfile(FileName3) and os.access(FileName3, os.R_OK): 
    os.remove(FileName3)
    print('%s deleted' %(FileName3))   


FunListAllFiles("4.")

print('------------------------------------------------------------')	#60個

import os
import os.path

if os.path.exists('./folder'):
    os.rmdir('./folder')
    print(os.getcwd())    
else: 
    os.mkdir('./folder')  
    os.chdir('./folder')
    print(os.getcwd())    

print('------------------------------------------------------------')	#60個

import xlrd
import xlwt

read=xlrd.open_workbook('water10705.xls')
sheet=read.sheets()[0]
#sheet=read.sheets("Sheet5")
print(sheet.nrows)
print(sheet.ncols)

write = xlwt.Workbook()
x1=0
write2 = write.add_sheet('MySheet')
for i in range(10,36):
    print(sheet.cell(i,12).value)
    value=sheet.cell(i,12).value
    try:
      x1=x1+float(value)
    except:
      print("")
    write2.write(i, 0, value)

print("total:",x1)
write.save('write.xls')

print('------------------------------------------------------------')	#60個

import xlrd
import xlwt

read=xlrd.open_workbook('workfile.xls')
sheet=read.sheets()[0]
#sheet=read.sheets("Sheet5")
print(sheet.nrows)
print(sheet.ncols)

print(sheet.cell(5,1).value)

write = xlwt.Workbook()
write2 = write.add_sheet('MySheet')
for i in range(0,sheet.nrows):
    print(sheet.cell(i,1).value)
    value=sheet.cell(i,1).value
    write2.write(i, 0, value)

write.save('write.xls')

print('------------------------------------------------------------')	#60個

import csv

with open('workfile.csv', 'r') as fin:
    with open('write.csv', 'w') as fout:
        read = csv.reader(fin, delimiter=',')
        write = csv.writer(fout, delimiter=',')
        header = next(read)
        print(header)
        # get number of columns
        #array = header.split(',')
        first_item = header[0]
        write.writerow(header)
        for row in read:
            print(','.join(row))
            write.writerow(row)
            print(row[2])

print('------------------------------------------------------------')	#60個
