import os
import sys

import getopt

length = len(sys.argv)
print('參數長度 : ', length);
for i in range (0, length):
    print(sys.argv[i])

if len(sys.argv) > 1:
    files = sys.argv[1:]
print(files)



opts, args = getopt.getopt(sys.argv[1:], "h:c:")
if len(opts) != 1:
    sys.stdout.write("Must specify exactly one output file\n")
    sys.exit(1)
for o, v in opts:
    if o == '-h':
        INC_DIR = v
    if o == '-c':
        SRC_DIR = v
if len(args) != 1:
    sys.stdout.write("Must specify single input file\n")
    sys.exit(1)

print(args[0])
















