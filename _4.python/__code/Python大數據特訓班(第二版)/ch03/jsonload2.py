import json
with open('class_str.json', 'r', encoding='utf-8') as f:
    datas = json.load(f)
    print(type(datas))
    for data in datas["一年甲班"]:
        print(data, data['姓名'])