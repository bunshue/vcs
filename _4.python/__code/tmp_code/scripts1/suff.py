'''
計算不同類型檔案出現次數

'''
import sys

def getsuffix(filename):
    name, sep, suff = filename.rpartition('.')
    return sep + suff if sep else ''


filename1 = 'C:/______test_files2/human2.jpg'
filename2 = 'C:/______test_files2/file2.txt'

files = [filename1, filename2]
suffixes = {}
for filename in files:
    suff = getsuffix(filename)
    suffixes.setdefault(suff, []).append(filename)
for suff, filenames in sorted(suffixes.items()):
    print(repr(suff), len(filenames))

