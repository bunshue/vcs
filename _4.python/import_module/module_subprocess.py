#測試執行外部命令

import subprocess

#cmd = 'svn propset svn:eol-style native "{}"'.format(path)
cmd = 'calc.exe'    #可
#cmd = 'systeminfo' #不可
propset = subprocess.Popen(cmd, shell = True)
propset.wait()

print('完成')




