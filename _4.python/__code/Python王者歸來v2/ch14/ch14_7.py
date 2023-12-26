# ch14_7.py
import os

myfile = 'test.py'
# 如果myfile存在就刪除此檔案
if os.path.exists(myfile):
    os.remove(myfile)
    print(f"刪除 {myfile} 檔案成功")
else:
    print(f"{myfile} 檔案不存在")


