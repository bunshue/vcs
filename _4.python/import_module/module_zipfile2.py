import os

def _ensure_directory(path):
    """Ensure that the parent directory of `path` exists"""
    dirname = os.path.dirname(path)
    if not os.path.isdir(dirname):
        os.makedirs(dirname)



'''
製作一個zip檔
'''




filename1 = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/poetry2.txt'
filename3 = 'C:/_git/vcs/_1.data/______test_files1/picture2.jpg'

filenames = [filename1, filename2, filename3]

#zip_filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_zip/PIL.zip'
zip_filename = 'ttttt.zip'


print('製作壓縮檔')
import zipfile

with zipfile.ZipFile(zip_filename, "w",
                     compression=zipfile.ZIP_DEFLATED) as zf:
    for filename in filenames:
        if os.path.isfile(filename):
            zf.write(filename, filename)


status = zipfile.is_zipfile(zip_filename)
print(status)





'''
解壓縮一個zip檔
'''


extract_dir = './'

import zipfile

zip = zipfile.ZipFile(zip_filename)
try:
    for info in zip.infolist():
        name = info.filename

        # don't extract absolute paths or ones with .. in them
        if name.startswith('/') or '..' in name:
            continue

        target = os.path.join(extract_dir, *name.split('/'))
        if not target:
            continue

        _ensure_directory(target)
        if not name.endswith('/'):
            # file
            data = zip.read(info.filename)
            f = open(target, 'wb')
            try:
                f.write(data)
            finally:
                f.close()
                del data
finally:
    zip.close()






