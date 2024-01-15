#各種檔案寫讀範例 bin 1

import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

#filename_rw1 = 'tmp_ABC.txt'

#print("將字串寫入檔案 : " + filename_rw1)


print("------------------------------------------------------------")  # 60個



dst = 'tmp_random_data.bin'

bytedata = bytes(range(0,256))
with open(dst, 'wb') as file_dst:
    file_dst.write(bytedata)

print('------------------------------------------------------------')	#60個

src = 'tmp_random_data.bin'

with open(src, 'rb') as file_src:
    print("目前位移 : ", file_src.tell())
    file_src.seek(10)
    print("目前位移 : ", file_src.tell())
    data = file_src.read()
    print("目前內容 : ", data[0])
    file_src.seek(255)
    print("目前位移 : ", file_src.tell())
    data = file_src.read()
    print("目前內容 : ", data[0])

print('------------------------------------------------------------')	#60個

print('複製binary檔案')

filename1 = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2 = 'tmp_picture1_copied.jpg'

tmp = ''

with open(filename1, 'rb') as file_rd:
    tmp = file_rd.read()
    with open(filename2, 'wb') as file_wr:
        file_wr.write(tmp)


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

