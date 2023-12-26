# ch14_43.py
import zipfile

fileUnZip = zipfile.ZipFile('out41.zip')
fileUnZip.extractall('out43')
fileUnZip.close()



