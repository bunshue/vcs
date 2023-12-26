# ch6_42.py
msg = '''CIA Mark told CIA Linda that the secret USB had given to CIA Peter'''
print(f"字串開頭是CIA : {msg.startswith('CIA')}")
print(f"字串結尾是CIA : {msg.endswith('CIA')}")
print(f"CIA出現的次數 : {msg.count('CIA')}")
msg = msg.replace('Linda','Lxx')
print(f"新的msg內容 : {msg}")





