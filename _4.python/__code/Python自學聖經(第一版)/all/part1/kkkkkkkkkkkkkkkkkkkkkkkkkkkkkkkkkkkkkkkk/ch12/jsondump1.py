import json
with open('class_str.json', 'r', encoding='utf-8') as f:
    datas = json.load(f)
print(datas, type(datas))
dumpdata = json.dumps(datas, ensure_ascii=False)
print(dumpdata, type(dumpdata))