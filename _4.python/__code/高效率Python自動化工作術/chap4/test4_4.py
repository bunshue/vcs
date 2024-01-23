from pathlib import Path

infolder = "testfolder"
ext = "*.txt"
filelist = []
for p in Path(infolder).rglob(ext): #將這個資料夾以及子資料夾的所有檔案
    filelist.append(str(p))         #新增至列表
for filename in sorted(filelist):   #再替每個檔案排序
    print(filename)