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

def shellQuote(value):
    """
    Return the string value in a form that can safely be inserted into
    a shell command.
    """
    return "'%s'"%(value.replace("'", "'\"'\"'"))

def grepValue(fn, variable):
    """
    Return the unquoted value of a variable from a file..
    QUOTED_VALUE='quotes'    -> str('quotes')
    UNQUOTED_VALUE=noquotes  -> str('noquotes')
    """
    variable = variable + '='
    for ln in open(fn, 'r'):
        if ln.startswith(variable):
            value = ln[len(variable):].strip()
            return value.strip("\"'")
    raise RuntimeError("Cannot find variable %s" % variable[:-1])

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

# Location of the preferred SDK

### There are some issues with the SDK selection below here,
### The resulting binary doesn't work on all platforms that
### it should. Always default to the 10.4u SDK until that
### issue is resolved.
###
##if int(os.uname()[2].split('.')[0]) == 8:
##    # Explicitly use the 10.4u (universal) SDK when
##    # building on 10.4, the system headers are not
##    # useable for a universal build
##    SDKPATH = "/Developer/SDKs/MacOSX10.4u.sdk"
##else:
##    SDKPATH = "/"

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

# $MACOSX_DEPLOYMENT_TARGET -> minimum OS X level
DEPTARGET = '10.3'

def getDeptargetTuple():
    return tuple([int(n) for n in DEPTARGET.split('.')[0:2]])

def getTargetCompilers():
    target_cc_map = {
        '10.3': ('gcc-4.0', 'g++-4.0'),
        '10.4': ('gcc-4.0', 'g++-4.0'),
        '10.5': ('gcc-4.2', 'g++-4.2'),
        '10.6': ('gcc-4.2', 'g++-4.2'),
    }
    return target_cc_map.get(DEPTARGET, ('clang', 'clang++') )

CC, CXX = getTargetCompilers()

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

# Dict of object file names with shared library names to check after building.
# This is to ensure that we ended up dynamically linking with the shared
# library paths and versions we expected.  For example:
#   EXPECTED_SHARED_LIBS['_tkinter.so'] = [
#                       '/Library/Frameworks/Tcl.framework/Versions/8.5/Tcl',
#                       '/Library/Frameworks/Tk.framework/Versions/8.5/Tk']
EXPECTED_SHARED_LIBS = {}

# List of names of third party software built with this installer.
# The names will be inserted into the rtf version of the License.
THIRD_PARTY_LIBS = []

def pkg_recipes():
    result = [
        dict(
            name="PythonFramework",
            long_name="Python Framework",
            source="/Library/Frameworks/Python.framework",
            readme="""\
                This package installs Python.framework, that is the python
                interpreter and the standard library. This also includes Python
                wrappers for lots of Mac OS X API's.
            """,
            postflight="scripts/postflight.framework",
            selected='selected',
        ),
        dict(
            name="PythonApplications",
            long_name="GUI Applications",
            source="/Applications/Python %(VER)s",
            readme="""\
                This package installs IDLE (an interactive Python IDE),
                Python Launcher and Build Applet (create application bundles
                from python scripts).

                It also installs a number of examples and demos.
                """,
            required=False,
            selected='selected',
        ),
        dict(
            name="PythonUnixTools",
            long_name="UNIX command-line tools",
            source="/usr/local/bin",
            readme="""\
                This package installs the unix tools in /usr/local/bin for
                compatibility with older releases of Python. This package
                is not necessary to use Python.
                """,
            required=False,
            selected='selected',
        ),
        dict(
            name="PythonDocumentation",
            long_name="Python Documentation",
            topdir="/Library/Frameworks/Python.framework/Versions/%(VER)s/Resources/English.lproj/Documentation",
            source="/pydocs",
            readme="""\
                This package installs the python documentation at a location
                that is useable for pydoc and IDLE.
                """,
            postflight="scripts/postflight.documentation",
            required=False,
            selected='selected',
        ),
        dict(
            name="PythonProfileChanges",
            long_name="Shell profile updater",
            readme="""\
                This packages updates your shell profile to make sure that
                the Python tools are found by your shell in preference of
                the system provided Python tools.

                If you don't install this package you'll have to add
                "/Library/Frameworks/Python.framework/Versions/%(VER)s/bin"
                to your PATH by hand.
                """,
            postflight="scripts/postflight.patch-profile",
            topdir="/Library/Frameworks/Python.framework",
            source="/empty-dir",
            required=False,
            selected='selected',
        ),
        dict(
            name="PythonInstallPip",
            long_name="Install or upgrade pip",
            readme="""\
                This package installs (or upgrades from an earlier version)
                pip, a tool for installing and managing Python packages.
                """,
            postflight="scripts/postflight.ensurepip",
            topdir="/Library/Frameworks/Python.framework",
            source="/empty-dir",
            required=False,
            selected='selected',
        ),
    ]
    return result

def fatal(msg):
    """
    A fatal error, bail out.
    """
    sys.stderr.write('FATAL: ')
    sys.stderr.write(msg)
    sys.stderr.write('\n')
    sys.exit(1)

def fileContents(fn):
    """
    Return the contents of the named file
    """
    return open(fn, 'r').read()

def runCommand(commandline):
    """
    Run a command and raise RuntimeError if it fails. Output is suppressed
    unless the command fails.
    """

    print('runCommand ', commandline)
    
    fd = os.popen(commandline, 'r')
    data = fd.read()
    xit = fd.close()
    if xit is not None:
        sys.stdout.write(data)
        raise RuntimeError("command failed: %s"%(commandline,))

    if VERBOSE:
        sys.stdout.write(data); sys.stdout.flush()

def captureCommand(commandline):
    fd = os.popen(commandline, 'r')
    data = fd.read()
    xit = fd.close()
    if xit is not None:
        sys.stdout.write(data)
        raise RuntimeError("command failed: %s"%(commandline,))

    return data


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

    #runCommand('hg --version')
    #runCommand('sphinx-build --version')

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

def downloadURL(url, fname):
    """
    Download the contents of the url into the file.
    """
    fpIn = urllib_request.urlopen(url)
    fpOut = open(fname, 'wb')
    block = fpIn.read(10240)
    try:
        while block:
            fpOut.write(block)
            block = fpIn.read(10240)
        fpIn.close()
        fpOut.close()
    except:
        try:
            os.unlink(fname)
        except:
            pass

def packageFromRecipe(targetDir, recipe):
    curdir = os.getcwd()
    try:
        # The major version (such as 2.5) is included in the package name
        # because having two version of python installed at the same time is
        # common.
        pkgname = '%s-%s'%(recipe['name'], 'aaaaa')
        srcdir  = recipe.get('source')
        pkgroot = recipe.get('topdir', srcdir)
        postflight = recipe.get('postflight')
        readme = textwrap.dedent(recipe['readme'])
        isRequired = recipe.get('required', True)

        print("- building package %s"%(pkgname,))

        # Substitute some variables
        textvars = dict(
            VER='aaaaa',
            FULLVER='bbbbb',
        )
        readme = readme % textvars

        print(readme)

        fp = open('ReadMe.txt', 'w')
        fp.write(readme)
        fp.close()

        vers = 'bbbbb'
    finally:
        os.chdir(curdir)

def buildInstaller():

    # Zap all compiled files
    for dirpath, _, filenames in os.walk(os.path.join(WORKDIR, '_root')):
        for fn in filenames:
            if fn.endswith('.pyc') or fn.endswith('.pyo'):
                os.unlink(os.path.join(dirpath, fn))

    outdir = os.path.join(WORKDIR, 'installer')
    if os.path.exists(outdir):
        shutil.rmtree(outdir)
    os.mkdir(outdir)

    pkgroot = os.path.join(outdir, 'Python.mpkg', 'Contents')
    pkgcontents = os.path.join(pkgroot, 'Packages')
    os.makedirs(pkgcontents)
    for recipe in pkg_recipes():
        packageFromRecipe(pkgcontents, recipe)

    rsrcDir = os.path.join(pkgroot, 'Resources')

    fn = os.path.join(pkgroot, 'PkgInfo')
    fp = open(fn, 'w')
    fp.write('pmkrpkg1')
    fp.close()

    os.mkdir(rsrcDir)

    for fn in os.listdir('resources'):
        if fn == '.svn': continue
        if fn.endswith('.jpg'):
            shutil.copy(os.path.join('resources', fn), os.path.join(rsrcDir, fn))

def main():
    # First parse options and check if we can perform our work
    parseOptions()
    checkEnvironment()

    print(USAGE)
    

    os.environ['MACOSX_DEPLOYMENT_TARGET'] = DEPTARGET
    os.environ['CC'] = CC
    os.environ['CXX'] = CXX

    if os.path.exists(WORKDIR):
        shutil.rmtree(WORKDIR)
    os.mkdir(WORKDIR)

    os.environ['LC_ALL'] = 'C'

    # Create the installer
    buildInstaller()

    fp = open(os.path.join(WORKDIR, 'installer', 'Build.txt'), 'w')
    fp.write("# BUILD INFO\n")
    fp.write("# Date: %s\n" % time.ctime())
    #fp.write("# By: %s\n" % pwd.getpwuid(os.getuid()).pw_gecos)
    fp.close()

if __name__ == "__main__":
    main()
