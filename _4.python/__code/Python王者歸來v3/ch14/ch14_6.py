# ch14_6.py
import os

mydir = 'test'
# 如果mydir不存在就建立此資料夾
if os.path.exists(mydir):
    print(f"{mydir} 已經存在")
else:
    os.mkdir(mydir)
    print(f"建立 {mydir} 資料夾成功")








