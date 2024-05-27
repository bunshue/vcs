import os
pName = 'c:/pcYah'
if os.path.exists(pName):
    print('%s 資料夾目前存在' %pName)
    os.rmdir(pName)
    print('%s 資料夾路徑已刪除' %pName)
else:
    print('%s 資料夾路徑不存在' %pName)
