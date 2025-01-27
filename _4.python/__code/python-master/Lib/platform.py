__version__ = '1.0.7'

import collections
import sys, os, re, subprocess

### Globals & Constants

# Determine the platform's /dev/null device
try:
    DEV_NULL = os.devnull
except AttributeError:
    # os.devnull was added in Python 2.4, so emulate it for earlier
    # Python versions
    if sys.platform in ('dos', 'win32', 'win16'):
        # Use the old CP/M NUL as device name
        DEV_NULL = 'NUL'
    else:
        # Standard Unix uses /dev/null
        DEV_NULL = '/dev/null'

# Directory to search for configuration information on Unix.
# Constant used by test_platform to test linux_distribution().
_UNIXCONFDIR = '/etc'

### Platform specific APIs

_libc_search = re.compile(b'(__libc_init)'
                          b'|'
                          b'(GLIBC_([0-9.]+))'
                          b'|'
                          br'(libc(_\w+)?\.so(?:\.(\d[0-9.]*))?)', re.ASCII)

def libc_ver(executable=sys.executable, lib='', version='',

             chunksize=16384):

    """ Tries to determine the libc version that the file executable
        (which defaults to the Python interpreter) is linked against.

        Returns a tuple of strings (lib,version) which default to the
        given parameters in case the lookup fails.

        Note that the function has intimate knowledge of how different
        libc versions add symbols to the executable and thus is probably
        only useable for executables compiled using gcc.

        The file is read and scanned in chunks of chunksize bytes.

    """
    if hasattr(os.path, 'realpath'):
        # Python 2.2 introduced os.path.realpath(); it is used
        # here to work around problems with Cygwin not being
        # able to open symlinks for reading
        executable = os.path.realpath(executable)
    f = open(executable, 'rb')
    binary = f.read(chunksize)
    pos = 0
    while 1:
        if b'libc' in binary or b'GLIBC' in binary:
            m = _libc_search.search(binary, pos)
        else:
            m = None
        if not m:
            binary = f.read(chunksize)
            if not binary:
                break
            pos = 0
            continue
        libcinit, glibc, glibcversion, so, threads, soversion = [
            s.decode('latin1') if s is not None else s
            for s in m.groups()]
        if libcinit and not lib:
            lib = 'libc'
        elif glibc:
            if lib != 'glibc':
                lib = 'glibc'
                version = glibcversion
            elif glibcversion > version:
                version = glibcversion
        elif so:
            if lib != 'glibc':
                lib = 'libc'
                if soversion and soversion > version:
                    version = soversion
                if threads and version[-len(threads):] != threads:
                    version = version + threads
        pos = m.end()
    f.close()
    return lib, version

def _dist_try_harder(distname, version, id):

    """ Tries some special tricks to get the distribution
        information in case the default method fails.

        Currently supports older SuSE Linux, Caldera OpenLinux and
        Slackware Linux distributions.

    """
    if os.path.exists('/var/adm/inst-log/info'):
        # SuSE Linux stores distribution information in that file
        distname = 'SuSE'
        for line in open('/var/adm/inst-log/info'):
            tv = line.split()
            if len(tv) == 2:
                tag, value = tv
            else:
                continue
            if tag == 'MIN_DIST_VERSION':
                version = value.strip()
            elif tag == 'DIST_IDENT':
                values = value.split('-')
                id = values[2]
        return distname, version, id

    if os.path.exists('/etc/.installed'):
        # Caldera OpenLinux has some infos in that file (thanks to Colin Kong)
        for line in open('/etc/.installed'):
            pkg = line.split('-')
            if len(pkg) >= 2 and pkg[0] == 'OpenLinux':
                # XXX does Caldera support non Intel platforms ? If yes,
                #     where can we find the needed id ?
                return 'OpenLinux', pkg[1], id

    if os.path.isdir('/usr/lib/setup'):
        # Check for slackware version tag file (thanks to Greg Andruk)
        verfiles = os.listdir('/usr/lib/setup')
        for n in range(len(verfiles)-1, -1, -1):
            if verfiles[n][:14] != 'slack-version-':
                del verfiles[n]
        if verfiles:
            verfiles.sort()
            distname = 'slackware'
            version = verfiles[-1][14:]
            return distname, version, id

    return distname, version, id

_release_filename = re.compile(r'(\w+)[-_](release|version)', re.ASCII)
_lsb_release_version = re.compile(r'(.+)'
                                   ' release '
                                   '([\d.]+)'
                                   '[^(]*(?:\((.+)\))?', re.ASCII)
_release_version = re.compile(r'([^0-9]+)'
                               '(?: release )?'
                               '([\d.]+)'
                               '[^(]*(?:\((.+)\))?', re.ASCII)

# See also http://www.novell.com/coolsolutions/feature/11251.html
# and http://linuxmafia.com/faq/Admin/release-files.html
# and http://data.linux-ntfs.org/rpm/whichrpm
# and http://www.die.net/doc/linux/man/man1/lsb_release.1.html

_supported_dists = (
    'SuSE', 'debian', 'fedora', 'redhat', 'centos',
    'mandrake', 'mandriva', 'rocks', 'slackware', 'yellowdog', 'gentoo',
    'UnitedLinux', 'turbolinux', 'arch', 'mageia')

def _parse_release_file(firstline):

    # Default to empty 'version' and 'id' strings.  Both defaults are used
    # when 'firstline' is empty.  'id' defaults to empty when an id can not
    # be deduced.
    version = ''
    id = ''

    # Parse the first line
    m = _lsb_release_version.match(firstline)
    if m is not None:
        # LSB format: "distro release x.x (codename)"
        return tuple(m.groups())

    # Pre-LSB format: "distro x.x (codename)"
    m = _release_version.match(firstline)
    if m is not None:
        return tuple(m.groups())

    # Unknown format... take the first two words
    l = firstline.strip().split()
    if l:
        version = l[0]
        if len(l) > 1:
            id = l[1]
    return '', version, id

def linux_distribution(distname='', version='', id='',

                       supported_dists=_supported_dists,
                       full_distribution_name=1):

    """ Tries to determine the name of the Linux OS distribution name.

        The function first looks for a distribution release file in
        /etc and then reverts to _dist_try_harder() in case no
        suitable files are found.

        supported_dists may be given to define the set of Linux
        distributions to look for. It defaults to a list of currently
        supported Linux distributions identified by their release file
        name.

        If full_distribution_name is true (default), the full
        distribution read from the OS is returned. Otherwise the short
        name taken from supported_dists is used.

        Returns a tuple (distname, version, id) which default to the
        args given as parameters.

    """
    try:
        etc = os.listdir(_UNIXCONFDIR)
    except OSError:
        # Probably not a Unix system
        return distname, version, id
    etc.sort()
    for file in etc:
        m = _release_filename.match(file)
        if m is not None:
            _distname, dummy = m.groups()
            if _distname in supported_dists:
                distname = _distname
                break
    else:
        return _dist_try_harder(distname, version, id)

    # Read the first line
    with open(os.path.join(_UNIXCONFDIR, file), 'r',
              encoding='utf-8', errors='surrogateescape') as f:
        firstline = f.readline()
    _distname, _version, _id = _parse_release_file(firstline)

    if _distname and full_distribution_name:
        distname = _distname
    if _version:
        version = _version
    if _id:
        id = _id
    return distname, version, id

# To maintain backwards compatibility:

def dist(distname='', version='', id='',

         supported_dists=_supported_dists):

    """ Tries to determine the name of the Linux OS distribution name.

        The function first looks for a distribution release file in
        /etc and then reverts to _dist_try_harder() in case no
        suitable files are found.

        Returns a tuple (distname, version, id) which default to the
        args given as parameters.

    """
    return linux_distribution(distname, version, id,
                              supported_dists=supported_dists,
                              full_distribution_name=0)

def popen(cmd, mode='r', bufsize=-1):

    """ Portable popen() interface.
    """
    import warnings
    warnings.warn('use os.popen instead', DeprecationWarning, stacklevel=2)
    return os.popen(cmd, mode, bufsize)

def _norm_version(version, build=''):

    """ Normalize the version and build strings and return a single
        version string using the format major.minor.build (or patchlevel).
    """
    l = version.split('.')
    if build:
        l.append(build)
    try:
        ints = map(int, l)
    except ValueError:
        strings = l
    else:
        strings = list(map(str, ints))
    version = '.'.join(strings[:3])
    return version

_ver_output = re.compile(r'(?:([\w ]+) ([\w.]+) '
                         '.*'
                         '\[.* ([\d.]+)\])')

def _win32_getvalue(key, name, default=''):

    """ Read a value for name from the registry key.

        In case this fails, default is returned.

    """
    try:
        # Use win32api if available
        from win32api import RegQueryValueEx
    except ImportError:
        # On Python 2.0 and later, emulate using winreg
        import winreg
        RegQueryValueEx = winreg.QueryValueEx
    try:
        return RegQueryValueEx(key, name)
    except:
        return default

def win32_ver(release='', version='', csd='', ptype=''):

    """ Get additional version information from the Windows Registry
        and return a tuple (version, csd, ptype) referring to version
        number, CSD level (service pack), and OS type (multi/single
        processor).

        As a hint: ptype returns 'Uniprocessor Free' on single
        processor NT machines and 'Multiprocessor Free' on multi
        processor machines. The 'Free' refers to the OS version being
        free of debugging code. It could also state 'Checked' which
        means the OS version uses debugging code, i.e. code that
        checks arguments, ranges, etc. (Thomas Heller).

        Note: this function works best with Mark Hammond's win32
        package installed, but also on Python 2.3 and later. It
        obviously only runs on Win32 compatible platforms.

    """
    # XXX Is there any way to find out the processor type on WinXX ?
    # XXX Is win32 available on Windows CE ?
    #
    # Adapted from code posted by Karl Putland to comp.lang.python.
    #
    # The mappings between reg. values and release names can be found
    # here: http://msdn.microsoft.com/library/en-us/sysinfo/base/osversioninfo_str.asp

    # Import the needed APIs
    try:
        from win32api import RegQueryValueEx, RegOpenKeyEx, \
             RegCloseKey, GetVersionEx
        from win32con import HKEY_LOCAL_MACHINE, VER_PLATFORM_WIN32_NT, \
             VER_PLATFORM_WIN32_WINDOWS, VER_NT_WORKSTATION
    except ImportError:
        # Emulate the win32api module using Python APIs
        try:
            sys.getwindowsversion
        except AttributeError:
            # No emulation possible, so return the defaults...
            return release, version, csd, ptype
        else:
            # Emulation using winreg (added in Python 2.0) and
            # sys.getwindowsversion() (added in Python 2.3)
            import winreg
            GetVersionEx = sys.getwindowsversion
            RegQueryValueEx = winreg.QueryValueEx
            RegOpenKeyEx = winreg.OpenKeyEx
            RegCloseKey = winreg.CloseKey
            HKEY_LOCAL_MACHINE = winreg.HKEY_LOCAL_MACHINE
            VER_PLATFORM_WIN32_WINDOWS = 1
            VER_PLATFORM_WIN32_NT = 2
            VER_NT_WORKSTATION = 1
            VER_NT_SERVER = 3
            REG_SZ = 1

    # Find out the registry key and some general version infos
    winver = GetVersionEx()
    maj, min, buildno, plat, csd = winver
    version = '%i.%i.%i' % (maj, min, buildno & 0xFFFF)
    if hasattr(winver, "service_pack"):
        if winver.service_pack != "":
            csd = 'SP%s' % winver.service_pack_major
    else:
        if csd[:13] == 'Service Pack ':
            csd = 'SP' + csd[13:]

    if plat == VER_PLATFORM_WIN32_WINDOWS:
        regkey = 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion'
        # Try to guess the release name
        if maj == 4:
            if min == 0:
                release = '95'
            elif min == 10:
                release = '98'
            elif min == 90:
                release = 'Me'
            else:
                release = 'postMe'
        elif maj == 5:
            release = '2000'

    elif plat == VER_PLATFORM_WIN32_NT:
        regkey = 'SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion'
        if maj <= 4:
            release = 'NT'
        elif maj == 5:
            if min == 0:
                release = '2000'
            elif min == 1:
                release = 'XP'
            elif min == 2:
                release = '2003Server'
            else:
                release = 'post2003'
        elif maj == 6:
            if hasattr(winver, "product_type"):
                product_type = winver.product_type
            else:
                product_type = VER_NT_WORKSTATION
                # Without an OSVERSIONINFOEX capable sys.getwindowsversion(),
                # or help from the registry, we cannot properly identify
                # non-workstation versions.
                try:
                    key = RegOpenKeyEx(HKEY_LOCAL_MACHINE, regkey)
                    name, type = RegQueryValueEx(key, "ProductName")
                    # Discard any type that isn't REG_SZ
                    if type == REG_SZ and name.find("Server") != -1:
                        product_type = VER_NT_SERVER
                except OSError:
                    # Use default of VER_NT_WORKSTATION
                    pass

            if min == 0:
                if product_type == VER_NT_WORKSTATION:
                    release = 'Vista'
                else:
                    release = '2008Server'
            elif min == 1:
                if product_type == VER_NT_WORKSTATION:
                    release = '7'
                else:
                    release = '2008ServerR2'
            elif min == 2:
                if product_type == VER_NT_WORKSTATION:
                    release = '8'
                else:
                    release = '2012Server'
            else:
                release = 'post2012Server'

    else:
        if not release:
            # E.g. Win3.1 with win32s
            release = '%i.%i' % (maj, min)
        return release, version, csd, ptype

    # Open the registry key
    try:
        keyCurVer = RegOpenKeyEx(HKEY_LOCAL_MACHINE, regkey)
        # Get a value to make sure the key exists...
        RegQueryValueEx(keyCurVer, 'SystemRoot')
    except:
        return release, version, csd, ptype

    # Parse values
    #subversion = _win32_getvalue(keyCurVer,
    #                            'SubVersionNumber',
    #                            ('',1))[0]
    #if subversion:
    #   release = release + subversion # 95a, 95b, etc.
    build = _win32_getvalue(keyCurVer,
                            'CurrentBuildNumber',
                            ('', 1))[0]
    ptype = _win32_getvalue(keyCurVer,
                           'CurrentType',
                           (ptype, 1))[0]

    # Normalize version
    version = _norm_version(version, build)

    # Close key
    RegCloseKey(keyCurVer)
    return release, version, csd, ptype

def _mac_ver_xml():
    fn = '/System/Library/CoreServices/SystemVersion.plist'
    if not os.path.exists(fn):
        return None

    try:
        import plistlib
    except ImportError:
        return None

    with open(fn, 'rb') as f:
        pl = plistlib.load(f)
    release = pl['ProductVersion']
    versioninfo = ('', '', '')
    machine = os.uname().machine
    if machine in ('ppc', 'Power Macintosh'):
        # Canonical name
        machine = 'PowerPC'

    return release, versioninfo, machine


def mac_ver(release='', versioninfo=('', '', ''), machine=''):

    """ Get MacOS version information and return it as tuple (release,
        versioninfo, machine) with versioninfo being a tuple (version,
        dev_stage, non_release_version).

        Entries which cannot be determined are set to the parameter values
        which default to ''. All tuple entries are strings.
    """

    # First try reading the information from an XML file which should
    # always be present
    info = _mac_ver_xml()
    if info is not None:
        return info

    # If that also doesn't work return the default values
    return release, versioninfo, machine

def _java_getprop(name, default):

    from java.lang import System
    try:
        value = System.getProperty(name)
        if value is None:
            return default
        return value
    except AttributeError:
        return default

def java_ver(release='', vendor='', vminfo=('', '', ''), osinfo=('', '', '')):

    """ Version interface for Jython.

        Returns a tuple (release, vendor, vminfo, osinfo) with vminfo being
        a tuple (vm_name, vm_release, vm_vendor) and osinfo being a
        tuple (os_name, os_version, os_arch).

        Values which cannot be determined are set to the defaults
        given as parameters (which all default to '').

    """
    # Import the needed APIs
    try:
        import java.lang
    except ImportError:
        return release, vendor, vminfo, osinfo

    vendor = _java_getprop('java.vendor', vendor)
    release = _java_getprop('java.version', release)
    vm_name, vm_release, vm_vendor = vminfo
    vm_name = _java_getprop('java.vm.name', vm_name)
    vm_vendor = _java_getprop('java.vm.vendor', vm_vendor)
    vm_release = _java_getprop('java.vm.version', vm_release)
    vminfo = vm_name, vm_release, vm_vendor
    os_name, os_version, os_arch = osinfo
    os_arch = _java_getprop('java.os.arch', os_arch)
    os_name = _java_getprop('java.os.name', os_name)
    os_version = _java_getprop('java.os.version', os_version)
    osinfo = os_name, os_version, os_arch

    return release, vendor, vminfo, osinfo

### System name aliasing

def system_alias(system, release, version):

    """ Returns (system, release, version) aliased to common
        marketing names used for some systems.

        It also does some reordering of the information in some cases
        where it would otherwise cause confusion.

    """
    if system == 'Rhapsody':
        # Apple's BSD derivative
        # XXX How can we determine the marketing release number ?
        return 'MacOS X Server', system+release, version

    elif system == 'SunOS':
        # Sun's OS
        if release < '5':
            # These releases use the old name SunOS
            return system, release, version
        # Modify release (marketing release = SunOS release - 3)
        l = release.split('.')
        if l:
            try:
                major = int(l[0])
            except ValueError:
                pass
            else:
                major = major - 3
                l[0] = str(major)
                release = '.'.join(l)
        if release < '6':
            system = 'Solaris'
        else:
            # XXX Whatever the new SunOS marketing name is...
            system = 'Solaris'

    elif system == 'IRIX64':
        # IRIX reports IRIX64 on platforms with 64-bit support; yet it
        # is really a version and not a different platform, since 32-bit
        # apps are also supported..
        system = 'IRIX'
        if version:
            version = version + ' (64bit)'
        else:
            version = '64bit'

    elif system in ('win32', 'win16'):
        # In case one of the other tricks
        system = 'Windows'

    return system, release, version

### Various internal helpers

def _platform(*args):

    """ Helper to format the platform string in a filename
        compatible format e.g. "system-version-machine".
    """
    # Format the platform string
    platform = '-'.join(x.strip() for x in filter(len, args))

    # Cleanup some possible filename obstacles...
    platform = platform.replace(' ', '_')
    platform = platform.replace('/', '-')
    platform = platform.replace('\\', '-')
    platform = platform.replace(':', '-')
    platform = platform.replace(';', '-')
    platform = platform.replace('"', '-')
    platform = platform.replace('(', '-')
    platform = platform.replace(')', '-')

    # No need to report 'unknown' information...
    platform = platform.replace('unknown', '')

    # Fold '--'s and remove trailing '-'
    while 1:
        cleaned = platform.replace('--', '-')
        if cleaned == platform:
            break
        platform = cleaned
    while platform[-1] == '-':
        platform = platform[:-1]

    return platform

def _node(default=''):

    """ Helper to determine the node name of this machine.
    """
    try:
        import socket
    except ImportError:
        # No sockets...
        return default
    try:
        return socket.gethostname()
    except OSError:
        # Still not working...
        return default

def _follow_symlinks(filepath):

    """ In case filepath is a symlink, follow it until a
        real file is reached.
    """
    filepath = os.path.abspath(filepath)
    while os.path.islink(filepath):
        filepath = os.path.normpath(
            os.path.join(os.path.dirname(filepath), os.readlink(filepath)))
    return filepath

def _syscmd_uname(option, default=''):

    """ Interface to the system's uname command.
    """
    if sys.platform in ('dos', 'win32', 'win16'):
        # XXX Others too ?
        return default
    try:
        f = os.popen('uname %s 2> %s' % (option, DEV_NULL))
    except (AttributeError, OSError):
        return default
    output = f.read().strip()
    rc = f.close()
    if not output or rc:
        return default
    else:
        return output

def _syscmd_file(target, default=''):

    """ Interface to the system's file command.

        The function uses the -b option of the file command to have it
        omit the filename in its output. Follow the symlinks. It returns
        default in case the command should fail.

    """
    if sys.platform in ('dos', 'win32', 'win16'):
        # XXX Others too ?
        return default
    target = _follow_symlinks(target)
    try:
        proc = subprocess.Popen(['file', target],
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    except (AttributeError, OSError):
        return default
    output = proc.communicate()[0].decode('latin-1')
    rc = proc.wait()
    if not output or rc:
        return default
    else:
        return output

### Information about the used architecture

# Default values for architecture; non-empty strings override the
# defaults given as parameters
_default_architecture = {
    'win32': ('', 'WindowsPE'),
    'win16': ('', 'Windows'),
    'dos': ('', 'MSDOS'),
}

def architecture(executable=sys.executable, bits='', linkage=''):

    """ Queries the given executable (defaults to the Python interpreter
        binary) for various architecture information.

        Returns a tuple (bits, linkage) which contains information about
        the bit architecture and the linkage format used for the
        executable. Both values are returned as strings.

        Values that cannot be determined are returned as given by the
        parameter presets. If bits is given as '', the sizeof(pointer)
        (or sizeof(long) on Python version < 1.5.2) is used as
        indicator for the supported pointer size.

        The function relies on the system's "file" command to do the
        actual work. This is available on most if not all Unix
        platforms. On some non-Unix platforms where the "file" command
        does not exist and the executable is set to the Python interpreter
        binary defaults from _default_architecture are used.

    """
    # Use the sizeof(pointer) as default number of bits if nothing
    # else is given as default.
    if not bits:
        import struct
        try:
            size = struct.calcsize('P')
        except struct.error:
            # Older installations can only query longs
            size = struct.calcsize('l')
        bits = str(size*8) + 'bit'

    # Get data from the 'file' system command
    if executable:
        fileout = _syscmd_file(executable, '')
    else:
        fileout = ''

    if not fileout and \
       executable == sys.executable:
        # "file" command did not return anything; we'll try to provide
        # some sensible defaults then...
        if sys.platform in _default_architecture:
            b, l = _default_architecture[sys.platform]
            if b:
                bits = b
            if l:
                linkage = l
        return bits, linkage

    if 'executable' not in fileout:
        # Format not supported
        return bits, linkage

    # Bits
    if '32-bit' in fileout:
        bits = '32bit'
    elif 'N32' in fileout:
        # On Irix only
        bits = 'n32bit'
    elif '64-bit' in fileout:
        bits = '64bit'

    # Linkage
    if 'ELF' in fileout:
        linkage = 'ELF'
    elif 'PE' in fileout:
        # E.g. Windows uses this format
        if 'Windows' in fileout:
            linkage = 'WindowsPE'
        else:
            linkage = 'PE'
    elif 'COFF' in fileout:
        linkage = 'COFF'
    elif 'MS-DOS' in fileout:
        linkage = 'MSDOS'
    else:
        # XXX the A.OUT format also falls under this class...
        pass

    return bits, linkage

### Portable uname() interface

uname_result = collections.namedtuple("uname_result",
                    "system node release version machine processor")

_uname_cache = None

def uname():

    """ Fairly portable uname interface. Returns a tuple
        of strings (system, node, release, version, machine, processor)
        identifying the underlying platform.

        Note that unlike the os.uname function this also returns
        possible processor information as an additional tuple entry.

        Entries which cannot be determined are set to ''.

    """
    global _uname_cache
    no_os_uname = 0

    if _uname_cache is not None:
        return _uname_cache

    processor = ''

    # Get some infos from the builtin os.uname API...
    try:
        system, node, release, version, machine = os.uname()
    except AttributeError:
        no_os_uname = 1

    if no_os_uname or not list(filter(None, (system, node, release, version, machine))):
        # Hmm, no there is either no uname or uname has returned
        #'unknowns'... we'll have to poke around the system then.
        if no_os_uname:
            system = sys.platform
            release = ''
            version = ''
            node = _node()
            machine = ''

        use_syscmd_ver = 1

        # Try win32_ver() on win32 platforms
        if system == 'win32':
            release, version, csd, ptype = win32_ver()
            if release and version:
                use_syscmd_ver = 0
            # Try to use the PROCESSOR_* environment variables
            # available on Win XP and later; see
            # http://support.microsoft.com/kb/888731 and
            # http://www.geocities.com/rick_lively/MANUALS/ENV/MSWIN/PROCESSI.HTM
            if not machine:
                # WOW64 processes mask the native architecture
                if "PROCESSOR_ARCHITEW6432" in os.environ:
                    machine = os.environ.get("PROCESSOR_ARCHITEW6432", '')
                else:
                    machine = os.environ.get('PROCESSOR_ARCHITECTURE', '')
            if not processor:
                processor = os.environ.get('PROCESSOR_IDENTIFIER', machine)

        # In case we still don't know anything useful, we'll try to
        # help ourselves
        if system in ('win32', 'win16'):
            if not version:
                if system == 'win32':
                    version = '32bit'
                else:
                    version = '16bit'
            system = 'Windows'

        elif system[:4] == 'java':
            release, vendor, vminfo, osinfo = java_ver()
            system = 'Java'
            version = ', '.join(vminfo)
            if not version:
                version = vendor

    # System specific extensions
    if system == 'OpenVMS':
        # OpenVMS seems to have release and version mixed up
        if not release or release == '0':
            release = version
            version = ''
        # Get processor information
        try:
            import vms_lib
        except ImportError:
            pass
        else:
            csid, cpu_number = vms_lib.getsyi('SYI$_CPU', 0)
            if (cpu_number >= 128):
                processor = 'Alpha'
            else:
                processor = 'VAX'
    if not processor:
        # Get processor information from the uname system command
        processor = _syscmd_uname('-p', '')

    #If any unknowns still exist, replace them with ''s, which are more portable
    if system == 'unknown':
        system = ''
    if node == 'unknown':
        node = ''
    if release == 'unknown':
        release = ''
    if version == 'unknown':
        version = ''
    if machine == 'unknown':
        machine = ''
    if processor == 'unknown':
        processor = ''

    #  normalize name
    if system == 'Microsoft' and release == 'Windows':
        system = 'Windows'
        release = 'Vista'

    _uname_cache = uname_result(system, node, release, version,
                                machine, processor)
    return _uname_cache

def system():
    return uname().system

def node():
    return uname().node

def release():
    return uname().release

def version():
    return uname().version

def machine():
    return uname().machine

def processor():
    return uname().processor

### Various APIs for extracting information from sys.version

_sys_version_parser = re.compile(
    r'([\w.+]+)\s*'
    '\(#?([^,]+),\s*([\w ]+),\s*([\w :]+)\)\s*'
    '\[([^\]]+)\]?', re.ASCII)


_sys_version_cache = {}

def _sys_version(sys_version=None):

    # Get the Python version
    if sys_version is None:
        sys_version = sys.version

    # Try the cache first
    result = _sys_version_cache.get(sys_version, None)
    if result is not None:
        return result

    print(sys_version)
    if 'IronPython' in sys_version:
        print('xxxxxx 1')
        buildno = ''
        builddate = ''
    else:
        print('xxxxxx 4')
        # CPython
        match = _sys_version_parser.match(sys_version)
        print(match)
        if match is None:
            raise ValueError(
                'failed to parse CPython sys.version: %s' %
                repr(sys_version))
        version, buildno, builddate, buildtime, compiler = \
              match.groups()
        name = 'CPython'
        builddate = builddate + ' ' + buildtime

    if hasattr(sys, '_mercurial'):
        _, branch, revision = sys._mercurial
    elif hasattr(sys, 'subversion'):
        # sys.subversion was added in Python 2.5
        _, branch, revision = sys.subversion
    else:
        branch = ''
        revision = ''

    # Add the patchlevel version if missing
    l = version.split('.')
    if len(l) == 2:
        l.append('0')
        version = '.'.join(l)

    # Build and cache the result
    result = (name, version, branch, revision, buildno, builddate, compiler)
    _sys_version_cache[sys_version] = result
    return result

def python_implementation():
    return _sys_version()[0]

def python_version():
    return _sys_version()[1]

def python_version_tuple():
    return tuple(_sys_version()[1].split('.'))

def python_branch():
    return _sys_version()[2]

def python_revision():
    return _sys_version()[3]

def python_build():
    return _sys_version()[4:6]

def python_compiler():
    return _sys_version()[6]

### The Opus Magnum of platform strings :-)

_platform_cache = {}

def platform(aliased=0, terse=0):

    result = _platform_cache.get((aliased, terse), None)
    if result is not None:
        return result

    # Get uname information and then apply platform specific cosmetics
    # to it...
    system, node, release, version, machine, processor = uname()
    if machine == processor:
        processor = ''
    if aliased:
        system, release, version = system_alias(system, release, version)

    if system == 'Windows':
        # MS platforms
        rel, vers, csd, ptype = win32_ver(version)
        if terse:
            platform = _platform(system, release)
        else:
            platform = _platform(system, release, version, csd)
        print(platform)

    _platform_cache[(aliased, terse)] = platform
    return platform


print(platform(True, False))


print(python_compiler())

