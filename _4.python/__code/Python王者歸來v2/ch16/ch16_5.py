# ch16_5.py
import re

msg1 = 'Please call my secretary using 0930-919-919 or 0952-001-001'
msg2 = '請明天17:30和我一起參加明志科大教師節晚餐'
msg3 = '請明天17:30和我一起參加明志科大教師節晚餐, 可用0933-080-080聯絡我'

def parseString(string):
    """解析字串是否含有電話號碼"""
    pattern = r'\d\d\d\d-\d\d\d-\d\d\d'
    phoneNum = re.search(pattern, string)
    if phoneNum != None:        # 如果phoneNum不是None表示取得號碼
        print(f"電話號碼是: {phoneNum.group()}")
    else:
        print(f"{string} 字串不含電話號碼")

parseString(msg1)
parseString(msg2)
parseString(msg3)


