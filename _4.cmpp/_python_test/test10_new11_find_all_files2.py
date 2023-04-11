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


	
