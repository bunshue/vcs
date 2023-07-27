import glob

foldername = 'C:/_git/vcs/_1.data/______test_files5'

pattern = '*'

filenames = glob.glob1(foldername, pattern)

print(filenames)

for f in glob.glob1(foldername, "*.dll"):
    print(f)

for f in glob.glob1(foldername, "*.pyd"):
    print(f)


import os
for f in os.listdir(foldername):
    if os.path.isdir(f):
        print('dir : ', f)
    else:
        print('file : ', f)


for file in os.listdir(foldername):
    afile = os.path.join(foldername, file)
    if os.path.isdir(afile):
        print('dir : ', afile)
    else:
        print('file : ', afile)
        

names = os.listdir(foldername)

for name in sorted(names):
    full = name
    if os.path.islink(full):
        print('link')
    elif os.path.isdir(full):
        print('dir')
    else:
        print('file')












