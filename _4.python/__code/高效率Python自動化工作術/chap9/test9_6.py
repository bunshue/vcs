from pathlib import Path

infolder = "testfolder"
extlist = ["*.jpg","*.png"]

msg = ""
for ext in extlist:                     #以多個副檔名調查
    filelist = []
    for p in Path(infolder).glob(ext):  #將這個資料夾的檔案
        filelist.append(str(p))         #新增至列表
    for filename in sorted(filelist):   #再替每個檔案排序
        msg += filename + "\n"
print(msg)
