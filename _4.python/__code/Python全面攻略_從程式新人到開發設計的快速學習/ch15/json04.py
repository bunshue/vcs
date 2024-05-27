import json
listMeal=[{"編號":"A", "品名":"雙人分享餐", "單價":120},
          {"編號":"B", "品名":"歡樂全家餐", "單價":399},
          {"編號":"C", "品名":"情人精緻餐", "單價":540}]

f=open("meal.json","w",encoding="utf_8")

json.dump(listMeal, f,  ensure_ascii=False, indent=4)
f.close()
print("JSON餐點記錄建置完成")
