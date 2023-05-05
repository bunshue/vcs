#調整資料夾內所有圖片檔影像寬度, 加logo
      
import sys, os, glob
from PIL import Image, ImageDraw

source_dir = 'C:/_git/vcs/_1.data/______test_files1/source_pic'
target_dir = 'C:/_git/vcs/_1.data/______test_files2/resized_pic'
#logo_filename = 'C:/_git/vcs/_1.data/______test_files1/burn.bmp'        #fail
logo_filename = 'C:/_git/vcs/_1.data/______test_files1/logo.png'

image_width = 800

print("將資料夾 " + source_dir + " 內所有圖片檔調整寬度成 " + str(image_width) + " 像素")

print('Processing: {}'.format(source_dir))

#單層
allfiles = glob.glob(source_dir + '/*.jpg') + glob.glob(source_dir + '/*.png')
if not os.path.exists(target_dir):
	os.mkdir(target_dir)

logo = Image.open(logo_filename)
logo = logo.resize((150, 150))   #調整圖像大小

for target_image in allfiles:
	pathname, filename = os.path.split(target_image)
	print(filename)
	im = Image.open(target_image)
	w, h = im.size
	im = im.resize((800, int(800 / float(w) * h)))
	im.paste(logo, (0, 0), logo)
	im.save(target_dir + '/' + filename)
	im.close()

print("完成")
	
