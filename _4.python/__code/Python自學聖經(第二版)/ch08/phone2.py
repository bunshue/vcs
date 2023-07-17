import re
numStr="tel:(04)12345678"
pat = r'(\(\d{2}\))(\d{8})'

phone = re.search(pat,numStr)
if not phone==None:
    print(phone.group())  #(04)12345678
    print(phone.group(1)) #(04)
    print(phone.group(2)) #12345678