
'''
print('用預設瀏覽器開啟網頁')

import webbrowser

filename = 'C:/_git/vcs/_1.data/______test_files1/beautifulsoup_data.html'

webbrowser.open(filename)
'''


import sys

usage = """Usage: %s [-cd] paths...
    -c: recognize Python source files trying to compile them
    -d: debug output""" % sys.argv[0]

print('msgsssssss', file=sys.stderr)
print(usage, file=sys.stderr)

import os

def walk_python_files(paths):
    for path in paths:
        if os.path.isfile(path):
            print(path)
        elif os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for filename in files:
                    if filename.endswith(".csv"):
                        print(filename)

foldername1 = 'C:/_git/vcs/_1.data/______test_files1'

paths = [foldername1]
walk_python_files(paths)



