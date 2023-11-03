#file: MessageBox.py
import win32api
import win32con
win32api.MessageBox(0, 'hi!', 'Python', win32con.MB_OK)
