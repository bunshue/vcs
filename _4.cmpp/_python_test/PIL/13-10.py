import sys, os, glob
from PIL import Image, ImageDraw

source_dir = 'source_pic'
target_dir = 'resized_pic'

image_width = 800

print("將資料夾 " + source_dir + " 內所有圖片檔調整寬度成 " + str(image_width) + " 像素")

print('Processing: {}'.format(source_dir))

allfiles = glob.glob(source_dir+'/*.jpg') + glob.glob(source_dir+'/*.png')
if not os.path.exists(target_dir):
	os.mkdir(target_dir)

logo = Image.open('logo.png')
logo = logo.resize((150,150))
for target_image in allfiles:
	pathname, filename = os.path.split(target_image)
	print(filename)
	if filename[0] == '.': continue  # Only for MacOS to skip the hidden files
	im = Image.open(target_image)
	w, h = im.size
	im = im.resize((800, int(800/float(w) * h)))
	im.paste(logo, (0,0), logo)
	im.save(target_dir+'/'+filename)
	im.close()


	
