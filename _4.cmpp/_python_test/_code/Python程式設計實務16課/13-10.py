# _*_ coding: utf-8 _*_
# 程式 13-10 (Python 3 Version)
import sys, os, glob
from PIL import Image, ImageDraw

source_dir = '.'
target_dir = 'resized_photo'
image_width = 800

if len(sys.argv) > 1:
	source_dir = sys.argv[1]

print('Processing: {}'.format(source_dir))

if not os.path.exists(source_dir):
	print("I can't find the specified directory.")
	exit(1)

allfiles = glob.glob(source_dir+'/*.jpg') + glob.glob(source_dir+'*.png')
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