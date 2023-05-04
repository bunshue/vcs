import os

def _listFiles(files, path):
    """List all files in the directory, recursively. """

    for item in os.listdir(path):
        item = os.path.join(path, item)
        if os.path.isdir(item):
            _listFiles(files, item)
        else:
            files.append(item)




def read_files(path, showProgress = False, readPixelData=False, force=False):
    print(path)

    # Init list of files
    files = []

    # Make dir nice
    basedir = os.path.abspath(path)
    print('basedir', basedir)
    print('files', files)
    # Check whether it exists
    if not os.path.isdir(basedir):
        raise ValueError('The given path is not a valid directory.')
    # Find files recursively
    _listFiles(files, basedir)
    print(files)



print('撈出資料夾下所有檔案')
'''
foldername = 'C:/______test_files3'
find_files(foldername)
'''


foldername = 'C:/______test_files1/__RW/_dicom'

all_series = read_files(foldername, True, False, False)




