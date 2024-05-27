import json
jsonStr='{"編號":"A", "品名":"雙人分享餐", "單價":120}'

dictMeal=json.loads(jsonStr)

print("編號：%s"%(dictMeal["編號"]))
print("品名：%s"%(dictMeal["品名"]))
print("單價：%d"%(dictMeal["單價"]))

