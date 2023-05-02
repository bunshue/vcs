import tempfile

filename = tempfile.NamedTemporaryFile().name
print('製作暫存檔案')
print(filename)


import tempfile

(os_id, abs_path) = tempfile.mkstemp(suffix='.pgm')

print(os_id)
print(abs_path)



import os
import tempfile
#tee_f = open(os.path.join(tempfile.gettempdir(), 'pywin32_postinstall.log'), "w")

print(tempfile.gettempdir())

tmp_filename = os.path.join(tempfile.gettempdir(), 'pywin32_postinstall.log')
print(tmp_filename)

tmp_filename = os.path.join(tempfile.gettempdir(), 'pywin32_postinstall.log', 'ccccc')
print(tmp_filename)

