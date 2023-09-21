import os
import docx

cur_path = os.path.dirname(__file__) # 取得目前路徑
sample_tree = os.walk(cur_path)

keyword = "籃球"
print("搜尋字串：{}".format(keyword))

for dirname, subdir, files in sample_tree:
   allfiles = []   
   for file in files:  # 取得所有 .docx 檔，存入 allfiles 串列中
      ext = file.split('.')[-1]
      if ext == "docx": # get *.docx to allfiles 
         allfiles.append(dirname + '/' + file)
         
   for file in allfiles:
      print("正在搜尋 <{}> 檔案...".format(file))
      try:
         doc = docx.Document(file)
         line = 0
         for p in doc.paragraphs:
             line += 1
             if keyword in p.text:
                 print("...在第 {} 段文字中找到「{}」\n {}。".format(line, keyword, p.text))
      except:
         print("無法讀取 {} 檔案..." .format(file))  
     
print("\n搜尋完畢...")
