# ch9_29.py
# 將串列轉成字典
seq1 = ['name', 'city']         # 定義串列
list_dict1 = dict.fromkeys(seq1)
print("字典1 ", list_dict1)
list_dict2 = dict.fromkeys(seq1, 'Chicago')
print("字典2 ", list_dict2)
# 將元組轉成字典
seq2 = ('name', 'city')         # 定義元組
tup_dict1 = dict.fromkeys(seq2)
print("字典3 ", tup_dict1)
tup_dict2 = dict.fromkeys(seq2, 'New York')
print("字典4 ", tup_dict2)

