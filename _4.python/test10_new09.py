import tempfile
import os
# write PGM file into temp dir
(os_id, abs_path) = tempfile.mkstemp(suffix='.pgm')

print(os_id)
print(abs_path)


'''
with open(abs_path, 'wb') as fd:
    fd.write(pgm)

os.close(os_id)
os.remove(abs_path)
'''


