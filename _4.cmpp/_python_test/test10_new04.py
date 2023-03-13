import os, shutil, glob

print("單層資料夾內所有檔案容量")

source_dir = 'C:/______test_files/__pic/_angry_bird/'

pngfiles = glob.glob(source_dir+"*.png")
jpgfiles = glob.glob(source_dir+"*.jpg")
giffiles = glob.glob(source_dir+"*.gif")
allfiles = pngfiles + jpgfiles + giffiles

allfilesize = 0
for f in allfiles:
    print("檔案 : " + f +", 大小 : " + str(os.path.getsize(f)) + " 拜")
    allfilesize += os.path.getsize(f)

print("總容量 : " + str(allfilesize))


'''
target_dir = source_dir + "output"

print("目標資料夾 : " + target_dir)

if os.path.exists(target_dir):
  print("目的資料夾已存在")
  exit(1)

split用法 TBD
os.mkdir(target_dir)
imageno = 0
for f in allfiles:
  dirname, filename = f.split('/')
  mainname, extname = filename.split('.')
  targetfile = target_dir + '/' + str(imageno) + '.' + extname
  shutil.copyfile(f, targetfile)
  imageno += 1
'''




