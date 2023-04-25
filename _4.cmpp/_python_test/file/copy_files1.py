import os, time, glob, sys, shutil

source_dir = 'C:/_git/vcs/_4.cmpp/_python_test/data/source_pic'
target_dir = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/photos'
if not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)

allfiles = glob.glob(source_dir+'/*.jpg') + glob.glob(source_dir+'/*.png')
for imagefile in allfiles:
        print(imagefile)

for imagefile in allfiles:
	filename = imagefile.split('\\')[-1]
	i=0
	ori_filename = filename
	while True:
		if not os.path.exists(target_dir+'/'+filename):
			shutil.copy(imagefile, target_dir+'/'+filename)
			print(filename)
			break
		else:
			ext = '.' + ori_filename.split('.')[-1]
			filename = ori_filename.split(ext)[0] + '_' + str(i) + ext
			i = i + 1

