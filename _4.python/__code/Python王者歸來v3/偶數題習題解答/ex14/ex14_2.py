# ex14_2.py
import os

fn = input("請輸入檔案 : ")
if os.path.exists(fn):    
    print(fn, ":", os.path.getsize(fn))
else:
    print(fn,"檔案不存在")
    
    





    
