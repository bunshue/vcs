# ex8_4.py
import hashlib

school = input('請輸入學校名稱 : ')
data = hashlib.md5()                                # 建立data物件
data.update(school.encode('utf-8'))                 # 更新data物件內容
print('Hash Value(16進位) = ', data.hexdigest())









