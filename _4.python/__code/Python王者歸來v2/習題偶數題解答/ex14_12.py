# ex14_12.py
import zipfile
import glob, os
zipdir = input("請輸入欲壓縮的目錄 : ")
zipdir = zipdir + '/*'
zipfn = input("請輸入保存壓縮檔案的名稱 : ")

fileZip = zipfile.ZipFile(zipfn, 'w')
for name in glob.glob(zipdir):        # 遍歷zipdir41目錄
    fileZip.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)
    
fileZip.close()




