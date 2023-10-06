# 7-6-1 使用 json.dumps() 美觀列印 dict

import json

config = {
    'lang': 'Python',
    'version': [3.6, 3.7, 3.8],
    'date': '2019-10-14',
    'platform': 'linux',
    'org': 'Python Software Foundation',
    'config_status': 0xc0ffee,
    'the_answer': 42
    }

print(json.dumps(config, indent=4, sort_keys=False))