import os

filename = __file__
print(filename)

path_split = filename.split(os.sep)
print(path_split)

print(os.sep)
print(os.altsep)

bn = os.path.basename(filename)
print(bn)

import test
packagedir = os.path.dirname(test.__file__)


import email
packagedir = os.path.dirname(email.__file__)
print(packagedir)

fpath = 'aaaaaaaaaaa'
correctfile = os.path.join(os.getcwd(), fpath)
correctfile = os.path.normpath(correctfile)

ccc = os.path.join(os.getcwd(), 'ziptest2dir')
print(ccc)

'''
import time
print(time.strptime(date, '%Y-%m-%d'))
print(time.strptime(time_, '%H:%M:%S'))
'''


print('------------------------------')  #30個

import zipfile

zip_filename = 'C:/_git/vcs/_1.data/______test_files1/_exe/ffmpeg.zip'
zip_filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_zip/PIL.zip'

with zipfile.ZipFile(zip_filename, 'r') as zipfp:
    names = zipfp.namelist()
    print(names)
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
    '''
    info2 = zipfp.getinfo('PIL/PIL00.py')
    print(info2)
    '''


print('------------------------------')  #30個


with zipfile.ZipFile(zip_filename, "r") as zipfp:
    zinfo = zipfp.getinfo('PIL/PIL02.py')
    print('--------------')
    print(zinfo)

print('------------------------------')  #30個


zip_filename = 'PIL2222.zip'
with zipfile.ZipFile(zip_filename, "w") as zipfp:
    zipfp.write('test10_new06.py')#預設為 zipfile.ZIP_STORED 模式
    zipfp.write('test10_new07.py', 'test10_new07.py')
    zipfp.write('test10_new08.py', 'test10_new08.py', zipfile.ZIP_STORED)
    zipfp.write('test10_new09.py', 'test10_new09.py', zipfile.ZIP_DEFLATED)
    sinfo = zipfp.getinfo('test10_new08.py')
    print(sinfo)
    dinfo = zipfp.getinfo('test10_new09.py')
    print(dinfo)

    '''
    # check getinfo
    for nm in ('test10_new09.py', "another.name", "strfile"):
        info = zipfp.getinfo(nm)
        print(info.filename, nm)
        print(info.file_size)
    '''

zip_filename = 'PIL3333.zip'
with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_STORED) as zipfp:
    zipfp.comment = b"this is a comment"
    zipfp.write('test10_new09.py', 'test10_new09.py')
    with open(zip_filename, 'a') as f:
        f.write("abcdef\r\n")

with zipfile.ZipFile(zip_filename, "r") as zipfp:
    print(zipfp, zipfile.ZipFile)
    print(zipfp.comment, b"this is a comment")

'''
    def test_write_default_name():
        """Check that calling ZipFile.write without arcname specified
        produces the expected result."""
        with zipfile.ZipFile(zip_filename, "w") as zipfp:
            zipfp.write('test10_new09.py')
            with open('test10_new09.py', "rb") as f:
                print(zipfp.read('test10_new09.py'), f.read())
'''

print('------------------------------')  #30個


zip_filename = 'PIL4444.zip'
compression = zipfile.ZIP_LZMA

zipfp = zipfile.ZipFile(zip_filename, "w")
zipfp.writestr("b.txt", "hello world", compress_type = compression)
info = zipfp.getinfo('b.txt')
print(info)




print('------------------------------')  #30個


print('------------------------------')  #30個


print('------------------------------')  #30個


