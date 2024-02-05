import pathlib

print("搜尋資料夾內所有檔名符合特定字串的檔案")

foldername = 'C:/_git/vcs/_1.data/______test_files1'
value1 = "vcs_R"

#【函數：確認在資料夾的檔案名稱是否包含特定字串】
def findfilename(foldername, findword):
    cnt = 0
    msg = ""
    filelist = []
    for p in pathlib.Path(foldername).rglob("*.*"):   #將這個資料夾以及子資料夾的所有檔案
        if p.name[0] != ".":                #沒有隱藏檔案的話
            filelist.append(str(p))         #新增至列表
    for filename in sorted(filelist):       #再替每個檔案排序
        if filename.count(findword) > 0:    #如果找到1個以上的特定字串
            msg += filename + "\n"
            cnt += 1
    msg = "檔案個數 = " + str(cnt) + "\n" + msg
    return msg

#【執行函數】
msg = findfilename(foldername, value1)
print(msg)
