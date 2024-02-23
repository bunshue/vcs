# ex8_2.py
def check_name(name):
    if voted.get(name):
        print('你已經投過票了')           
    else:
        print('歡迎投票')
        voted[name] = True     

voted = {}                  # 建立選民名單

name = input('請輸入名字 : ')
check_name(name)
