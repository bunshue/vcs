import os
filePath = input("請輸入檔案或路徑：")
show = "不存在，可能檔案或路徑有誤"
if os.path.exists(filePath):
    show = "存在"
    if os.path.isfile(filePath): 
        show += "，為檔案路徑"
    if os.path.isdir(filePath):
        show += "，為目錄路徑"     
print("%s %s" %(filePath, show))