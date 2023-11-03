# ch6_46.py
mysports = ['basketball', 'baseball']
sports1 = mysports          # 拷貝位址
sports2 = mysports[:]       # 拷貝新串列
print("我喜歡的運動 = ", mysports, "位址是 = ", id(mysports))
print("運動 1       = ", sports1,  "位址是 = ", id(sports1))
print("運動 2       = ", sports2,  "位址是 = ", id(sports2))
boolean_value = mysports is sports1
print("我喜歡的運動 is 運動 1     = ", boolean_value)

boolean_value = mysports is sports2
print("我喜歡的運動 is 運動 2     = ", boolean_value)

boolean_value = mysports is not sports1
print("我喜歡的運動 is not 運動 1 = ", boolean_value)

boolean_value = mysports is not sports2
print("我喜歡的運動 is not 運動 2 = ", boolean_value)
