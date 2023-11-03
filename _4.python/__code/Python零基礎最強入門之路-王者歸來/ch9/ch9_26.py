# ch9_26.py
# 建立內含字典的字典
wechat_account = {'cshung':{
                        'last_name':'洪',
                        'first_name':'錦魁',
                        'city':'台北'},
                  'kevin':{
                        'last_name':'鄭',
                        'first_name':'義盟',
                        'city':'北京'}}
# 列印內含字典的字典
for account, account_info in wechat_account.items( ):
    print("使用者帳號 = ", account)                   # 列印鍵(key)
    name = account_info['last_name'] + " " + account_info['first_name']
    print("姓名       = ", name)                      # 列印值(value)
    print("城市       = ", account_info['city'])      # 列印值(value)

