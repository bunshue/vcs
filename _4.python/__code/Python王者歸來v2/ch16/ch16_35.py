# ch16_35.py
import re
#測試1搜尋使用re.match()
msg = 'John will attend my party tonight.'  
pattern = 'John'
txt = re.match(pattern,msg)                 # re.match()
if txt != None:
    print("搜尋成功字串的起始索引位置 :  ", txt.start())
    print("搜尋成功字串的結束索引位置 :  ", txt.end())
    print("搜尋成功字串的結束索引位置 :  ", txt.span())
#測試2搜尋使用re.search()
msg = 'My best friend is John.'  
txt = re.search(pattern,msg)                # re.search()
if txt != None:
    print("搜尋成功字串的起始索引位置 :  ", txt.start())
    print("搜尋成功字串的結束索引位置 :  ", txt.end())
    print("搜尋成功字串的結束索引位置 :  ", txt.span())








