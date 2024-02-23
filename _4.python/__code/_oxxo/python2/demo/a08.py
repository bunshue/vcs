# encoding:UTF-8

while(True):
    a = input('請輸入簡單的數學式：')
    answer = '你輸入的不是數字呦～'
    if('+' in a):
        p = a.split('+')
        if(p[0].isdigit() and p[1].isdigit()):
            answer = int(p[0]) + int(p[1])
    elif('-' in a):
        p = a.split('-')
        if(p[0].isdigit() and p[1].isdigit()):
            answer = int(p[0]) - int(p[1])
    elif('/' in a):
        p = a.split('/')
        if(p[0].isdigit() and p[1].isdigit()):
            answer = int(p[0]) / int(p[1])
    elif('*' in a):
        p = a.split('*')
        if(p[0].isdigit() and p[1].isdigit()):
            answer = int(p[0]) * int(p[1])
    print(answer)
