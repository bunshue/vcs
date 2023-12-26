# ch16_21.py
import re

def searchStr(pattern, msg):
    txt = re.search(pattern, msg)
    if txt == None:         # 搜尋失敗
        print("搜尋失敗 ",txt)
    else:                   # 搜尋成功
        print("搜尋成功 ",txt.group())

msg = 'sonsonsonsonson'
pattern = '(son){3,5}'
searchStr(pattern,msg)


    
