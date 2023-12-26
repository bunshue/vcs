# ch14_31.py
import zipfile

fileUnZip = zipfile.ZipFile('out29.zip')
fileUnZip.extractall('out31')
fileUnZip.close()



