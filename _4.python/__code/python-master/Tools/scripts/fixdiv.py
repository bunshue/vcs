import sys
import getopt
import re
import tokenize

multi_ok = 0

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hm")
    except getopt.error as msg:
        usage(msg)
        return 2
    for o, a in opts:
        if o == "-h":
            print(__doc__)
            return
        if o == "-m":
            global multi_ok
            multi_ok = 1
    if not args:
        usage("at least one file argument is required")
        return 2
    if args[1:]:
        sys.stderr.write("%s: extra file arguments ignored\n", sys.argv[0])
    warnings = readwarnings(args[0])
    if warnings is None:
        return 1
    files = list(warnings.keys())
    if not files:
        print("No classic division warnings read from", args[0])
        return
    files.sort()
    exit = None
    for filename in files:
        x = process(filename, warnings[filename])
        exit = exit or x
    return exit

def usage(msg):
    sys.stderr.write("%s: %s\n" % (sys.argv[0], msg))
    sys.stderr.write("Usage: %s [-m] warnings\n" % sys.argv[0])
    sys.stderr.write("Try `%s -h' for more information.\n" % sys.argv[0])

PATTERN = ("^(.+?):(\d+): DeprecationWarning: "
           "classic (int|long|float|complex) division$")

def readwarnings(warningsfile):
    prog = re.compile(PATTERN)
    try:
        f = open(warningsfile)
    except IOError as msg:
        sys.stderr.write("can't open: %s\n" % msg)
        return
    warnings = {}
    while 1:
        line = f.readline()
        if not line:
            break
        m = prog.match(line)
        if not m:
            if line.find("division") >= 0:
                sys.stderr.write("Warning: ignored input " + line)
            continue
        filename, lineno, what = m.groups()
        list = warnings.get(filename)
        if list is None:
            warnings[filename] = list = []
        list.append((int(lineno), sys.intern(what)))
    f.close()
    return warnings

def process(filename, list):
    print("-"*70)
    assert list # if this fails, readwarnings() is broken
    try:
        fp = open(filename)
    except IOError as msg:
        sys.stderr.write("can't open: %s\n" % msg)
        return 1
    print("Index:", filename)
    f = FileContext(fp)
    list.sort()
    index = 0 # list[:index] has been processed, list[index:] is still to do
    g = tokenize.generate_tokens(f.readline)
    while 1:
        startlineno, endlineno, slashes = lineinfo = scanline(g)
        if startlineno is None:
            break
        assert startlineno <= endlineno is not None
        orphans = []
        while index < len(list) and list[index][0] < startlineno:
            orphans.append(list[index])
            index += 1
        if orphans:
            reportphantomwarnings(orphans, f)
        warnings = []
        while index < len(list) and list[index][0] <= endlineno:
            warnings.append(list[index])
            index += 1
        if not slashes and not warnings:
            pass
        elif slashes and not warnings:
            report(slashes, "No conclusive evidence")
        elif warnings and not slashes:
            reportphantomwarnings(warnings, f)
        else:
            if len(slashes) > 1:
                if not multi_ok:
                    rows = []
                    lastrow = None
                    for (row, col), line in slashes:
                        if row == lastrow:
                            continue
                        rows.append(row)
                        lastrow = row
                    assert rows
                    if len(rows) == 1:
                        print("*** More than one / operator in line", rows[0])
                    else:
                        print("*** More than one / operator per statement", end=' ')
                        print("in lines %d-%d" % (rows[0], rows[-1]))
            intlong = []
            floatcomplex = []
            bad = []
            for lineno, what in warnings:
                if what in ("int", "long"):
                    intlong.append(what)
                elif what in ("float", "complex"):
                    floatcomplex.append(what)
                else:
                    bad.append(what)
            lastrow = None
            for (row, col), line in slashes:
                if row == lastrow:
                    continue
                lastrow = row
                line = chop(line)
                if line[col:col+1] != "/":
                    print("*** Can't find the / operator in line %d:" % row)
                    print("*", line)
                    continue
                if bad:
                    print("*** Bad warning for line %d:" % row, bad)
                    print("*", line)
                elif intlong and not floatcomplex:
                    print("%dc%d" % (row, row))
                    print("<", line)
                    print("---")
                    print(">", line[:col] + "/" + line[col:])
                elif floatcomplex and not intlong:
                    print("True division / operator at line %d:" % row)
                    print("=", line)
                elif intlong and floatcomplex:
                    print("*** Ambiguous / operator (%s, %s) at line %d:" % (
                        "|".join(intlong), "|".join(floatcomplex), row))
                    print("?", line)
    fp.close()

def reportphantomwarnings(warnings, f):
    blocks = []
    lastrow = None
    lastblock = None
    for row, what in warnings:
        if row != lastrow:
            lastblock = [row]
            blocks.append(lastblock)
        lastblock.append(what)
    for block in blocks:
        row = block[0]
        whats = "/".join(block[1:])
        print("*** Phantom %s warnings for line %d:" % (whats, row))
        f.report(row, mark="*")

def report(slashes, message):
    lastrow = None
    for (row, col), line in slashes:
        if row != lastrow:
            print("*** %s on line %d:" % (message, row))
            print("*", chop(line))
            lastrow = row

class FileContext:
    def __init__(self, fp, window=5, lineno=1):
        self.fp = fp
        self.window = 5
        self.lineno = 1
        self.eoflookahead = 0
        self.lookahead = []
        self.buffer = []
    def fill(self):
        while len(self.lookahead) < self.window and not self.eoflookahead:
            line = self.fp.readline()
            if not line:
                self.eoflookahead = 1
                break
            self.lookahead.append(line)
    def readline(self):
        self.fill()
        if not self.lookahead:
            return ""
        line = self.lookahead.pop(0)
        self.buffer.append(line)
        self.lineno += 1
        return line
    def truncate(self):
        del self.buffer[-window:]
    def __getitem__(self, index):
        self.fill()
        bufstart = self.lineno - len(self.buffer)
        lookend = self.lineno + len(self.lookahead)
        if bufstart <= index < self.lineno:
            return self.buffer[index - bufstart]
        if self.lineno <= index < lookend:
            return self.lookahead[index - self.lineno]
        raise KeyError
    def report(self, first, last=None, mark="*"):
        if last is None:
            last = first
        for i in range(first, last+1):
            try:
                line = self[first]
            except KeyError:
                line = "<missing line>"
            print(mark, chop(line))

def scanline(g):
    slashes = []
    startlineno = None
    endlineno = None
    for type, token, start, end, line in g:
        endlineno = end[0]
        if startlineno is None:
            startlineno = endlineno
        if token in ("/", "/="):
            slashes.append((start, line))
        if type == tokenize.NEWLINE:
            break
    return startlineno, endlineno, slashes

def chop(line):
    if line.endswith("\n"):
        return line[:-1]
    else:
        return line

if __name__ == "__main__":
    sys.exit(main())
