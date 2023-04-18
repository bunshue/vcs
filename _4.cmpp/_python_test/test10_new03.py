print(__file__)
print(__file__.upper())
print(__file__.lower())
print(__name__)


print(__name__)
#print(__name__._version)


print(__doc__)


import sys
print(sys.path)


import os
this_dir = os.path.dirname(__file__)
print(this_dir)

cwd = os.getcwd()
print(cwd)

aa = os.chdir(cwd)
print(aa)

dirname = 'C:/_git/vcs/_4.cmpp/_python_test'
cc = os.chdir(dirname)
print(cc)

cmd = '%s "%s" %s' % (sys.executable, 'aaaa', 'bbbb')
print(cmd)


print('顯示目前的系統編碼')
import sys
print(sys.getdefaultencoding())






string_data1 = '你好'

print('原字串 :', string_data1)
print('用 gb2312 編碼 ')
encode_data = string_data1.encode('gb2312')
print(encode_data)

print('再用 big5 解碼出來')
string_data2 = encode_data.decode('big5')
print(string_data2)

print('萬國碼 unicode, 我')
print('我'.encode('utf8'))

string_data1 = '扂砑腕善衄壽unicode腔垀衄砆牉訧蹋,掀:unicode 2.0 3.0 4.0 梗摯崋欴晤鎢.gb,big-5,gbk,脹脹.坳蠅眳潔腔梗摯薊炵..秪峈扂猁勤森輛俴惆豢,眕扂植懂羶衄勤晤鎢衄徹旃噶,腕悝.褫岆婓厙奻梑祥善涴笱砆牉腔恅梒..洷咡籵徹蠟夔腕善.郅郅!'

print('原字串 :', string_data1)
print('用 big5 編碼 ')
encode_data = string_data1.encode('big5')
print(encode_data)

print('再用 gb2312 解碼出來')
string_data2 = encode_data.decode('gb2312')
print(string_data2)








import sys
print(sys.platform)

print(sys.version)

'''
import win32api, win32con
rc = win32api.MessageBox(0, 'kkkkk', "Installation Error", win32con.MB_ABORTRETRYIGNORE)
if rc == win32con.IDABORT:
    print('1111')
elif rc == win32con.IDIGNORE:
    print('2222')
else:
    print('3333')
'''


ver_string = "%d.%d" % (sys.version_info[0], sys.version_info[1])
root_key_name = "Software\\Python\\PythonCore\\" + ver_string
print(sys.version_info)
print(ver_string)
print(root_key_name)



import tempfile
#tee_f = open(os.path.join(tempfile.gettempdir(), 'pywin32_postinstall.log'), "w")

print(tempfile.gettempdir())

tmp_filename = os.path.join(tempfile.gettempdir(), 'pywin32_postinstall.log')
print(tmp_filename)

tmp_filename = os.path.join(tempfile.gettempdir(), 'pywin32_postinstall.log', 'ccccc')
print(tmp_filename)

vi = sys.version_info
install_group = "Python %d.%d" % (vi[0], vi[1])
print(install_group)

filename1 = 'C:/_git/vcs/_4.cmpp/_python_test/data/aaaaa.jpg'
filename2 = 'C:/_git/vcs/_4.cmpp/_python_test/data/bbbbb.jpg'

print("Copied %s to %s" % (filename1, filename2))

#強制離開程式, 並說明原因
sys.exit('強制離開程式, 並說明原因')


