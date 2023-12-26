# ch6_55.py
mysports = ['basketball', 'baseball']
sports1 = mysports          # 賦值
sports2 = mysports[:]       # 切片拷貝新串列
print(f"我喜歡的運動 = {mysports}", f"位址是 = {id(mysports)}")
print(f"運動 1       = {sports1}", f"位址是 = {id(sports1)}")
print(f"運動 2       = {sports2}", f"位址是 = {id(sports2)}")
bool_value = mysports is sports1
print("我喜歡的運動 is 運動 1     = ", bool_value)

bool_value = mysports is sports2
print("我喜歡的運動 is 運動 2     = ", bool_value)

bool_value = mysports is not sports1
print("我喜歡的運動 is not 運動 1 = ", bool_value)

bool_value = mysports is not sports2
print("我喜歡的運動 is not 運動 2 = ", bool_value)


