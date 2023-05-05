import os

def find_files(foldername):
    names = os.listdir(foldername)
    print(names)

    files = []
    for name in names:
        fn = os.path.join(foldername, name)
        print(fn, end = '\t')
        if os.path.isdir(fn):
            print('資料夾')
        else:
            print('檔案')

    files.sort(key=os.path.normcase)


print('撈出資料夾下所有檔案')

foldername = 'C:/_git/vcs/_1.data/______test_files2'
find_files(foldername)
