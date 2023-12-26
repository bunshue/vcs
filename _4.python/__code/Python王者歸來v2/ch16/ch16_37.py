# ch16_37.py
import re
# 使用隱藏文字執行取代
msg = 'CIA Mark told CIA Linda that secret USB had given to CIA Peter.'
pattern = r'CIA (\w)\w*'            # 欲搜尋CIA + 空一格後的名字        
newstr = r'\1***'                   # 新字串使用隱藏文字
txt = re.sub(pattern,newstr,msg)    # 執行取代
print("取代成功: ", txt)            # 列出取代結果


