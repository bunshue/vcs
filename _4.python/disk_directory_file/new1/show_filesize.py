import pathlib

foldername = 'C:/_git/vcs/_1.data/______test_files1'
file_type = "*.bmp"

#【函數：以最佳單位傳回檔案容量】
def format_bytes(size):
    units = ["位元組","KB","MB","GB","TB","PB","EB"]
    n = 0
    while size > 1024:
        size = size / 1024.0
        n += 1
    return str(int(size)) + " " + units[n]

#【函數：加總資料夾與子資料夾所有檔案的檔案容量】
def foldersize(foldername, file_type):
    msg = ""
    allsize = 0
    filelist = []
    for p in pathlib.Path(foldername).rglob(file_type):     #將這個資料夾以及子資料夾的所有檔案
        if p.name[0] != ".":                #沒有隱藏檔案的話
            filelist.append(str(p))         #新增至列表
    for filename in sorted(filelist):       #再替每個檔案排序
        size = pathlib.Path(filename).stat().st_size
        msg += filename + " : "+format_bytes(size)+"\n"
        allsize += size
    filesize = "檔案容量總和 = " + format_bytes(allsize) + "\n"
    filesize += "檔案個數 = " + str(len(filelist))+ "\n"
    msg = filesize + msg
    return msg

#【執行函數】
msg = foldersize(foldername, file_type)
print(msg)
