# coding: utf-8
try:
    fp = open("myfile.txt", "r")
    print(fp.read())
    fp.close()
except FileNotFoundError:
    print("錯誤! myfile.txt檔案不存在!")
