import os,shutil
output_dir = 'output'
cur_path=os.path.dirname(__file__) # 取得目前路徑
sample_tree=os.walk(cur_path)

for dirname,subdir,files in sample_tree:
   allfiles=[]
   basename= os.path.basename(dirname)
   if basename == output_dir:  # output 目錄不再重複處理
      continue
   
   for file in files:  # 讀取所有 mp3 檔名，存入 allfiles 串列中
      ext=file.split('.')[-1]
      if ext=="mp3": # 讀取 *.mp3 to allfiles
         allfiles.append(file)
         
   if len(allfiles)>0: # 將 mp3 存入 output 目錄中
      target_dir = dirname + '/' + output_dir
      if not os.path.exists(target_dir):
         os.mkdir(target_dir)
  
      for file in allfiles:  
         filename=file.split('.')[0] #主檔名         
         m_filename =""
         for c in filename: # 將主檔名中不合法的字元去除
            if c==" " or c=="." or c=="," or c=="、" or c=="，" or c=="(" or c==")":
                m_filename += ""  # 去除不合法字元
            else:
                m_filename += c   

         destfile = "{}.{}".format(target_dir+'/'+m_filename, ext) # 加上完整路徑
         srcfile=dirname + "/" + file
         print(destfile)
         shutil.copy(srcfile,destfile); # 複製檔案
     
print("完成...")