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
