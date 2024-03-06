def emptydir(dirname):
    if os.path.isdir(dirname):
        shutil.rmtree(dirname)
        sleep(1)  #需延遲,否則會出錯
    os.mkdir(dirname)

import PIL
from PIL import Image
import glob
import shutil, os
from time import sleep

image_dir="pic"
target_dir = 'bmp_photo'
target_dir2 = 'gray_photo'
emptydir(target_dir)
emptydir(target_dir2)
files=glob.glob(image_dir+"\*.jpg") + glob.glob(image_dir+"\*.png")
for i, f in enumerate(files):
    img = Image.open(f)
    img_new = img.resize((800, 600), PIL.Image.ANTIALIAS)
    path,filename = f.split("\\") #路徑、檔名   
    name,ext = filename.split(".") #主檔名、副檔名
    #以bmp格式存檔
    img_new.save(target_dir+'/' + name + '.bmp')
    
    #轉換為灰階
    img_gray = img_new.convert('L')  
    # gray001.jpg、gray002.jpg...
    outname = str("gray") + str('{:0>3d}').format(i+1) + '.jpg'
    img_gray.save(target_dir2+'/'+outname)
    print("{} 複製完成!".format(f))
    img.close()   

print('轉換尺寸及灰階處理結束！')