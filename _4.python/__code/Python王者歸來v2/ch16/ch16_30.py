# ch16_30.py
import re
msg = 'cat hat sat at matter flat'
pattern = '.at'           
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)




