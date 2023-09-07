def read_file(filename, encoding):
    fp =  open(filename, encoding = encoding)
    data = fp.read()
    fp.close()
    print(data)

print('\nbig5 = cp950 ------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/__text/Compressor.c'
encoding = 'big5'
read_file(filename, encoding)

print('\nunicode utf-8 ------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/__text/Form1.cs.txt'
encoding = 'utf-8'
read_file(filename, encoding)

print('\nshift-jis = cp932 ------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/__text/jap/饩Ⓚ丗钡冦冦葢轿瘅.txt'
encoding = 'shift-jis'
read_file(filename, encoding)

print('\ngb2312 = cp936 ------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/__text/sc/Compressor.ori.c'
encoding = 'gb2312'
read_file(filename, encoding)

print('------------------------------------------------------------')	#60個

