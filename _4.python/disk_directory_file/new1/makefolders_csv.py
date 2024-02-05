import pathlib

foldername = 'C:/_git/vcs/_1.data/______test_files5'


msg = ""
pathlib.Path(foldername).mkdir(exist_ok=True)   #建立轉存檔案的資料夾

name = "AAAA"
newfolder = pathlib.Path(foldername).joinpath(name)
newfolder.mkdir(exist_ok=True)  #建立資料夾
msg = "在" + foldername + "建立了" + name + "了。"
print(msg)

name = "BBBB"
newfolder = pathlib.Path(foldername).joinpath(name)
newfolder.mkdir(exist_ok=True)  #建立資料夾
msg = "在" + foldername + "建立了" + name + "了。"
print(msg)

name = "CCCC"
newfolder = pathlib.Path(foldername).joinpath(name)
newfolder.mkdir(exist_ok=True)  #建立資料夾
msg = "在" + foldername + "建立了" + name + "了。"
print(msg)



