import os
dirPath = "D:\\PythonHw"
if os.path.exists(dirPath)  :
    os.rmdir(dirPath)
    pathname = os.path.split(dirPath)[0] # 取得路徑
    filename = os.path.split(dirPath)[1] # 取得目錄名稱
    print("刪除 %s 下的 %s 目錄" %(pathname, filename))
else:
    print("目錄不存在或路徑有誤，無法刪除")
