
import os
import logging

class MyLog(object):

    def __init__(self, log):
        self.log = log
        self.first_log = True

    def set_filename(self, filename):
        self.filename = filename

    def get_filename(self):
        return self.filename

    def log_message(self, message):
        if self.first_log:
            self.first_log = False
            self.log.append("### In file %s ###" % self.filename)
        self.log.append(message)

    def get_log(self):
        return self.log

    def path_mtime(self, filename):
        filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
        return os.stat(filename)


        

log = []

ccc = MyLog(log)

filename = 'kkkkk.dat'
ccc.set_filename(filename)

ddd = ccc.get_filename()
print(ddd)

mesg1 = 'aaaa'
mesg2 = 'bbbb'
mesg3 = 'cccc'

ccc.log_message(mesg1)
ccc.log_message(mesg2)
ccc.log_message(mesg3)

lineno = 123
for_output = 'cccc.txt'
msg = "Line %d: could not convert: %s"
ccc.log_message(msg % (lineno, for_output))

ddd = ccc.get_log()
print(ddd)

eee = ccc.path_mtime('aaaaa')
print(type(eee))
print(eee)

