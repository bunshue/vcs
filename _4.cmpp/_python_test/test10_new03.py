import os
import sys
import ast
import getopt
import struct
import array
from email.parser import HeaderParser


infile = 'aaaaaaa'
lno = 1234
print('Syntax error on %s:%d' % (infile, lno), 'before:', file=sys.stderr)


print(__doc__, file=sys.stderr)
