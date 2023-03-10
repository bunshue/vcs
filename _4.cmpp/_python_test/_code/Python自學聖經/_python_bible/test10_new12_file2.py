# Python 新進測試 12

import glob
files = glob.glob("glob.py") + glob.glob("os*.py") + glob.glob("*.txt") 
for file in files:
    print(file)

import os,shutil
cur_path=os.path.dirname(__file__) # 取得目前路徑
print("現在路徑："+cur_path)
destfile= cur_path + "\\__temp\\" + "ccccc.py"
print("拷貝檔案 " + destfile)
shutil.copy("test10_new10.py",destfile )  # 檔案複製
print("拷貝檔案 " + destfile)
shutil.copyfile("test10_new10.py","__temp\\test10_new10_cpd.py" )  # 檔案複製


'''
print("刪除目錄, 直接刪除, 不會放入資源回收筒")
import shutil
shutil.rmtree("C:\\dddddddddd\\aaa" )  # 刪除目錄
'''

'''
#import ast
import json
data = dict()
with open('data\password.txt','r', encoding = 'UTF-8-sig') as f:
   filedata = f.read()
   print(filedata)
#   filedata = filedata.replace("\'", "\"")
#   data = ast.literal_eval(filedata)
   data = json.loads(filedata)

print(type(data),data)

'''

