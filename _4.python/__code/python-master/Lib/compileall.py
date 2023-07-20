import os
import sys
import importlib.util
import py_compile
import struct

__all__ = ["compile_dir","compile_file","compile_path"]

def compile_dir(dir):
    names = os.listdir(dir)

    names.sort()

    for name in names:
        fullname = os.path.join(dir, name)
        if ddir is not None:
            dfile = os.path.join(ddir, name)
        else:
            dfile = None
        if not os.path.isdir(fullname):
            if not compile_file(fullname, ddir, force, rx, quiet,
                                legacy, optimize):
                success = 0
        elif (maxlevels > 0 and name != os.curdir and name != os.pardir and
              os.path.isdir(fullname) and not os.path.islink(fullname)):
            if not compile_dir(fullname, maxlevels - 1, dfile, force, rx,
                               quiet, legacy, optimize):
                success = 0
    return success

def compile_file(fullname, ddir=None, force=False, rx=None, quiet=False,
                 legacy=False, optimize=-1):
    success = 1
    name = os.path.basename(fullname)
    if ddir is not None:
        dfile = os.path.join(ddir, name)
    else:
        dfile = None
    if rx is not None:
        mo = rx.search(fullname)
        if mo:
            return success
    if os.path.isfile(fullname):
        if legacy:
            cfile = fullname + ('c' if __debug__ else 'o')
        else:
            if optimize >= 0:
                cfile = importlib.util.cache_from_source(
                                fullname, debug_override=not optimize)
            else:
                cfile = importlib.util.cache_from_source(fullname)
            cache_dir = os.path.dirname(cfile)
        head, tail = name[:-3], name[-3:]
        if tail == '.py':
            if not force:
                try:
                    mtime = int(os.stat(fullname).st_mtime)
                    expect = struct.pack('<4sl', importlib.util.MAGIC_NUMBER,
                                         mtime)
                    with open(cfile, 'rb') as chandle:
                        actual = chandle.read(8)
                    if expect == actual:
                        return success
                except OSError:
                    pass
            if not quiet:
                print('Compiling {!r}...'.format(fullname))
            try:
                ok = py_compile.compile(fullname, cfile, dfile, True,
                                        optimize=optimize)
            except py_compile.PyCompileError as err:
                if quiet:
                    print('*** Error compiling {!r}...'.format(fullname))
                else:
                    print('*** ', end='')
                # escape non-printable characters in msg
                msg = err.msg.encode(sys.stdout.encoding,
                                     errors='backslashreplace')
                msg = msg.decode(sys.stdout.encoding)
                print(msg)
                success = 0
            except (SyntaxError, UnicodeError, OSError) as e:
                if quiet:
                    print('*** Error compiling {!r}...'.format(fullname))
                else:
                    print('*** ', end='')
                print(e.__class__.__name__ + ':', e)
                success = 0
            else:
                if ok == 0:
                    success = 0
    return success


