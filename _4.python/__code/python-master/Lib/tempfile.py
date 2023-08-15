import os as _os
from random import Random as _Random

class _RandomNameSequence:
    characters = "abcdefghijklmnopqrstuvwxyz0123456789_"

    @property
    def rng(self):
        cur_pid = _os.getpid()
        if cur_pid != getattr(self, '_rng_pid', None):
            self._rng = _Random()
            self._rng_pid = cur_pid
        return self._rng

    def __iter__(self):
        return self

    def __next__(self):
        c = self.characters
        choose = self.rng.choice
        letters = [choose(c) for dummy in range(8)]
        return ''.join(letters)

tmp_name = _RandomNameSequence()
for seq in range(10):
    name = next(tmp_name)
    print(tmp_name)
    print(name)

print(_os.name)
print(_os.sys.platform)


for envname in 'TMPDIR', 'TEMP', 'TMP':
    dirname = _os.getenv(envname)
    print(dirname)

    
