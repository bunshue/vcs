import abc
import ast
import atexit
import collections
import contextlib
import copy
import cpp
import functools
import inspect
import io
import itertools
import os
import pprint
import re
import shlex
import string
import sys
import tempfile
import textwrap
import traceback

def indent_all_lines(s, prefix):
    """
    Returns 's', with 'prefix' prepended to all lines.

    If the last line is empty, prefix is not prepended
    to it.  (If s is blank, returns s unchanged.)

    (textwrap.indent only adds to non-blank lines.)
    """
    split = s.split('\n')
    last = split.pop()
    final = []
    for line in split:
        final.append(prefix)
        final.append(line)
        final.append('\n')
    if last:
        final.append(prefix)
        final.append(last)
    return ''.join(final)

def suffix_all_lines(s, suffix):
    """
    Returns 's', with 'suffix' appended to all lines.

    If the last line is empty, suffix is not appended
    to it.  (If s is blank, returns s unchanged.)
    """
    split = s.split('\n')
    last = split.pop()
    final = []
    for line in split:
        final.append(line)
        final.append(suffix)
        final.append('\n')
    if last:
        final.append(last)
        final.append(suffix)
    return ''.join(final)


def version_splitter(s):
    """Splits a version string into a tuple of integers.

    The following ASCII characters are allowed, and employ
    the following conversions:
        a -> -3
        b -> -2
        c -> -1
    (This permits Python-style version strings such as "1.4b3".)
    """
    version = []
    accumulator = []
    def flush():
        if not accumulator:
            raise ValueError('Unsupported version string: ' + repr(s))
        version.append(int(''.join(accumulator)))
        accumulator.clear()

    for c in s:
        if c.isdigit():
            accumulator.append(c)
        elif c == '.':
            flush()
        elif c in 'abc':
            flush()
            version.append('abc'.index(c) - 3)
        else:
            raise ValueError('Illegal character ' + repr(c) + ' in version string ' + repr(s))
    flush()
    return tuple(version)

class CRenderData:
    def __init__(self):

        # The C statements to declare variables.
        # Should be full lines with \n eol characters.
        self.declarations = []

        # The C statements required to initialize the variables before the parse call.
        # Should be full lines with \n eol characters.
        self.initializers = []

        # The C statements needed to dynamically modify the values
        # parsed by the parse call, before calling the impl.
        self.modifications = []

        # The entries for the "keywords" array for PyArg_ParseTuple.
        # Should be individual strings representing the names.
        self.keywords = []

        # The "format units" for PyArg_ParseTuple.
        # Should be individual strings that will get
        self.format_units = []

        # The varargs arguments for PyArg_ParseTuple.
        self.parse_arguments = []

        # The parameter declarations for the impl function.
        self.impl_parameters = []

        # The arguments to the impl function at the time it's called.
        self.impl_arguments = []

        # For return converters: the name of the variable that
        # should receive the value returned by the impl.
        self.return_value = "return_value"

        # For return converters: the code to convert the return
        # value from the parse function.  This is also where
        # you should check the _return_value for errors, and
        # "goto exit" if there are any.
        self.return_conversion = []

        # The C statements required to clean up after the impl call.
        self.cleanup = []


class FormatCounterFormatter(string.Formatter):
    """
    This counts how many instances of each formatter
    "replacement string" appear in the format string.

    e.g. after evaluating "string {a}, {b}, {c}, {a}"
         the counts dict would now look like
         {'a': 2, 'b': 1, 'c': 1}
    """
    def __init__(self):
        self.counts = collections.Counter()

    def get_value(self, key, args, kwargs):
        self.counts[key] += 1
        return ''

class Language(metaclass=abc.ABCMeta):

    start_line = ""
    body_prefix = ""
    stop_line = ""
    checksum_line = ""

    def __init__(self, filename):
        pass

    @abc.abstractmethod
    def render(self, clinic, signatures):
        pass

    def parse_line(self, line):
        pass

    def validate(self):
        def assert_only_one(attr, *additional_fields):
            """
            Ensures that the string found at getattr(self, attr)
            contains exactly one formatter replacement string for
            each valid field.  The list of valid fields is
            ['dsl_name'] extended by additional_fields.

            e.g.
                self.fmt = "{dsl_name} {a} {b}"

                # this passes
                self.assert_only_one('fmt', 'a', 'b')

                # this fails, the format string has a {b} in it
                self.assert_only_one('fmt', 'a')

                # this fails, the format string doesn't have a {c} in it
                self.assert_only_one('fmt', 'a', 'b', 'c')

                # this fails, the format string has two {a}s in it,
                # it must contain exactly one
                self.fmt2 = '{dsl_name} {a} {a}'
                self.assert_only_one('fmt2', 'a')

            """
            fields = ['dsl_name']
            fields.extend(additional_fields)
            line = getattr(self, attr)
            fcf = FormatCounterFormatter()
            fcf.format(line)
            def local_fail(should_be_there_but_isnt):
                if should_be_there_but_isnt:
                    fail("{} {} must contain {{{}}} exactly once!".format(
                        self.__class__.__name__, attr, name))
                else:
                    fail("{} {} must not contain {{{}}}!".format(
                        self.__class__.__name__, attr, name))

            for name, count in fcf.counts.items():
                if name in fields:
                    if count > 1:
                        local_fail(True)
                else:
                    local_fail(False)
            for name in fields:
                if fcf.counts.get(name) != 1:
                    local_fail(True)

        assert_only_one('start_line')
        assert_only_one('stop_line')

        field = "arguments" if "{arguments}" in self.checksum_line else "checksum"
        assert_only_one('checksum_line', field)



class PythonLanguage(Language):

    language      = 'Python'
    start_line    = "#/*[{dsl_name} input]"
    body_prefix   = "#"
    stop_line     = "#[{dsl_name} start generated code]*/"
    checksum_line = "#/*[{dsl_name} end generated code: {arguments}]*/"


def permute_left_option_groups(l):
    """
    Given [1, 2, 3], should yield:
       ()
       (3,)
       (2, 3)
       (1, 2, 3)
    """
    yield tuple()
    accumulator = []
    for group in reversed(l):
        accumulator = list(group) + accumulator
        yield tuple(accumulator)


def permute_right_option_groups(l):
    """
    Given [1, 2, 3], should yield:
      ()
      (1,)
      (1, 2)
      (1, 2, 3)
    """
    yield tuple()
    accumulator = []
    for group in l:
        accumulator.extend(group)
        yield tuple(accumulator)


def permute_optional_groups(left, required, right):
    """
    Generator function that computes the set of acceptable
    argument lists for the provided iterables of
    argument groups.  (Actually it generates a tuple of tuples.)

    Algorithm: prefer left options over right options.

    If required is empty, left must also be empty.
    """
    required = tuple(required)
    result = []

    if not required:
        assert not left

    accumulator = []
    counts = set()
    for r in permute_right_option_groups(right):
        for l in permute_left_option_groups(left):
            t = l + required + r
            if len(t) in counts:
                continue
            counts.add(len(t))
            accumulator.append(t)

    accumulator.sort(key=len)
    return tuple(accumulator)


def strip_leading_and_trailing_blank_lines(s):
    lines = s.rstrip().split('\n')
    while lines:
        line = lines[0]
        if line.strip():
            break
        del lines[0]
    return '\n'.join(lines)

@functools.lru_cache()
def normalize_snippet(s, *, indent=0):
    """
    Reformats s:
        * removes leading and trailing blank lines
        * ensures that it does not end with a newline
        * dedents so the first nonwhite character on any line is at column "indent"
    """
    s = strip_leading_and_trailing_blank_lines(s)
    s = textwrap.dedent(s)
    if indent:
        s = textwrap.indent(s, ' ' * indent)
    return s


class CLanguage(Language):

    body_prefix   = "#"
    language      = 'C'
    start_line    = "/*[{dsl_name} input]"
    body_prefix   = ""
    stop_line     = "[{dsl_name} start generated code]*/"
    checksum_line = "/*[{dsl_name} end generated code: {arguments}]*/"

    def __init__(self, filename):
        super().__init__(filename)
        self.cpp = cpp.Monitor(filename)
        self.cpp.fail = fail

    def parse_line(self, line):
        self.cpp.writeline(line)

    def render(self, clinic, signatures):
        function = None
        for o in signatures:
            if isinstance(o, Function):
                if function:
                    fail("You may specify at most one function per block.\nFound a block containing at least two:\n\t" + repr(function) + " and " + repr(o))
                function = o
        return self.render_function(clinic, function)

    def docstring_for_c_string(self, f):
        text, add, output = _text_accumulator()
        # turn docstring into a properly quoted C string
        for line in f.docstring.split('\n'):
            add('"')
            add(quoted_for_c_string(line))
            add('\\n"\n')

        text.pop()
        add('"')
        return ''.join(text)

    def output_templates(self, f):
        parameters = list(f.parameters.values())
        assert parameters
        assert isinstance(parameters[0].converter, self_converter)
        del parameters[0]
        converters = [p.converter for p in parameters]

        has_option_groups = parameters and (parameters[0].group or parameters[-1].group)
        default_return_converter = (not f.return_converter or
            f.return_converter.type == 'PyObject *')

        positional = parameters and (parameters[-1].kind == inspect.Parameter.POSITIONAL_ONLY)
        all_boring_objects = False # yes, this will be false if there are 0 parameters, it's fine
        first_optional = len(parameters)
        for i, p in enumerate(parameters):
            c = p.converter
            if type(c) != object_converter:
                break
            if c.format_unit != 'O':
                break
            if p.default is not unspecified:
                first_optional = min(first_optional, i)
        else:
            all_boring_objects = True

        new_or_init = f.kind in (METHOD_NEW, METHOD_INIT)

        meth_o = (len(parameters) == 1 and
              parameters[0].kind == inspect.Parameter.POSITIONAL_ONLY and
              not converters[0].is_optional() and
              isinstance(converters[0], object_converter) and
              converters[0].format_unit == 'O' and
              not new_or_init)

        # we have to set these things before we're done:
        #
        # docstring_prototype
        # docstring_definition
        # impl_prototype
        # methoddef_define
        # parser_prototype
        # parser_definition
        # impl_definition
        # cpp_if
        # cpp_endif
        # methoddef_ifndef

        return_value_declaration = "PyObject *return_value = NULL;"

        methoddef_define = normalize_snippet("""
            #define {methoddef_name}    \\
                {{"{name}", (PyCFunction){c_basename}, {methoddef_flags}, {c_basename}__doc__}},
            """)
        if new_or_init and not f.docstring:
            docstring_prototype = docstring_definition = ''
        else:
            docstring_prototype = normalize_snippet("""
                PyDoc_VAR({c_basename}__doc__);
                """)
            docstring_definition = normalize_snippet("""
                PyDoc_STRVAR({c_basename}__doc__,
                {docstring});
                """)
        impl_definition = normalize_snippet("""
            static {impl_return_type}
            {c_basename}_impl({impl_parameters})
            """)
        impl_prototype = parser_prototype = parser_definition = None

        parser_prototype_keyword = normalize_snippet("""
            static PyObject *
            {c_basename}({self_type}{self_name}, PyObject *args, PyObject *kwargs)
            """)

        parser_prototype_varargs = normalize_snippet("""
            static PyObject *
            {c_basename}({self_type}{self_name}, PyObject *args)
            """)

        # parser_body_fields remembers the fields passed in to the
        # previous call to parser_body. this is used for an awful hack.
        parser_body_fields = ()
        def parser_body(prototype, *fields):
            nonlocal parser_body_fields
            add, output = text_accumulator()
            add(prototype)
            parser_body_fields = fields

            fields = list(fields)
            fields.insert(0, normalize_snippet("""
                {{
                    {return_value_declaration}
                    {declarations}
                    {initializers}
                """) + "\n")
            # just imagine--your code is here in the middle
            fields.append(normalize_snippet("""
                    {modifications}
                    {return_value} = {c_basename}_impl({impl_arguments});
                    {return_conversion}

                {exit_label}
                    {cleanup}
                    return return_value;
                }}
                """))
            for field in fields:
                add('\n')
                add(field)
            return output()

        def insert_keywords(s):
            return linear_format(s, declarations="static char *_keywords[] = {{{keywords}, NULL}};\n{declarations}")

        if not parameters:
            # no parameters, METH_NOARGS

            flags = "METH_NOARGS"

            parser_prototype = normalize_snippet("""
                static PyObject *
                {c_basename}({self_type}{self_name}, PyObject *Py_UNUSED(ignored))
                """)
            parser_definition = parser_prototype

            if default_return_converter:
                parser_definition = parser_prototype + '\n' + normalize_snippet("""
                    {{
                        return {c_basename}_impl({impl_arguments});
                    }}
                    """)
            else:
                parser_definition = parser_body(parser_prototype)

        elif meth_o:
            flags = "METH_O"

            meth_o_prototype = normalize_snippet("""
                static PyObject *
                {c_basename}({impl_parameters})
                """)

            if default_return_converter:
                # maps perfectly to METH_O, doesn't need a return converter.
                # so we skip making a parse function
                # and call directly into the impl function.
                impl_prototype = parser_prototype = parser_definition = ''
                impl_definition = meth_o_prototype
            else:
                # SLIGHT HACK
                # use impl_parameters for the parser here!
                parser_prototype = meth_o_prototype
                parser_definition = parser_body(parser_prototype)

        elif has_option_groups:
            # positional parameters with option groups
            # (we have to generate lots of PyArg_ParseTuple calls
            #  in a big switch statement)

            flags = "METH_VARARGS"
            parser_prototype = parser_prototype_varargs

            parser_definition = parser_body(parser_prototype, '    {option_group_parsing}')

        elif positional and all_boring_objects:
            # positional-only, but no option groups,
            # and nothing but normal objects:
            # PyArg_UnpackTuple!

            flags = "METH_VARARGS"
            parser_prototype = parser_prototype_varargs

            parser_definition = parser_body(parser_prototype, normalize_snippet("""
                if (!PyArg_UnpackTuple(args, "{name}",
                    {unpack_min}, {unpack_max},
                    {parse_arguments}))
                    goto exit;
                """, indent=4))

        elif positional:
            # positional-only, but no option groups
            # we only need one call to PyArg_ParseTuple

            flags = "METH_VARARGS"
            parser_prototype = parser_prototype_varargs

            parser_definition = parser_body(parser_prototype, normalize_snippet("""
                if (!PyArg_ParseTuple(args,
                    "{format_units}:{name}",
                    {parse_arguments}))
                    goto exit;
                """, indent=4))

        else:
            # positional-or-keyword arguments
            flags = "METH_VARARGS|METH_KEYWORDS"

            parser_prototype = parser_prototype_keyword

            body = normalize_snippet("""
                if (!PyArg_ParseTupleAndKeywords(args, kwargs,
                    "{format_units}:{name}", _keywords,
                    {parse_arguments}))
                    goto exit;
            """, indent=4)
            parser_definition = parser_body(parser_prototype, normalize_snippet("""
                if (!PyArg_ParseTupleAndKeywords(args, kwargs,
                    "{format_units}:{name}", _keywords,
                    {parse_arguments}))
                    goto exit;
                """, indent=4))
            parser_definition = insert_keywords(parser_definition)


        if new_or_init:
            methoddef_define = ''

            if f.kind == METHOD_NEW:
                parser_prototype = parser_prototype_keyword
            else:
                return_value_declaration = "int return_value = -1;"
                parser_prototype = normalize_snippet("""
                    static int
                    {c_basename}({self_type}{self_name}, PyObject *args, PyObject *kwargs)
                    """)

            fields = list(parser_body_fields)
            parses_positional = 'METH_NOARGS' not in flags
            parses_keywords = 'METH_KEYWORDS' in flags
            if parses_keywords:
                assert parses_positional

            if not parses_keywords:
                fields.insert(0, normalize_snippet("""
                    if ({self_type_check}!_PyArg_NoKeywords("{name}", kwargs))
                        goto exit;
                    """, indent=4))
                if not parses_positional:
                    fields.insert(0, normalize_snippet("""
                        if ({self_type_check}!_PyArg_NoPositional("{name}", args))
                            goto exit;
                        """, indent=4))

            parser_definition = parser_body(parser_prototype, *fields)
            if parses_keywords:
                parser_definition = insert_keywords(parser_definition)


        if f.methoddef_flags:
            flags += '|' + f.methoddef_flags

        methoddef_define = methoddef_define.replace('{methoddef_flags}', flags)

        methoddef_ifndef = ''
        conditional = self.cpp.condition()
        if not conditional:
            cpp_if = cpp_endif = ''
        else:
            cpp_if = "#if " + conditional
            cpp_endif = "#endif /* " + conditional + " */"

            if methoddef_define:
                methoddef_ifndef = normalize_snippet("""
                    #ifndef {methoddef_name}
                        #define {methoddef_name}
                    #endif /* !defined({methoddef_name}) */
                    """)


        # add ';' to the end of parser_prototype and impl_prototype
        # (they mustn't be None, but they could be an empty string.)
        assert parser_prototype is not None
        if parser_prototype:
            assert not parser_prototype.endswith(';')
            parser_prototype += ';'

        if impl_prototype is None:
            impl_prototype = impl_definition
        if impl_prototype:
            impl_prototype += ";"

        parser_definition = parser_definition.replace("{return_value_declaration}", return_value_declaration)

        d = {
            "docstring_prototype" : docstring_prototype,
            "docstring_definition" : docstring_definition,
            "impl_prototype" : impl_prototype,
            "methoddef_define" : methoddef_define,
            "parser_prototype" : parser_prototype,
            "parser_definition" : parser_definition,
            "impl_definition" : impl_definition,
            "cpp_if" : cpp_if,
            "cpp_endif" : cpp_endif,
            "methoddef_ifndef" : methoddef_ifndef,
        }

        # make sure we didn't forget to assign something,
        # and wrap each non-empty value in \n's
        d2 = {}
        for name, value in d.items():
            assert value is not None, "got a None value for template " + repr(name)
            if value:
                value = '\n' + value + '\n'
            d2[name] = value
        return d2

    @staticmethod
    def group_to_variable_name(group):
        adjective = "left_" if group < 0 else "right_"
        return "group_" + adjective + str(abs(group))

    def render_option_group_parsing(self, f, template_dict):
        # positional only, grouped, optional arguments!
        # can be optional on the left or right.
        # here's an example:
        #
        # [ [ [ A1 A2 ] B1 B2 B3 ] C1 C2 ] D1 D2 D3 [ E1 E2 E3 [ F1 F2 F3 ] ]
        #
        # Here group D are required, and all other groups are optional.
        # (Group D's "group" is actually None.)
        # We can figure out which sets of arguments we have based on
        # how many arguments are in the tuple.
        #
        # Note that you need to count up on both sides.  For example,
        # you could have groups C+D, or C+D+E, or C+D+E+F.
        #
        # What if the number of arguments leads us to an ambiguous result?
        # Clinic prefers groups on the left.  So in the above example,
        # five arguments would map to B+C, not C+D.

        add, output = text_accumulator()
        parameters = list(f.parameters.values())
        if isinstance(parameters[0].converter, self_converter):
            del parameters[0]

        groups = []
        group = None
        left = []
        right = []
        required = []
        last = unspecified

        for p in parameters:
            group_id = p.group
            if group_id != last:
                last = group_id
                group = []
                if group_id < 0:
                    left.append(group)
                elif group_id == 0:
                    group = required
                else:
                    right.append(group)
            group.append(p)

        count_min = sys.maxsize
        count_max = -1

        add("switch (PyTuple_GET_SIZE(args)) {{\n")
        for subset in permute_optional_groups(left, required, right):
            count = len(subset)
            count_min = min(count_min, count)
            count_max = max(count_max, count)

            if count == 0:
                add("""    case 0:
        break;
""")
                continue

            group_ids = {p.group for p in subset}  # eliminate duplicates
            d = {}
            d['count'] = count
            d['name'] = f.name
            d['groups'] = sorted(group_ids)
            d['format_units'] = "".join(p.converter.format_unit for p in subset)

            parse_arguments = []
            for p in subset:
                p.converter.parse_argument(parse_arguments)
            d['parse_arguments'] = ", ".join(parse_arguments)

            group_ids.discard(0)
            lines = [self.group_to_variable_name(g) + " = 1;" for g in group_ids]
            lines = "\n".join(lines)

            s = """
    case {count}:
        if (!PyArg_ParseTuple(args, "{format_units}:{name}", {parse_arguments}))
            goto exit;
        {group_booleans}
        break;
"""[1:]
            s = linear_format(s, group_booleans=lines)
            s = s.format_map(d)
            add(s)

        add("    default:\n")
        s = '        PyErr_SetString(PyExc_TypeError, "{} requires {} to {} arguments");\n'
        add(s.format(f.full_name, count_min, count_max))
        add('        goto exit;\n')
        add("}}")
        template_dict['option_group_parsing'] = output()

    def render_function(self, clinic, f):
        if not f:
            return ""

        add, output = text_accumulator()
        data = CRenderData()

        assert f.parameters, "We should always have a 'self' at this point!"
        parameters = f.render_parameters
        converters = [p.converter for p in parameters]

        templates = self.output_templates(f)

        f_self = parameters[0]
        selfless = parameters[1:]
        assert isinstance(f_self.converter, self_converter), "No self parameter in " + repr(f.full_name) + "!"

        last_group = 0
        first_optional = len(selfless)
        positional = selfless and selfless[-1].kind == inspect.Parameter.POSITIONAL_ONLY
        new_or_init = f.kind in (METHOD_NEW, METHOD_INIT)
        default_return_converter = (not f.return_converter or
            f.return_converter.type == 'PyObject *')
        has_option_groups = False

        # offset i by -1 because first_optional needs to ignore self
        for i, p in enumerate(parameters, -1):
            c = p.converter

            if (i != -1) and (p.default is not unspecified):
                first_optional = min(first_optional, i)

            # insert group variable
            group = p.group
            if last_group != group:
                last_group = group
                if group:
                    group_name = self.group_to_variable_name(group)
                    data.impl_arguments.append(group_name)
                    data.declarations.append("int " + group_name + " = 0;")
                    data.impl_parameters.append("int " + group_name)
                    has_option_groups = True

            c.render(p, data)

        if has_option_groups and (not positional):
            fail("You cannot use optional groups ('[' and ']')\nunless all parameters are positional-only ('/').")

        # HACK
        # when we're METH_O, but have a custom return converter,
        # we use "impl_parameters" for the parsing function
        # because that works better.  but that means we must
        # suppress actually declaring the impl's parameters
        # as variables in the parsing function.  but since it's
        # METH_O, we have exactly one anyway, so we know exactly
        # where it is.
        if ("METH_O" in templates['methoddef_define'] and
            not default_return_converter):
            data.declarations.pop(0)

        template_dict = {}

        full_name = f.full_name
        template_dict['full_name'] = full_name

        if new_or_init:
            name = f.cls.name
        else:
            name = f.name

        template_dict['name'] = name

        if f.c_basename:
            c_basename = f.c_basename
        else:
            fields = full_name.split(".")
            if fields[-1] == '__new__':
                fields.pop()
            c_basename = "_".join(fields)

        template_dict['c_basename'] = c_basename

        methoddef_name = "{}_METHODDEF".format(c_basename.upper())
        template_dict['methoddef_name'] = methoddef_name

        template_dict['docstring'] = self.docstring_for_c_string(f)

        template_dict['self_name'] = template_dict['self_type'] = template_dict['self_type_check'] = ''
        f_self.converter.set_template_dict(template_dict)

        f.return_converter.render(f, data)
        template_dict['impl_return_type'] = f.return_converter.type

        template_dict['declarations'] = "\n".join(data.declarations)
        template_dict['initializers'] = "\n\n".join(data.initializers)
        template_dict['modifications'] = '\n\n'.join(data.modifications)
        template_dict['keywords'] = '"' + '", "'.join(data.keywords) + '"'
        template_dict['format_units'] = ''.join(data.format_units)
        template_dict['parse_arguments'] = ', '.join(data.parse_arguments)
        template_dict['impl_parameters'] = ", ".join(data.impl_parameters)
        template_dict['impl_arguments'] = ", ".join(data.impl_arguments)
        template_dict['return_conversion'] = "".join(data.return_conversion).rstrip()
        template_dict['cleanup'] = "".join(data.cleanup)
        template_dict['return_value'] = data.return_value

        # used by unpack tuple code generator
        ignore_self = -1 if isinstance(converters[0], self_converter) else 0
        unpack_min = first_optional
        unpack_max = len(selfless)
        template_dict['unpack_min'] = str(unpack_min)
        template_dict['unpack_max'] = str(unpack_max)

        if has_option_groups:
            self.render_option_group_parsing(f, template_dict)

        for name, destination in clinic.field_destinations.items():
            template = templates[name]
            if has_option_groups:
                template = linear_format(template,
                        option_group_parsing=template_dict['option_group_parsing'])
            template = linear_format(template,
                declarations=template_dict['declarations'],
                return_conversion=template_dict['return_conversion'],
                initializers=template_dict['initializers'],
                modifications=template_dict['modifications'],
                cleanup=template_dict['cleanup'],
                )

            # Only generate the "exit:" label
            # if we have any gotos
            need_exit_label = "goto exit;" in template
            template = linear_format(template,
                exit_label="exit:" if need_exit_label else ''
                )

            s = template.format_map(template_dict)

            if clinic.line_prefix:
                s = indent_all_lines(s, clinic.line_prefix)
            if clinic.line_suffix:
                s = suffix_all_lines(s, clinic.line_suffix)

            destination.append(s)

        return clinic.get_destination('block').dump()




@contextlib.contextmanager
def OverrideStdioWith(stdout):
    saved_stdout = sys.stdout
    sys.stdout = stdout
    try:
        yield
    finally:
        assert sys.stdout is stdout
        sys.stdout = saved_stdout


def create_regex(before, after, word=True, whole_line=True):
    """Create an re object for matching marker lines."""
    group_re = "\w+" if word else ".+"
    pattern = r'{}({}){}'
    if whole_line:
        pattern = '^' + pattern + '$'
    pattern = pattern.format(re.escape(before), group_re, re.escape(after))
    return re.compile(pattern)


class Block:
    r"""
    Represents a single block of text embedded in
    another file.  If dsl_name is None, the block represents
    verbatim text, raw original text from the file, in
    which case "input" will be the only non-false member.
    If dsl_name is not None, the block represents a Clinic
    block.

    input is always str, with embedded \n characters.
    input represents the original text from the file;
    if it's a Clinic block, it is the original text with
    the body_prefix and redundant leading whitespace removed.

    dsl_name is either str or None.  If str, it's the text
    found on the start line of the block between the square
    brackets.

    signatures is either list or None.  If it's a list,
    it may only contain clinic.Module, clinic.Class, and
    clinic.Function objects.  At the moment it should
    contain at most one of each.

    output is either str or None.  If str, it's the output
    from this block, with embedded '\n' characters.

    indent is either str or None.  It's the leading whitespace
    that was found on every line of input.  (If body_prefix is
    not empty, this is the indent *after* removing the
    body_prefix.)

    preindent is either str or None.  It's the whitespace that
    was found in front of every line of input *before* the
    "body_prefix" (see the Language object).  If body_prefix
    is empty, preindent must always be empty too.

    To illustrate indent and preindent: Assume that '_'
    represents whitespace.  If the block processed was in a
    Python file, and looked like this:
      ____#/*[python]
      ____#__for a in range(20):
      ____#____print(a)
      ____#[python]*/
    "preindent" would be "____" and "indent" would be "__".

    """
    def __init__(self, input, dsl_name=None, signatures=None, output=None, indent='', preindent=''):
        assert isinstance(input, str)
        self.input = input
        self.dsl_name = dsl_name
        self.signatures = signatures or []
        self.output = output
        self.indent = indent
        self.preindent = preindent

    def __repr__(self):
        dsl_name = self.dsl_name or "text"
        def summarize(s):
            s = repr(s)
            if len(s) > 30:
                return s[:26] + "..." + s[0]
            return s
        return "".join((
            "<Block ", dsl_name, " input=", summarize(self.input), " output=", summarize(self.output), ">"))


class BlockParser:
    """
    Block-oriented parser for Argument Clinic.
    Iterator, yields Block objects.
    """

    def __init__(self, input, language, *, verify=True):
        """
        "input" should be a str object
        with embedded \n characters.

        "language" should be a Language object.
        """
        language.validate()

        self.input = collections.deque(reversed(input.splitlines(keepends=True)))
        self.block_start_line_number = self.line_number = 0

        self.language = language
        before, _, after = language.start_line.partition('{dsl_name}')
        assert _ == '{dsl_name}'
        self.find_start_re = create_regex(before, after, whole_line=False)
        self.start_re = create_regex(before, after)
        self.verify = verify
        self.last_checksum_re = None
        self.last_dsl_name = None
        self.dsl_name = None
        self.first_block = True

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if not self.input:
                raise StopIteration

            if self.dsl_name:
                return_value = self.parse_clinic_block(self.dsl_name)
                self.dsl_name = None
                self.first_block = False
                return return_value
            block = self.parse_verbatim_block()
            if self.first_block and not block.input:
                continue
            self.first_block = False
            return block


    def is_start_line(self, line):
        match = self.start_re.match(line.lstrip())
        return match.group(1) if match else None

    def _line(self):
        self.line_number += 1
        line = self.input.pop()
        self.language.parse_line(line)
        return line

    def parse_verbatim_block(self):
        add, output = text_accumulator()
        self.block_start_line_number = self.line_number

        while self.input:
            line = self._line()
            dsl_name = self.is_start_line(line)
            if dsl_name:
                self.dsl_name = dsl_name
                break
            add(line)

        return Block(output())

    def parse_clinic_block(self, dsl_name):
        input_add, input_output = text_accumulator()
        self.block_start_line_number = self.line_number + 1
        stop_line = self.language.stop_line.format(dsl_name=dsl_name)
        body_prefix = self.language.body_prefix.format(dsl_name=dsl_name)

        def is_stop_line(line):
            # make sure to recognize stop line even if it
            # doesn't end with EOL (it could be the very end of the file)
            if not line.startswith(stop_line):
                return False
            remainder = line[len(stop_line):]
            return (not remainder) or remainder.isspace()

        # consume body of program
        while self.input:
            line = self._line()
            if is_stop_line(line) or self.is_start_line(line):
                break
            if body_prefix:
                line = line.lstrip()
                assert line.startswith(body_prefix)
                line = line[len(body_prefix):]
            input_add(line)

        # consume output and checksum line, if present.
        if self.last_dsl_name == dsl_name:
            checksum_re = self.last_checksum_re
        else:
            before, _, after = self.language.checksum_line.format(dsl_name=dsl_name, arguments='{arguments}').partition('{arguments}')
            assert _ == '{arguments}'
            checksum_re = create_regex(before, after, word=False)
            self.last_dsl_name = dsl_name
            self.last_checksum_re = checksum_re

        # scan forward for checksum line
        output_add, output_output = text_accumulator()
        arguments = None
        while self.input:
            line = self._line()
            match = checksum_re.match(line.lstrip())
            arguments = match.group(1) if match else None
            if arguments:
                break
            output_add(line)
            if self.is_start_line(line):
                break

        return Block(input_output(), dsl_name, output=output)


class BlockPrinter:

    def __init__(self, language, f=None):
        self.language = language
        self.f = f or io.StringIO()

    def print_block(self, block):
        input = block.input
        output = block.output
        dsl_name = block.dsl_name
        write = self.f.write

        assert not ((dsl_name == None) ^ (output == None)), "you must specify dsl_name and output together, dsl_name " + repr(dsl_name)

        if not dsl_name:
            write(input)
            return

        write(self.language.start_line.format(dsl_name=dsl_name))
        write("\n")

        body_prefix = self.language.body_prefix.format(dsl_name=dsl_name)
        if not body_prefix:
            write(input)
        else:
            for line in input.split('\n'):
                write(body_prefix)
                write(line)
                write("\n")

        write(self.language.stop_line.format(dsl_name=dsl_name))
        write("\n")

        input = ''.join(block.input)
        output = ''.join(block.output)
        if output:
            if not output.endswith('\n'):
                output += '\n'
            write(output)


    def write(self, text):
        self.f.write(text)


class Destination:
    def __init__(self, name, type, clinic, *args):
        self.name = name
        self.type = type
        self.clinic = clinic
        valid_types = ('buffer', 'file', 'suppress', 'two-pass')
        if type not in valid_types:
            fail("Invalid destination type " + repr(type) + " for " + name + " , must be " + ', '.join(valid_types))
        extra_arguments = 1 if type == "file" else 0
        if len(args) < extra_arguments:
            fail("Not enough arguments for destination " + name + " new " + type)
        if len(args) > extra_arguments:
            fail("Too many arguments for destination " + name + " new " + type)
        if type =='file':
            d = {}
            filename = clinic.filename
            d['path'] = filename
            dirname, basename = os.path.split(filename)
            if not dirname:
                dirname = '.'
            d['dirname'] = dirname
            d['basename'] = basename
            d['basename_root'], d['basename_extension'] = os.path.splitext(filename)
            self.filename = args[0].format_map(d)
        if type == 'two-pass':
            self.id = None

        self.text, self.append, self._dump = _text_accumulator()

    def __repr__(self):
        if self.type == 'file':
            file_repr = " " + repr(self.filename)
        else:
            file_repr = ''
        return "".join(("<Destination ", self.name, " ", self.type, file_repr, ">"))

    def clear(self):
        if self.type != 'buffer':
            fail("Can't clear destination" + self.name + " , it's not of type buffer")
        self.text.clear()


# maps strings to Language objects.
# "languages" maps the name of the language ("C", "Python").
# "extensions" maps the file extension ("c", "py").
languages = { 'C': CLanguage, 'Python': PythonLanguage }
extensions = { name: CLanguage for name in "c cc cpp cxx h hh hpp hxx".split() }
extensions['py'] = PythonLanguage


# maps strings to callables.
# these callables must be of the form:
#   def foo(name, default, *, ...)
# The callable may have any number of keyword-only parameters.
# The callable must return a CConverter object.
# The callable should not call builtins.print.
converters = {}

# maps strings to callables.
# these callables follow the same rules as those for "converters" above.
# note however that they will never be called with keyword-only parameters.
legacy_converters = {}


# maps strings to callables.
# these callables must be of the form:
#   def foo(*, ...)
# The callable may have any number of keyword-only parameters.
# The callable must return a CConverter object.
# The callable should not call builtins.print.
return_converters = {}

clinic = None
class Clinic:

    presets_text = """
preset block
everything block
docstring_prototype suppress
parser_prototype suppress
cpp_if suppress
cpp_endif suppress
methoddef_ifndef buffer

preset original
everything block
docstring_prototype suppress
parser_prototype suppress
cpp_if suppress
cpp_endif suppress
methoddef_ifndef buffer

preset file
everything file
docstring_prototype suppress
parser_prototype suppress
impl_definition block

preset buffer
everything buffer
docstring_prototype suppress
impl_prototype suppress
parser_prototype suppress
impl_definition block

preset partial-buffer
everything buffer
docstring_prototype block
impl_prototype suppress
methoddef_define block
parser_prototype block
impl_definition block

preset two-pass
everything buffer
docstring_prototype two-pass
impl_prototype suppress
methoddef_define two-pass
parser_prototype two-pass
impl_definition block

"""

    def __init__(self, language, printer=None, *, force=False, verify=True, filename=None):
        # maps strings to Parser objects.
        # (instantiated from the "parsers" global.)
        self.parsers = {}
        self.language = language
        if printer:
            fail("Custom printers are broken right now")
        self.printer = printer or BlockPrinter(language)
        self.verify = verify
        self.force = force
        self.filename = filename
        self.modules = collections.OrderedDict()
        self.classes = collections.OrderedDict()
        self.functions = []

        self.line_prefix = self.line_suffix = ''

        self.destinations = {}
        self.add_destination("block", "buffer")
        self.add_destination("suppress", "suppress")
        self.add_destination("buffer", "buffer")
        self.add_destination("two-pass", "two-pass")
        if filename:
            self.add_destination("file", "file", "{dirname}/clinic/{basename}.h")

        d = self.destinations.get
        self.field_destinations = collections.OrderedDict((
            ('cpp_if', d('suppress')),
            ('docstring_prototype', d('suppress')),
            ('docstring_definition', d('block')),
            ('methoddef_define', d('block')),
            ('impl_prototype', d('block')),
            ('parser_prototype', d('suppress')),
            ('parser_definition', d('block')),
            ('cpp_endif', d('suppress')),
            ('methoddef_ifndef', d('buffer')),
            ('impl_definition', d('block')),
        ))

        self.field_destinations_stack = []

        self.presets = {}
        preset = None
        for line in self.presets_text.strip().split('\n'):
            line = line.strip()
            if not line:
                continue
            name, value = line.split()
            if name == 'preset':
                self.presets[value] = preset = collections.OrderedDict()
                continue

            destination = self.get_destination(value)

            if name == 'everything':
                for name in self.field_destinations:
                    preset[name] = destination
                continue

            assert name in self.field_destinations
            preset[name] = destination

        global clinic
        clinic = self

    def parse(self, input):
        printer = self.printer
        self.block_parser = BlockParser(input, self.language, verify=self.verify)
        for block in self.block_parser:
            dsl_name = block.dsl_name
            if dsl_name:
                if dsl_name not in self.parsers:
                    assert dsl_name in parsers, "No parser to handle {!r} block.".format(dsl_name)
                    self.parsers[dsl_name] = parsers[dsl_name](self)
                parser = self.parsers[dsl_name]
                try:
                    parser.parse(block)
                except Exception:
                    fail('Exception raised during parsing:\n' +
                         traceback.format_exc().rstrip())
            printer.print_block(block)

        second_pass_replacements = {}

        for name, destination in self.destinations.items():
            if destination.type == 'suppress':
                continue
            output = destination._dump()

            if destination.type == 'two-pass':
                if destination.id:
                    second_pass_replacements[destination.id] = output
                elif output:
                    fail("Two-pass buffer " + repr(name) + " not empty at end of file!")
                continue

            if output:

                block = Block("", dsl_name="clinic", output=output)

                if destination.type == 'buffer':
                    block.input = "dump " + name + "\n"
                    warn("Destination buffer " + repr(name) + " not empty at end of file, emptying.")
                    printer.write("\n")
                    printer.print_block(block)
                    continue

                if destination.type == 'file':
                    try:
                        dirname = os.path.dirname(destination.filename)
                        try:
                            os.makedirs(dirname)
                        except FileExistsError:
                            if not os.path.isdir(dirname):
                                fail("Can't write to destination {}, "
                                     "can't make directory {}!".format(
                                        destination.filename, dirname))
                        if self.verify:
                            with open(destination.filename, "rt") as f:
                                parser_2 = BlockParser(f.read(), language=self.language)
                                blocks = list(parser_2)
                                if (len(blocks) != 1) or (blocks[0].input != 'preserve\n'):
                                    fail("Modified destination file " + repr(destination.filename) + ", not overwriting!")
                    except FileNotFoundError:
                        pass

                    block.input = 'preserve\n'
                    printer_2 = BlockPrinter(self.language)
                    printer_2.print_block(block)
                    with open(destination.filename, "wt") as f:
                        f.write(printer_2.f.getvalue())
                    continue
        text = printer.f.getvalue()

        if second_pass_replacements:
            printer_2 = BlockPrinter(self.language)
            parser_2 = BlockParser(text, self.language)
            changed = False
            for block in parser_2:
                if block.dsl_name:
                    for id, replacement in second_pass_replacements.items():
                        if id in block.output:
                            changed = True
                            block.output = block.output.replace(id, replacement)
                printer_2.print_block(block)
            if changed:
                text = printer_2.f.getvalue()

        return text


    def _module_and_class(self, fields):
        """
        fields should be an iterable of field names.
        returns a tuple of (module, class).
        the module object could actually be self (a clinic object).
        this function is only ever used to find the parent of where
        a new class/module should go.
        """
        in_classes = False
        parent = module = self
        cls = None
        so_far = []

        for field in fields:
            so_far.append(field)
            if not in_classes:
                child = parent.modules.get(field)
                if child:
                    parent = module = child
                    continue
                in_classes = True
            if not hasattr(parent, 'classes'):
                return module, cls
            child = parent.classes.get(field)
            if not child:
                fail('Parent class or module ' + '.'.join(so_far) + " does not exist.")
            cls = parent = child

        return module, cls


class PythonParser:
    def __init__(self, clinic):
        pass

    def parse(self, block):
        s = io.StringIO()
        with OverrideStdioWith(s):
            exec(block.input)
        block.output = s.getvalue()


class Module:
    def __init__(self, name, module=None):
        self.name = name
        self.module = self.parent = module

        self.modules = collections.OrderedDict()
        self.classes = collections.OrderedDict()
        self.functions = []

    def __repr__(self):
        return "<clinic.Module " + repr(self.name) + " at " + str(id(self)) + ">"

class Class:
    def __init__(self, name, module=None, cls=None, typedef=None, type_object=None):
        self.name = name
        self.module = module
        self.cls = cls
        self.typedef = typedef
        self.type_object = type_object
        self.parent = cls or module

        self.classes = collections.OrderedDict()
        self.functions = []

    def __repr__(self):
        return "<clinic.Class " + repr(self.name) + " at " + str(id(self)) + ">"

unsupported_special_methods = set("""

__abs__
__add__
__and__
__bytes__
__call__
__complex__
__delitem__
__divmod__
__eq__
__float__
__floordiv__
__ge__
__getattr__
__getattribute__
__getitem__
__gt__
__hash__
__iadd__
__iand__
__idivmod__
__ifloordiv__
__ilshift__
__imod__
__imul__
__index__
__int__
__invert__
__ior__
__ipow__
__irshift__
__isub__
__iter__
__itruediv__
__ixor__
__le__
__len__
__lshift__
__lt__
__mod__
__mul__
__neg__
__new__
__next__
__or__
__pos__
__pow__
__radd__
__rand__
__rdivmod__
__repr__
__rfloordiv__
__rlshift__
__rmod__
__rmul__
__ror__
__round__
__rpow__
__rrshift__
__rshift__
__rsub__
__rtruediv__
__rxor__
__setattr__
__setitem__
__str__
__sub__
__truediv__
__xor__

""".strip().split())


INVALID, CALLABLE, STATIC_METHOD, CLASS_METHOD, METHOD_INIT, METHOD_NEW = """
INVALID, CALLABLE, STATIC_METHOD, CLASS_METHOD, METHOD_INIT, METHOD_NEW
""".replace(",", "").strip().split()

class LandMine:
    # try to access any
    def __init__(self, message):
        self.__message__ = message

    def __repr__(self):
        return '<LandMine ' + repr(self.__message__) + ">"

    def __getattribute__(self, name):
        if name in ('__repr__', '__message__'):
            return super().__getattribute__(name)
        # raise RuntimeError(repr(name))
        fail("Stepped on a land mine, trying to access attribute " + repr(name) + ":\n" + self.__message__)


def add_c_converter(f, name=None):
    if not name:
        name = f.__name__
        if not name.endswith('_converter'):
            return f
        name = name[:-len('_converter')]
    converters[name] = f
    return f

def add_default_legacy_c_converter(cls):
    # automatically add converter for default format unit
    # (but without stomping on the existing one if it's already
    # set, in case you subclass)
    if ((cls.format_unit not in ('O&', '')) and
        (cls.format_unit not in legacy_converters)):
        legacy_converters[cls.format_unit] = cls
    return cls

def add_legacy_c_converter(format_unit, **kwargs):
    """
    Adds a legacy converter.
    """
    def closure(f):
        if not kwargs:
            added_f = f
        else:
            added_f = functools.partial(f, **kwargs)
        if format_unit:
            legacy_converters[format_unit] = added_f
        return f
    return closure

class CConverterAutoRegister(type):
    def __init__(cls, name, bases, classdict):
        add_c_converter(cls)
        add_default_legacy_c_converter(cls)

def correct_name_for_self(f):
    if f.kind in (CALLABLE, METHOD_INIT):
        if f.cls:
            return "PyObject *", "self"
        return "PyModuleDef *", "module"
    if f.kind == STATIC_METHOD:
        return "void *", "null"
    if f.kind in (CLASS_METHOD, METHOD_NEW):
        return "PyTypeObject *", "type"
    raise RuntimeError("Unhandled type of function f: " + repr(f.kind))

def required_type_for_self_for_parser(f):
    type, _ = correct_name_for_self(f)
    if f.kind in (METHOD_INIT, METHOD_NEW, STATIC_METHOD, CLASS_METHOD):
        return type
    return None


def add_c_return_converter(f, name=None):
    if not name:
        name = f.__name__
        if not name.endswith('_return_converter'):
            return f
        name = name[:-len('_return_converter')]
    return_converters[name] = f
    return f


class CReturnConverterAutoRegister(type):
    def __init__(cls, name, bases, classdict):
        add_c_return_converter(cls)

class CReturnConverter(metaclass=CReturnConverterAutoRegister):

    # The C type to use for this variable.
    # 'type' should be a Python string specifying the type, e.g. "int".
    # If this is a pointer type, the type string should end with ' *'.
    type = 'PyObject *'

    # The Python default value for this parameter, as a Python value.
    # Or the magic value "unspecified" if there is no default.
    default = None

    def __init__(self, *, py_default=None, **kwargs):
        self.py_default = py_default
        try:
            self.return_converter_init(**kwargs)
        except TypeError as e:
            s = ', '.join(name + '=' + repr(value) for name, value in kwargs.items())
            sys.exit(self.__class__.__name__ + '(' + s + ')\n' + str(e))

    def return_converter_init(self):
        pass

    def declare(self, data, name="_return_value"):
        line = []
        add = line.append
        add(self.type)
        if not self.type.endswith('*'):
            add(' ')
        add(name + ';')
        data.declarations.append(''.join(line))
        data.return_value = name

    def err_occurred_if(self, expr, data):
        data.return_conversion.append('if (({}) && PyErr_Occurred())\n    goto exit;\n'.format(expr))

    def err_occurred_if_null_pointer(self, variable, data):
        data.return_conversion.append('if ({} == NULL)\n    goto exit;\n'.format(variable))

    def render(self, function, data):
        """
        function is a clinic.Function instance.
        data is a CRenderData instance.
        """
        pass

add_c_return_converter(CReturnConverter, 'object')

class NoneType_return_converter(CReturnConverter):
    def render(self, function, data):
        self.declare(data)
        data.return_conversion.append('''
if (_return_value != Py_None)
    goto exit;
return_value = Py_None;
Py_INCREF(Py_None);
'''.strip())

class bool_return_converter(CReturnConverter):
    type = 'int'

    def render(self, function, data):
        self.declare(data)
        self.err_occurred_if("_return_value == -1", data)
        data.return_conversion.append('return_value = PyBool_FromLong((long)_return_value);\n')

class long_return_converter(CReturnConverter):
    type = 'long'
    conversion_fn = 'PyLong_FromLong'
    cast = ''

    def render(self, function, data):
        self.declare(data)
        self.err_occurred_if("_return_value == -1", data)
        data.return_conversion.append(
            ''.join(('return_value = ', self.conversion_fn, '(', self.cast, '_return_value);\n')))

class int_return_converter(long_return_converter):
    type = 'int'
    cast = '(long)'

class init_return_converter(long_return_converter):
    """
    Special return converter for __init__ functions.
    """
    type = 'int'
    cast = '(long)'

    def render(self, function, data):
        pass

class unsigned_long_return_converter(long_return_converter):
    type = 'unsigned long'
    conversion_fn = 'PyLong_FromUnsignedLong'

class unsigned_int_return_converter(unsigned_long_return_converter):
    type = 'unsigned int'
    cast = '(unsigned long)'

class Py_ssize_t_return_converter(long_return_converter):
    type = 'Py_ssize_t'
    conversion_fn = 'PyLong_FromSsize_t'

class size_t_return_converter(long_return_converter):
    type = 'size_t'
    conversion_fn = 'PyLong_FromSize_t'


class double_return_converter(CReturnConverter):
    type = 'double'
    cast = ''

    def render(self, function, data):
        self.declare(data)
        self.err_occurred_if("_return_value == -1.0", data)
        data.return_conversion.append(
            'return_value = PyFloat_FromDouble(' + self.cast + '_return_value);\n')

class float_return_converter(double_return_converter):
    type = 'float'
    cast = '(double)'


class DecodeFSDefault_return_converter(CReturnConverter):
    type = 'char *'

    def render(self, function, data):
        self.declare(data)
        self.err_occurred_if_null_pointer("_return_value", data)
        data.return_conversion.append(
            'return_value = PyUnicode_DecodeFSDefault(_return_value);\n')


class IndentStack:
    def __init__(self):
        self.indents = []
        self.margin = None

    def _ensure(self):
        if not self.indents:
            fail('IndentStack expected indents, but none are defined.')

    def measure(self, line):
        """
        Returns the length of the line's margin.
        """
        if '\t' in line:
            fail('Tab characters are illegal in the Argument Clinic DSL.')
        stripped = line.lstrip()
        if not len(stripped):
            # we can't tell anything from an empty line
            # so just pretend it's indented like our current indent
            self._ensure()
            return self.indents[-1]
        return len(line) - len(stripped)

    def infer(self, line):
        """
        Infer what is now the current margin based on this line.
        Returns:
            1 if we have indented (or this is the first margin)
            0 if the margin has not changed
           -N if we have dedented N times
        """
        indent = self.measure(line)
        margin = ' ' * indent
        if not self.indents:
            self.indents.append(indent)
            self.margin = margin
            return 1
        current = self.indents[-1]
        if indent == current:
            return 0
        if indent > current:
            self.indents.append(indent)
            self.margin = margin
            return 1
        # indent < current
        if indent not in self.indents:
            fail("Illegal outdent.")
        outdent_count = 0
        while indent != current:
            self.indents.pop()
            current = self.indents[-1]
            outdent_count -= 1
        self.margin = margin
        return outdent_count

    @property
    def depth(self):
        """
        Returns how many margins are currently defined.
        """
        return len(self.indents)

    def indent(self, line):
        """
        Indents a line by the currently defined margin.
        """
        return self.margin + line

    def dedent(self, line):
        """
        Dedents a line by the currently defined margin.
        (The inverse of 'indent'.)
        """
        margin = self.margin
        indent = self.indents[-1]
        if not line.startswith(margin):
            fail('Cannot dedent, line does not start with the previous margin:')
        return line[indent:]


class DSLParser:
    def __init__(self, clinic):
        self.clinic = clinic

        self.directives = {}
        for name in dir(self):
            # functions that start with directive_ are added to directives
            _, s, key = name.partition("directive_")
            if s:
                self.directives[key] = getattr(self, name)

            # functions that start with at_ are too, with an @ in front
            _, s, key = name.partition("at_")
            if s:
                self.directives['@' + key] = getattr(self, name)

        self.reset()

    def reset(self):
        self.function = None
        self.state = self.state_dsl_start
        self.parameter_indent = None
        self.keyword_only = False
        self.group = 0
        self.parameter_state = self.ps_start
        self.seen_positional_with_default = False
        self.indent = IndentStack()
        self.kind = CALLABLE
        self.coexist = False
        self.parameter_continuation = ''
        self.preserve_output = False

    def directive_module(self, name):
        fields = name.split('.')
        new = fields.pop()
        module, cls = self.clinic._module_and_class(fields)
        if cls:
            fail("Can't nest a module inside a class!")

        if name in module.classes:
            fail("Already defined module " + repr(name) + "!")

        m = Module(name, module)
        module.modules[name] = m
        self.block.signatures.append(m)

    def directive_class(self, name, typedef, type_object):
        fields = name.split('.')
        in_classes = False
        parent = self
        name = fields.pop()
        so_far = []
        module, cls = self.clinic._module_and_class(fields)

        parent = cls or module
        if name in parent.classes:
            fail("Already defined class " + repr(name) + "!")

        c = Class(name, module, cls, typedef, type_object)
        parent.classes[name] = c
        self.block.signatures.append(c)

    def directive_set(self, name, value):
        if name not in ("line_prefix", "line_suffix"):
            fail("unknown variable", repr(name))

        value = value.format_map({
            'block comment start': '/*',
            'block comment end': '*/',
            })

        self.clinic.__dict__[name] = value

    def directive_destination(self, name, command, *args):
        if command == 'new':
            self.clinic.add_destination(name, *args)
            return

        if command == 'clear':
            self.clinic.get_destination(name).clear()
        fail("unknown destination command", repr(command))


    def directive_output(self, field, destination=''):
        fd = self.clinic.field_destinations

        if field == "preset":
            preset = self.clinic.presets.get(destination)
            if not preset:
                fail("Unknown preset " + repr(destination) + "!")
            fd.update(preset)
            return

        if field == "push":
            self.clinic.field_destinations_stack.append(fd.copy())
            return

        if field == "pop":
            if not self.clinic.field_destinations_stack:
                fail("Can't 'output pop', stack is empty!")
            previous_fd = self.clinic.field_destinations_stack.pop()
            fd.update(previous_fd)
            return

        # secret command for debugging!
        if field == "print":
            self.block.output.append(pprint.pformat(fd))
            self.block.output.append('\n')
            return

        d = self.clinic.get_destination(destination)

        if field == "everything":
            for name in list(fd):
                fd[name] = d
            return

        if field not in fd:
            fail("Invalid field " + repr(field) + ", must be one of:\n  preset push pop print everything " + " ".join(fd))
        fd[field] = d

    def directive_dump(self, name):
        self.block.output.append(self.clinic.get_destination(name).dump())

    def directive_print(self, *args):
        self.block.output.append(' '.join(args))
        self.block.output.append('\n')

    def directive_preserve(self):
        if self.preserve_output:
            fail("Can't have preserve twice in one block!")
        self.preserve_output = True

    def at_classmethod(self):
        if self.kind is not CALLABLE:
            fail("Can't set @classmethod, function is not a normal callable")
        self.kind = CLASS_METHOD

    def at_staticmethod(self):
        if self.kind is not CALLABLE:
            fail("Can't set @staticmethod, function is not a normal callable")
        self.kind = STATIC_METHOD

    def at_coexist(self):
        if self.coexist:
            fail("Called @coexist twice!")
        self.coexist = True

    def parse(self, block):
        self.reset()
        self.block = block
        self.saved_output = self.block.output
        block.output = []
        block_start = self.clinic.block_parser.line_number
        lines = block.input.split('\n')
        for line_number, line in enumerate(lines, self.clinic.block_parser.block_start_line_number):
            if '\t' in line:
                fail('Tab characters are illegal in the Clinic DSL.\n\t' + repr(line), line_number=block_start)
            self.state(line)

        self.next(self.state_terminal)
        self.state(None)

        block.output.extend(self.clinic.language.render(clinic, block.signatures))

        if self.preserve_output:
            if block.output:
                fail("'preserve' only works for blocks that don't produce any output!")
            block.output = self.saved_output

    @staticmethod
    def ignore_line(line):
        # ignore comment-only lines
        if line.lstrip().startswith('#'):
            return True

        # Ignore empty lines too
        # (but not in docstring sections!)
        if not line.strip():
            return True

        return False

    @staticmethod
    def calculate_indent(line):
        return len(line) - len(line.strip())

    def next(self, state, line=None):
        # real_print(self.state.__name__, "->", state.__name__, ", line=", line)
        self.state = state
        if line is not None:
            self.state(line)

    def state_dsl_start(self, line):
        # self.block = self.ClinicOutputBlock(self)
        if self.ignore_line(line):
            return

        # is it a directive?
        fields = shlex.split(line)
        directive_name = fields[0]
        directive = self.directives.get(directive_name, None)
        if directive:
            try:
                directive(*fields[1:])
            except TypeError as e:
                fail(str(e))
            return

        self.next(self.state_modulename_name, line)

    def state_modulename_name(self, line):
        # looking for declaration, which establishes the leftmost column
        # line should be
        #     modulename.fnname [as c_basename] [-> return annotation]
        # square brackets denote optional syntax.
        #
        # alternatively:
        #     modulename.fnname [as c_basename] = modulename.existing_fn_name
        # clones the parameters and return converter from that
        # function.  you can't modify them.  you must enter a
        # new docstring.
        #
        # (but we might find a directive first!)
        #
        # this line is permitted to start with whitespace.
        # we'll call this number of spaces F (for "function").

        if not line.strip():
            return

        self.indent.infer(line)

        # are we cloning?
        before, equals, existing = line.rpartition('=')
        if equals:
            full_name, _, c_basename = before.partition(' as ')
            full_name = full_name.strip()
            c_basename = c_basename.strip()
            existing = existing.strip()
            if (is_legal_py_identifier(full_name) and
                (not c_basename or is_legal_c_identifier(c_basename)) and
                is_legal_py_identifier(existing)):
                # we're cloning!
                fields = [x.strip() for x in existing.split('.')]
                function_name = fields.pop()
                module, cls = self.clinic._module_and_class(fields)

                for existing_function in (cls or module).functions:
                    if existing_function.name == function_name:
                        break
                else:
                    existing_function = None
                if not existing_function:
                    print("class", cls, "module", module, "existing", existing)
                    print("cls. functions", cls.functions)
                    fail("Couldn't find existing function " + repr(existing) + "!")

                fields = [x.strip() for x in full_name.split('.')]
                function_name = fields.pop()
                module, cls = self.clinic._module_and_class(fields)

                if not (existing_function.kind == self.kind and existing_function.coexist == self.coexist):
                    fail("'kind' of function and cloned function don't match!  (@classmethod/@staticmethod/@coexist)")
                self.function = existing_function.copy(name=function_name, full_name=full_name, module=module, cls=cls, c_basename=c_basename, docstring='')

                self.block.signatures.append(self.function)
                (cls or module).functions.append(self.function)
                self.next(self.state_function_docstring)
                return

        line, _, returns = line.partition('->')

        full_name, _, c_basename = line.partition(' as ')
        full_name = full_name.strip()
        c_basename = c_basename.strip() or None

        if not is_legal_py_identifier(full_name):
            fail("Illegal function name: {}".format(full_name))
        if c_basename and not is_legal_c_identifier(c_basename):
            fail("Illegal C basename: {}".format(c_basename))

        return_converter = None
        if returns:
            ast_input = "def x() -> {}: pass".format(returns)
            module = None
            try:
                module = ast.parse(ast_input)
            except SyntaxError:
                pass
            if not module:
                fail("Badly-formed annotation for " + full_name + ": " + returns)
            try:
                name, legacy, kwargs = self.parse_converter(module.body[0].returns)
                if legacy:
                    fail("Legacy converter {!r} not allowed as a return converter"
                         .format(name))
                if name not in return_converters:
                    fail("No available return converter called " + repr(name))
                return_converter = return_converters[name](**kwargs)
            except ValueError:
                fail("Badly-formed annotation for " + full_name + ": " + returns)

        fields = [x.strip() for x in full_name.split('.')]
        function_name = fields.pop()
        module, cls = self.clinic._module_and_class(fields)

        fields = full_name.split('.')
        if fields[-1] == '__new__':
            if (self.kind != CLASS_METHOD) or (not cls):
                fail("__new__ must be a class method!")
            self.kind = METHOD_NEW
        elif fields[-1] == '__init__':
            if (self.kind != CALLABLE) or (not cls):
                fail("__init__ must be a normal method, not a class or static method!")
            self.kind = METHOD_INIT
            if not return_converter:
                return_converter = init_return_converter()
        elif fields[-1] in unsupported_special_methods:
            fail(fields[-1] + " is a special method and cannot be converted to Argument Clinic!  (Yet.)")

        if not return_converter:
            return_converter = CReturnConverter()

        if not module:
            fail("Undefined module used in declaration of " + repr(full_name.strip()) + ".")
        self.function = Function(name=function_name, full_name=full_name, module=module, cls=cls, c_basename=c_basename,
                                 return_converter=return_converter, kind=self.kind, coexist=self.coexist)
        self.block.signatures.append(self.function)

        # insert a self converter automatically
        type, name = correct_name_for_self(self.function)
        kwargs = {}
        if cls and type == "PyObject *":
            kwargs['type'] = cls.typedef
        sc = self.function.self_converter = self_converter(name, name, self.function, **kwargs)
        p_self = Parameter(sc.name, inspect.Parameter.POSITIONAL_ONLY, function=self.function, converter=sc)
        self.function.parameters[sc.name] = p_self

        (cls or module).functions.append(self.function)
        self.next(self.state_parameters_start)

    # Now entering the parameters section.  The rules, formally stated:
    #
    #   * All lines must be indented with spaces only.
    #   * The first line must be a parameter declaration.
    #   * The first line must be indented.
    #       * This first line establishes the indent for parameters.
    #       * We'll call this number of spaces P (for "parameter").
    #   * Thenceforth:
    #       * Lines indented with P spaces specify a parameter.
    #       * Lines indented with > P spaces are docstrings for the previous
    #         parameter.
    #           * We'll call this number of spaces D (for "docstring").
    #           * All subsequent lines indented with >= D spaces are stored as
    #             part of the per-parameter docstring.
    #           * All lines will have the first D spaces of the indent stripped
    #             before they are stored.
    #           * It's illegal to have a line starting with a number of spaces X
    #             such that P < X < D.
    #       * A line with < P spaces is the first line of the function
    #         docstring, which ends processing for parameters and per-parameter
    #         docstrings.
    #           * The first line of the function docstring must be at the same
    #             indent as the function declaration.
    #       * It's illegal to have any line in the parameters section starting
    #         with X spaces such that F < X < P.  (As before, F is the indent
    #         of the function declaration.)
    #
    # Also, currently Argument Clinic places the following restrictions on groups:
    #   * Each group must contain at least one parameter.
    #   * Each group may contain at most one group, which must be the furthest
    #     thing in the group from the required parameters.  (The nested group
    #     must be the first in the group when it's before the required
    #     parameters, and the last thing in the group when after the required
    #     parameters.)
    #   * There may be at most one (top-level) group to the left or right of
    #     the required parameters.
    #   * You must specify a slash, and it must be after all parameters.
    #     (In other words: either all parameters are positional-only,
    #      or none are.)
    #
    #  Said another way:
    #   * Each group must contain at least one parameter.
    #   * All left square brackets before the required parameters must be
    #     consecutive.  (You can't have a left square bracket followed
    #     by a parameter, then another left square bracket.  You can't
    #     have a left square bracket, a parameter, a right square bracket,
    #     and then a left square bracket.)
    #   * All right square brackets after the required parameters must be
    #     consecutive.
    #
    # These rules are enforced with a single state variable:
    # "parameter_state".  (Previously the code was a miasma of ifs and
    # separate boolean state variables.)  The states are:
    #
    #  [ [ a, b, ] c, ] d, e, f=3, [ g, h, [ i ] ] /   <- line
    # 01   2          3       4    5           6   7   <- state transitions
    #
    # 0: ps_start.  before we've seen anything.  legal transitions are to 1 or 3.
    # 1: ps_left_square_before.  left square brackets before required parameters.
    # 2: ps_group_before.  in a group, before required parameters.
    # 3: ps_required.  required parameters, positional-or-keyword or positional-only
    #     (we don't know yet).  (renumber left groups!)
    # 4: ps_optional.  positional-or-keyword or positional-only parameters that
    #    now must have default values.
    # 5: ps_group_after.  in a group, after required parameters.
    # 6: ps_right_square_after.  right square brackets after required parameters.
    # 7: ps_seen_slash.  seen slash.
    ps_start, ps_left_square_before, ps_group_before, ps_required, \
    ps_optional, ps_group_after, ps_right_square_after, ps_seen_slash = range(8)

    def state_parameters_start(self, line):
        if self.ignore_line(line):
            return

        # if this line is not indented, we have no parameters
        if not self.indent.infer(line):
            return self.next(self.state_function_docstring, line)

        self.parameter_continuation = ''
        return self.next(self.state_parameter, line)


    def to_required(self):
        """
        Transition to the "required" parameter state.
        """
        if self.parameter_state != self.ps_required:
            self.parameter_state = self.ps_required
            for p in self.function.parameters.values():
                p.group = -p.group

    def state_parameter(self, line):
        if self.parameter_continuation:
            line = self.parameter_continuation + ' ' + line.lstrip()
            self.parameter_continuation = ''

        if self.ignore_line(line):
            return

        assert self.indent.depth == 2
        indent = self.indent.infer(line)
        if indent == -1:
            # we outdented, must be to definition column
            return self.next(self.state_function_docstring, line)

        if indent == 1:
            # we indented, must be to new parameter docstring column
            return self.next(self.state_parameter_docstring_start, line)

        line = line.rstrip()
        if line.endswith('\\'):
            self.parameter_continuation = line[:-1]
            return

        line = line.lstrip()

        if line in ('*', '/', '[', ']'):
            self.parse_special_symbol(line)
            return

        if self.parameter_state in (self.ps_start, self.ps_required):
            self.to_required()
        elif self.parameter_state == self.ps_left_square_before:
            self.parameter_state = self.ps_group_before
        elif self.parameter_state == self.ps_group_before:
            if not self.group:
                self.to_required()
        elif self.parameter_state in (self.ps_group_after, self.ps_optional):
            pass
        else:
            fail("Function " + self.function.name + " has an unsupported group configuration. (Unexpected state " + str(self.parameter_state) + ".a)")

        # handle "as" for  parameters too
        c_name = None
        name, have_as_token, trailing = line.partition(' as ')
        if have_as_token:
            name = name.strip()
            if ' ' not in name:
                fields = trailing.strip().split(' ')
                if not fields:
                    fail("Invalid 'as' clause!")
                c_name = fields[0]
                if c_name.endswith(':'):
                    name += ':'
                    c_name = c_name[:-1]
                fields[0] = name
                line = ' '.join(fields)

        base, equals, default = line.rpartition('=')
        if not equals:
            base = default
            default = None

        module = None
        try:
            ast_input = "def x({}): pass".format(base)
            module = ast.parse(ast_input)
        except SyntaxError:
            try:
                # the last = was probably inside a function call, like
                #   i: int(nullable=True)
                # so assume there was no actual default value.
                default = None
                ast_input = "def x({}): pass".format(line)
                module = ast.parse(ast_input)
            except SyntaxError:
                pass
        if not module:
            fail("Function " + self.function.name + " has an invalid parameter declaration:\n\t" + line)

        function_args = module.body[0].args
        parameter = function_args.args[0]

        parameter_name = parameter.arg
        name, legacy, kwargs = self.parse_converter(parameter.annotation)

        if not default:
            if self.parameter_state == self.ps_optional:
                fail("Can't have a parameter without a default (" + repr(parameter_name) + ")\nafter a parameter with a default!")
            value = unspecified
            if 'py_default' in kwargs:
                fail("You can't specify py_default without specifying a default value!")
        else:
            if self.parameter_state == self.ps_required:
                self.parameter_state = self.ps_optional
            default = default.strip()
            bad = False
            ast_input = "x = {}".format(default)
            bad = False
            try:
                module = ast.parse(ast_input)

                if 'c_default' not in kwargs:
                    # we can only represent very simple data values in C.
                    # detect whether default is okay, via a blacklist
                    # of disallowed ast nodes.
                    class DetectBadNodes(ast.NodeVisitor):
                        bad = False
                        def bad_node(self, node):
                            self.bad = True

                        # inline function call
                        visit_Call = bad_node
                        # inline if statement ("x = 3 if y else z")
                        visit_IfExp = bad_node

                        # comprehensions and generator expressions
                        visit_ListComp = visit_SetComp = bad_node
                        visit_DictComp = visit_GeneratorExp = bad_node

                        # literals for advanced types
                        visit_Dict = visit_Set = bad_node
                        visit_List = visit_Tuple = bad_node

                        # "starred": "a = [1, 2, 3]; *a"
                        visit_Starred = bad_node

                        # allow ellipsis, for now
                        # visit_Ellipsis = bad_node

                    blacklist = DetectBadNodes()
                    blacklist.visit(module)
                    bad = blacklist.bad
                else:
                    # if they specify a c_default, we can be more lenient about the default value.
                    # but at least make an attempt at ensuring it's a valid expression.
                    try:
                        value = eval(default)
                        if value == unspecified:
                            fail("'unspecified' is not a legal default value!")
                    except NameError:
                        pass # probably a named constant
                    except Exception as e:
                        fail("Malformed expression given as default value\n"
                             "{!r} caused {!r}".format(default, e))
                if bad:
                    fail("Unsupported expression as default value: " + repr(default))

                expr = module.body[0].value
                # mild hack: explicitly support NULL as a default value
                if isinstance(expr, ast.Name) and expr.id == 'NULL':
                    value = NULL
                    py_default = 'None'
                    c_default = "NULL"
                elif (isinstance(expr, ast.BinOp) or
                    (isinstance(expr, ast.UnaryOp) and not isinstance(expr.operand, ast.Num))):
                    c_default = kwargs.get("c_default")
                    if not (isinstance(c_default, str) and c_default):
                        fail("When you specify an expression (" + repr(default) + ") as your default value,\nyou MUST specify a valid c_default.")
                    py_default = default
                    value = unknown
                elif isinstance(expr, ast.Attribute):
                    a = []
                    n = expr
                    while isinstance(n, ast.Attribute):
                        a.append(n.attr)
                        n = n.value
                    if not isinstance(n, ast.Name):
                        fail("Unsupported default value " + repr(default) + " (looked like a Python constant)")
                    a.append(n.id)
                    py_default = ".".join(reversed(a))

                    c_default = kwargs.get("c_default")
                    if not (isinstance(c_default, str) and c_default):
                        fail("When you specify a named constant (" + repr(py_default) + ") as your default value,\nyou MUST specify a valid c_default.")

                    try:
                        value = eval(py_default)
                    except NameError:
                        value = unknown
                else:
                    value = ast.literal_eval(expr)
                    py_default = repr(value)
                    if isinstance(value, (bool, None.__class__)):
                        c_default = "Py_" + py_default
                    elif isinstance(value, str):
                        c_default = c_repr(value)
                    else:
                        c_default = py_default

            except SyntaxError as e:
                fail("Syntax error: " + repr(e.text))
            except (ValueError, AttributeError):
                value = unknown
                c_default = kwargs.get("c_default")
                py_default = default
                if not (isinstance(c_default, str) and c_default):
                    fail("When you specify a named constant (" + repr(py_default) + ") as your default value,\nyou MUST specify a valid c_default.")

            kwargs.setdefault('c_default', c_default)
            kwargs.setdefault('py_default', py_default)

        dict = legacy_converters if legacy else converters
        legacy_str = "legacy " if legacy else ""
        if name not in dict:
            fail('{} is not a valid {}converter'.format(name, legacy_str))
        # if you use a c_name for the parameter, we just give that name to the converter
        # but the parameter object gets the python name
        converter = dict[name](c_name or parameter_name, parameter_name, self.function, value, **kwargs)

        kind = inspect.Parameter.KEYWORD_ONLY if self.keyword_only else inspect.Parameter.POSITIONAL_OR_KEYWORD

        if isinstance(converter, self_converter):
            if len(self.function.parameters) == 1:
                if (self.parameter_state != self.ps_required):
                    fail("A 'self' parameter cannot be marked optional.")
                if value is not unspecified:
                    fail("A 'self' parameter cannot have a default value.")
                if self.group:
                    fail("A 'self' parameter cannot be in an optional group.")
                kind = inspect.Parameter.POSITIONAL_ONLY
                self.parameter_state = self.ps_start
                self.function.parameters.clear()
            else:
                fail("A 'self' parameter, if specified, must be the very first thing in the parameter block.")

        p = Parameter(parameter_name, kind, function=self.function, converter=converter, default=value, group=self.group)

        if parameter_name in self.function.parameters:
            fail("You can't have two parameters named " + repr(parameter_name) + "!")
        self.function.parameters[parameter_name] = p

    def parse_converter(self, annotation):
        if isinstance(annotation, ast.Str):
            return annotation.s, True, {}

        if isinstance(annotation, ast.Name):
            return annotation.id, False, {}

        if not isinstance(annotation, ast.Call):
            fail("Annotations must be either a name, a function call, or a string.")

        name = annotation.func.id
        kwargs = {node.arg: ast.literal_eval(node.value) for node in annotation.keywords}
        return name, False, kwargs

    def parse_special_symbol(self, symbol):
        if self.parameter_state == self.ps_seen_slash:
            fail("Function " + self.function.name + " specifies " + symbol + " after /, which is unsupported.")

        if symbol == '*':
            if self.keyword_only:
                fail("Function " + self.function.name + " uses '*' more than once.")
            self.keyword_only = True
        elif symbol == '[':
            if self.parameter_state in (self.ps_start, self.ps_left_square_before):
                self.parameter_state = self.ps_left_square_before
            elif self.parameter_state in (self.ps_required, self.ps_group_after):
                self.parameter_state = self.ps_group_after
            else:
                fail("Function " + self.function.name + " has an unsupported group configuration. (Unexpected state " + str(self.parameter_state) + ".b)")
            self.group += 1
            self.function.docstring_only = True
        elif symbol == ']':
            if not self.group:
                fail("Function " + self.function.name + " has a ] without a matching [.")
            if not any(p.group == self.group for p in self.function.parameters.values()):
                fail("Function " + self.function.name + " has an empty group.\nAll groups must contain at least one parameter.")
            self.group -= 1
            if self.parameter_state in (self.ps_left_square_before, self.ps_group_before):
                self.parameter_state = self.ps_group_before
            elif self.parameter_state in (self.ps_group_after, self.ps_right_square_after):
                self.parameter_state = self.ps_right_square_after
            else:
                fail("Function " + self.function.name + " has an unsupported group configuration. (Unexpected state " + str(self.parameter_state) + ".c)")
        elif symbol == '/':
            # ps_required and ps_optional are allowed here, that allows positional-only without option groups
            # to work (and have default values!)
            if (self.parameter_state not in (self.ps_required, self.ps_optional, self.ps_right_square_after, self.ps_group_before)) or self.group:
                fail("Function " + self.function.name + " has an unsupported group configuration. (Unexpected state " + str(self.parameter_state) + ".d)")
            if self.keyword_only:
                fail("Function " + self.function.name + " mixes keyword-only and positional-only parameters, which is unsupported.")
            self.parameter_state = self.ps_seen_slash
            # fixup preceding parameters
            for p in self.function.parameters.values():
                if (p.kind != inspect.Parameter.POSITIONAL_OR_KEYWORD and not isinstance(p.converter, self_converter)):
                    fail("Function " + self.function.name + " mixes keyword-only and positional-only parameters, which is unsupported.")
                p.kind = inspect.Parameter.POSITIONAL_ONLY

    def state_parameter_docstring_start(self, line):
        self.parameter_docstring_indent = len(self.indent.margin)
        assert self.indent.depth == 3
        return self.next(self.state_parameter_docstring, line)

    # every line of the docstring must start with at least F spaces,
    # where F > P.
    # these F spaces will be stripped.
    def state_parameter_docstring(self, line):
        stripped = line.strip()
        if stripped.startswith('#'):
            return

        indent = self.indent.measure(line)
        if indent < self.parameter_docstring_indent:
            self.indent.infer(line)
            assert self.indent.depth < 3
            if self.indent.depth == 2:
                # back to a parameter
                return self.next(self.state_parameter, line)
            assert self.indent.depth == 1
            return self.next(self.state_function_docstring, line)

        assert self.function.parameters
        last_parameter = next(reversed(list(self.function.parameters.values())))

        new_docstring = last_parameter.docstring

        if new_docstring:
            new_docstring += '\n'
        if stripped:
            new_docstring += self.indent.dedent(line)

        last_parameter.docstring = new_docstring

    # the final stanza of the DSL is the docstring.
    def state_function_docstring(self, line):
        if self.group:
            fail("Function " + self.function.name + " has a ] without a matching [.")

        stripped = line.strip()
        if stripped.startswith('#'):
            return

        new_docstring = self.function.docstring
        if new_docstring:
            new_docstring += "\n"
        if stripped:
            line = self.indent.dedent(line).rstrip()
        else:
            line = ''
        new_docstring += line
        self.function.docstring = new_docstring

    def format_docstring(self):
        f = self.function

        new_or_init = f.kind in (METHOD_NEW, METHOD_INIT)
        if new_or_init and not f.docstring:
            # don't render a docstring at all, no signature, nothing.
            return f.docstring

        text, add, output = _text_accumulator()
        parameters = f.render_parameters

        ##
        ## docstring first line
        ##

        if new_or_init:
            # classes get *just* the name of the class
            # not __new__, not __init__, and not module.classname
            assert f.cls
            add(f.cls.name)
        else:
            add(f.name)
        add('(')

        # populate "right_bracket_count" field for every parameter
        assert parameters, "We should always have a self parameter. " + repr(f)
        assert isinstance(parameters[0].converter, self_converter)
        parameters[0].right_bracket_count = 0
        parameters_after_self = parameters[1:]
        if parameters_after_self:
            # for now, the only way Clinic supports positional-only parameters
            # is if all of them are positional-only...
            #
            # ... except for self!  self is always positional-only.

            positional_only_parameters = [p.kind == inspect.Parameter.POSITIONAL_ONLY for p in parameters_after_self]
            if parameters_after_self[0].kind == inspect.Parameter.POSITIONAL_ONLY:
                assert all(positional_only_parameters)
                for p in parameters:
                    p.right_bracket_count = abs(p.group)
            else:
                # don't put any right brackets around non-positional-only parameters, ever.
                for p in parameters_after_self:
                    p.right_bracket_count = 0

        right_bracket_count = 0

        def fix_right_bracket_count(desired):
            nonlocal right_bracket_count
            s = ''
            while right_bracket_count < desired:
                s += '['
                right_bracket_count += 1
            while right_bracket_count > desired:
                s += ']'
                right_bracket_count -= 1
            return s

        need_slash = False
        added_slash = False
        need_a_trailing_slash = False

        # we only need a trailing slash:
        #   * if this is not a "docstring_only" signature
        #   * and if the last *shown* parameter is
        #     positional only
        if not f.docstring_only:
            for p in reversed(parameters):
                if not p.converter.show_in_signature:
                    continue
                if p.is_positional_only():
                    need_a_trailing_slash = True
                break


        added_star = False

        first_parameter = True
        last_p = parameters[-1]
        line_length = len(''.join(text))
        indent = " " * line_length
        def add_parameter(text):
            nonlocal line_length
            nonlocal first_parameter
            if first_parameter:
                s = text
                first_parameter = False
            else:
                s = ' ' + text
                if line_length + len(s) >= 72:
                    add('\n')
                    add(indent)
                    line_length = len(indent)
                    s = text
            line_length += len(s)
            add(s)

        for p in parameters:
            if not p.converter.show_in_signature:
                continue
            assert p.name

            is_self = isinstance(p.converter, self_converter)
            if is_self and f.docstring_only:
                # this isn't a real machine-parsable signature,
                # so let's not print the "self" parameter
                continue

            if p.is_positional_only():
                need_slash = not f.docstring_only
            elif need_slash and not (added_slash or p.is_positional_only()):
                added_slash = True
                add_parameter('/,')

            if p.is_keyword_only() and not added_star:
                added_star = True
                add_parameter('*,')

            p_add, p_output = text_accumulator()
            p_add(fix_right_bracket_count(p.right_bracket_count))

            if isinstance(p.converter, self_converter):
                # annotate first parameter as being a "self".
                #
                # if inspect.Signature gets this function,
                # and it's already bound, the self parameter
                # will be stripped off.
                #
                # if it's not bound, it should be marked
                # as positional-only.
                #
                # note: we don't print "self" for __init__,
                # because this isn't actually the signature
                # for __init__.  (it can't be, __init__ doesn't
                # have a docstring.)  if this is an __init__
                # (or __new__), then this signature is for
                # calling the class to construct a new instance.
                p_add('$')

            name = p.converter.signature_name or p.name
            p_add(name)

            if p.converter.is_optional():
                p_add('=')
                value = p.converter.py_default
                if not value:
                    value = repr(p.converter.default)
                p_add(value)

            if (p != last_p) or need_a_trailing_slash:
                p_add(',')

            add_parameter(p_output())

        add(fix_right_bracket_count(0))
        if need_a_trailing_slash:
            add_parameter('/')
        add(')')

        # PEP 8 says:
        #
        #     The Python standard library will not use function annotations
        #     as that would result in a premature commitment to a particular
        #     annotation style. Instead, the annotations are left for users
        #     to discover and experiment with useful annotation styles.
        #
        # therefore this is commented out:
        #
        # if f.return_converter.py_default:
        #     add(' -> ')
        #     add(f.return_converter.py_default)

        if not f.docstring_only:
            add("\n--\n")

        docstring_first_line = output()

        # now fix up the places where the brackets look wrong
        docstring_first_line = docstring_first_line.replace(', ]', ',] ')

        # okay.  now we're officially building the "parameters" section.
        # create substitution text for {parameters}
        spacer_line = False
        for p in parameters:
            if not p.docstring.strip():
                continue
            if spacer_line:
                add('\n')
            else:
                spacer_line = True
            add("  ")
            add(p.name)
            add('\n')
            add(textwrap.indent(rstrip_lines(p.docstring.rstrip()), "    "))
        parameters = output()
        if parameters:
            parameters += '\n'

        ##
        ## docstring body
        ##

        docstring = f.docstring.rstrip()
        lines = [line.rstrip() for line in docstring.split('\n')]

        # Enforce the summary line!
        # The first line of a docstring should be a summary of the function.
        # It should fit on one line (80 columns? 79 maybe?) and be a paragraph
        # by itself.
        #
        # Argument Clinic enforces the following rule:
        #  * either the docstring is empty,
        #  * or it must have a summary line.
        #
        # Guido said Clinic should enforce this:
        # http://mail.python.org/pipermail/python-dev/2013-June/127110.html

        if len(lines) >= 2:
            if lines[1]:
                fail("Docstring for " + f.full_name + " does not have a summary line!\n" +
                    "Every non-blank function docstring must start with\n" +
                    "a single line summary followed by an empty line.")
        elif len(lines) == 1:
            # the docstring is only one line right now--the summary line.
            # add an empty line after the summary line so we have space
            # between it and the {parameters} we're about to add.
            lines.append('')

        parameters_marker_count = len(docstring.split('{parameters}')) - 1
        if parameters_marker_count > 1:
            fail('You may not specify {parameters} more than once in a docstring!')

        if not parameters_marker_count:
            # insert after summary line
            lines.insert(2, '{parameters}')

        # insert at front of docstring
        lines.insert(0, docstring_first_line)

        docstring = "\n".join(lines)

        add(docstring)
        docstring = output()

        docstring = linear_format(docstring, parameters=parameters)
        docstring = docstring.rstrip()

        return docstring

    def state_terminal(self, line):
        """
        Called when processing the block is done.
        """
        assert not line

        if not self.function:
            return

        if self.keyword_only:
            values = self.function.parameters.values()
            if not values:
                no_parameter_after_star = True
            else:
                last_parameter = next(reversed(list(values)))
                no_parameter_after_star = last_parameter.kind != inspect.Parameter.KEYWORD_ONLY
            if no_parameter_after_star:
                fail("Function " + self.function.name + " specifies '*' without any parameters afterwards.")

        # remove trailing whitespace from all parameter docstrings
        for name, value in self.function.parameters.items():
            if not value:
                continue
            value.docstring = value.docstring.rstrip()

        self.function.docstring = self.format_docstring()


parsers = {'clinic' : DSLParser, 'python': PythonParser}

clinic = None


print('here')

