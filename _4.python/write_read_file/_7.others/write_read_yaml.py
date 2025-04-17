"""
pip install pyyaml

"""

import yaml

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("yaml 轉 字典")

filename = "data/yyyy.yaml"

with open(filename, "r") as f:
    # data = yaml.load(f)
    data = yaml.load(f, Loader=yaml.FullLoader)

print(yaml.dump(data))
print("---")
print(type(data))
print(data)
print("---")
print(data["name"])
print(data["age"])
print(data["sex"])
print(data["money"])

print("------------------------------------------------------------")  # 60個

print("字典 轉 yaml")

dddd = {"name": "Amy", "age": "20", "languages": ["English", "French"]}
print(type(dddd))

with open("tmp_yyyy.yaml", "w") as f:
    yaml.dump(dddd, f)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
