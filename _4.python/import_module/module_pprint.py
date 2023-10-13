# import pprint

print('------------------------------------------------------------')	#60個

import json
from pprint import pprint
from urllib.request import urlopen

with urlopen('https://pypi.org/pypi/sampleproject/json') as resp:
    project_info = json.load(resp)['info']

pprint(project_info)

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個
