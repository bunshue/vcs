# 程式 7-4.py (Python 3 version)
adict = {'book':10, 'pen':3, 'earser':6, 'ruler':2}

for key, value in adict.items():
    if value < 5:
      print("({},{})".format(key, value))

