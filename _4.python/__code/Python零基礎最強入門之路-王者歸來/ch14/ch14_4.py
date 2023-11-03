# ch14_4.py
import os

print("檔案或資料夾存在 = ", os.path.exists('ch14'))
print("檔案或資料夾存在 = ", os.path.exists('D:\\Python\\ch14'))
print("檔案或資料夾存在 = ", os.path.exists('ch14_4.py'))
print(" --- ")

print("是絕對路徑 = ", os.path.isabs('ch14_4.py'))
print("是絕對路徑 = ", os.path.isabs('D:\\Python\\ch14\\ch14_4.py'))
print(" --- ")

print("是資料夾 = ", os.path.isdir('D:\\Python\\ch14\\ch14_4.py'))
print("是資料夾 = ", os.path.isdir('D:\\Python\\ch14'))
print(" --- ")

print("是檔案 = ", os.path.isfile('D:\\Python\\ch14\\ch14_4.py'))
print("是檔案 = ", os.path.isfile('D:\\Python\\ch14'))







