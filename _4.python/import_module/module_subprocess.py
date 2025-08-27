# 測試執行外部命令

import subprocess

print("------------------------------------------------------------")  # 60個

# cmd = 'svn propset svn:eol-style native "{}"'.format(path)
# cmd = 'calc.exe'    #可
# cmd = 'systeminfo' #不可
cmd = r"C:\_git\ims1\IMSCap\IMSCap\bin\Debug\IMSCap.exe"  # 可

propset = subprocess.Popen(cmd, shell=True)
propset.wait()

print("完成")


"""
import subprocess

ocr = subprocess.Popen("tesseract media\\text1.jpg media\\result", shell=True)
ocr.wait()

"""

print("------------------------------------------------------------")  # 60個

import subprocess

calcPro = subprocess.Popen("calc.exe")  # 傳回值是子行程
notePro = subprocess.Popen("notepad.exe")  # 傳回值是子行程
writePro = subprocess.Popen("write.exe")  # 傳回值是子行程
print(f"資料型態     = {type(calcPro)}")
print(f"列印calcPro  = {calcPro}")
print(f"列印notePro  = {notePro}")
print(f"列印writePro = {writePro}")

print("------------------------------------------------------------")  # 60個

import subprocess

filename = "D:/_git/vcs/_1.data/______test_files1/picture1.jpg"

paintPro = subprocess.Popen(["mspaint.exe", filename])
print(paintPro)

print("------------------------------------------------------------")  # 60個

import subprocess

path = r"C:\Users\User\AppData\Local\Programs\Python\Python311\python.exe"
pyPro = subprocess.Popen([path, "ch30_12.py"])
print(pyPro)

print("------------------------------------------------------------")  # 60個

import subprocess

filename1 = "D:/_git/vcs/_1.data/______test_files1/__RW/_txt/poetry.txt"
filename2 = "D:/_git/vcs/_1.data/______test_files1/picture1.jpg"

textPro = subprocess.Popen(["start", filename1], shell=True)
pictPro = subprocess.Popen(["start", filename2], shell=True)
print("文字檔案子行程 = ", textPro)
print("圖片檔案子行程 = ", pictPro)

print("------------------------------------------------------------")  # 60個

import subprocess

calcPro = subprocess.run("calc.exe")
print(f"資料型態     = {type(calcPro)}")
print(f"列印calcPro  = {calcPro}")

print("------------------------------------------------------------")  # 60個

import subprocess

ret = subprocess.run("echo %time%", shell=True, stdout=subprocess.PIPE)
print(f"資料型態       = {type(ret)}")
print(f"列印ret        = {ret}")
print(f"列印ret.stdout = {ret.stdout}")

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
