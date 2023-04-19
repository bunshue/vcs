#! /usr/bin/env python3

import sys,re

expr = r'^[ \t]*(def|class)[ \t]+([a-zA-Z_][a-zA-Z0-9_]*)[ \t]*[:\(]'
matcher = re.compile(expr)

def treat_file(filename, outfp):
    """Append tags found in file named 'filename' to the open file 'outfp'"""
    try:
        fp = open(filename, 'r')
    except OSError:
        sys.stderr.write('Cannot open %s\n'%filename)
        return
    charno = 0
    lineno = 0
    tags = []
    size = 0
    while 1:
        line = fp.readline()
        if not line:
            break
        lineno = lineno + 1
        m = matcher.search(line)
        if m:
            tag = m.group(0) + '\177%d,%d\n' % (lineno, charno)
            tags.append(tag)
            size = size + len(tag)
        charno = charno + len(line)
    outfp.write('\f\n%s,%d\n' % (filename,size))
    for tag in tags:
        outfp.write(tag)

def main():
    outfp = open('TAGS', 'w')
    for filename in sys.argv[1:]:
        treat_file(filename, outfp)

if __name__=="__main__":
    main()
