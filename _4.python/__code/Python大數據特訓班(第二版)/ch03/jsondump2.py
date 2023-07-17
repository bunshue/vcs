import json
with open('class_str.json', 'r', encoding='utf-8') as f:
    datas = json.load(f)
with open('new_class_str.json', 'w', encoding='utf-8') as f:
    dumpdata = json.dump(datas, f, ensure_ascii=False)