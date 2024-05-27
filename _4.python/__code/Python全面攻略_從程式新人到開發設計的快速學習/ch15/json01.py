import json
dictMeal={"編號":"A", "品名":"雙人分享餐", "單價":120}
jsonStr=json.dumps(dictMeal, ensure_ascii=False, indent=4)
print(jsonStr)

