import re
phoneList=["0412345678","(04)12345678","(04)-12345678","(049)2987654","0937-998877"]
pat = r'''
 \(\d{2,4}\)-?\d{6,8} #(04)12345678、(04)-12345678、(049)2987654 等電話格式
|\d{9,10}             #0412345678 等含 9~10 位數字
|\d{4}-\d{6,8}        #0937-998877 等手機格式
'''

for phone in phoneList:
    phoneNum = re.search(pat,phone,re.VERBOSE)
    if not phoneNum==None:
        print(phoneNum.group())