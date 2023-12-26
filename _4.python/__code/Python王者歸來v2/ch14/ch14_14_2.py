# ch14_4_2.py
import os
import stat

fn = "ch14_4_1.txt"
os.chmod(fn, stat.S_IXGRP)
os.chmod(fn, stat.S_IWOTH)
print("更改成功了")


