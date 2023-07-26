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






