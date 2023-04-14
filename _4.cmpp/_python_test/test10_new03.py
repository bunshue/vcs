import os
import glob

print('撈出一層資料 .jpg檔')
files = glob.glob('data\*.jpg')
for file in files:
    print(file)
    if os.path.isfile(file):
        print('是一個檔案')
    else:
        print('不是一個檔案')
    time = os.path.getmtime(file)
    print(time)

    if not os.path.exists(file):
        print('檔案不存在')
    else:
        abspath = os.path.abspath(file)
        directory, filename = os.path.split(abspath)
        print('全檔名', abspath)
        print('資料夾', directory)
        print('短檔名', filename)
        new_filename = os.path.join('新資料夾', filename)
        print('新全檔名', new_filename)
        print()

print(__file__)
print(__file__.upper())
print(__file__.lower())
print(__name__)

import time
version = time.strftime("-%Y%m%d")
print(version)

import sys
print(sys.path)



print(os.curdir)
print(version)
print(version)


#強制離開程式, 並說明原因
sys.exit('強制離開程式, 並說明原因')



