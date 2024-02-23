import json
fruit={'banana':'香蕉','papaya':'木瓜','apple':'蘋果'}
print(json.dumps(fruit,ensure_ascii=False))
print(json.dumps(fruit,ensure_ascii=False,sort_keys=True))
print(json.dumps(fruit,ensure_ascii=False,sort_keys=True, indent=4))



 


