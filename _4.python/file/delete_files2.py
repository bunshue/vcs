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


foldername = 'C:/_git/vcs/_4.python'

num1, num2 = deltree(foldername)

print('清除資料夾中的特定檔案, 多層')

print(num1, ".pyc deleted,", num2, ".pyo deleted")

print(num1, ".jpg deleted,", num2, ".csv deleted")

print('已清除', num1, '個.jpg檔, ', num2, '個.csv檔')
