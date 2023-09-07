import sys
import platform

# Horizontal line length
LINE = 79

def get_machine_details():
    print('Getting machine details...')
    buildno, builddate = platform.python_build()
    python = platform.python_version()
    # XXX this is now always UCS4, maybe replace it with 'PEP393' in 3.3+?
    if sys.maxunicode == 65535:
        # UCS2 build (standard)
        unitype = 'UCS2'
    else:
        # UCS4 build (most recent Linux distros)
        unitype = 'UCS4'
    bits, linkage = platform.architecture()
    return {
        'platform': platform.platform(),
        'processor': platform.processor(),
        'executable': sys.executable,
        'implementation': getattr(platform, 'python_implementation',
                                  lambda:'n/a')(),
        'python': platform.python_version(),
        'compiler': platform.python_compiler(),
        'buildno': buildno,
        'builddate': builddate,
        'unicode': unitype,
        'bits': bits,
        }

def print_machine_details(d, indent=''):

    l = ['Machine Details:',
         '   Platform ID:    %s' % d.get('platform', 'n/a'),
         '   Processor:      %s' % d.get('processor', 'n/a'),
         '',
         'Python:',
         '   Implementation: %s' % d.get('implementation', 'n/a'),
         '   Executable:     %s' % d.get('executable', 'n/a'),
         '   Version:        %s' % d.get('python', 'n/a'),
         '   Compiler:       %s' % d.get('compiler', 'n/a'),
         '   Bits:           %s' % d.get('bits', 'n/a'),
         '   Build:          %s (#%s)' % (d.get('builddate', 'n/a'),
                                          d.get('buildno', 'n/a')),
         '   Unicode:        %s' % d.get('unicode', 'n/a'),
         ]
    joiner = '\n' + indent
    print(indent + joiner.join(l) + '\n')


def print_header(title='Benchmark'):
    name = 'david'
    print('-' * LINE)
    print('%s: %s' % (title, name))
    print('-' * LINE)
    print()
    print()
    if machine_details:
        print_machine_details(machine_details, indent='    ')
        print()

machine_details = None

machine_details = get_machine_details()

print_header()




import sys


'''
name = 'os.path'
module = sys.modules[name]
spec = module.__spec__
print(spec)

#module = sys.modules.get(name)

print(type(sys.modules))
#print(sys.modules)
for module_or_name in sys.modules:
    print(module_or_name, end = ' ')
print()

print(sys.modules.get(name))
print(sys.modules[name])
loader = sys.modules[name].__loader__
print(loader)
'''

'''
systeminfo
        module = sys.modules[fullname]
        if module is None:
            return None
        try:
            spec = module.__spec__
        except AttributeError:
            raise ValueError('{}.__spec__ is not set'.format(name))
        else:
            if spec is None:
                raise ValueError('{}.__spec__ is None'.format(name))
            return spec
'''




import _locale
print(_locale._getdefaultlocale())
print(_locale._getdefaultlocale()[1])


import os
import sys


print()

for path in sys.builtin_module_names:
    print(path)

print()






PYTHONDOCS = os.environ.get("PYTHONDOCS",
                            "http://docs.python.org/%d.%d/library"
                            % sys.version_info[:2])
print('PYTHONDOCS')
print(PYTHONDOCS)

encoding = sys.getfilesystemencoding()
print(encoding)




print('顯示模組的所有名稱')

import random
print(dir(random))







