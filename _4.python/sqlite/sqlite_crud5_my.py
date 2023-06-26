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




filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

print('全檔名/長檔名 : ', filename)


filename1 = filename.split(".")[-2] # 取得檔案名稱(不添加副檔名)

print(filename1)
print('前檔名 : ', filename1)


'''
sql 
資料庫準備資料

D:/AAAA/BBBB/CCCC/DDDD/EEEE.mp4	4.64GB

全檔名、長檔名			D:/AAAA/BBBB/CCCC/DDDD/EEEE.mp4
簡檔名、短檔名			EEEE.mpg
前檔名				EEEE
全路徑 全資料夾 長路徑 長資料夾	D:/AAAA/BBBB/CCCC/DDDD
短路徑 短資料夾			DDDD
副檔名				mp4
檔案大小			4.46GB
影片格式			W = 1920, H =1080


描述1				kaede
描述2				kaede
描述3				kaede


另有更好

中文版

4K
非1080p

720p
480p

name
airi
anna
sora
jun
3333
7777
 



series

gggg
debut

ssss	same
dddd	delete
mmmm




'''
