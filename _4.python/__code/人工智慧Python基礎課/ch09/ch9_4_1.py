# coding: utf-8
fp = open("temp\\note.txt", "w")
if fp != None:
    print("檔案開啟成功!")
fp.write("陳會安\n")
fp.write("Python")
fp.write("程式設計\n")
fp.close()
