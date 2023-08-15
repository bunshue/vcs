import sys
import os
import time
import marshal
import re
from functools import cmp_to_key

if __name__ == '__main__':
    
    import cmd
    try:
        import readline
    except ImportError:
        pass

    class ProfileBrowser(cmd.Cmd):
        def __init__(self, profile=None):
            cmd.Cmd.__init__(self)
            self.prompt = "% "
            self.stats = None
            self.stream = sys.stdout

        def generic_help(self):
            print("Arguments may be:", file=self.stream)
            print("* An integer maximum number of entries to print.", file=self.stream)
            print("* A decimal fractional number between 0 and 1, controlling", file=self.stream)
            print("  what fraction of selected entries to print.", file=self.stream)
            print("* A regular expression; only entries with function names", file=self.stream)
            print("  that match it are printed.", file=self.stream)

        def do_callees(self, line):
            return self.generic('print_callees', line)
        
        def do_quit(self, line):
            print('xxxxxx')
            return 1
        
        def help_quit(self):
            print("Leave the profile brower.", file=self.stream)

        def do_test(self):
            print('test')
            print("AALeave the profile brower.", file=self.stream)
            self.generic_help()

        def help_stats(self):
            print("Print statistics from the current stat object.", file=self.stream)
            self.generic_help()

        def postcmd(self, stop, line):
            if stop:
                return stop
            return None




initprofile = None
browser = ProfileBrowser(initprofile)

print('1')
browser.do_test()

print('6-------')

print("Welcome to the profile statistics browser.", file = browser.stream)
browser.cmdloop()

print("Goodbye.", file = browser.stream)


