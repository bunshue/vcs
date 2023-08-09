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
            if profile is not None:
                self.do_read(profile)

        def generic(self, fn, line):
            args = line.split()
            processed = []
            for term in args:
                try:
                    processed.append(int(term))
                    continue
                except ValueError:
                    pass
                try:
                    frac = float(term)
                    if frac > 1 or frac < 0:
                        print("Fraction argument must be in [0, 1]", file=self.stream)
                        continue
                    processed.append(frac)
                    continue
                except ValueError:
                    pass
                processed.append(term)
            if self.stats:
                getattr(self.stats, fn)(*processed)
            else:
                print("No statistics object is loaded.", file=self.stream)
            return 0
        def generic_help(self):
            print("Arguments may be:", file=self.stream)
            print("* An integer maximum number of entries to print.", file=self.stream)
            print("* A decimal fractional number between 0 and 1, controlling", file=self.stream)
            print("  what fraction of selected entries to print.", file=self.stream)
            print("* A regular expression; only entries with function names", file=self.stream)
            print("  that match it are printed.", file=self.stream)

        def do_add(self, line):
            if self.stats:
                self.stats.add(line)
            else:
                print("No statistics object is loaded.", file=self.stream)
            return 0
        def help_add(self):
            print("Add profile info from given file to current statistics object.", file=self.stream)

        def do_callees(self, line):
            return self.generic('print_callees', line)
        def help_callees(self):
            print("Print callees statistics from the current stat object.", file=self.stream)
            self.generic_help()

        def do_callers(self, line):
            return self.generic('print_callers', line)
        def help_callers(self):
            print("Print callers statistics from the current stat object.", file=self.stream)
            self.generic_help()

        def do_EOF(self, line):
            print("", file=self.stream)
            return 1
        def help_EOF(self):
            print("AALeave the profile brower.", file=self.stream)

        def do_quit(self, line):
            return 1
        def help_quit(self):
            print("Leave the profile brower.", file=self.stream)

        def do_read(self, line):
            if line:
                try:
                    self.stats = Stats(line)
                except OSError as err:
                    print(err.args[1], file=self.stream)
                    return
                except Exception as err:
                    print(err.__class__.__name__ + ':', err, file=self.stream)
                    return
                self.prompt = line + "% "
            elif len(self.prompt) > 2:
                line = self.prompt[:-2]
                self.do_read(line)
            else:
                print("No statistics object is current -- cannot reload.", file=self.stream)
            return 0
        def help_read(self):
            print("Read in profile data from a specified file.", file=self.stream)
            print("Without argument, reload the current file.", file=self.stream)

        def do_reverse(self, line):
            if self.stats:
                self.stats.reverse_order()
            else:
                print("No statistics object is loaded.", file=self.stream)
            return 0
        def help_reverse(self):
            print("Reverse the sort order of the profiling report.", file=self.stream)

        def do_sort(self, line):
            if not self.stats:
                print("No statistics object is loaded.", file=self.stream)
                return
            abbrevs = self.stats.get_sort_arg_defs()
            if line and all((x in abbrevs) for x in line.split()):
                self.stats.sort_stats(*line.split())
            else:
                print("Valid sort keys (unique prefixes are accepted):", file=self.stream)
                for (key, value) in Stats.sort_arg_dict_default.items():
                    print("%s -- %s" % (key, value[1]), file=self.stream)
            return 0
        def help_sort(self):
            print("Sort profile data according to specified keys.", file=self.stream)
            print("(Typing `sort' without arguments lists valid keys.)", file=self.stream)
        def complete_sort(self, text, *args):
            return [a for a in Stats.sort_arg_dict_default if a.startswith(text)]

        def do_stats(self, line):
            return self.generic('print_stats', line)
        def help_stats(self):
            print("Print statistics from the current stat object.", file=self.stream)
            self.generic_help()

        def do_strip(self, line):
            if self.stats:
                self.stats.strip_dirs()
            else:
                print("No statistics object is loaded.", file=self.stream)
        def help_strip(self):
            print("Strip leading path information from filenames in the report.", file=self.stream)

        def help_help(self):
            print("Show help for a given command.", file=self.stream)

        def postcmd(self, stop, line):
            if stop:
                return stop
            return None





print('1111')

initprofile = None
browser = ProfileBrowser(initprofile)

print('1')
browser.help_EOF()
print('2')
browser.help_callers()
print('3')
browser.help_add()
print('4')
browser.help_read()
print('5')
browser.help_help()
print('6')

print("Welcome to the profile statistics browser.", file = browser.stream)
browser.cmdloop()

print("Goodbye.", file = browser.stream)





