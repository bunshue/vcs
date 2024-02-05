import pathlib

foldername = 'C:/_git/vcs/_1.data/______test_files1'
file_type = "*.bmp"

#【函數：建立檔案列表】
def listfiles(foldername, file_type):
    msg = ""
    filelist = []
    for p in pathlib.Path(foldername).rglob(file_type): #將這個資料夾以及子資料夾的所有檔案
        filelist.append(str(p))         #新增至列表
    for filename in sorted(filelist):   #再替每個檔案排序
        msg += filename + "\n"
    msg = "檔案個數 = " + str(len(filelist)) + "\n" + msg
    return msg

#【執行函數】
msg = listfiles(foldername, file_type)
print(msg)
