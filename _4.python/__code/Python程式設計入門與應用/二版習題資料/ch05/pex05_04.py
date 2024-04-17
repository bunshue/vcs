# Filename: pex05_04.py
def check_anagram(s1, s2):
    list_s1 = list(s1)
    list_s1.sort()
    list_s2 = list(s2)
    list_s2.sort()
    return (list_s1 == list_s2)

ps1 = input("請輸入第一個字串：")
ps2 = input("請輸入第二個字串：")
if (check_anagram(ps1,ps2)):
    print("輸入的二個字串是anagram")
else:
    print("輸入的二個字不是anagram")    