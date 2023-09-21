import os
from PIL import Image

source_foldername = 'C:/_git/vcs/_1.data/______test_files3/DrAP_test'
target_foldername = 'my_tmp_dir2'

sample_tree = os.walk(source_foldername)

image_width = 800

for dirname, subdir, files in sample_tree:
    allfiles = [] 
    basename = os.path.basename(dirname)
    if basename == target_foldername:  # resized_photo 目錄不再重複處理
        continue  
    for file in files:  # 取得所有 .png .jpg 檔，存入 allfiles 串列中
        ext = file.split('.')[-1]
        if ext == "png" or ext == "jpg":
            allfiles.append(dirname +'/'+file)
         
    if len(allfiles) > 0: 
        target_dir = dirname + '/' + target_foldername
        if not os.path.exists(target_dir):
            os.mkdir(target_dir)
        for file in allfiles:
            pathname,filename = os.path.split(file)
            img = Image.open(file)
            w, h = img.size
            img = img.resize((image_width,int(image_width / float(w) * h)))
            #img.save(target_dir + '/' + filename)
            print("<{}> 複製完成!".format(target_dir + '/' + filename))
            img.close()
            
print("完成...")  
