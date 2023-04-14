import sys, os, glob

source_dir = 'C:/______test_files/__pic'

print('資料夾: ' + source_dir)

print('Processing: {}'.format(source_dir))

#單層
allfiles = glob.glob(source_dir+'/*.jpg') + glob.glob(source_dir+'/*.png')

cnt = 0
for target_image in allfiles:
	pathname, filename = os.path.split(target_image)
	print(filename)
	cnt = cnt + 1
	'''
	if filename[0] == '.': continue  # Only for MacOS to skip the hidden files
	im = Image.open(target_image)
	w, h = im.size
	'''

print('cnt = ' + str(cnt))
print("完成")


	
#撈出一個資料夾下所有檔案
'''
import sys, os, glob
from PIL import Image, ImageDraw

source_dir = 'C:/______test_files/__pic'

print('Processing: {}'.format(source_dir))

allfiles = glob.glob(source_dir+'/*.jpg') + glob.glob(source_dir+'/*.png')

print(allfiles)
'''


#尋找檔案
import glob
print('尋找目前目錄下之 *.py *.txt')
files = glob.glob("glob.py") + glob.glob("os*.py") + glob.glob("*.txt") 
for file in files:
    print(file)



import glob, os

allfiles = glob.glob('*.jpg') + glob.glob('*.png')
count = 1
for afile in allfiles:
	print(afile)
	ext = afile.split('.')[-1]
	newfilename = "{}.{}".format(str(count), ext)
	os.rename(afile, newfilename)
	count += 1
print("完成...")


import os, hashlib, glob

allfiles = glob.glob('*.jpg') + glob.glob('*.png')

allmd5s = dict()
for imagefile in allfiles:
	print(imagefile + " is processing...")
	img_md5 = hashlib.md5(open(imagefile,'rb').read()).digest()
	if img_md5 in allmd5s:
		print("---------------")
		print("以下為重覆的檔案：")
		os.system("open " + os.path.abspath(imagefile))
		os.system("open " + allmd5s[img_md5])
	else:
		allmd5s[img_md5] = 	os.path.abspath(imagefile) 



import os, hashlib, glob

allfiles = glob.glob('*.jpg') + glob.glob('*.png')

allmd5s = dict()
for imagefile in allfiles:
	print(imagefile + " is processing...")
	img_md5 = hashlib.md5(open(imagefile,'rb').read()).digest()
	if img_md5 in allmd5s:
		print("---------------")
		print("以下為重覆的檔案：")
		print(os.path.abspath(imagefile))
		print(allmd5s[img_md5])
	else:
		allmd5s[img_md5] = 	os.path.abspath(imagefile) 












