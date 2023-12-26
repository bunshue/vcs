# ch6_51.py
password = 'deepmind'
ch = input("請輸入字元 = ")
print("in運算式")
if ch in password:
    print("輸入字元在密碼中")
else:
    print("輸入字元不在密碼中")
    
print("not in運算式")
if ch not in password:
    print("輸入字元不在密碼中")
else:
    print("輸入字元在密碼中")
        
