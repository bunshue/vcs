# ch14_41.py
import zipfile
import glob, os

fileZip = zipfile.ZipFile('out41.zip', 'w')
for name in glob.glob('zipdir41/*'):        # 遍歷zipdir41目錄
    fileZip.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)
    
fileZip.close()




