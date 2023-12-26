# ch6_50.py
msg = '''CIA Mark told CIA Linda that the secret USB had given to CIA Peter'''
print("字串開頭是CIA: ", msg.startswith("CIA"))
print("字串結尾是CIA: ", msg.endswith("CIA"))
print("CIA出現的次數: ",msg.count("CIA"))
msg = msg.replace('Linda','Lxx')
print("新的msg內容 : ", msg)





