# ch14_7.py
import os

myfile = 'test.py'
# 如果myfile存在就刪除此檔案
if os.path.exists(myfile):
    os.remove(myfile)
    print("刪除 %s 檔案成功" % myfile)
else:
    print("%s 檔案不存在" % myfile)


