#測試執行外部命令

import subprocess

#cmd = 'svn propset svn:eol-style native "{}"'.format(path)
#cmd = 'calc.exe'    #可
#cmd = 'systeminfo' #不可
cmd = r'C:\_git\ims1\IMSCap\IMSCap\bin\Debug\IMSCap.exe'    #可

propset = subprocess.Popen(cmd, shell = True)
propset.wait()

print('完成')


'''
import subprocess

ocr = subprocess.Popen("tesseract media\\text1.jpg media\\result", shell=True)
ocr.wait()

'''
