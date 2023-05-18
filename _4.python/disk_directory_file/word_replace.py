import sys, os

print('判斷檔案路徑屬性')

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
if os.path.isdir(filename):
    print(filename, '目錄')
else:
    print(filename, '檔案, 開啟之')
    with open(filename, "rb") as f:
        data = f.read()
    if b'\0' in data:
        print(filename, "二進位")


filename1 = 'C:/_git/vcs/_1.data/______test_files1/poetry2.txt'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/poetry222.txt'
if os.path.isdir(filename1):
    print(filename1, '目錄')
else:
    print(filename1, '檔案, 開啟之')
    with open(filename1, "rb") as f:
        data = f.read()
    if b'\0' in data:
        print(filename1, "二進位")
    else:
        print(filename1, "文字檔")
        #將檔案所有文字全部改變, 存檔
        #newdata = data.replace(b"\r\n", b"")
        newdata = data.replace(b"c", b"k")#其實這是二進位修改
        if newdata != data:
            print(filename1)
            with open(filename2, "wb") as f:
                f.write(newdata)
