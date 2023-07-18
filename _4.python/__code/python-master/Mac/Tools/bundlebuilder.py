__all__ = ["BundleBuilder", "BundleBuilderError", "AppBuilder", "buildapp"]


import sys
import os, errno, shutil
import imp, marshal
import re
from copy import deepcopy
import getopt

from types import FunctionType as function



cmdline_doc = """\
Usage:
  python bundlebuilder.py [options] command
  python mybuildscript.py [options] command

Commands:
  build      build the application
  report     print a report

Options:
  -b, --builddir=DIR     the build directory; defaults to "build"
  -n, --name=NAME        application name
  -r, --resource=FILE    extra file or folder to be copied to Resources
  -f, --file=SRC:DST     extra file or folder to be copied into the bundle;
                         DST must be a path relative to the bundle root
  -e, --executable=FILE  the executable to be used
  -m, --mainprogram=FILE the Python main program
  -a, --argv             add a wrapper main program to create sys.argv
  -p, --plist=FILE       .plist file (default: generate one)
      --nib=NAME         main nib name
  -c, --creator=CCCC     4-char creator code (default: '????')
      --iconfile=FILE    filename of the icon (an .icns file) to be used
                         as the Finder icon
      --bundle-id=ID     the CFBundleIdentifier, in reverse-dns format
                         (eg. org.python.BuildApplet; this is used for
                         the preferences file name)
  -l, --link             symlink files/folder instead of copying them
      --link-exec        symlink the executable instead of copying it
      --standalone       build a standalone application, which is fully
                         independent of a Python installation
      --semi-standalone  build a standalone application, which depends on
                         an installed Python, yet includes all third-party
                         modules.
      --python=FILE      Python to use in #! line in stead of current Python
      --lib=FILE         shared library or framework to be copied into
                         the bundle
  -x, --exclude=MODULE   exclude module (with --(semi-)standalone)
  -i, --include=MODULE   include module (with --(semi-)standalone)
      --package=PACKAGE  include a whole package (with --(semi-)standalone)
      --strip            strip binaries (remove debug info)
  -v, --verbose          increase verbosity level
  -q, --quiet            decrease verbosity level
  -h, --help             print this message
"""

def usage(msg=None):
    if msg:
        print(msg)
    print(cmdline_doc)
    sys.exit(1)

def main(builder=None):

    shortopts = "b:n:r:f:e:m:c:p:lx:i:hvqa"
    longopts = ("builddir=", "name=", "resource=", "file=", "executable=",
        "mainprogram=", "creator=", "nib=", "plist=", "link",
        "link-exec", "help", "verbose", "quiet", "argv", "standalone",
        "exclude=", "include=", "package=", "strip", "iconfile=",
        "lib=", "python=", "semi-standalone", "bundle-id=", "destroot=")

    try:
        options, args = getopt.getopt(sys.argv[1:], shortopts, longopts)
    except getopt.error:
        usage()

    for opt, arg in options:
        if opt in ('-b', '--builddir'):
            builder.builddir = arg
        elif opt in ('-n', '--name'):
            builder.name = arg
        elif opt in ('-r', '--resource'):
            builder.resources.append(os.path.normpath(arg))
        elif opt in ('-f', '--file'):
            srcdst = arg.split(':')
            if len(srcdst) != 2:
                usage("-f or --file argument must be two paths, "
                      "separated by a colon")
            builder.files.append(srcdst)
        elif opt in ('-e', '--executable'):
            builder.executable = arg
        elif opt in ('-m', '--mainprogram'):
            builder.mainprogram = arg
        elif opt in ('-a', '--argv'):
            builder.argv_emulation = 1
        elif opt in ('-c', '--creator'):
            builder.creator = arg
        elif opt == '--bundle-id':
            builder.bundle_id = arg
        elif opt == '--iconfile':
            builder.iconfile = arg
        elif opt == "--lib":
            builder.libs.append(os.path.normpath(arg))
        elif opt == "--nib":
            builder.nibname = arg
        elif opt in ('-p', '--plist'):
            builder.plist = Plist.fromFile(arg)
        elif opt in ('-l', '--link'):
            builder.symlink = 1
        elif opt == '--link-exec':
            builder.symlink_exec = 1
        elif opt in ('-h', '--help'):
            usage()
        elif opt in ('-v', '--verbose'):
            builder.verbosity += 1
        elif opt in ('-q', '--quiet'):
            builder.verbosity -= 1
        elif opt == '--standalone':
            builder.standalone = 1
        elif opt == '--semi-standalone':
            builder.semi_standalone = 1
        elif opt == '--python':
            builder.python = arg
        elif opt in ('-x', '--exclude'):
            builder.excludeModules.append(arg)
        elif opt in ('-i', '--include'):
            builder.includeModules.append(arg)
        elif opt == '--package':
            builder.includePackages.append(arg)
        elif opt == '--strip':
            builder.strip = 1
        elif opt == '--destroot':
            builder.destroot = arg

    if len(args) != 1:
        usage("Must specify one command ('build', 'report' or 'help')")
    command = args[0]

    if command == "build":
        builder.setup()
        builder.build()
    elif command == "report":
        builder.setup()
        builder.report()
    elif command == "help":
        usage()
    else:
        usage("Unknown command '%s'" % command)


if __name__ == "__main__":
    main()
