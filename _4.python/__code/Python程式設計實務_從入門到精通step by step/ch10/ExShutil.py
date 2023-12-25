import shutil, pathlib

file = str(input("請輸入欲要複製的檔名(可含副檔名)："))
copyFile = str(input("請輸入複製檔案的名稱(可含副檔名):"))

path = pathlib.Path.cwd() / copyFile

if path.exists() == True:
    print("\n該檔名已存在")
else:
    is_Success = shutil.copyfile(file, copyFile)
    print("已複製完成檔案{}：".format(is_Success))

    is_Move = shutil.move(copyFile, "D:\\")
    print("並移動至該路徑：{}".format(is_Move))
