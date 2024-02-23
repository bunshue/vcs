import json
listProduct=[
	  {"編號":"P01", "品名":"五香豆干", "單價":89} ,
	  {"編號":"P02", "品名":"龍哥可樂", "單價":20} ,
	  {"編號":"P03", "品名":"阿才紅茶", "單價":15}
    ]
f=open("product.json","w",encoding="utf_8")
json.dump(listProduct, f ,ensure_ascii=False, indent=4)
f.close()
print("JSON產品資料存檔成功")
