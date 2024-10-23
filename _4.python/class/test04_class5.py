import os
import time
import datetime


class Module:
    def __init__(self, name, file=None, path=None):
        self.__name__ = name
        self.__file__ = file
        self.__path__ = path
        self.__folder__ = "C:/_git/vcs/_1.data/______test_files1"
        self.__code__ = None
        self._date = time.time()

    def __repr__(self):
        s = "Module(%r" % (self.__name__,)
        if self.__file__ is not None:
            s = s + ", %r" % (self.__file__,)
        if self.__path__ is not None:
            s = s + ", %r" % (self.__path__,)
        s = s + ")"
        return s

    def get_date(self):
        """Return delivery date of message, in seconds since the epoch."""
        return self._date

    def set_date(self, date):
        """Set delivery date of message, in seconds since the epoch."""
        try:
            self._date = float(date)
        except ValueError:
            raise TypeError("can't convert to float: %s" % date)

    def list_folders(self):
        print("轉出一層")
        result = []
        for entry in os.listdir(self.__folder__):
            if not os.path.isdir(os.path.join(self.__folder__, entry)):
                result.append(entry)
        return result


fqname = "mmmmm"
m = Module(fqname)
msg = m.__repr__()
print(msg)

print("創建時間 :", m.get_date())

cc = m.list_folders()
print(cc)
