"""
對python檔案做black
"""

import os
import sys
import time
import datetime

print("------------------------------------------------------------")  # 60個

cmd = "black python07_check_python_files.py"
tmp_filename = "C:/_git/vcs/_big_files/tmp_black_mesg.txt"

ret = os.system(cmd + " 2>" + tmp_filename)
if ret == 0:
    with open(tmp_filename, "r") as file:
        print(file.read())
else:
    print("black 失敗")

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
