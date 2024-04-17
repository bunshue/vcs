# Filename: pex04_03.py
ps1 = input("請輸入第一個字串：")
ps2 = input("請輸入第二個字串：")
list_ps1 = list(ps1)
list_ps1.sort()
list_ps2 = list(ps2)
list_ps2.sort()
if (list_ps1 == list_ps2):
    print("輸入的二個字串是anagram")
else:
    print("輸入的二個字串不是anagram")    