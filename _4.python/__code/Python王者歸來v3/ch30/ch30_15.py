# ch30_15.py
import subprocess

txtPro = subprocess.Popen(['start', 'trip.txt'], shell=True)
pictPro = subprocess.Popen(['start', 'book.jpg'], shell=True)
print("txt檔案子行程  = ", txtPro)
print("pict檔案子行程 = ", pictPro)




