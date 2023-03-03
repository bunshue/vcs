# _*_ coding: utf-8 _*_
# Mac OS, Python 2.7.11

import os, shutil, glob
source_dir = "images/"
disk = os.statvfs("/") 
freespace = disk.f_bsize * disk.f_blocks;
pngfiles = glob.glob(source_dir+"*.png")
jpgfiles = glob.glob(source_dir+"*.jpg")
giffiles = glob.glob(source_dir+"*.gif")
allfiles = pngfiles + jpgfiles + giffiles

allfilesize = 0
for f in allfiles:
  allfilesize += os.path.getsize(f)

if allfilesize > freespace:
  print("磁碟空間不足")
  exit(1)

target_dir = source_dir + "output"
if os.path.exists(target_dir):
  print("目的資料夾已存在")
  exit(1)

os.mkdir(target_dir)
imageno = 0
for f in allfiles:
  dirname, filename = f.split('/')
  mainname, extname = filename.split('.')
  targetfile = target_dir + '/' + str(imageno) + '.' + extname
  shutil.copyfile(f, targetfile)
  imageno += 1
