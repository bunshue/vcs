# ch30_33.py
import subprocess

txtPro = subprocess.Popen(['start', 'trip.txt'], shell=True)
pictPro = subprocess.Popen(['start', 'book.jpg'], shell=True)
m4vPro = subprocess.Popen(['start', 'pegiun.m4v'], shell=True)
print("txt檔案子行程  = ", txtPro)
print("pict檔案子行程 = ", pictPro)
print("m4v檔案子行程  = ", m4vPro)



