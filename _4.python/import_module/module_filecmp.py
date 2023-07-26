import filecmp

filename1 = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/picture2.jpg'

if filecmp.cmp(filename1, filename2, shallow = 0):
    print('兩個檔案 相同')
else:
    print('兩個檔案 不同')

