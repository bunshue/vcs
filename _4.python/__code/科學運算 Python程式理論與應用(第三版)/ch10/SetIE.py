#  -*- coding: utf-8 -*-
#  file: SetIE.py
#
import datetime
#import string
import win32api
import win32con
# 要修改的登錄記錄
keyname = 'Software\Microsoft\Internet Explorer\Main'
# 要設定為主頁的網址
page = 'www.python.org'
# 取得目前日期
today = datetime.date.today()
# 將日期格式化為xxxx年xx月xx日的形式
title = today.strftime('%Y')+'年'+today.strftime('%m')+'月'+today.strftime('%d')+'日'
# 例外處理
try:
    # 開啟登錄記錄，獲得控制碼
    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, keyname, 0, win32con.KEY_ALL_ACCESS)
    # 讀取"Start Page"的項值資料
    StartPage = win32api.RegQueryValueEx(key, 'Start Page')
except:
    print('error')
else:
    # 判斷主頁是否為要修改的主頁，若果不是則修改
    if StartPage[0] != page:
        win32api.RegSetValueEx(key, 'Start Page', 0, win32con.REG_SZ, page)
    # 設定IE的標題欄為xxxx年xx月xx日
    win32api.RegSetValueEx(key, 'Window Title', 0, win32con.REG_SZ, title)
    # 關閉登錄表
    win32api.RegCloseKey(key)    