# ch16_23.py
import re
# 測試1將字串從句子分離
msg = 'John, Johnson, Johnnason and Johnnathan will attend my party tonight.'
pattern = '\w+'                    # 不限長度的單字
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試2將John開始的字串分離
msg = 'John, Johnson, Johnnason and Johnnathan will attend my party tonight.'
pattern = 'John\w*'                # John開頭的單字
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)

    
