# 測試執行外部命令

import sys
import subprocess

print("------------------------------------------------------------")  # 60個

# cmd = 'svn propset svn:eol-style native "{}"'.format(path)
# cmd = 'calc.exe'    #可
# cmd = 'systeminfo' #不可
cmd = r"C:\_git\ims1\IMSCap\IMSCap\bin\Debug\IMSCap.exe"  # 可

propset = subprocess.Popen(cmd, shell=True)
propset.wait()

"""
ocr = subprocess.Popen("tesseract media\\text1.jpg media\\result", shell=True)
ocr.wait()
"""
print("------------------------------------------------------------")  # 60個

# subprocess.Popen("data/vcs_test_pyautogui.exe")  # 打開應用程式
# subprocess.Popen("notepad.exe")  # 打開應用程式, 記事本

calcPro = subprocess.Popen("calc.exe")  # 傳回值是子行程
notePro = subprocess.Popen("notepad.exe")  # 傳回值是子行程
writePro = subprocess.Popen("write.exe")  # 傳回值是子行程
print(f"資料型態     = {type(calcPro)}")
print(f"列印calcPro  = {calcPro}")
print(f"列印notePro  = {notePro}")
print(f"列印writePro = {writePro}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "D:/_git/vcs/_1.data/______test_files1/picture1.jpg"

paintPro = subprocess.Popen(["mspaint.exe", filename])
print(paintPro)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

path = "C:/Users/User/AppData/Local/Programs/Python/Python311/python.exe"
pyPro = subprocess.Popen([path, "ch30_12.py"])
print(pyPro)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename1 = "D:/_git/vcs/_1.data/______test_files1/__RW/_txt/poetry.txt"
filename2 = "D:/_git/vcs/_1.data/______test_files1/picture1.jpg"

textPro = subprocess.Popen(["start", filename1], shell=True)
pictPro = subprocess.Popen(["start", filename2], shell=True)
print("文字檔案子行程 = ", textPro)
print("圖片檔案子行程 = ", pictPro)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

calcPro = subprocess.run("calc.exe")
print(f"資料型態     = {type(calcPro)}")
print(f"列印calcPro  = {calcPro}")

print("------------------------------------------------------------")  # 60個

ret = subprocess.run("echo %time%", shell=True, stdout=subprocess.PIPE)
print(f"資料型態       = {type(ret)}")
print(f"列印ret        = {ret}")
print(f"列印ret.stdout = {ret.stdout}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 通過subprocess模塊的call函數啟動子進程
process_name = "notepad"
status = subprocess.call(process_name)

# subprocess.call(["ipython", "trust", fullpath, "--profile", "scipybook2"])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 強制讓目前執行這個程式的 Python 環境去安裝套件
subprocess.check_call([sys.executable, "-m", "pip", "install", "currency_converter"])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

# 6060
print("------------------------------------------------------------")  # 60個
# 3030
print("------------------------------")  # 30個
# 1515
print("---------------")  # 15個
