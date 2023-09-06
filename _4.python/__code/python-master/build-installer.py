import platform, os, sys, getopt, textwrap, shutil, stat, time

try:
    import urllib2 as urllib_request
except ImportError:
    import urllib.request as urllib_request

STAT_0o755 = ( stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR
             | stat.S_IRGRP |                stat.S_IXGRP
             | stat.S_IROTH |                stat.S_IXOTH )

STAT_0o775 = ( stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR
             | stat.S_IRGRP | stat.S_IWGRP | stat.S_IXGRP
             | stat.S_IROTH |                stat.S_IXOTH )

INCLUDE_TIMESTAMP = 1
VERBOSE = 1

_cache_getVersion = None

_cache_getFullVersion = None

FW_PREFIX = ["Library", "Frameworks", "Python.framework"]
FW_VERSION_PREFIX = "--undefined--"

# The directory we'll use to create the build (will be erased and recreated)
WORKDIR = 'C:/_git/vcs/_1.data/______test_files3aaaa'

# The directory we'll use to store third-party sources. Set this to something
# else if you don't want to re-fetch required libraries every time.
DEPSRC = os.path.join(WORKDIR, 'third-party')
DEPSRC = os.path.expanduser('~/Universal/other-sources')

SDKPATH = "/Developer/SDKs/MacOSX10.4u.sdk"

universal_opts_map = { '32-bit': ('i386', 'ppc',),
                       '64-bit': ('x86_64', 'ppc64',),
                       'intel':  ('i386', 'x86_64'),
                       '3-way':  ('ppc', 'i386', 'x86_64'),
                       'all':    ('i386', 'ppc', 'x86_64', 'ppc64',) }
default_target_map = {
        '64-bit': '10.5',
        '3-way': '10.5',
        'intel': '10.5',
        'all': '10.5',
}

UNIVERSALOPTS = tuple(universal_opts_map.keys())

UNIVERSALARCHS = '32-bit'

ARCHLIST = universal_opts_map[UNIVERSALARCHS]

# Source directory (assume we're in Mac/BuildScript)
SRCDIR = os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__
        ))))

DEPTARGET = '10.3'

def getTargetCompilers():
    target_cc_map = {
        '10.3': ('gcc-4.0', 'g++-4.0'),
        '10.4': ('gcc-4.0', 'g++-4.0'),
        '10.5': ('gcc-4.2', 'g++-4.2'),
        '10.6': ('gcc-4.2', 'g++-4.2'),
    }
    return target_cc_map.get(DEPTARGET, ('clang', 'clang++') )

USAGE = textwrap.dedent("""\
    Usage: build_python [options]

    Options:
    -? or -h:            Show this message
    -b DIR
    --build-dir=DIR:     Create build here (default: %(WORKDIR)r)
    --third-party=DIR:   Store third-party sources here (default: %(DEPSRC)r)
    --sdk-path=DIR:      Location of the SDK (default: %(SDKPATH)r)
    --src-dir=DIR:       Location of the Python sources (default: %(SRCDIR)r)
    --dep-target=10.n    OS X deployment target (default: %(DEPTARGET)r)
    --universal-archs=x  universal architectures (options: %(UNIVERSALOPTS)r, default: %(UNIVERSALARCHS)r)
""")% globals()



def checkEnvironment():
    """
    Check that we're running on a supported system.
    """
    print('sys.version_info = ', sys.version_info)
    print('platform.system() = ', platform.system())
    print('platform.release() = ', platform.release())
    print('os.environ = ', os.environ)

    for ev in list(os.environ):
        print(ev)

def parseOptions(args=None):
    """
    Parse arguments and update global settings.
    """
    global WORKDIR, DEPSRC, SDKPATH, SRCDIR, DEPTARGET
    global UNIVERSALOPTS, UNIVERSALARCHS, ARCHLIST, CC, CXX
    global FW_VERSION_PREFIX

    SRCDIR=os.path.abspath(SRCDIR)
    WORKDIR=os.path.abspath(WORKDIR)
    SDKPATH=os.path.abspath(SDKPATH)
    DEPSRC=os.path.abspath(DEPSRC)

    CC, CXX = getTargetCompilers()

    FW_VERSION_PREFIX = FW_PREFIX[:] + ["Versions", 'aaaaa']

    print("-- Settings:")
    print("   * Source directory:    %s" % SRCDIR)
    print("   * Build directory:     %s" % WORKDIR)
    print("   * SDK location:        %s" % SDKPATH)
    print("   * Third-party source:  %s" % DEPSRC)
    print("   * Deployment target:   %s" % DEPTARGET)
    print("   * Universal archs:     %s" % str(ARCHLIST))
    print("   * C compiler:          %s" % CC)
    print("   * C++ compiler:        %s" % CXX)
    print("")


parseOptions()
checkEnvironment()

  
print(USAGE)



