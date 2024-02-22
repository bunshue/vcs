import os
import sys
import time
import getopt

print('------------------------------------------------------------')	#60個

length = len(sys.argv)
print('參數長度 : ', length);
for i in range (0, length):
    print(sys.argv[i])

if len(sys.argv) > 1:
    files = sys.argv[1:]
    print(files)

print('------------------------------------------------------------')	#60個

prog = sys.argv[0]
print(prog)

print('------------------------------------------------------------')	#60個

opts, args = getopt.getopt(sys.argv[1:], "h:c:")
if len(opts) != 1:
    sys.stdout.write("Must specify exactly one output file\n")

for o, v in opts:
    if o == '-h':
        INC_DIR = v
    if o == '-c':
        SRC_DIR = v
if len(args) != 1:
    sys.stdout.write("Must specify single input file\n")

if len(opts) > 0:
    print(args[0])

print('------------------------------------------------------------')	#60個

import sys, os

import getopt
inplace = False
backup = False
opts, args = getopt.getopt(sys.argv[1:], "ib:")
for o, a in opts:
    if o == '-i':
        inplace = True
    if o == '-b':
        backup = a


def errprint(*args):
    sep = ""
    for arg in args:
        sys.stderr.write(sep + str(arg))
        sep = " "
    sys.stderr.write("\n")

#global verbose, filename_only
try:
    opts, args = getopt.getopt(sys.argv[1:], "qv")
except getopt.error as msg:
    errprint(msg)
for o, a in opts:
    if o == '-q':
        filename_only = filename_only + 1
    if o == '-v':
        verbose = verbose + 1
if not args:
    errprint("Usage:", sys.argv[0], "[-v] file_or_directory ...")
for arg in args:
    #check(arg)
    print(arg)

print('------------------------------------------------------------')	#60個

import getopt

try:
    opts, args = getopt.getopt(args, "n:s:r:tcpvh",
                               ["number=", "setup=", "repeat=",
                                "time", "clock", "process",
                                "verbose", "help"])
except getopt.error as err:
    print(err)
    print("use -h/--help for command line help")


print('aaaaaaaaaaaaaaaaaaaaaa')

timer = time.time
stmt = "\n".join(args) or "pass"
number = 0 # auto-determine
setup = []
repeat = 5
verbose = 0
precision = 3
for o, a in opts:
    if o in ("-n", "--number"):
        number = int(a)
    if o in ("-s", "--setup"):
        setup.append(a)
    if o in ("-r", "--repeat"):
        repeat = int(a)
        if repeat <= 0:
            repeat = 1
    if o in ("-t", "--time"):
        timer = time.time
    if o in ("-c", "--clock"):
        timer = time.clock
    if o in ("-p", "--process"):
        timer = time.process_time
    if o in ("-v", "--verbose"):
        if verbose:
            precision += 1
        verbose += 1
    if o in ("-h", "--help"):
        print(__doc__, end=' ')


print('ccccccc')

print('------------------------------------------------------------')	#60個

import argparse
cmdline = argparse.ArgumentParser()
print(cmdline)

cmdline.add_argument("-f", "--force", action='store_true')
cmdline.add_argument("-o", "--output", type=str)
cmdline.add_argument("-v", "--verbose", action='store_true')
cmdline.add_argument("--converters", action='store_true')
cmdline.add_argument("--make", action='store_true')
cmdline.add_argument("filename", type=str, nargs="*")
print('---------------------')
print(cmdline)

cmdline.print_usage()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


