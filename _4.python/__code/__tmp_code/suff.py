'''
計算不同類型檔案出現次數

'''
import sys

def get_suffix(filename):
    name, sep, suff = filename.rpartition('.')
    return sep + suff if sep else ''


filename1 = 'D:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2 = 'D:/_git/vcs/_1.data/______test_files1/file2.txt'

files = [filename1, filename2]
suffixes = {}

for filename in files:
    suff = get_suffix(filename)
    suffixes.setdefault(suff, []).append(filename)

for suff, filenames in sorted(suffixes.items()):
    print(repr(suff), len(filenames))


print('files')
print(files)
print('suffixes')
print(suffixes)
