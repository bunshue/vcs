'''

準備做資料庫用


'''

import os

def walk_python_files(paths):
    for path in paths:
        if os.path.isfile(path):
            print(path)
        elif os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for filename in files:
                    if filename.endswith(".csv"):
                        print(filename)

foldername1 = 'C:/_git/vcs/_1.data/______test_files3'

paths = [foldername1]
walk_python_files(paths)




filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/lena.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/human1.jpg'

print(filename)

filename1 = filename.split(".")[0] # 取得檔案名稱(不添加副檔名)

print(filename1)


