# ch6_44.py
mysports = ['basketball', 'baseball']
friendsports = mysports[:]
print("列出mysports位址     = ", id(mysports))
print("列出friendsports位址 = ", id(friendsports))
print("我喜歡的運動     = ", mysports)
print("我朋友喜歡的運動 = ", friendsports)
mysports.append('football')
friendsports.append('soccer')
print(" -- 新增運動項目後 -- ")
print("列出mysports位址     = ", id(mysports))
print("列出friendsports位址 = ", id(friendsports))
print("我喜歡的最新運動     = ", mysports)
print("我朋友喜歡的最新運動 = ", friendsports)
                   
