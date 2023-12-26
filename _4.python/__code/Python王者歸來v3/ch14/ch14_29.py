# ch14_29.py
import zipfile
import glob, os

fileZip = zipfile.ZipFile('out29.zip', 'w')
for name in glob.glob('zipdir29/*'):        # 遍歷zipdir29目錄
    fileZip.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)
    
fileZip.close()




