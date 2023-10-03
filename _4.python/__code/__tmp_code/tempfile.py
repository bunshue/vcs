import os
import random

class _RandomNameSequence:
    characters = "abcdefghijklmnopqrstuvwxyz0123456789_"

    @property
    def rng(self):
        cur_pid = os.getpid()
        print('cur_pid = ', cur_pid)
        if cur_pid != getattr(self, '_rng_pid', None):
            self._rng = random.Random()
            self._rng_pid = cur_pid
        return self._rng

    def __iter__(self):
        return self

    def __next__(self):
        print('next next next')
        c = self.characters
        choose = self.rng.choice
        letters = [choose(c) for dummy in range(8)]
        return ''.join(letters)

print('建立 _RandomNameSequence() 物件')
tmp_name = _RandomNameSequence()

for seq in range(5):
    print(seq)
    name = next(tmp_name)
    #print(tmp_name)
    print(name)


