import os

source_foldername = 'C:/_git/vcs/_1.data/______test_files3/DrAP_test'   #來源資料夾
target_foldername = 'my_tmp_dir' #輸出資料夾

filenames = os.walk(source_foldername)

import hashlib

allmd5s = dict() 
n = 0

for dirname, subdir, files in filenames:
   allfiles = []
   for file in files:  # 取得所有 .png .jpg 檔，存入 allfiles 串列中
      print(dirname + '/' + file)
      ext = file.split('.')[-1]
      if ext == "png" or ext == "jpg":
         allfiles.append(dirname + '/' + file)
         
   if len(allfiles) > 0: 
      for imagefile in allfiles:
          img_md5 = hashlib.md5(open(imagefile, 'rb').read()).digest()
          #print(type(img_md5))
          #print(img_md5)
          if img_md5 in allmd5s:
              if n == 0:
                  print("找到下列重覆的檔案：")
              n += 1
              print(os.path.abspath(imagefile))
              print(allmd5s[img_md5] + "\n")
          else:
              allmd5s[img_md5] = os.path.abspath(imagefile)#以md5為key, 以檔案路徑為value
     
print("完成...")

'''
print(type(allmd5s))
#print(allmd5s)

print()
print()
print('keys')
print(allmd5s.keys())

print()
print()
print('values')
print(allmd5s.values())

print()
print()
print(allmd5s.items())
'''
