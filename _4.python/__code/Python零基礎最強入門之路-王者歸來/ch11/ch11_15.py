# ch11_15.py
def guest_info(firstname, lastname, gender, middlename = ''):
    """ 整合客戶名字資料 """
    if gender == "M":
        welcome = lastname + middlename + firstname + '先生歡迎你'
    else:
        welcome = lastname + middlename + firstname + '小姐歡迎妳'
    return welcome

info1 = guest_info('濤', '劉', 'M')
info2 = guest_info('雨', '洪', 'F', '冰')
print(info1)
print(info2)



