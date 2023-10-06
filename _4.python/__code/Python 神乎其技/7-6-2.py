# 7-6-2 使用 pprint 美觀列印 dict

from pprint import pprint

config = {
    'lang': 'Python',
    'version': [3.6, 3.7, 3.8],
    'date': '2019-10-14',
    'platform': 'linux',
    'org': 'Python Software Foundation',
    'config_status': 0xc0ffee,
    'the_answer': 42
    }

pprint(config, indent=4, sort_dicts=False)
