"""
os模組
os.getcwd()
os.listdir()
os.mkdir()	建立目錄
os.chdir()	切換目錄
os.rmdir()	刪除目錄
os.remove()	刪除檔案
os.rename()	更名目錄/檔案


os.getpid()

"""

import os

print("------------------------------------------------------------")  # 60個

print("取得環境變數")

"""用法
os.getenv(key, default = None)
"""

print("key存在")
key = "HOME"
value = os.getenv(key)
print("取得 :", value)

print("key不存在")
value = os.getenv("OPENAI_API_KEY")
print("取得 :", value)

print("key不存在, 使用預設值")
value = os.getenv("OPENAI_API_KEY", "抱歉, API key不存在")
print("取得 :", value)

print("預設環境變數")

key = "TEMP"
value = os.getenv(key)
print("TEMP取得 :", value)

key = "TMP"
value = os.getenv(key)
print("TMP取得 :", value)

key = "PATH"
value = os.getenv(key)
print("PATH取得 :", value)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


"""
user = 'uid %s' % os.getuid()

import os
print(os.getpid())

userhome = os.environ['HOME']
print(userhome)
userhome = os.fsencode(userhome)
print(userhome)

os.getcwd()

"""

