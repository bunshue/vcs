import os
import tempfile

filename = tempfile.NamedTemporaryFile().name
print('製作暫存檔案')
print(filename)

print('------------------------------')  #30個

(os_id, abs_path) = tempfile.mkstemp(suffix='.pgm')

print(os_id)
print(abs_path)

print('----臨時資料夾--------------------------')  #30個

tempdir = tempfile.gettempdir()
print('臨時資料夾 : ', tempdir)

tempdir1 = os.path.join(tempdir, 'dir')
tempdir_same = os.path.join(tempdir, 'dir-same')
tempdir_diff = os.path.join(tempdir, 'dir-diff')

print('臨時資料夾1 : ', tempdir1)
print('臨時資料夾2 : ', tempdir_same)
print('臨時資料夾3 : ', tempdir_diff)

tmp_filename = os.path.join(tempdir, 'pywin32_postinstall.log')
print(tmp_filename)

tmp_filename = os.path.join(tempdir, 'pywin32_postinstall.log', 'ccccc')
print(tmp_filename)

print('------------------------------')  #30個
