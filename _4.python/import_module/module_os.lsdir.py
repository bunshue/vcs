'''
os.listdir
'''

import os
import stat
import time

def test_file(name):
    files = os.listdir(name)    #單層
    
    for filename in files:
        print(filename)

#name = 'cccc.dat'
name = 'dddd.pdf'
name = 'C:/_git/vcs/_4.python/__code/'

#test_file(name)


#多層

starting_path = 'C:/_git/vcs/_1.data/______test_files1/_emgu'

def add_files_in_folder(dirname):
    files = os.listdir(dirname)
    for file in files:
        fullname = os.path.join(dirname, file)
        if os.path.isdir(fullname): #資料夾 再找下去
            print('D', fullname)
            add_files_in_folder(fullname)
        else:   #檔案
            print('f', fullname, os.stat(fullname).st_size)

add_files_in_folder(starting_path)




