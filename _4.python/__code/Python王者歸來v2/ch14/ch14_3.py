# ch14_3.py
import os

print(os.path.relpath('D:\\'))              # 列出目前工作目錄至D:\的相對路徑
print(os.path.relpath('D:\\Python\\ch13'))  # 列出目前工作目錄至特定path的相對路徑
print(os.path.relpath('D:\\', 'ch14_3.py')) # 列出目前檔案至D:\的相對路徑






