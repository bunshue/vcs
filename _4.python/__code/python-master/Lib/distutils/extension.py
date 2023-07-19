import os
import sys
import warnings

class Extension:
    def __init__(self, name, sources,
                  include_dirs=None,
                  define_macros=None,
                  undef_macros=None,
                  library_dirs=None,
                  libraries=None,
                  runtime_library_dirs=None,
                  extra_objects=None,
                  extra_compile_args=None,
                  extra_link_args=None,
                  export_symbols=None,
                  swig_opts = None,
                  depends=None,
                  language=None,
                  optional=None,
                  **kw                      # To catch unknown keywords
                 ):
        if not isinstance(name, str):
            raise AssertionError("'name' must be a string")
        if not (isinstance(sources, list) and
                all(isinstance(v, str) for v in sources)):
            raise AssertionError("'sources' must be a list of strings")

        self.name = name
        self.sources = sources
        self.include_dirs = include_dirs or []
        self.define_macros = define_macros or []
        self.undef_macros = undef_macros or []
        self.library_dirs = library_dirs or []
        self.libraries = libraries or []
        self.runtime_library_dirs = runtime_library_dirs or []
        self.extra_objects = extra_objects or []
        self.extra_compile_args = extra_compile_args or []
        self.extra_link_args = extra_link_args or []
        self.export_symbols = export_symbols or []
        self.swig_opts = swig_opts or []
        self.depends = depends or []
        self.language = language
        self.optional = optional

        # If there are unknown keyword options, warn about them
        if len(kw) > 0:
            options = [repr(option) for option in kw]
            options = ', '.join(sorted(options))
            msg = "Unknown Extension options: %s" % options
            warnings.warn(msg)

def read_setup_file(filename):
    """Reads a Setup file and returns Extension instances."""
    from distutils.sysconfig import (parse_makefile, expand_makefile_vars,
                                     _variable_rx)

    from distutils.text_file import TextFile
    from distutils.util import split_quoted

    # First pass over the file to gather "VAR = VALUE" assignments.
    vars = parse_makefile(filename)

    # Second pass to gobble up the real content: lines of the form
    #   <module> ... [<sourcefile> ...] [<cpparg> ...] [<library> ...]
    file = TextFile(filename,
                    strip_comments=1, skip_blanks=1, join_lines=1,
                    lstrip_ws=1, rstrip_ws=1)
    try:
        extensions = []

        while True:
            line = file.readline()
            if line is None:                # eof
                break
            if _variable_rx.match(line):    # VAR=VALUE, handled in first pass
                continue

            if line[0] == line[-1] == "*":
                file.warn("'%s' lines not handled yet" % line)
                continue

            line = expand_makefile_vars(line, vars)
            words = split_quoted(line)

            # NB. this parses a slightly different syntax than the old
            # makesetup script: here, there must be exactly one extension per
            # line, and it must be the first word of the line.  I have no idea
            # why the old syntax supported multiple extensions per line, as
            # they all wind up being the same.

            module = words[0]
            ext = Extension(module, [])
            append_next_word = None

            for word in words[1:]:
                if append_next_word is not None:
                    append_next_word.append(word)
                    append_next_word = None
                    continue

                suffix = os.path.splitext(word)[1]
                switch = word[0:2] ; value = word[2:]

                if suffix in (".c", ".cc", ".cpp", ".cxx", ".c++", ".m", ".mm"):
                    # hmm, should we do something about C vs. C++ sources?
                    # or leave it up to the CCompiler implementation to
                    # worry about?
                    ext.sources.append(word)
                elif switch == "-I":
                    ext.include_dirs.append(value)
                elif switch == "-D":
                    equals = value.find("=")
                    if equals == -1:        # bare "-DFOO" -- no value
                        ext.define_macros.append((value, None))
                    else:                   # "-DFOO=blah"
                        ext.define_macros.append((value[0:equals],
                                                  value[equals+2:]))
                elif switch == "-U":
                    ext.undef_macros.append(value)
                elif switch == "-C":        # only here 'cause makesetup has it!
                    ext.extra_compile_args.append(word)
                elif switch == "-l":
                    ext.libraries.append(value)
                elif switch == "-L":
                    ext.library_dirs.append(value)
                elif switch == "-R":
                    ext.runtime_library_dirs.append(value)
                elif word == "-rpath":
                    append_next_word = ext.runtime_library_dirs
                elif word == "-Xlinker":
                    append_next_word = ext.extra_link_args
                elif word == "-Xcompiler":
                    append_next_word = ext.extra_compile_args
                elif switch == "-u":
                    ext.extra_link_args.append(word)
                    if not value:
                        append_next_word = ext.extra_link_args
                elif suffix in (".a", ".so", ".sl", ".o", ".dylib"):
                    # NB. a really faithful emulation of makesetup would
                    # append a .o file to extra_objects only if it
                    # had a slash in it; otherwise, it would s/.o/.c/
                    # and append it to sources.  Hmmmm.
                    ext.extra_objects.append(word)
                else:
                    file.warn("unrecognized argument '%s'" % word)

            extensions.append(ext)
    finally:
        file.close()

    return extensions
