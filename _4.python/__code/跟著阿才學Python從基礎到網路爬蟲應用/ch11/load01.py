import json
f=open('product.json','r',encoding='utf_8')
pObj=json.load(f)	
f.close()
print("====== DTC商店 ======")
for product in pObj:
    for key in product:
        print(key, "：", product[key])
    print("="*20)
