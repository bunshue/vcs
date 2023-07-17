import os,shutil
cur_path=os.path.dirname(__file__) # 取得目前路徑
destfile= cur_path + "\\" + "newfile.py"
shutil.copy("shutil.py",destfile )  # 檔案複製
shutil.copyfile("shutil.py","D:\\new.py" )  # 檔案複製