# 7-6-3 官方 pprint 範例

import json
from pprint import pprint
from urllib.request import urlopen

with urlopen('https://pypi.org/pypi/sampleproject/json') as resp:
    project_info = json.load(resp)['info']

pprint(project_info)