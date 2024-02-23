# ch8_3.py
def check_name(name):
    if voted[name]:
        print('你已經投過票了')
    else:
        print('歡迎投票')
        voted[name] = True

voted = {'Trump':None,
         'Lisa':None,
         'Mike':None}

name = input('請輸入名字 : ')
if name in voted:
    check_name(name)
else:
    print('你不是選民')
