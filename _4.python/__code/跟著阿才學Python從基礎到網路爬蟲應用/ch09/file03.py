import os
dirPath = "D:\\PythonHw"
if os.path.exists(dirPath)  :
    print("目錄已存在或路徑有誤，無法建立")
else:
    os.mkdir(dirPath)
    pathname = os.path.split(dirPath)[0] # 取得路徑
    filename = os.path.split(dirPath)[1] # 取得目錄名稱
    print("於 %s 建立 %s 目錄" %(pathname, filename))