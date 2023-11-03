# ch14_6.py
import os

mydir = 'testch14'
# 如果mydir存在就刪除此資料夾
if os.path.exists(mydir):
    os.rmdir(mydir)
    print("刪除 %s 資料夾成功" % mydir)
else:
    print("%s 資料夾不存在" % mydir)


