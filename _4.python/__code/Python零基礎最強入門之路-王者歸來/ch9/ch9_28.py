# ch9_28.py
# 建立內含字典的字典
wechat_account = {'cshung':{
                        'last_name':'洪',
                        'first_name':'錦魁',
                        'city':'台北'},
                  'kevin':{
                        'last_name':'鄭',
                        'first_name':'義盟',
                        'city':'北京'}}
# 列印字典元素個數
print("wechat_account字典元素個數       ", len(wechat_account))
print("wechat_account['cshung']元素個數 ", len(wechat_account['cshung']))
print("wechat_account['kevin']元素個數  ", len(wechat_account['kevin']))
