#append

import os
pName = 'C:/pcYah'
if not os.path.exists(pName):
    os.mkdir(pName)
f = open('C:/pcYah/philo.txt', 'a')
f.write('珍惜每一天\n')
f.flush()
f.close()





#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch12\create.py

import os
pName = 'C:/pcYah'
fName1 = 'C:/pcYah/score.txt'
fName2 = 'C:/pcYah/stu.txt'
if not os.path.exists(pName):
    os.mkdir(pName)
f1 = open(fName1, 'r')
f2 = open(fName2, 'w')
st = '姓名\t國文\t數學\t平均'
print(st)                          # 輸出到螢幕
f2.write(st+'\n')                  # 輸出到檔案
lst = f1.readlines()
for i in range(3):
    st = lst[i].strip().split(',')
    avg = (float(st[1])+float(st[2]))/2
    wr = '{0}\t{1}\t{2}\t{3}'.format(st[0],st[1],st[2],avg)
    print(wr)                     # 輸出到螢幕
    f2.write(wr+ '\n')            # 輸出到檔案
f1.close()
f2.flush()
f2.close

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch12\cwd.py

import os
print(os.getcwd())    # 顯示目前的工作目錄

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch12\file.py

import os
pName = 'c:/pcYah'
if not os.path.exists(pName):
    os.mkdir(pName)
f = open('c:/pcYah/data1.txt', 'w')
f.close()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch12\mkdir.py

import os
pName = 'C:/pcYah'
if os.path.exists(pName):
    print('%s 資料夾已存在,不必再建立' %pName)
else:
    print('%s 路徑不存在' %pName)
    os.mkdir(pName)
    print('%s 資料夾建立成功' %pName)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch12\open1.py

import os
fPath = 'c:\\data\\'
if not os.path.exists(fPath):
    os.mkdir(fPath)
f = open('c:/data/file01.txt', 'w')
#f = open('c:\\data\\file01.txt', 'w')
f.close()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch12\path1.py

import os
pName = 'C:/pcYah'
if os.path.isdir(pName):           # 檢查資料夾路徑是否存在
    print('%s 資料夾路徑存在' %pName)
else:
    print('%s 資料夾路徑不存在' %pName)
     
fName = 'C:/Windows/win.ini'
if os.path.isfile(fName):         # 檢查檔案路徑是否存在
    print('%s 檔案路徑存在' %fName)
else:
    print('%s 檔案路徑不存在' %fName)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch12\path2.py

import os
pName = 'C:/pcYah'
if os.path.exists(pName):        # 檢查資料夾路徑是否存在
    print('%s 資料夾路徑存在' %pName)
else:
    print('%s 資料夾路徑不存在' %pName)
     
fName = 'C:/Windows/win.ini'
if os.path.exists(fName):        # 檢查檔案路徑是否存在
    print('%s 檔案路徑存在' %fName)
else:
    print('%s 檔案路徑不存在' %fName)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch12\read1.py

import os
fName = 'C:/pcYah/score.txt'
if os.path.isfile(fName):
    f = open(fName, 'r')
    str1 = f.read(4)
    print(str1)
    print(f.read())
    f.close()
else:
    print('%s 檔案路徑不存在' %fName)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch12\read2.py

import os
fName = 'C:/pcYah/score.txt'
if os.path.isfile(fName):
    f = open(fName, 'r')
    str1 = f.readline()
    print(str1)
    str2 = f.readline(4)
    print(str2)
    print(f.read())
    f.close()
else:
    print(None)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch12\read3.py

import os
fName = 'C:/pcYah/score.txt'
if os.path.isfile(fName):
    with open(fName, 'r') as f:
       lst = f.readlines()
       print(lst[0], end='')
       print(lst[1], end='')
       print(lst[2], end='')
else:
    print('%s 檔案路徑不存在' %fName)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch12\rmdir.py

import os
pName = 'c:/pcYah'
if os.path.exists(pName):
    print('%s 資料夾目前存在' %pName)
    os.rmdir(pName)
    print('%s 資料夾路徑已刪除' %pName)
else:
    print('%s 資料夾路徑不存在' %pName)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch12\split.py

import os
fName = 'C:/pcYah/score.txt'
if os.path.isfile(fName):
    print ('姓名','國文','數學','平均',sep='\t')
    with open(fName, 'r') as f:
       lst = f.readlines()
       for i in range(3):
           st = lst[i].strip()
           stA = st.split(',')
           print(stA[0], end='\t')
           print(stA[1], end='\t')
           print(stA[2], end='\t')
           avg = (float(stA[1])+float(stA[2]))/2
           print(avg)
else:
    print('%s 檔案路徑不存在' %fName)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch12\strip.py

import os
fName = 'C:/pcYah/score.txt'
if os.path.isfile(fName):
    with open(fName, 'r') as f:
        lst = f.readlines()
        for i in range(3):
            st = lst[i].strip()
            print(st)
else:
    print('%s 檔案路徑不存在' %fName)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch12\try1.py

n1 = 8
n2 = 0
d = n1/n2
print('%d / %d = %d' %(n1, n2, d))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch12\try2.py

n1 = 8
n2 = 0
try:
    d = n1/n2
    print('%d / %d = %d' %(n1, n2, d))
except Exception as e:
    print('錯誤類型 :', end =' ')
    print(e)
finally:
    print('執行 finally: 敘述\n')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch12\try3.py

lst = [0 for x in range(4)]
try:
    lst[3] = 33
    print('lst[3] =', lst[3])
    lst[8] = 88
    print('lst[8] =', lst[8])
except ZeroDivisionError: 
    print('錯誤類型 : 除數為零')
except IndexError: 
    print('錯誤類型 : 串列註標超出範圍')
except MemoryErroe: 
    print('錯誤類型 : 超出記憶體空間')  
except Exception as e:
    print('錯誤類型 :', e) 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch12\write.py

import os
pName = 'C:/pcYah'
if not os.path.exists(pName):
    os.mkdir(pName)
f = open('C:/pcYah/philo.txt', 'w')
f.write('時光不倒帶\n')
f.write('歲月不重來\n')
f.flush()
f.close()

print("------------------------------------------------------------")  # 60個

