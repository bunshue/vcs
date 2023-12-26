# ch16_34.py
import re
#測試1搜尋使用re.match()
msg = 'John will attend my party tonight.'  
pattern = 'John'
txt = re.match(pattern,msg)                 # re.match()
if txt != None:
    print("使用re.match()輸出MatchObject物件:  ", txt)
else:
    print("測試1搜尋失敗")
#測試1搜尋使用re.search()
txt = re.search(pattern,msg)                # re.search()
if txt != None:
    print("使用re.search()輸出MatchObject物件: ", txt)
else:
    print("測試1搜尋失敗")






