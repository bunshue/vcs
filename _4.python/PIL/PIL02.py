#調整資料夾內所有圖片檔影像寬度, 加logo
      
import sys, os, glob
from PIL import Image, ImageDraw
import shutil

source_dir = 'C:/_git/vcs/_1.data/______test_files1/source_pic'
target_dir = 'C:/_git/vcs/_1.data/______test_files2/resized_pic'
#logo_filename = 'C:/_git/vcs/_1.data/______test_files1/burn.bmp'        #fail
logo_filename = 'C:/_git/vcs/_1.data/______test_files1/logo.png'

#準備輸出資料夾 若已存在, 則先刪除再建立 若不存在, 則建立
if os.path.exists(target_dir):
        #os.remove(target_dir)  #存取被拒 不可用
        shutil.rmtree(target_dir)
if not os.path.exists(target_dir):
        os.mkdir(target_dir)

image_width = 800

print("將資料夾 " + source_dir + " 內所有圖片檔調整寬度成 " + str(image_width) + " 像素")

print('Processing: {}'.format(source_dir))

#單層
allfiles = glob.glob(source_dir + '/*.jpg') + glob.glob(source_dir + '/*.png')

logo = Image.open(logo_filename)    #PIL讀取本機圖片
logo = logo.resize((150, 150))   #調整圖像大小

for target_image in allfiles:
	pathname, filename = os.path.split(target_image)
	print(filename)
	image = Image.open(target_image)    #PIL讀取本機圖片
	w, h = image.size
	image = image.resize((800, int(800 / float(w) * h)))
	image.paste(logo, (0, 0), logo)
	image.save(target_dir + '/' + filename)
	image.close()

print("完成")
print('輸出圖片資料夾 : ', target_dir)

	
