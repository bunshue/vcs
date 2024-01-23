from pathlib import Path

infolder = "testfolder"
value1 = "*.txt"

#【函數：建立檔案列表】
def listfiles(infolder, ext):
    msg = ""
    filelist = []
    for p in Path(infolder).rglob(ext): #將這個資料夾以及子資料夾的所有檔案
        filelist.append(str(p))         #新增至列表
    for filename in sorted(filelist):   #再替每個檔案排序
        msg += filename + "\n"
    msg = "檔案個數 = " + str(len(filelist)) + "\n" + msg
    return msg

#【執行函數】
msg = listfiles(infolder, value1)
print(msg)