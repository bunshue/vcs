import os
import sys
import docx

print('搜尋字串')
keyword = 'shutil'
print("搜尋字串：{}".format(keyword))

#cur_path = os.path.dirname(__file__) # 取得目前路徑
cur_path = os.getcwd()
print(cur_path)
sample_tree = os.walk(cur_path)

for dirname, subdir, files in sample_tree:
   allfiles = []   
   for file in files:  # 取得所有 .py .txt .docx 檔，存入 allfiles 串列中
      print(file)
      ext = file.split('.')[-1]
      if ext == "py" or ext == "txt" or ext == "docx": 
         allfiles.append(dirname + '/' + file)
         
   if len(allfiles) > 0:  
      for file in allfiles:  # 讀取 allfiles 串列所有檔案  
         try:
            if file.split('.')[-1] == "docx": # .docx
                doc = docx.Document(file)
                line = 0
                for p in doc.paragraphs:
                    line += 1
                    if keyword in p.text:
                        print("...在第 {} 段文字中找到「{}」\n {}。".format(line, keyword, p.text))
            else:  # .py or .txt             
                fp = open(file, "r", encoding = 'UTF-8')
                article = fp.readlines()
                fp.close 
                line = 0            
                for row in article:
                   line += 1
                   if keyword in row:
                       print("在 {}，第 {} 列找到「{}」。".format(file, line, keyword))
         except:
            print("{} 無法讀取..." .format(file)) 
     
print("完成...")
