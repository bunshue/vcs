import os

files = (os.getcwd(), "ch5-3-3.py")
for f in files:
    print("項目 = " + str(f))
    if os.path.exists(f):
        print("存在!")
    if os.path.isdir(f):
        print("是目錄!")
    if os.path.isfile(f):
        print("是檔案!")
        