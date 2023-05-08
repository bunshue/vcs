import os, time, glob, sys, shutil

source_dir = 'C:/_git/vcs/_1.data/______test_files1/source_pic'
target_dir = 'C:/_git/vcs/_1.data/______test_files2/photos'

#準備輸出資料夾 若已存在, 則先刪除再建立 若不存在, 則建立
if os.path.exists(target_dir):
        #os.remove(target_dir)  #存取被拒 不可用
        shutil.rmtree(target_dir)
if not os.path.exists(target_dir):
        os.mkdir(target_dir)
        #os.makedirs(target_dir, exist_ok=True)

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

print("完成")
print('輸出資料夾 : ', target_dir)
