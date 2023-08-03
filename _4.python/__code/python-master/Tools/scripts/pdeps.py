import sys
import re
import os

def main():
    args = sys.argv[1:]
    if not args:
        print('usage: pdeps file.py file.py ...')
        return 2
    #
    table = {}
    for arg in args:
        process(arg, table)
    #
    print('--- Uses ---')
    printresults(table)
    #
    print('--- Used By ---')
    inv = inverse(table)
    printresults(inv)
    #
    print('--- Closure of Uses ---')
    reach = closure(table)
    printresults(reach)
    #
    print('--- Closure of Used By ---')
    invreach = inverse(reach)
    printresults(invreach)
    #
    return 0


# Compiled regular expressions to search for import statements
#
m_import = re.compile('^[ \t]*from[ \t]+([^ \t]+)[ \t]+')
m_from = re.compile('^[ \t]*import[ \t]+([^#]+)')


# Collect data from one file
#
def process(filename, table):
    fp = open(filename, 'r')
    mod = os.path.basename(filename)
    if mod[-3:] == '.py':
        mod = mod[:-3]
    table[mod] = list = []
    while 1:
        line = fp.readline()
        if not line: break
        while line[-1:] == '\\':
            nextline = fp.readline()
            if not nextline: break
            line = line[:-1] + nextline
        m_found = m_import.match(line) or m_from.match(line)
        if m_found:
            (a, b), (a1, b1) = m_found.regs[:2]
        else: continue
        words = line[a1:b1].split(',')
        # print '#', line, words
        for word in words:
            word = word.strip()
            if word not in list:
                list.append(word)
    fp.close()


# Compute closure (this is in fact totally general)
#
def closure(table):
    modules = list(table.keys())
    #
    # Initialize reach with a copy of table
    #
    reach = {}
    for mod in modules:
        reach[mod] = table[mod][:]
    #
    # Iterate until no more change
    #
    change = 1
    while change:
        change = 0
        for mod in modules:
            for mo in reach[mod]:
                if mo in modules:
                    for m in reach[mo]:
                        if m not in reach[mod]:
                            reach[mod].append(m)
                            change = 1
    #
    return reach




