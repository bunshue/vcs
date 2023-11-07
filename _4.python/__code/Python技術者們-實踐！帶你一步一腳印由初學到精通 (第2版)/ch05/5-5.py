import re # 使用前要先匯入 re 模組
print(re.match (r'pyt', 'python')) # pyt 由開頭即符合, 因此成功
print(re.match (r'yth', 'python')) # yth 與開頭不符合, 因此失敗
print(re.search(r'yth', 'python')) # seach( ) 不限開頭, 因此成功