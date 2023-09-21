import os
import shutil

source_foldername = 'C:/_git/vcs/_1.data/______test_files3/DrAP_test'
target_foldername = 'my_tmp_dir1'

output_dir = 'my_tmp_dir'

sample_tree = os.walk(source_foldername)

for dirname,subdir,files in sample_tree:
   allfiles = []
   basename = os.path.basename(dirname)
   if basename == output_dir:  # output 目錄不再重複處理
      continue
   
   for file in files:  # 讀取所有 jpg 檔名，存入 allfiles 串列中
      ext = file.split('.')[-1]
      if ext == "jpg": # 讀取 *.jpg to allfiles
         allfiles.append(file)
         
   if len(allfiles) > 0: # 將 jpg 存入 output 目錄中
      target_dir = dirname + '/' + output_dir
      if not os.path.exists(target_dir):
         os.mkdir(target_dir)
  
      for file in allfiles:  
         filename = file.split('.')[0] #主檔名         
         m_filename = ""
         for c in filename: # 將主檔名中不合法的字元去除
            if c == " " or c == "." or c == "," or c == "、" or c == "，" or c == "(" or c == ")":
                m_filename += ""  # 去除不合法字元
            else:
                m_filename += c   

         destfile = "{}.{}".format(target_dir + '/' + m_filename, ext) # 加上完整路徑
         srcfile = dirname + "/" + file
         print(srcfile, ' -> ', destfile)
         #shutil.copy(srcfile, destfile); # 複製檔案
     
print("完成...")

