import os
import win32process
import win32event
#os.system('makecode.py test.c')
handle = win32process.CreateProcess('c:\\windows\\notepad.exe', '', None , None , 0 ,win32process. CREATE_NO_WINDOW , None , None ,win32process.STARTUPINFO())
win32event.WaitForSingleObject(handle[0], -1)
print 'notepad ended!'
