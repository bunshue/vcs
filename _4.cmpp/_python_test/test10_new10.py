import os

PATH = "/".join(os.path.abspath(__file__).split("/")[:-2])

#sys.path.append(PATH)
print(PATH)

import os

print(os.environ.get("CI_COMMIT_TAG", "0.0.0"))
_version = os.environ.get("CI_COMMIT_TAG", "0.0.1.dev2")


'''here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()
'''

import time
def get_time():
    return time.strftime("%Y/%m/%d %A %H:%M:%S", time.localtime(time.time()))

localtime = get_time()
print('現在時間 : ' + localtime)


import time
print("現在時間")
localtime = time.strftime("%Y/%m/%d %A %H:%M:%S", time.localtime(time.time()))
print('現在時間 : ' + localtime)



print(__name__)
#print(__name__._version)


