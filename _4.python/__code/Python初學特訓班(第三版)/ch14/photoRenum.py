import os, shutil
cur_path = os.path.dirname(__file__) # 取得目前路徑
sample_tree = os.walk(cur_path)
output_dir = 'output2'

for dirname, subdir, files in sample_tree:
   allfiles = []
   basename = os.path.basename(dirname)
   if basename == output_dir:  # output2 目錄不再重複處理
      continue
   
   for file in files:  # 讀取所有 jpg 檔名，存入 allfiles 串列中
      ext = file.split('.')[-1]
      if ext == "jpg": # 讀取 *.jpg to allfiles
         allfiles.append(file)
         
   if len(allfiles) > 0: # 將 jpg 存入 output 目錄中
      target_dir = dirname + '/' + output_dir
      if not os.path.exists(target_dir):
         os.mkdir(target_dir)
      
      counter = 0
      for file in allfiles:  
         filename = file.split('.')[0] #主檔名         
         m_filename = "p" + str(counter) 
         destfile = target_dir + '/' + m_filename + '.jpg' # 加上完整路徑
         srcfile = dirname + "/" + file
         print(destfile)
         shutil.copy(srcfile,destfile); # 複製檔案
         counter += 1
     
print("完成...")
