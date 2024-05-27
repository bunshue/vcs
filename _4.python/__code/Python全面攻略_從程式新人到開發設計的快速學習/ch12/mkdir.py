import os
pName = 'C:/pcYah'
if os.path.exists(pName):
    print('%s 資料夾已存在,不必再建立' %pName)
else:
    print('%s 路徑不存在' %pName)
    os.mkdir(pName)
    print('%s 資料夾建立成功' %pName)
