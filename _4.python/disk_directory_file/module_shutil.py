import sys
import shutil

filename1 = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2 = 'picture1b.jpg'
filename3 = 'picture1c.jpg'

foldername1 = 'C:/_git/vcs/_1.data/______test_files5'
foldername2 = 'C:/_git/vcs/_1.data/______test_files6'

print("------------------------------------------------------------")  # 60個

print("複製 檔案 -> 檔案")
shutil.copy(filename1, filename2)
shutil.copy(filename1, filename3)

print("複製 檔案 -> 資料夾")
shutil.copy(filename1, foldername1)

print("------------------------------------------------------------")  # 60個

print("複製 資料夾 -> 資料夾")
shutil.copytree(foldername1, foldername2)

print("------------------------------------------------------------")  # 60個

print("移動 檔案 -> 資料夾")
shutil.move(filename2, foldername2)

print("------------------------------------------------------------")  # 60個

filename3 = 'picture1c.jpg'
filename4 = 'picture1d.jpg'

print("更改檔案名稱")
shutil.move(filename3, filename4)

print("------------------------------------------------------------")  # 60個

print("移動 資料夾 -> 資料夾")

foldername2 = 'C:/_git/vcs/_1.data/______test_files6'
foldername3 = 'C:/_git/vcs/_1.data/______test_files6b'

shutil.move(foldername2, foldername3)

print("------------------------------------------------------------")  # 60個

print("刪除 資料夾")
shutil.rmtree(foldername3)

print("------------------------------------------------------------")  # 60個




