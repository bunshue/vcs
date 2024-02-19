import os
import sys
import time
import random


print("------------------------------------------------------------")  # 60個

# 使用 json.dumps() 美觀列印 dict

import json

animals = {
    "鼠": 3,
    "牛": 48,
    "虎": 33,
    "兔": 8,
    "龍": 38,
    "蛇": 16,
}

print(type(animals))

print(json.dumps(animals, indent=4, sort_keys=True))


print("------------------------------------------------------------")  # 60個

import pathlib


HERE = pathlib.Path(__file__).resolve().parent

print(HERE)

cc = pathlib.Path
print(cc)

cc = pathlib.Path.home() / ".pydicom"

print(cc)
print('------------------------------------------------------------')	#60個



import pathlib
cur_path = pathlib.Path(".")
FILE_PATTERN = "*.txt"
path_list = cur_path.glob(FILE_PATTERN)
print(list(path_list))
#[PosixPath('item_attributes.txt'), PosixPath('related_items.txt'), PosixPath('item_info.txt')]

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個








print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

