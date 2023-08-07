"""Pathname and path-related operations for the Macintosh."""

import os
from stat import *
import genericpath
from genericpath import *


def splitdrive(p):
    """Split a pathname into a drive specification and the rest of the
    path.  Useful on DOS/Windows/NT; on the Mac, the drive is always
    empty (don't use the volume name -- it doesn't have the same
    syntactic and semantic oddities as DOS drive letters, such as there
    being a separate current directory per drive)."""

    return p[:0], p

def lexists(path):
    """Test whether a path exists.  Returns True for broken symbolic links"""

    try:
        st = os.lstat(path)
    except OSError:
        return False
    return True


def abspath(path):
    """Return an absolute path."""
    if not isabs(path):
        if isinstance(path, bytes):
            cwd = os.getcwdb()
        else:
            cwd = os.getcwd()
        path = join(cwd, path)
    return normpath(path)

# realpath is a no-op on systems without islink support
def realpath(path):
    path = abspath(path)
    try:
        import Carbon.File
    except ImportError:
        return path
    if not path:
        return path
    colon = _get_colon(path)
    components = path.split(colon)
    path = components[0] + colon
    for c in components[1:]:
        path = join(path, c)
        try:
            path = Carbon.File.FSResolveAliasFile(path, 1)[0].as_pathname()
        except Carbon.File.Error:
            pass
    return path




