#! /usr/bin/env python3

"Replace LF with CRLF in argument files.  Print names of changed files."

import sys, re, os

filename1 = 'C:/_git/vcs/_1.data/______test_files1/human2.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/poetry2.txt'
filename3 = 'C:/______test_files2'

filenames = [filename1, filename2, filename3]

for filename in filenames:
    if os.path.isdir(filename):
        print(filename, "Directory!")
        continue
    with open(filename, "rb") as f:
        data = f.read()
    if b'\0' in data:
        print(filename, "Binary!")
        continue
    newdata = re.sub(b"\r?\n", b"\r\n", data)
    if newdata != data:
        print(filename)
        with open(filename, "wb") as f:
            f.write(newdata)
