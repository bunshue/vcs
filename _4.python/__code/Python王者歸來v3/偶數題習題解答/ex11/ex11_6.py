# ex11_6.py
def guest_info(firstname, middlename, lastname, gender):
    """ 整合客戶名字資料 """
    if gender == "M":
        welcome = 'Mr. ' + firstname + middlename + lastname + 'Welcome'
    else:
        welcome = 'Miss ' + firstname + middlename + lastname + 'Welcome'
    return welcome

info1 = guest_info('Ivan ', 'Carl ', 'Hung ', 'M')
info2 = guest_info('Mary ', 'Ice ', 'Hung ', 'F')
print(info1)
print(info2)



