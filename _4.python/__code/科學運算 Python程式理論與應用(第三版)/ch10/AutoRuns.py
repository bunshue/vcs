#  -*- coding: utf-8 -*-
#  file: AutoRuns.py
#
# 匯入所需要的模組
from win32api import *
from win32con import *
# GetValues函數用於獲得某登錄記錄下所有的項值
def GetValues(fullname):
    # 把完整的項分割成根項和次基碼兩部分
    name = str.split(fullname,'\\',1)
    #當登錄表中沒有某項時將拋出例外
    try:
        # 開啟對應的項，為了讓該函數更通用
        # 使用了多個判斷敘述
        if name[0] == 'HKEY_LOCAL_MACHINE':
           key = RegOpenKey(HKEY_LOCAL_MACHINE,name[1],0,KEY_READ)
        elif name[0] == 'HKEY_CURRENT_USER':
            key = RegOpenKey(HKEY_CURRENT_USER,name[1], 0, KEY_READ)
        elif name[0] == 'HKEY_CLASSES_ROOT':
            key = RegOpenKey(HKEY_CLASSES_ROOT,name[1], 0, KEY_READ)
        elif name[0] == 'HKEY_CURRENT_CONFIG':
            key = RegOpenKey(HKEY_CURRENT_CONFIG,name[1], 0, KEY_READ)
        elif name[0] == 'HKEY_USERS':
            key = RegOpenKey(HKEY_USERS,name[1], 0, KEY_READ)
        else:
            print('err,no key named %s' % name[0])
    
        # 查詢項的項值數目     
        info = RegQueryInfoKey(key)
        # 檢查項值獲得項值資料
        for i in range(0,info[1]):
           ValueName = RegEnumValue(key, i)
            #調整項值名稱長度，使輸出更好看
           print(str.ljust(ValueName[0],20),ValueName[1])
        # 關閉開啟的項
        RegCloseKey(key)
    except:
        pass

# 因為GetValues函數比較通用，可以在其它指令稿中呼叫
# 這裡先檢查指令稿是否被其它指令稿呼叫       
if __name__ == '__main__': 
    # 因為要要檢查的項較多，故將將其放在清單中，便於增減  
    KeyNames = ['HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run',\
                'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce',\
                'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnceEx',\
                'HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run',\
                'HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce']
    # 檢查清單，呼叫GetValues函數，輸出項值
    for KeyName in KeyNames:
        print(KeyName)
        GetValues(KeyName) 