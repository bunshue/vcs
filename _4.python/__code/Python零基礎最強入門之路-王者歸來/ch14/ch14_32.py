# ch14_32.py
import shutil

shutil.copy('source.txt', 'dest.txt')       # 目前工作目錄檔案複製
shutil.copy('source.txt', 'D:\\Python')     # 目前工作目錄檔案複製至D:\Python
shutil.copy('D:\\Python\\source.txt', 'D:\\dest.txt') # 不同工作目錄檔案複製


