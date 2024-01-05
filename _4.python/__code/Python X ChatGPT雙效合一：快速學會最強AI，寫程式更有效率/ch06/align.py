str1 = 'Python is funny and powerful'
print('原字串', str1)
print('欄寬40，字串置中', str1.center(40))
print('字串置中，* 填補', str1.center(40, '*'))
print('欄寬10，字串靠左', str1.ljust(40, '='))
print('欄寬40，字串靠右', str1.rjust(40, '#'))

mobilephone = '931666888'
print('字串左側補0:', mobilephone.zfill(10))

str2 = 'Mayor,President'
print('以逗點分割字元', str2.partition(','))

str3 = '禮\n義\n廉\n恥'
print('依\\n分割字串', str3.splitlines(False))
