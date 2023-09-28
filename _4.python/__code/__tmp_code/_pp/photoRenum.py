import os

source_foldername = 'C:/_git/vcs/_1.data/______test_files3/DrAP_test'   #來源資料夾
target_foldername = 'my_tmp_dir' #輸出資料夾

sample_tree = os.walk(source_foldername)

import shutil

for dirname, subdir, files in sample_tree:
   allfiles = []
   basename = os.path.basename(dirname)
   if basename == target_foldername:  # 輸出資料夾不再重複處理
      continue
   
   for file in files:  # 讀取所有 jpg 檔名，存入 allfiles 串列中
      ext = file.split('.')[-1]
      if ext == "jpg": # 讀取 *.jpg to allfiles
         allfiles.append(file)
         
   if len(allfiles) > 0: # 將 jpg 存入 輸出資料夾 中
      target_dir = dirname + '/' + target_foldername
      if not os.path.exists(target_dir):
         os.mkdir(target_dir)
      
      counter = 0
      for file in allfiles:  
         filename = file.split('.')[0] #主檔名         
         m_filename = "p" + str(counter) 
         destfile = target_dir + '/' + m_filename + '.jpg' # 加上完整路徑
         srcfile = dirname + "/" + file
         print(destfile)
         #shutil.copy(srcfile,destfile); # 複製檔案
         counter += 1
     
print("完成...")
