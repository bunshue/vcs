import os

source_foldername = 'C:/_git/vcs/_1.data/______test_files3/DrAP_test'   #來源資料夾
target_foldername = 'my_tmp_dir' #輸出資料夾

sample_tree = os.walk(source_foldername)

import hashlib

allmd5s = dict() 
n = 0

for dirname, subdir, files in sample_tree:
   allfiles = []   
   for file in files:  # 取得所有 .png .jpg 檔，存入 allfiles 串列中
      ext = file.split('.')[-1]
      if ext == "png" or ext == "jpg": 
         allfiles.append(dirname + '/' + file)       
         
   if len(allfiles) > 0: 
      for imagefile in allfiles:
          img_md5 = hashlib.md5(open(imagefile, 'rb').read()).digest()          
          if img_md5 in allmd5s:
              if n == 0:
                  print("找到下列重覆的檔案：")
              n += 1
              print(os.path.abspath(imagefile))
              print(allmd5s[img_md5] + "\n")
          else:
              allmd5s[img_md5] = os.path.abspath(imagefile) 
     
print("完成...")

