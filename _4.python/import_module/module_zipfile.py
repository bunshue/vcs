'''
解壓縮一個zip檔
'''

import zipfile

filename = 'C:/_git/vcs/_1.data/______test_files1/_exe/ffmpeg.zip'
#filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_ntuh.zip'
file_dir = './' #解壓縮目錄

f = zipfile.ZipFile(filename) #開啟壓縮檔

for fileName in f.namelist(): #壓縮檔案列表檔名
    f.extract(fileName, file_dir) #擷取壓縮檔案
    print('解壓縮檔案 : ', fileName) #印出解壓縮檔案名稱

f.close() #關檔


print('判斷是否為一個壓縮檔')
#filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

if zipfile.is_zipfile(filename):
    print('是壓縮檔')
else:
    print('不是壓縮檔')






import zipfile

filename1 = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/picture2.jpg'
filename3 = 'C:/_git/vcs/_1.data/______test_files1/bear.jpg'

filenames = [filename1, filename2, filename3]

zip_filename = 'zipfilename.zip'


zz = zipfile.ZipFile(zip_filename, 'w')
for filename in filenames:
    zz.write(filename)
    print(filename)

zz.close()



zz = zipfile.ZipFile(zip_filename, 'r')
print('Contents of %r:' % zip_filename)
zz.printdir()
zz.close()



