import os
import logging

__copyright__ = """\
Copyright (c), 1997-2006, Marc-Andre Lemburg (mal@lemburg.com)
Copyright (c), 2000-2006, eGenix.com Software GmbH (info@egenix.com)
See the documentation for further information on copyrights,
or contact the author. All Rights Reserved.
"""
__version__ = "1.2"

# Name (defaults to program name)
name = ""
optionlist = None  # List of passed options


class MyLog(object):
    options = []
    # Header (default to program name)
    header = ""

    # Synopsis (%(name)s is replaced by the program name)
    synopsis = "%(name)s [option] files..."

    # General information printed after the possible options (optional)
    about = ""

    # Copyright to show
    copyright = __copyright__

    # Version (optional)
    version = ""

    def __init__(self, log):
        self.log = log
        self.first_log = True
        self.name = name

    def set_filename(self, filename):
        self.filename = filename

    def get_filename(self):
        return self.filename

    def log_message(self, message):
        if self.first_log:
            self.first_log = False
            self.log.append("### In file %s ###" % self.filename)
        self.log.append(message)

    def get_log(self):
        return self.log

    def path_mtime(self, filename):
        filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
        return os.stat(filename)

    def print_header(self):
        print("-" * 72)
        print(self.header % self.__dict__)
        print("-" * 72)
        print()

    def handle__copyright(self, arg):
        self.print_header()
        copyright = self.copyright % self.__dict__
        print(copyright.strip())
        print()
        return 0

    def help(self, note=""):
        if self.synopsis:
            print("Synopsis:")
            # To remain backward compatible:
            try:
                synopsis = self.synopsis % self.name
            except (NameError, KeyError, TypeError):
                synopsis = self.synopsis % self.__dict__
            print(" " + synopsis)
        print()
        self.print_options()
        if self.version:
            print("Version:")
            print(" %s" % self.version)
            print()
        if self.about:
            about = self.about % self.__dict__
            print(about.strip())
            print()
        if note:
            print("-" * 72)
            print("Note:", note)
            print()

    def notice(self, note):
        print("-" * 72)
        print("Note:", note)
        print("-" * 72)
        print()

    def print_options(self):
        options = self.options
        print("Options and default settings:")
        if not options:
            print("  None")
            return
        int = [x for x in options if x.prefix == "--"]
        short = [x for x in options if x.prefix == "-"]
        items = short + int
        for o in options:
            print(" ", o)
        print()


log = []

ccc = MyLog(log)

filename = "kkkkk.dat"
ccc.set_filename(filename)

ddd = ccc.get_filename()
print(ddd)

mesg1 = "aaaa"
mesg2 = "bbbb"
mesg3 = "cccc"

ccc.log_message(mesg1)
ccc.log_message(mesg2)
ccc.log_message(mesg3)

lineno = 123
for_output = "cccc.txt"
msg = "Line %d: could not convert: %s"
ccc.log_message(msg % (lineno, for_output))

ddd = ccc.get_log()
print(ddd)

eee = ccc.path_mtime("aaaaa")
print(type(eee))
print(eee)

fff = ccc.handle__copyright("tttt")

ggg = ccc.help("222")


class BufferedSubFile(object):
    def __init__(self):
        self.mesg_stack = []
        self.mesg_count = 0
        self._closed = False

    def push_mesg(self, mesg):
        self.mesg_stack.append(mesg)
        self.mesg_count += 1

    def pop_mesg(self):
        if self.mesg_count > 0:
            mesg = self.mesg_stack.pop()
            self.mesg_count -= 1
        else:
            mesg = "無資料"
        return mesg

    def close(self):
        self.mesg_stack = []
        self.mesg_count = 0
        self._closed = True


ccc = BufferedSubFile()
ccc.push_mesg("aaa")
ccc.push_mesg("bbb")
ccc.push_mesg("ccc")

ppp = ccc.pop_mesg()
print(ppp)
ppp = ccc.pop_mesg()
print(ppp)
ppp = ccc.pop_mesg()
print(ppp)
ppp = ccc.pop_mesg()
print(ppp)
ppp = ccc.pop_mesg()
print(ppp)
