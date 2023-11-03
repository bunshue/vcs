#  -*- coding: utf-8 -*-
#  file: Add2AutoRun.py
#
import win32api
import win32con
# 要加入的項值名稱
name = 'SetIE'
# 要加入的Python指令稿的路徑
path = 'C:\\SetIE.py'
# 登錄記錄名
KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
# 例外處理
try:
    # 開啟登錄記錄
    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,\
                              KeyName,\
                              0,\
                              win32con.KEY_ALL_ACCESS)
    # 設定項值
    win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)
    # 關閉登錄表
    win32api.RegCloseKey(key)
except:
    print('error')
print('added that!')
