import os
filePath = input("請輸入檔案或路徑：")	# 輸入檔案或路徑
show = "不存在，可能檔案或路徑有誤"
if os.path.exists(filePath):				# 判斷檔案或路徑是否存在
   show = "存在"
print("%s %s" %(filePath, show))
