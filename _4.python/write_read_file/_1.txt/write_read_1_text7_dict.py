import ast

# 讀取文字檔後轉換為 dict
filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/python_password.txt'

data = dict()

with open(filename, 'r', encoding = 'UTF-8-sig') as f:
    filedata = f.read()
    if filedata != "":
        data = ast.literal_eval(filedata)

print(data)

print("帳號\t密碼")
print("================")
for key in data:
    print("{}\t{}".format(key, data[key]))

print('新增資料 2筆')
data['david'] = '12345678'
data['john'] = '88888888'

print("帳號\t密碼")
print("================")
for key in data:
    print("{}\t{}".format(key, data[key]))


print('檢查資料')


name = 'david'
if not name in data:
    print("{} 帳號不存在!".format(name))
else:
    print("{} 帳號存在!, 修改資料".format(name))
    data[name] = '3333'


name = 'alex'
if not name in data:
    print("{} 帳號不存在!".format(name))
else:
    print("{} 帳號存在!, 修改資料".format(name))
    data[name] = '3333'


print("帳號\t密碼")
print("================")
for key in data:
    print("{}\t{}".format(key, data[key]))

print('刪除資料')
name = 'david'
del data[name]

print("帳號\t密碼")
print("================")
for key in data:
    print("{}\t{}".format(key, data[key]))


filename2 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/python_password2222.txt'

print('將字典寫為檔案')
with open(filename2, 'w', encoding = 'UTF-8-sig') as f:
    f.write(str(data))
print("{}已被儲存完畢".format(name)) 
 
print("程式執行完畢！")
