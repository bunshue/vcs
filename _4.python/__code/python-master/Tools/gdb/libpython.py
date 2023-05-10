    def current_line(self):
        '''Get the text of the current source line as a string, with a trailing
        newline character'''
        if self.is_optimized_out():
            return '(frame information optimized out)'
        filename = self.filename()
        try:
            f = open(os_fsencode(filename), 'r')
        except IOError:
            return None
        with f:
            all_lines = f.readlines()
            # Convert from 1-based current_line_num to 0-based list offset:
            return all_lines[self.current_line_num()-1]










def _unichr_is_printable(char):
    # Logic adapted from Python 3's Tools/unicode/makeunicodedata.py
    if char == u" ":
        return True
    import unicodedata
    return unicodedata.category(char) not in ("C", "Z")

if sys.maxunicode >= 0x10000:
    _unichr = unichr
else:
    # Needed for proper surrogate support if sizeof(Py_UNICODE) is 2 in gdb
    def _unichr(x):
        if x < 0x10000:
            return unichr(x)
        x -= 0x10000
        ch1 = 0xD800 | (x >> 10)
        ch2 = 0xDC00 | (x & 0x3FF)
        return unichr(ch1) + unichr(ch2)


class PyUnicodeObjectPtr(PyObjectPtr):
    _typename = 'PyUnicodeObject'

    def char_width(self):
        _type_Py_UNICODE = gdb.lookup_type('Py_UNICODE')
        return _type_Py_UNICODE.sizeof

    def proxyval(self, visited):
        global _is_pep393
        if _is_pep393 is None:
            fields = gdb.lookup_type('PyUnicodeObject').target().fields()
            _is_pep393 = 'data' in [f.name for f in fields]
        if _is_pep393:
            # Python 3.3 and newer
            may_have_surrogates = False
            compact = self.field('_base')
            ascii = compact['_base']
            state = ascii['state']
            is_compact_ascii = (int(state['ascii']) and int(state['compact']))
            if not int(state['ready']):
                # string is not ready
                field_length = long(compact['wstr_length'])
                may_have_surrogates = True
                field_str = ascii['wstr']
            else:
                field_length = long(ascii['length'])
                if is_compact_ascii:
                    field_str = ascii.address + 1
                elif int(state['compact']):
                    field_str = compact.address + 1
                else:
                    field_str = self.field('data')['any']
                repr_kind = int(state['kind'])
                if repr_kind == 1:
                    field_str = field_str.cast(_type_unsigned_char_ptr)
                elif repr_kind == 2:
                    field_str = field_str.cast(_type_unsigned_short_ptr)
                elif repr_kind == 4:
                    field_str = field_str.cast(_type_unsigned_int_ptr)
        else:
            # Python 3.2 and earlier
            field_length = long(self.field('length'))
            field_str = self.field('str')
            may_have_surrogates = self.char_width() == 2

        # Gather a list of ints from the Py_UNICODE array; these are either
        # UCS-1, UCS-2 or UCS-4 code points:
        if not may_have_surrogates:
            Py_UNICODEs = [int(field_str[i]) for i in safe_range(field_length)]
        else:
            # A more elaborate routine if sizeof(Py_UNICODE) is 2 in the
            # inferior process: we must join surrogate pairs.
            Py_UNICODEs = []
            i = 0
            limit = safety_limit(field_length)
            while i < limit:
                ucs = int(field_str[i])
                i += 1
                if ucs < 0xD800 or ucs >= 0xDC00 or i == field_length:
                    Py_UNICODEs.append(ucs)
                    continue
                # This could be a surrogate pair.
                ucs2 = int(field_str[i])
                if ucs2 < 0xDC00 or ucs2 > 0xDFFF:
                    continue
                code = (ucs & 0x03FF) << 10
                code |= ucs2 & 0x03FF
                code += 0x00010000
                Py_UNICODEs.append(code)
                i += 1

        # Convert the int code points to unicode characters, and generate a
        # local unicode instance.
        # This splits surrogate pairs if sizeof(Py_UNICODE) is 2 here (in gdb).
        result = u''.join([
            (_unichr(ucs) if ucs <= 0x10ffff else '\ufffd')
            for ucs in Py_UNICODEs])
        return result

    def write_repr(self, out, visited):
        # Write this out as a Python 3 str literal, i.e. without a "u" prefix

        # Get a PyUnicodeObject* within the Python 2 gdb process:
        proxy = self.proxyval(visited)

        # Transliteration of Python 3's Object/unicodeobject.c:unicode_repr
        # to Python 2:
        if "'" in proxy and '"' not in proxy:
            quote = '"'
        else:
            quote = "'"
        out.write(quote)

        i = 0
        while i < len(proxy):
            ch = proxy[i]
            i += 1

            # Escape quotes and backslashes
            if ch == quote or ch == '\\':
                out.write('\\')
                out.write(ch)

            #  Map special whitespace to '\t', \n', '\r'
            elif ch == '\t':
                out.write('\\t')
            elif ch == '\n':
                out.write('\\n')
            elif ch == '\r':
                out.write('\\r')

            # Map non-printable US ASCII to '\xhh' */
            elif ch < ' ' or ch == 0x7F:
                out.write('\\x')
                out.write(hexdigits[(ord(ch) >> 4) & 0x000F])
                out.write(hexdigits[ord(ch) & 0x000F])

            # Copy ASCII characters as-is
            elif ord(ch) < 0x7F:
                out.write(ch)

            # Non-ASCII characters
            else:
                ucs = ch
                ch2 = None
                if sys.maxunicode < 0x10000:
                    # If sizeof(Py_UNICODE) is 2 here (in gdb), join
                    # surrogate pairs before calling _unichr_is_printable.
                    if (i < len(proxy)
                    and 0xD800 <= ord(ch) < 0xDC00 \
                    and 0xDC00 <= ord(proxy[i]) <= 0xDFFF):
                        ch2 = proxy[i]
                        ucs = ch + ch2
                        i += 1

                # Unfortuately, Python 2's unicode type doesn't seem
                # to expose the "isprintable" method
                printable = _unichr_is_printable(ucs)
                if printable:
                    try:
                        ucs.encode(ENCODING)
                    except UnicodeEncodeError:
                        printable = False

                # Map Unicode whitespace and control characters
                # (categories Z* and C* except ASCII space)
                if not printable:
                    if ch2 is not None:
                        # Match Python 3's representation of non-printable
                        # wide characters.
                        code = (ord(ch) & 0x03FF) << 10
                        code |= ord(ch2) & 0x03FF
                        code += 0x00010000
                    else:
                        code = ord(ucs)

                    # Map 8-bit characters to '\\xhh'
                    if code <= 0xff:
                        out.write('\\x')
                        out.write(hexdigits[(code >> 4) & 0x000F])
                        out.write(hexdigits[code & 0x000F])
                    # Map 21-bit characters to '\U00xxxxxx'
                    elif code >= 0x10000:
                        out.write('\\U')
                        out.write(hexdigits[(code >> 28) & 0x0000000F])
                        out.write(hexdigits[(code >> 24) & 0x0000000F])
                        out.write(hexdigits[(code >> 20) & 0x0000000F])
                        out.write(hexdigits[(code >> 16) & 0x0000000F])
                        out.write(hexdigits[(code >> 12) & 0x0000000F])
                        out.write(hexdigits[(code >> 8) & 0x0000000F])
                        out.write(hexdigits[(code >> 4) & 0x0000000F])
                        out.write(hexdigits[code & 0x0000000F])
                    # Map 16-bit characters to '\uxxxx'
                    else:
                        out.write('\\u')
                        out.write(hexdigits[(code >> 12) & 0x000F])
                        out.write(hexdigits[(code >> 8) & 0x000F])
                        out.write(hexdigits[(code >> 4) & 0x000F])
                        out.write(hexdigits[code & 0x000F])
                else:
                    # Copy characters as-is
                    out.write(ch)
                    if ch2 is not None:
                        out.write(ch2)

        out.write(quote)




def int_from_int(gdbval):
    return int(str(gdbval))


def stringify(val):
    # TODO: repr() puts everything on one line; pformat can be nicer, but
    # can lead to v.long results; this function isolates the choice
    if True:
        return repr(val)
    else:
        from pprint import pformat
        return pformat(val)


class PyObjectPtrPrinter:
    "Prints a (PyObject*)"

    def __init__ (self, gdbval):
        self.gdbval = gdbval

    def to_string (self):
        pyop = PyObjectPtr.from_pyobject_ptr(self.gdbval)
        if True:
            return pyop.get_truncated_repr(MAX_OUTPUT_LEN)
        else:
            # Generate full proxy value then stringify it.
            # Doing so could be expensive
            proxyval = pyop.proxyval(set())
            return stringify(proxyval)

def pretty_printer_lookup(gdbval):
    type = gdbval.type.unqualified()
    if type.code == gdb.TYPE_CODE_PTR:
        type = type.target().unqualified()
        t = str(type)
        if t in ("PyObject", "PyFrameObject", "PyUnicodeObject"):
            return PyObjectPtrPrinter(gdbval)

"""
During development, I've been manually invoking the code in this way:
(gdb) python

import sys
sys.path.append('/home/david/coding/python-gdb')
import libpython
end

then reloading it after each edit like this:
(gdb) python reload(libpython)

The following code should ensure that the prettyprinter is registered
if the code is autoloaded by gdb when visiting libpython.so, provided
that this python file is installed to the same path as the library (or its
.debug file) plus a "-gdb.py" suffix, e.g:
  /usr/lib/libpython2.6.so.1.0-gdb.py
  /usr/lib/debug/usr/lib/libpython2.6.so.1.0.debug-gdb.py
"""
def register (obj):
    if obj is None:
        obj = gdb

    # Wire up the pretty-printer
    obj.pretty_printers.append(pretty_printer_lookup)

register (gdb.current_objfile ())



# Unfortunately, the exact API exposed by the gdb module varies somewhat
# from build to build
# See http://bugs.python.org/issue8279?#msg102276

class Frame(object):
    '''
    Wrapper for gdb.Frame, adding various methods
    '''
    def __init__(self, gdbframe):
        self._gdbframe = gdbframe

    def older(self):
        older = self._gdbframe.older()
        if older:
            return Frame(older)
        else:
            return None

    def newer(self):
        newer = self._gdbframe.newer()
        if newer:
            return Frame(newer)
        else:
            return None

    def select(self):
        '''If supported, select this frame and return True; return False if unsupported

        Not all builds have a gdb.Frame.select method; seems to be present on Fedora 12
        onwards, but absent on Ubuntu buildbot'''
        if not hasattr(self._gdbframe, 'select'):
            print ('Unable to select frame: '
                   'this build of gdb does not expose a gdb.Frame.select method')
            return False
        self._gdbframe.select()
        return True

    def get_index(self):
        '''Calculate index of frame, starting at 0 for the newest frame within
        this thread'''
        index = 0
        # Go down until you reach the newest frame:
        iter_frame = self
        while iter_frame.newer():
            index += 1
            iter_frame = iter_frame.newer()
        return index

    # We divide frames into:
    #   - "python frames":
    #       - "bytecode frames" i.e. PyEval_EvalFrameEx
    #       - "other python frames": things that are of interest from a python
    #         POV, but aren't bytecode (e.g. GC, GIL)
    #   - everything else

    def is_python_frame(self):
        '''Is this a PyEval_EvalFrameEx frame, or some other important
        frame? (see is_other_python_frame for what "important" means in this
        context)'''
        if self.is_evalframeex():
            return True
        if self.is_other_python_frame():
            return True
        return False

    def is_evalframeex(self):
        '''Is this a PyEval_EvalFrameEx frame?'''
        if self._gdbframe.name() == 'PyEval_EvalFrameEx':
            '''
            I believe we also need to filter on the inline
            struct frame_id.inline_depth, only regarding frames with
            an inline depth of 0 as actually being this function

            So we reject those with type gdb.INLINE_FRAME
            '''
            if self._gdbframe.type() == gdb.NORMAL_FRAME:
                # We have a PyEval_EvalFrameEx frame:
                return True

        return False

    def is_other_python_frame(self):
        '''Is this frame worth displaying in python backtraces?
        Examples:
          - waiting on the GIL
          - garbage-collecting
          - within a CFunction
         If it is, return a descriptive string
         For other frames, return False
         '''
        if self.is_waiting_for_gil():
            return 'Waiting for the GIL'
        elif self.is_gc_collect():
            return 'Garbage-collecting'
        else:
            # Detect invocations of PyCFunction instances:
            older = self.older()
            if older and older._gdbframe.name() == 'PyCFunction_Call':
                # Within that frame:
                #   "func" is the local containing the PyObject* of the
                # PyCFunctionObject instance
                #   "f" is the same value, but cast to (PyCFunctionObject*)
                #   "self" is the (PyObject*) of the 'self'
                try:
                    # Use the prettyprinter for the func:
                    func = older._gdbframe.read_var('func')
                    return str(func)
                except RuntimeError:
                    return 'PyCFunction invocation (unable to read "func")'

        # This frame isn't worth reporting:
        return False

    def is_waiting_for_gil(self):
        '''Is this frame waiting on the GIL?'''
        # This assumes the _POSIX_THREADS version of Python/ceval_gil.h:
        name = self._gdbframe.name()
        if name:
            return 'pthread_cond_timedwait' in name

    def is_gc_collect(self):
        '''Is this frame "collect" within the garbage-collector?'''
        return self._gdbframe.name() == 'collect'

    def get_pyop(self):
        try:
            f = self._gdbframe.read_var('f')
            frame = PyFrameObjectPtr.from_pyobject_ptr(f)
            if not frame.is_optimized_out():
                return frame
            # gdb is unable to get the "f" argument of PyEval_EvalFrameEx()
            # because it was "optimized out". Try to get "f" from the frame
            # of the caller, PyEval_EvalCodeEx().
            orig_frame = frame
            caller = self._gdbframe.older()
            if caller:
                f = caller.read_var('f')
                frame = PyFrameObjectPtr.from_pyobject_ptr(f)
                if not frame.is_optimized_out():
                    return frame
            return orig_frame
        except ValueError:
            return None

    @classmethod
    def get_selected_frame(cls):
        _gdbframe = gdb.selected_frame()
        if _gdbframe:
            return Frame(_gdbframe)
        return None

    @classmethod
    def get_selected_python_frame(cls):
        '''Try to obtain the Frame for the python-related code in the selected
        frame, or None'''
        frame = cls.get_selected_frame()

        while frame:
            if frame.is_python_frame():
                return frame
            frame = frame.older()

        # Not found:
        return None

    @classmethod
    def get_selected_bytecode_frame(cls):
        '''Try to obtain the Frame for the python bytecode interpreter in the
        selected GDB frame, or None'''
        frame = cls.get_selected_frame()

        while frame:
            if frame.is_evalframeex():
                return frame
            frame = frame.older()

        # Not found:
        return None

    def print_summary(self):
        if self.is_evalframeex():
            pyop = self.get_pyop()
            if pyop:
                line = pyop.get_truncated_repr(MAX_OUTPUT_LEN)
                write_unicode(sys.stdout, '#%i %s\n' % (self.get_index(), line))
                if not pyop.is_optimized_out():
                    line = pyop.current_line()
                    if line is not None:
                        sys.stdout.write('    %s\n' % line.strip())
            else:
                sys.stdout.write('#%i (unable to read python frame information)\n' % self.get_index())
        else:
            info = self.is_other_python_frame()
            if info:
                sys.stdout.write('#%i %s\n' % (self.get_index(), info))
            else:
                sys.stdout.write('#%i\n' % self.get_index())

    def print_traceback(self):
        if self.is_evalframeex():
            pyop = self.get_pyop()
            if pyop:
                pyop.print_traceback()
                if not pyop.is_optimized_out():
                    line = pyop.current_line()
                    if line is not None:
                        sys.stdout.write('    %s\n' % line.strip())
            else:
                sys.stdout.write('  (unable to read python frame information)\n')
        else:
            info = self.is_other_python_frame()
            if info:
                sys.stdout.write('  %s\n' % info)
            else:
                sys.stdout.write('  (not a python frame)\n')

class PyList(gdb.Command):
    '''List the current Python source code, if any

    Use
       py-list START
    to list at a different line number within the python source.

    Use
       py-list START, END
    to list a specific range of lines within the python source.
    '''

    def __init__(self):
        gdb.Command.__init__ (self,
                              "py-list",
                              gdb.COMMAND_FILES,
                              gdb.COMPLETE_NONE)


    def invoke(self, args, from_tty):
        import re

        start = None
        end = None

        m = re.match(r'\s*(\d+)\s*', args)
        if m:
            start = int(m.group(0))
            end = start + 10

        m = re.match(r'\s*(\d+)\s*,\s*(\d+)\s*', args)
        if m:
            start, end = map(int, m.groups())

        # py-list requires an actual PyEval_EvalFrameEx frame:
        frame = Frame.get_selected_bytecode_frame()
        if not frame:
            print('Unable to locate gdb frame for python bytecode interpreter')
            return

        pyop = frame.get_pyop()
        if not pyop or pyop.is_optimized_out():
            print('Unable to read information on python frame')
            return

        filename = pyop.filename()
        lineno = pyop.current_line_num()

        if start is None:
            start = lineno - 5
            end = lineno + 5

        if start<1:
            start = 1

        try:
            f = open(os_fsencode(filename), 'r')
        except IOError as err:
            sys.stdout.write('Unable to open %s: %s\n'
                             % (filename, err))
            return
        with f:
            all_lines = f.readlines()
            # start and end are 1-based, all_lines is 0-based;
            # so [start-1:end] as a python slice gives us [start, end] as a
            # closed interval
            for i, line in enumerate(all_lines[start-1:end]):
                linestr = str(i+start)
                # Highlight current line:
                if i + start == lineno:
                    linestr = '>' + linestr
                sys.stdout.write('%4s    %s' % (linestr, line))


# ...and register the command:
PyList()

def move_in_stack(move_up):
    '''Move up or down the stack (for the py-up/py-down command)'''
    frame = Frame.get_selected_python_frame()
    while frame:
        if move_up:
            iter_frame = frame.older()
        else:
            iter_frame = frame.newer()

        if not iter_frame:
            break

        if iter_frame.is_python_frame():
            # Result:
            if iter_frame.select():
                iter_frame.print_summary()
            return

        frame = iter_frame

    if move_up:
        print('Unable to find an older python frame')
    else:
        print('Unable to find a newer python frame')

class PyUp(gdb.Command):
    'Select and print the python stack frame that called this one (if any)'
    def __init__(self):
        gdb.Command.__init__ (self,
                              "py-up",
                              gdb.COMMAND_STACK,
                              gdb.COMPLETE_NONE)


    def invoke(self, args, from_tty):
        move_in_stack(move_up=True)

class PyDown(gdb.Command):
    'Select and print the python stack frame called by this one (if any)'
    def __init__(self):
        gdb.Command.__init__ (self,
                              "py-down",
                              gdb.COMMAND_STACK,
                              gdb.COMPLETE_NONE)


    def invoke(self, args, from_tty):
        move_in_stack(move_up=False)

# Not all builds of gdb have gdb.Frame.select
if hasattr(gdb.Frame, 'select'):
    PyUp()
    PyDown()

class PyBacktraceFull(gdb.Command):
    'Display the current python frame and all the frames within its call stack (if any)'
    def __init__(self):
        gdb.Command.__init__ (self,
                              "py-bt-full",
                              gdb.COMMAND_STACK,
                              gdb.COMPLETE_NONE)


    def invoke(self, args, from_tty):
        frame = Frame.get_selected_python_frame()
        while frame:
            if frame.is_python_frame():
                frame.print_summary()
            frame = frame.older()

PyBacktraceFull()

class PyBacktrace(gdb.Command):
    'Display the current python frame and all the frames within its call stack (if any)'
    def __init__(self):
        gdb.Command.__init__ (self,
                              "py-bt",
                              gdb.COMMAND_STACK,
                              gdb.COMPLETE_NONE)


    def invoke(self, args, from_tty):
        sys.stdout.write('Traceback (most recent call first):\n')
        frame = Frame.get_selected_python_frame()
        while frame:
            if frame.is_python_frame():
                frame.print_traceback()
            frame = frame.older()

PyBacktrace()

class PyPrint(gdb.Command):
    'Look up the given python variable name, and print it'
    def __init__(self):
        gdb.Command.__init__ (self,
                              "py-print",
                              gdb.COMMAND_DATA,
                              gdb.COMPLETE_NONE)


    def invoke(self, args, from_tty):
        name = str(args)

        frame = Frame.get_selected_python_frame()
        if not frame:
            print('Unable to locate python frame')
            return

        pyop_frame = frame.get_pyop()
        if not pyop_frame:
            print('Unable to read information on python frame')
            return

        pyop_var, scope = pyop_frame.get_var_by_name(name)

        if pyop_var:
            print('%s %r = %s'
                   % (scope,
                      name,
                      pyop_var.get_truncated_repr(MAX_OUTPUT_LEN)))
        else:
            print('%r not found' % name)

PyPrint()

class PyLocals(gdb.Command):
    'Look up the given python variable name, and print it'
    def __init__(self):
        gdb.Command.__init__ (self,
                              "py-locals",
                              gdb.COMMAND_DATA,
                              gdb.COMPLETE_NONE)


    def invoke(self, args, from_tty):
        name = str(args)

        frame = Frame.get_selected_python_frame()
        if not frame:
            print('Unable to locate python frame')
            return

        pyop_frame = frame.get_pyop()
        if not pyop_frame:
            print('Unable to read information on python frame')
            return

        for pyop_name, pyop_value in pyop_frame.iter_locals():
            print('%s = %s'
                   % (pyop_name.proxyval(set()),
                      pyop_value.get_truncated_repr(MAX_OUTPUT_LEN)))

PyLocals()
