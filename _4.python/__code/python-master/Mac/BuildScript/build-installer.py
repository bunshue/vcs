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

# Instructions for building libraries that are necessary for building a
# batteries included python.
#   [The recipes are defined here for convenience but instantiated later after
#    command line options have been processed.]
def library_recipes():
    result = []

    LT_10_5 = bool(getDeptargetTuple() < (10, 5))

    if getDeptargetTuple() < (10, 6):
        # The OpenSSL libs shipped with OS X 10.5 and earlier are
        # hopelessly out-of-date and do not include Apple's tie-in to
        # the root certificates in the user and system keychains via TEA
        # that was introduced in OS X 10.6.  Note that this applies to
        # programs built and linked with a 10.5 SDK even when run on
        # newer versions of OS X.
        #
        # Dealing with CAs is messy.  For now, just supply a
        # local libssl and libcrypto for the older installer variants
        # (e.g. the python.org 10.5+ 32-bit-only installer) that use the
        # same default ssl certfile location as the system libs do:
        #   /System/Library/OpenSSL/cert.pem
        # Then at least TLS connections can be negotiated with sites that
        # use sha-256 certs like python.org, assuming the proper CA certs
        # have been supplied.  The default CA cert management issues for
        # 10.5 and earlier builds are the same as before, other than it is
        # now more obvious with cert checking enabled by default in the
        # standard library.
        #
        # For builds with 10.6+ SDKs, continue to use the deprecated but
        # less out-of-date Apple 0.9.8 libs for now.  While they are less
        # secure than using an up-to-date 1.0.1 version, doing so
        # avoids the big problems of forcing users to have to manage
        # default CAs themselves, thanks to the Apple libs using private TEA
        # APIs for cert validation from keychains if validation using the
        # standard OpenSSL locations (/System/Library/OpenSSL, normally empty)
        # fails.

        result.extend([
          dict(
              name="OpenSSL 1.0.1l",
              url="https://www.openssl.org/source/openssl-1.0.1l.tar.gz",
              checksum='cdb22925fc9bc97ccbf1e007661f2aa6',
              patches=[
                  "openssl_sdk_makedepend.patch",
                   ],
              buildrecipe=build_universal_openssl,
              configure=None,
              install=None,
          ),
        ])

#   Disable for now
    if False:   # if getDeptargetTuple() > (10, 5):
        result.extend([
          dict(
              name="Tcl 8.5.15",
              url="ftp://ftp.tcl.tk/pub/tcl//tcl8_5/tcl8.5.15-src.tar.gz",
              checksum='f3df162f92c69b254079c4d0af7a690f',
              buildDir="unix",
              configure_pre=[
                    '--enable-shared',
                    '--enable-threads',
                    '--libdir=/Library/Frameworks/Python.framework/Versions/%s/lib'%('aaaaa',),
              ],
              useLDFlags=False,
              install='make TCL_LIBRARY=%(TCL_LIBRARY)s && make install TCL_LIBRARY=%(TCL_LIBRARY)s DESTDIR=%(DESTDIR)s'%{
                  "DESTDIR": shellQuote(os.path.join(WORKDIR, 'libraries')),
                  "TCL_LIBRARY": shellQuote('/Library/Frameworks/Python.framework/Versions/%s/lib/tcl8.5'%('aaaaa')),
                  },
              ),
          dict(
              name="Tk 8.5.15",
              url="ftp://ftp.tcl.tk/pub/tcl//tcl8_5/tk8.5.15-src.tar.gz",
              checksum='55b8e33f903210a4e1c8bce0f820657f',
              patches=[
                  "issue19373_tk_8_5_15_source.patch",
                   ],
              buildDir="unix",
              configure_pre=[
                    '--enable-aqua',
                    '--enable-shared',
                    '--enable-threads',
                    '--libdir=/Library/Frameworks/Python.framework/Versions/%s/lib'%('aaaaa',),
              ],
              useLDFlags=False,
              install='make TCL_LIBRARY=%(TCL_LIBRARY)s TK_LIBRARY=%(TK_LIBRARY)s && make install TCL_LIBRARY=%(TCL_LIBRARY)s TK_LIBRARY=%(TK_LIBRARY)s DESTDIR=%(DESTDIR)s'%{
                  "DESTDIR": shellQuote(os.path.join(WORKDIR, 'libraries')),
                  "TCL_LIBRARY": shellQuote('/Library/Frameworks/Python.framework/Versions/%s/lib/tcl8.5'%('aaaaa')),
                  "TK_LIBRARY": shellQuote('/Library/Frameworks/Python.framework/Versions/%s/lib/tk8.5'%('aaaaa')),
                  },
                ),
        ])

    if PYTHON_3:
        result.extend([
          dict(
              name="XZ 5.0.5",
              url="http://tukaani.org/xz/xz-5.0.5.tar.gz",
              checksum='19d924e066b6fff0bc9d1981b4e53196',
              configure_pre=[
                    '--disable-dependency-tracking',
              ]
              ),
        ])

    result.extend([
          dict(
              name="NCurses 5.9",
              url="http://ftp.gnu.org/pub/gnu/ncurses/ncurses-5.9.tar.gz",
              checksum='8cb9c412e5f2d96bc6f459aa8c6282a1',
              configure_pre=[
                  "--enable-widec",
                  "--without-cxx",
                  "--without-cxx-binding",
                  "--without-ada",
                  "--without-curses-h",
                  "--enable-shared",
                  "--with-shared",
                  "--without-debug",
                  "--without-normal",
                  "--without-tests",
                  "--without-manpages",
                  "--datadir=/usr/share",
                  "--sysconfdir=/etc",
                  "--sharedstatedir=/usr/com",
                  "--with-terminfo-dirs=/usr/share/terminfo",
                  "--with-default-terminfo-dir=/usr/share/terminfo",
                  "--libdir=/Library/Frameworks/Python.framework/Versions/%s/lib"%('aaaaa',),
              ],
              patchscripts=[
                  ("ftp://invisible-island.net/ncurses//5.9/ncurses-5.9-20120616-patch.sh.bz2",
                   "f54bf02a349f96a7c4f0d00922f3a0d4"),
                   ],
              useLDFlags=False,
              install='make && make install DESTDIR=%s && cd %s/usr/local/lib && ln -fs ../../../Library/Frameworks/Python.framework/Versions/%s/lib/lib* .'%(
                  shellQuote(os.path.join(WORKDIR, 'libraries')),
                  shellQuote(os.path.join(WORKDIR, 'libraries')),
                  'aaaaa',
                  ),
          ),
          dict(
              name="SQLite 3.8.3.1",
              url="http://www.sqlite.org/2014/sqlite-autoconf-3080301.tar.gz",
              checksum='509ff98d8dc9729b618b7e96612079c6',
              extra_cflags=('-Os '
                            '-DSQLITE_ENABLE_FTS4 '
                            '-DSQLITE_ENABLE_FTS3_PARENTHESIS '
                            '-DSQLITE_ENABLE_RTREE '
                            '-DSQLITE_TCL=0 '
                 '%s' % ('','-DSQLITE_WITHOUT_ZONEMALLOC ')[LT_10_5]),
              configure_pre=[
                  '--enable-threadsafe',
                  '--enable-shared=no',
                  '--enable-static=yes',
                  '--disable-readline',
                  '--disable-dependency-tracking',
              ]
          ),
        ])

    if getDeptargetTuple() < (10, 5):
        result.extend([
          dict(
              name="Bzip2 1.0.6",
              url="http://bzip.org/1.0.6/bzip2-1.0.6.tar.gz",
              checksum='00b516f4704d4a7cb50a1d97e6e8e15b',
              configure=None,
              install='make install CC=%s CXX=%s, PREFIX=%s/usr/local/ CFLAGS="-arch %s -isysroot %s"'%(
                  CC, CXX,
                  shellQuote(os.path.join(WORKDIR, 'libraries')),
                  ' -arch '.join(ARCHLIST),
                  SDKPATH,
              ),
          ),
          dict(
              name="ZLib 1.2.3",
              url="http://www.gzip.org/zlib/zlib-1.2.3.tar.gz",
              checksum='debc62758716a169df9f62e6ab2bc634',
              configure=None,
              install='make install CC=%s CXX=%s, prefix=%s/usr/local/ CFLAGS="-arch %s -isysroot %s"'%(
                  CC, CXX,
                  shellQuote(os.path.join(WORKDIR, 'libraries')),
                  ' -arch '.join(ARCHLIST),
                  SDKPATH,
              ),
          ),
          dict(
              # Note that GNU readline is GPL'd software
              name="GNU Readline 6.1.2",
              url="http://ftp.gnu.org/pub/gnu/readline/readline-6.1.tar.gz" ,
              checksum='fc2f7e714fe792db1ce6ddc4c9fb4ef3',
              patchlevel='0',
              patches=[
                  # The readline maintainers don't do actual micro releases, but
                  # just ship a set of patches.
                  ('http://ftp.gnu.org/pub/gnu/readline/readline-6.1-patches/readline61-001',
                   'c642f2e84d820884b0bf9fd176bc6c3f'),
                  ('http://ftp.gnu.org/pub/gnu/readline/readline-6.1-patches/readline61-002',
                   '1a76781a1ea734e831588285db7ec9b1'),
              ]
          ),
        ])

    if not PYTHON_3:
        result.extend([
          dict(
              name="Sleepycat DB 4.7.25",
              url="http://download.oracle.com/berkeley-db/db-4.7.25.tar.gz",
              checksum='ec2b87e833779681a0c3a814aa71359e',
              buildDir="build_unix",
              configure="../dist/configure",
              configure_pre=[
                  '--includedir=/usr/local/include/db4',
              ]
          ),
        ])

    return result


# Instructions for building packages inside the .mpkg.
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

def extractArchive(builddir, archiveName):
    """
    Extract a source archive into 'builddir'. Returns the path of the
    extracted archive.

    XXX: This function assumes that archives contain a toplevel directory
    that is has the same name as the basename of the archive. This is
    safe enough for almost anything we use.  Unfortunately, it does not
    work for current Tcl and Tk source releases where the basename of
    the archive ends with "-src" but the uncompressed directory does not.
    For now, just special case Tcl and Tk tar.gz downloads.
    """
    curdir = os.getcwd()
    try:
        os.chdir(builddir)
        if archiveName.endswith('.tar.gz'):
            retval = os.path.basename(archiveName[:-7])
            if ((retval.startswith('tcl') or retval.startswith('tk'))
                    and retval.endswith('-src')):
                retval = retval[:-4]
            if os.path.exists(retval):
                shutil.rmtree(retval)
            fp = os.popen("tar zxf %s 2>&1"%(shellQuote(archiveName),), 'r')

        elif archiveName.endswith('.tar.bz2'):
            retval = os.path.basename(archiveName[:-8])
            if os.path.exists(retval):
                shutil.rmtree(retval)
            fp = os.popen("tar jxf %s 2>&1"%(shellQuote(archiveName),), 'r')

        elif archiveName.endswith('.tar'):
            retval = os.path.basename(archiveName[:-4])
            if os.path.exists(retval):
                shutil.rmtree(retval)
            fp = os.popen("tar xf %s 2>&1"%(shellQuote(archiveName),), 'r')

        elif archiveName.endswith('.zip'):
            retval = os.path.basename(archiveName[:-4])
            if os.path.exists(retval):
                shutil.rmtree(retval)
            fp = os.popen("unzip %s 2>&1"%(shellQuote(archiveName),), 'r')

        data = fp.read()
        xit = fp.close()
        if xit is not None:
            sys.stdout.write(data)
            raise RuntimeError("Cannot extract %s"%(archiveName,))

        return os.path.join(builddir, retval)

    finally:
        os.chdir(curdir)

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

def verifyThirdPartyFile(url, checksum, fname):
    """
    Download file from url to filename fname if it does not already exist.
    Abort if file contents does not match supplied md5 checksum.
    """
    name = os.path.basename(fname)
    if os.path.exists(fname):
        print("Using local copy of %s"%(name,))
    else:
        print("Did not find local copy of %s"%(name,))
        print("Downloading %s"%(name,))
        downloadURL(url, fname)
        print("Archive for %s stored as %s"%(name, fname))
    if os.system(
            'MD5=$(openssl md5 %s) ; test "${MD5##*= }" = "%s"'
                % (shellQuote(fname), checksum) ):
        fatal('MD5 checksum mismatch for file %s' % fname)

def build_universal_openssl(basedir, archList):
    """
    Special case build recipe for universal build of openssl.

    The upstream OpenSSL build system does not directly support
    OS X universal builds.  We need to build each architecture
    separately then lipo them together into fat libraries.
    """

    # OpenSSL fails to build with Xcode 2.5 (on OS X 10.4).
    # If we are building on a 10.4.x or earlier system,
    # unilaterally disable assembly code building to avoid the problem.
    no_asm = int(platform.release().split(".")[0]) < 9

    def build_openssl_arch(archbase, arch):
        "Build one architecture of openssl"
        arch_opts = {
            "i386": ["darwin-i386-cc"],
            "x86_64": ["darwin64-x86_64-cc", "enable-ec_nistp_64_gcc_128"],
            "ppc": ["darwin-ppc-cc"],
            "ppc64": ["darwin64-ppc-cc"],
        }
        configure_opts = [
            "no-krb5",
            "no-idea",
            "no-mdc2",
            "no-rc5",
            "no-zlib",
            "enable-tlsext",
            "no-ssl2",
            "no-ssl3",
            "no-ssl3-method",
            # "enable-unit-test",
            "shared",
            "--install_prefix=%s"%shellQuote(archbase),
            "--prefix=%s"%os.path.join("/", *FW_VERSION_PREFIX),
            "--openssldir=/System/Library/OpenSSL",
        ]
        if no_asm:
            configure_opts.append("no-asm")
        runCommand(" ".join(["perl", "Configure"]
                        + arch_opts[arch] + configure_opts))
        runCommand("make depend OSX_SDK=%s" % SDKPATH)
        runCommand("make all OSX_SDK=%s" % SDKPATH)
        runCommand("make install_sw OSX_SDK=%s" % SDKPATH)
        # runCommand("make test")
        return

    srcdir = os.getcwd()
    universalbase = os.path.join(srcdir, "..",
                        os.path.basename(srcdir) + "-universal")
    os.mkdir(universalbase)
    archbasefws = []
    for arch in archList:
        # fresh copy of the source tree
        archsrc = os.path.join(universalbase, arch, "src")
        shutil.copytree(srcdir, archsrc, symlinks=True)
        # install base for this arch
        archbase = os.path.join(universalbase, arch, "root")
        os.mkdir(archbase)
        # Python framework base within install_prefix:
        # the build will install into this framework..
        # This is to ensure that the resulting shared libs have
        # the desired real install paths built into them.
        archbasefw = os.path.join(archbase, *FW_VERSION_PREFIX)

        # build one architecture
        os.chdir(archsrc)
        build_openssl_arch(archbase, arch)
        os.chdir(srcdir)
        archbasefws.append(archbasefw)

    # copy arch-independent files from last build into the basedir framework
    basefw = os.path.join(basedir, *FW_VERSION_PREFIX)
    shutil.copytree(
            os.path.join(archbasefw, "include", "openssl"),
            os.path.join(basefw, "include", "openssl")
            )

    shlib_version_number = grepValue(os.path.join(archsrc, "Makefile"),
            "SHLIB_VERSION_NUMBER")
    #   e.g. -> "1.0.0"
    libcrypto = "libcrypto.dylib"
    libcrypto_versioned = libcrypto.replace(".", "."+shlib_version_number+".")
    #   e.g. -> "libcrypto.1.0.0.dylib"
    libssl = "libssl.dylib"
    libssl_versioned = libssl.replace(".", "."+shlib_version_number+".")
    #   e.g. -> "libssl.1.0.0.dylib"

    try:
        os.mkdir(os.path.join(basefw, "lib"))
    except OSError:
        pass

    # merge the individual arch-dependent shared libs into a fat shared lib
    archbasefws.insert(0, basefw)
    for (lib_unversioned, lib_versioned) in [
                (libcrypto, libcrypto_versioned),
                (libssl, libssl_versioned)
            ]:
        runCommand("lipo -create -output " +
                    " ".join(shellQuote(
                            os.path.join(fw, "lib", lib_versioned))
                                    for fw in archbasefws))
        # and create an unversioned symlink of it
        os.symlink(lib_versioned, os.path.join(basefw, "lib", lib_unversioned))

    # Create links in the temp include and lib dirs that will be injected
    # into the Python build so that setup.py can find them while building
    # and the versioned links so that the setup.py post-build import test
    # does not fail.
    relative_path = os.path.join("..", "..", "..", *FW_VERSION_PREFIX)
    for fn in [
            ["include", "openssl"],
            ["lib", libcrypto],
            ["lib", libssl],
            ["lib", libcrypto_versioned],
            ["lib", libssl_versioned],
        ]:
        os.symlink(
            os.path.join(relative_path, *fn),
            os.path.join(basedir, "usr", "local", *fn)
        )

    return

def buildRecipe(recipe, basedir, archList):
    """
    Build software using a recipe. This function does the
    'configure;make;make install' dance for C software, with a possibility
    to customize this process, basically a poor-mans DarwinPorts.
    """
    curdir = os.getcwd()

    name = recipe['name']
    THIRD_PARTY_LIBS.append(name)
    url = recipe['url']
    configure = recipe.get('configure', './configure')
    buildrecipe = recipe.get('buildrecipe', None)
    install = recipe.get('install', 'make && make install DESTDIR=%s'%(
        shellQuote(basedir)))

    archiveName = os.path.split(url)[-1]
    sourceArchive = os.path.join(DEPSRC, archiveName)

    if not os.path.exists(DEPSRC):
        os.mkdir(DEPSRC)

    verifyThirdPartyFile(url, recipe['checksum'], sourceArchive)
    print("Extracting archive for %s"%(name,))
    buildDir=os.path.join(WORKDIR, '_bld')
    if not os.path.exists(buildDir):
        os.mkdir(buildDir)

    workDir = extractArchive(buildDir, sourceArchive)
    os.chdir(workDir)

    for patch in recipe.get('patches', ()):
        if isinstance(patch, tuple):
            url, checksum = patch
            fn = os.path.join(DEPSRC, os.path.basename(url))
            verifyThirdPartyFile(url, checksum, fn)
        else:
            # patch is a file in the source directory
            fn = os.path.join(curdir, patch)
        runCommand('patch -p%s < %s'%(recipe.get('patchlevel', 1),
            shellQuote(fn),))

    for patchscript in recipe.get('patchscripts', ()):
        if isinstance(patchscript, tuple):
            url, checksum = patchscript
            fn = os.path.join(DEPSRC, os.path.basename(url))
            verifyThirdPartyFile(url, checksum, fn)
        else:
            # patch is a file in the source directory
            fn = os.path.join(curdir, patchscript)
        if fn.endswith('.bz2'):
            runCommand('bunzip2 -fk %s' % shellQuote(fn))
            fn = fn[:-4]
        runCommand('sh %s' % shellQuote(fn))
        os.unlink(fn)

    if 'buildDir' in recipe:
        os.chdir(recipe['buildDir'])

    if configure is not None:
        configure_args = [
            "--prefix=/usr/local",
            "--enable-static",
            "--disable-shared",
            #"CPP=gcc -arch %s -E"%(' -arch '.join(archList,),),
        ]

        if 'configure_pre' in recipe:
            args = list(recipe['configure_pre'])
            if '--disable-static' in args:
                configure_args.remove('--enable-static')
            if '--enable-shared' in args:
                configure_args.remove('--disable-shared')
            configure_args.extend(args)

        if recipe.get('useLDFlags', 1):
            configure_args.extend([
                "CFLAGS=%s-mmacosx-version-min=%s -arch %s -isysroot %s "
                            "-I%s/usr/local/include"%(
                        recipe.get('extra_cflags', ''),
                        DEPTARGET,
                        ' -arch '.join(archList),
                        shellQuote(SDKPATH)[1:-1],
                        shellQuote(basedir)[1:-1],),
                "LDFLAGS=-mmacosx-version-min=%s -isysroot %s -L%s/usr/local/lib -arch %s"%(
                    DEPTARGET,
                    shellQuote(SDKPATH)[1:-1],
                    shellQuote(basedir)[1:-1],
                    ' -arch '.join(archList)),
            ])
        else:
            configure_args.extend([
                "CFLAGS=%s-mmacosx-version-min=%s -arch %s -isysroot %s "
                            "-I%s/usr/local/include"%(
                        recipe.get('extra_cflags', ''),
                        DEPTARGET,
                        ' -arch '.join(archList),
                        shellQuote(SDKPATH)[1:-1],
                        shellQuote(basedir)[1:-1],),
            ])

        if 'configure_post' in recipe:
            configure_args = configure_args + list(recipe['configure_post'])

        configure_args.insert(0, configure)
        configure_args = [ shellQuote(a) for a in configure_args ]

        print("Running configure for %s"%(name,))
        runCommand(' '.join(configure_args) + ' 2>&1')

    if buildrecipe is not None:
        # call special-case build recipe, e.g. for openssl
        buildrecipe(basedir, archList)

    if install is not None:
        print("Running install for %s"%(name,))
        runCommand('{ ' + install + ' ;} 2>&1')

    print("Done %s"%(name,))
    print("")

    os.chdir(curdir)


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

def installSize(clear=False, _saved=[]):
    if clear:
        del _saved[:]
    if not _saved:
        data = captureCommand("du -ks %s"%(
                    shellQuote(os.path.join(WORKDIR, '_root'))))
        _saved.append("%d"%((0.5 + (int(data.split()[0]) / 1024.0)),))
    return _saved[0]

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
