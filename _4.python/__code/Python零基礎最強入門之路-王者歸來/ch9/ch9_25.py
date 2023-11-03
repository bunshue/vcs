# ch9_25.py
# 建立內含字串的字典
sports = {'Curry':['籃球', '美式足球'],
          'Durant':['棒球'],
          'James':['美式足球', '棒球', '籃球']}
# 列印key名字 + 字串'喜歡的運動'
for name, favorite_sport in sports.items( ):
          print("%s 喜歡的運動是: " % name)
# 列印value,這是串列
          for sport in favorite_sport:
              print("   ", sport)

