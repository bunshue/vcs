import json

listScore = [89, 100, 23, 78, 89]
print("listScore串列：" , listScore)
print("listScore型別：", type(listScore))

jsonScore = json.dumps(listScore)
print("jsonScore字串：", jsonScore)
print("jsonScore型別：", type(jsonScore))


dictEmp = {"編號":"P01", "品名":"五香豆干", "單價":89}
print("dictEmp字典：", dictEmp)
print("dictEmp型別：", type(dictEmp))

jsonEmp = json.dumps(dictEmp, ensure_ascii=False)
print("jsonEmp字串：", jsonEmp)
print("jsonEmp型別：", type(jsonEmp))
 


