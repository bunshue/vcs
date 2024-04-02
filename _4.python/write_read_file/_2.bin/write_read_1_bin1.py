#各種檔案寫讀範例 bin 1

import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

filename = 'tmp_binary256.bin'

print('建立一個0~255的binary檔案')
binary_data = bytes(range(0,256))
with open(filename, 'wb') as f:
    f.write(binary_data)

print('------------------------------------------------------------')	#60個

filename = 'tmp_binary256.bin'

print('測試移動檔案指標, 讀取一個0~255的binary檔案')

with open(filename, 'rb') as f:
    print("目前位移 : ", f.tell())
    f.seek(10)
    print("目前位移 : ", f.tell())
    data = f.read()
    print("目前內容 : ", data[0])
    f.seek(255)
    print("目前位移 : ", f.tell())
    data = f.read()
    print("目前內容 : ", data[0])

print('------------------------------------------------------------')	#60個

print('複製binary檔案')

filename1 = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2 = 'tmp_picture1_copied.jpg'

tmp = ''

with open(filename1, 'rb') as f1:
    tmp = f1.read()
    with open(filename2, 'wb') as f2:
        f2.write(tmp)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

""" many
inf = open(filename, "rb")    # jpeg圖檔就是二進位檔案

byte = inf.read(1)               # 一次讀一個byte
while byte:
    print(byte)
    byte = inf.read(1)           # 繼續讀下一個byte

inf.close()
"""

print("------------------------------------------------------------")  # 60個

# BMP parser
def b4_2_int(bytes1):
    return (bytes1[0] | bytes1[1]<<8 | bytes1[2]<<16 | bytes1[3]<<24)

def b2_2_int(bytes1):
    return (bytes1[0] | bytes1[1]<<8)

filename = '../data/Medrust3.bmp'
infile = open(filename, 'rb')

# 'B' 'M'
b2 = infile.read(2)
print(b2)
b4 = infile.read(4)
size = b4_2_int(b4)
print('file size =', size, 'bytes')
infile.read(4)
infile.read(4)
infile.read(4)
width = b4_2_int(infile.read(4))
height = b4_2_int(infile.read(4))
print('image dimension =', width, 'x', height)
planes = b2_2_int(infile.read(2))
print('image planes =', planes)
bitsPerPixel = b2_2_int(infile.read(2))
print('bits per pixel =', bitsPerPixel)

infile.close()


print("------------------------------------------------------------")  # 60個

bytestr1 = b'This is a byte string'
int1 = 65
float1 = 3.14
int2s = [1, 2, 3]

outfname = 'tmp_test.bin'
outfile = open(outfname, 'wb')

outfile.write(bytestr1)
bint1 = int1.to_bytes(4, byteorder='big')
outfile.write(bint1)
bfloat1 = bytes(float1.hex(), 'utf-8')
outfile.write(bfloat1)
outfile.write(bytearray(int2s))

outfile.close()

print('------------------------------------------------------------')	#60個

"""
读写二进制文件
"""
import base64

with open('../data/mm.jpg', 'rb') as f:
    data = f.read()
    # print(type(data))
    # print(data)
    print('字节数:', len(data))
    # 将图片处理成BASE-64编码
    print(base64.b64encode(data))

with open('tmp_girl.jpg', 'wb') as f:
    f.write(data)
print('写入完成!')

print('------------------------------------------------------------')	#60個

# BMP解析程式

# Little Endian的 4 bytes處理函數
def b4_2_int(b4):
    # 針對每個byte使用位元平移
    ii = b4[0] | b4[1]<<8 | b4[2]<<16 | b4[3]<<24
    return ii
# Little Endian的 2 bytes處理函數
def b2_2_int(b2):
    # 針對每個byte使用位元平移
    ii = b2[0] | b2[1]<<8
    return ii

filename = '../data/Lenna.bmp'       # 786554 bytes, 512x512
infile = open(filename, 'rb')

# 標頭識別碼：'B'和'M'
b2 = infile.read(2)
print(b2)
# 檔案大小
b4 = infile.read(4)
filesize = b4_2_int(b4)
print('File size:', filesize, 'bytes')
# 跳過不在意的欄位
infile.read(4)
# 跳過不在意的欄位
infile.read(4)
# 跳過不在意的欄位
infile.read(4)
# 圖像寬度（長度）
b4 = infile.read(4)
width = b4_2_int(b4)
# 圖像高度（寬度）
b4 = infile.read(4)
height = b4_2_int(b4)
print('Image dimension:', width, 'x', height)
b2 = infile.read(2)
planes = b2_2_int(b2)
print('Image planes:', planes)
# 圖像顏色深度（bit數）
b2 = infile.read(2)
depth = b2_2_int(b2)
print('Color depth:', depth)

infile.close()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

