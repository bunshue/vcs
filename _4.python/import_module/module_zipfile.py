"""
壓縮 / 解壓縮 一個zip檔
"""

import zipfile

print('------------------------------------------------------------')	#60個

print('解壓縮一個zip檔')

zip_filename = 'C:/_git/vcs/_1.data/______test_files1/_exe/ffmpeg.zip'
#zip_filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_ntuh.zip'
file_dir = './' #解壓縮目錄

#with zipfile.ZipFile(zip_filename) as zipfp:   #開啟壓縮檔
with zipfile.ZipFile(zip_filename, 'r') as zipfp:   #開啟壓縮檔
    for filename in zipfp.namelist(): #壓縮檔案列表檔名
        zipfp.extract(filename, file_dir) #擷取壓縮檔案
        print('解壓縮檔案 : ', filename) #印出解壓縮檔案名稱

print('------------------------------------------------------------')	#60個

print('判斷是否為一個壓縮檔')
#zip_filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

if zipfile.is_zipfile(zip_filename):
    print('是壓縮檔')
else:
    print('不是壓縮檔')

print('------------------------------------------------------------')	#60個

filename1 = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/picture2.jpg'
filename3 = 'C:/_git/vcs/_1.data/______test_files1/bear.jpg'

filenames = [filename1, filename2, filename3]

zip_filename = 'zipfilename.zip'


with zipfile.ZipFile(zip_filename, 'w') as zipfp:   #開啟壓縮檔
    for filename in filenames:
        zipfp.write(filename)
        print(filename)

with zipfile.ZipFile(zip_filename, 'r') as zipfp:   #開啟壓縮檔
    zipfp = zipfile.ZipFile(zip_filename, 'r')
    print('Contents of %r:' % zip_filename)
    zipfp.printdir()

print('------------------------------------------------------------')	#60個

zip_filename = 'C:/_git/vcs/_1.data/______test_files1/_exe/ffmpeg.zip'
zip_filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_zip/PIL.zip'

with zipfile.ZipFile(zip_filename, 'r') as zipfp:   #開啟壓縮檔
    print('顯示壓縮檔內的檔案')
    names = zipfp.namelist()    #壓縮檔案列表檔名
    for name in names:
        print(name)

    # Check infolist
    infos = zipfp.infolist()
    names = [i.filename for i in infos]
    print('len = ', len(names))
    for nm in names:
        info = zipfp.getinfo(nm)
        print(info.filename, nm, end = '\t')
        print(info.file_size)

    print()
    for i in infos:
        print(i.filename, end = '\t')
        print(i.file_size)

    #info2 = zipfp.getinfo('PIL/PIL00.py')
    #print(info2)

print('------------------------------------------------------------')	#60個

with zipfile.ZipFile(zip_filename, 'r') as zipfp:   #開啟壓縮檔
    zinfo = zipfp.getinfo('PIL/PIL02.py')
    print('--------------')
    print(zinfo)

print('------------------------------------------------------------')	#60個

zip_filename = 'PIL2222.zip'
#with zipfile.ZipFile(zip_filename, "w") as zipfp:
    #zipfp.write('test10_new06.py')#預設為 zipfile.ZIP_STORED 模式
    #zipfp.write('test10_new07.py', 'test10_new07.py')
    #zipfp.write('test10_new08.py', 'test10_new08.py', zipfile.ZIP_STORED)
    #zipfp.write('test10_new09.py', 'test10_new09.py', zipfile.ZIP_DEFLATED)
    #sinfo = zipfp.getinfo('test10_new08.py')
    #print(sinfo)
    #dinfo = zipfp.getinfo('test10_new09.py')
    #print(dinfo)

    # check getinfo
    #for nm in ('test10_new09.py', "another.name", "strfile"):
    #    info = zipfp.getinfo(nm)
    #    print(info.filename, nm)
    #    print(info.file_size)

zip_filename = 'PIL3333.zip'
with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_STORED) as zipfp:
    zipfp.comment = b"this is a comment"
    #zipfp.write('test10_new09.py', 'test10_new09.py')
    with open(zip_filename, 'a') as f:
        f.write("abcdef\r\n")

with zipfile.ZipFile(zip_filename, "r") as zipfp:
    print(zipfp, zipfile.ZipFile)
    print(zipfp.comment, b"this is a comment")

print('------------------------------------------------------------')	#60個

zip_filename = 'PIL4444.zip'
compression = zipfile.ZIP_LZMA

zipfp = zipfile.ZipFile(zip_filename, "w")
zipfp.writestr("b.txt", "hello world", compress_type = compression)
info = zipfp.getinfo('b.txt')
print(info)

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('各種壓縮方法 壓縮同樣的檔案 比較壓縮率')

big_filename = 'C:/_git/vcs/_1.data/______test_files1/_json/ChinaBoundary'

def make_test_archive(zip_filename, compression):
    with zipfile.ZipFile(zip_filename, "w", compression) as zipfp:  #開啟壓縮檔
        #壓縮一檔
        short_filename = 'ChinaBoundary'
        zipfp.write(big_filename, short_filename, compress_type = compression)

zip_filename = 'zip111.zip'
compression = zipfile.ZIP_STORED
make_test_archive(zip_filename, compression)


"""
#zipfile.ZIP_STORED	未被壓縮的歸檔成員的數字常數, 僅拷貝, 無壓縮
#zipfile.ZIP_DEFLATED	常用的 ZIP 壓縮方法的數字常數
#zipfile.ZIP_BZIP2	BZIP2 壓縮方法的數字常數
#zipfile.ZIP_LZMA	LZMA 壓縮方法的數字常數, 強力壓縮

zip_filename = 'zip111.zip'
compression = zipfile.ZIP_STORED
make_test_archive(zip_filename, compression)

zip_filename = 'zip222.zip'
compression = zipfile.ZIP_DEFLATED
make_test_archive(zip_filename, compression)

zip_filename = 'zip333.zip'
compression = zipfile.ZIP_BZIP2
make_test_archive(zip_filename, compression)

zip_filename = 'zip444.zip'
compression = zipfile.ZIP_LZMA
make_test_archive(zip_filename, compression)
"""

print('------------------------------------------------------------')	#60個



import os

print('------------------------------------------------------------')	#60個

print('製作一個zip檔')

filename1 = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/poetry2.txt'
filename3 = 'C:/_git/vcs/_1.data/______test_files1/picture2.jpg'

filenames = [filename1, filename2, filename3]

#zip_filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_zip/PIL.zip'
zip_filename = 'ttttt.zip'

with zipfile.ZipFile(zip_filename, "w",
                     compression=zipfile.ZIP_DEFLATED) as zf:
    for filename in filenames:
        if os.path.isfile(filename):
            zf.write(filename, filename)


status = zipfile.is_zipfile(zip_filename)
print(status)

print('------------------------------------------------------------')	#60個

print('解壓縮一個zip檔')

def _ensure_directory(path):
    """Ensure that the parent directory of `path` exists"""
    dirname = os.path.dirname(path)
    if not os.path.isdir(dirname):
        os.makedirs(dirname)

extract_dir = './'

zip = zipfile.ZipFile(zip_filename)
try:
    for info in zip.infolist():
        name = info.filename

        # don't extract absolute paths or ones with .. in them
        if name.startswith('/') or '..' in name:
            continue

        target = os.path.join(extract_dir, *name.split('/'))
        if not target:
            continue

        _ensure_directory(target)
        if not name.endswith('/'):
            # file
            data = zip.read(info.filename)
            f = open(target, 'wb')
            try:
                f.write(data)
            finally:
                f.close()
                del data
finally:
    zip.close()

print('------------------------------------------------------------')	#60個




print("------------------------------------------------------------")  # 60個

import zipfile
import glob, os

print("將一個資料夾下檔檔案壓縮起來")

zip_filename = "tmp_zipfile1.zip"

fileZip = zipfile.ZipFile(zip_filename, 'w')
for name in glob.glob('C:/_git/vcs/_1.data/______test_files1/__pic/_animals/*'):        # 遍歷目錄
    fileZip.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)
    
fileZip.close()


print("將幾個檔案壓縮起來")

zip_filename = "tmp_zipfile2.zip"

filename1 = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/picture2.jpg'
filename3 = 'C:/_git/vcs/_1.data/______test_files1/poetry2.txt'

fileZip = zipfile.ZipFile(zip_filename, 'w')

fileZip.write(filename1, os.path.basename(filename1), zipfile.ZIP_DEFLATED)
fileZip.write(filename2, os.path.basename(filename2), zipfile.ZIP_DEFLATED)
fileZip.write(filename3, os.path.basename(filename3), zipfile.ZIP_DEFLATED)
    
fileZip.close()

print("------------------------------------------------------------")  # 60個

print('列出壓縮檔內的檔案資料')

import zipfile

zip_filename = "tmp_zipfile2.zip"

listZipInfo = zipfile.ZipFile(zip_filename, 'r')
print(listZipInfo.namelist())       # 以列表列出所有壓縮檔案
print("詳細內容 檔名 檔案大小 壓縮後的檔案大小 壓縮比例")
for info in listZipInfo.infolist():
    print(info.filename, info.file_size, info.compress_size)

print("------------------------------------------------------------")  # 60個

print('解壓縮檔案')

import zipfile

zip_filename = "tmp_zipfile1.zip"
extract_folder = "tmp_folder"

fileUnZip = zipfile.ZipFile(zip_filename)
fileUnZip.extractall(extract_folder)
fileUnZip.close()

print("------------------------------------------------------------")  # 60個


print('------------------------------------------------------------')	#60個


'''

tmptmp

    def test_write_default_name():
        """Check that calling ZipFile.write without arcname specified
        produces the expected result."""
        with zipfile.ZipFile(zip_filename, 'w') as zipfp:   #開啟壓縮檔
            zipfp.write('test10_new09.py')
            with open('test10_new09.py', "rb") as f:
                print(zipfp.read('test10_new09.py'), f.read())

'''








