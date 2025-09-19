#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: JSON读写
Desc :
"""
import json
from collections import OrderedDict


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def rw_json():
    data = {
        'name': 'ACME',
        'shares': 100,
        'price': 542.23
    }

    json_str = json.dumps(data)  # str类型
    data = json.loads(json_str)

    # Writing JSON data
    with open('data.json', 'w') as f:
        json.dump(data, f)

    # Reading data back
    with open('data.json', 'r') as f:
        data = json.load(f)

    # 使用object_pairs_hook
    s = '{"name": "ACME", "shares": 50, "price": 490.1}'
    data = json.loads(s, object_pairs_hook=OrderedDict)
    print(data)

    # 解码为自定义对象
    data = json.loads(s)

    print(json.dumps(data))
    print(json.dumps(data, indent=4))


if __name__ == '__main__':
    rw_json()

