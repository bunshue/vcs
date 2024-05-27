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
