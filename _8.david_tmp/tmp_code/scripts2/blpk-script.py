#!.\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'bloscpack==0.9.0','console_scripts','blpk'
__requires__ = 'bloscpack==0.9.0'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('bloscpack==0.9.0', 'console_scripts', 'blpk')()
    )
