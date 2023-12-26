# ex11_12.py
def isPalindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[len(s)-1]:
        return False
    else:
        return isPalindrome(s[1:len(s)-1])

string = input("請輸入字串 : ")
if isPalindrome(string):
    print(f"{string} 是回文字串")
else:
    print(f"{string} 不是回文字串")





