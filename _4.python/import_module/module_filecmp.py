import filecmp

filename1 = "D:/_git/vcs/_1.data/______test_files1/picture1.jpg"
filename2 = "D:/_git/vcs/_1.data/______test_files1/picture2.jpg"

if filecmp.cmp(filename1, filename2, shallow=0) == True:
    print("兩個檔案 相同")
else:
    print("兩個檔案 不同")


result1 = filecmp.cmp(filename1, filename2)
print(result1)
result2 = filecmp.cmp(filename1, filename2, shallow=False)
print(result2)
result3 = filecmp.cmp(filename1, filename2, shallow=True)
print(result3)


foldername1 = "D:/_git/vcs/_1.data/______test_files4"
foldername2 = "D:/_git/vcs/_1.data/______test_files5"

left_dir, right_dir = foldername1, foldername2
d = filecmp.dircmp(left_dir, right_dir)
print(type(d))
print(d)


result1 = filecmp.cmpfiles(foldername1, foldername2, ["file"])
print(result1)
result2 = filecmp.cmpfiles(foldername1, foldername2, ["file"], shallow=False)
print(result2)
result3 = filecmp.cmpfiles(foldername1, foldername2, ["file"], shallow=True)
print(result3)
result4 = filecmp.cmpfiles(foldername1, foldername2, ["file", "file2"])
print(result4)
