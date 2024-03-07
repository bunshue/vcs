"""
PIL 新進

"""

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image   # Importing Image class from PIL module

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

from PIL import Image

print("------------------------------------------------------------")  # 60個

img = Image.open("data/img01.jpg")
#img.show()
w,h=img.size
print(w,h) #320 240

filename=img.filename
print(filename)

print("------------------------------------------------------------")  # 60個

img = Image.open("data/img01.jpg")
w,h=img.size #320 240

img1=img.resize((w*2,h))

img2=img.resize((w,h*2))

print("------------------------------------------------------------")  # 60個

img = Image.open("data/img01.jpg")

img1=img.rotate(45)#旋轉45度
img2=img.rotate(90) #旋轉90度
img3=img.rotate(180)#旋轉180度

print("------------------------------------------------------------")  # 60個

img = Image.open("data/img01.jpg")

img2=img.transpose(Image.FLIP_LEFT_RIGHT)#左右翻轉
img3=img.transpose(Image.FLIP_TOP_BOTTOM)#上下翻轉

print("------------------------------------------------------------")  # 60個

img = Image.open("data/img01.jpg") # w,h=img.size #320 240

img1=img.crop((0,0,160,120))
img2=img.crop((161,0,320,120))
img3=img.crop((0,121,160,240))
img4=img.crop((161,121,320,240))

img.close()

print("------------------------------------------------------------")  # 60個

img = Image.open("data/img01.jpg")
imgcopy=img.copy()

print("------------------------------------------------------------")  # 60個

img = Image.open("data/panda.jpg")
imgcopy=img.copy() #複製
#切割貓熊並改變尺寸
img1=imgcopy.crop((190,184,415,350)).resize((160,140))
imgcopy.paste(img1,(40,30)) #貼上
img2=img1.transpose(Image.FLIP_LEFT_RIGHT)#左右翻轉
imgcopy.paste(img2,(220,40))#貼上

print("------------------------------------------------------------")  # 60個

def emptydir(dirname):
    if os.path.isdir(dirname):
        shutil.rmtree(dirname)
        sleep(1)  #需延遲,否則會出錯
    os.mkdir(dirname)

import glob
import shutil, os
from time import sleep

image_dir="pic"
target_dir = 'tmp_bmp_photo'
target_dir2 = 'tmp_gray_photo'
emptydir(target_dir)
emptydir(target_dir2)
files=glob.glob(image_dir+"\*.jpg") + glob.glob(image_dir+"\*.png")
for i, f in enumerate(files):
    img = Image.open(f)
    img_new = img.resize((800, 600), Image.LANCZOS)
    path,filename = f.split("\\") #路徑、檔名   
    name,ext = filename.split(".") #主檔名、副檔名
    #以bmp格式存檔
    img_new.save(target_dir+'/' + name + 'aaa.bmp')
    
    #轉換為灰階
    img_gray = img_new.convert('L')  
    # gray001.jpg、gray002.jpg...
    outname = str("gray") + str('{:0>3d}').format(i+1) + 'aaa.jpg'
    img_gray.save(target_dir2+'/'+outname)
    print("{} 複製完成!".format(f))
    img.close()   

print('轉換尺寸及灰階處理結束！')

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


"""
img1.save("resize01aaa.jpg")
img2.save("resize02aaa.jpg")
"""

