def deltree(root):
    import os
    from os.path import join

    num1 = num2 = 0
    for root, dirs, files in os.walk(root):
        for name in files:
            delete = False
            if name.endswith('.pyc'):
                delete = True
                num1 += 1
            elif name.endswith('.pyo'):
                delete = True
                num2 += 1

            '''偽執行
            if delete:
                os.remove(join(root, name))
            '''

    return num1, num2

print('清除資料夾中的特定檔案, 多層, *.pyc 和 *.pyo')
print('偽執行')

foldername = 'D:/_git/vcs/_4.python'
num1, num2 = deltree(foldername)

print('已清除', num1, '個.pyc檔, ', num2, '個.pyo檔')
