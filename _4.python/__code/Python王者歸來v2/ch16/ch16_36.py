# ch16_36.py
import re
#測試1取代使用re.sub()結果成功
msg = 'Eli Nan will attend my party tonight. My best friend is Eli Nan'  
pattern = 'Eli Nan'                 # 欲搜尋字串        
newstr = 'Kevin Thomson'            # 新字串
txt = re.sub(pattern,newstr,msg)    # 如果找到則取代
if txt != msg:                      # 如果txt與msg內容不同表示取代成功
    print("取代成功: ", txt)        # 列出成功取代結果
else:
    print("取代失敗: ", txt)        # 列出失敗取代結果
#測試2取代使用re.sub()結果失敗  
pattern = 'Eli Thomson'             # 欲搜尋字串        
txt = re.sub(pattern,newstr,msg)    # 如果找到則取代           
if txt != msg:                      # 如果txt與msg內容不同表示取代成功
    print("取代成功: ", txt)        # 列出成功取代結果
else:
    print("取代失敗: ", txt)        # 列出失敗取代結果



