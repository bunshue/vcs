# ex11_10.py
def reverse(n):
    reverseN = 0
    while n != 0:
        r = n % 10
        reverseN = reverseN * 10 + r
        n //= 10
    return reverseN 

def isPalindrome(n):
    return n == reverse(n)
        
x = eval(input("請輸入1個數值 = "))
if isPalindrome(x):
    print("這是回文數")
else:
    print("這不是回文數")








