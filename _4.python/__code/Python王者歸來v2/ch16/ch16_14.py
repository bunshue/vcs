# ch16_14.py
import re

msg = 'Johnson, Johnnason and Johnnathan will attend my party tonight.'
pattern = 'John(son|nason|nathan)'
txts = re.findall(pattern,msg)      # 傳回搜尋結果
print(txts)
for txt in txts:                    # 將搜尋到內容加上John
    print('John'+txt)


    
