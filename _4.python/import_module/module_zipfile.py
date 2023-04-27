'''
解壓縮一個zip檔
'''

import zipfile

filename = 'C:/______test_files/_exe/ffmpeg.zip'
#filename = 'C:/______test_files/__pic/_ntuh.zip'
file_dir = './' #解壓縮目錄

f = zipfile.ZipFile(filename) #開啟壓縮檔

for fileName in f.namelist(): #壓縮檔案列表檔名
    f.extract(fileName, file_dir) #擷取壓縮檔案
    print('解壓縮檔案 : ', fileName) #印出解壓縮檔案名稱

f.close() #關檔
