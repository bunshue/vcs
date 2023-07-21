import os


print('----------------------------------------------------------------------')	#70個
print('ls 測試 os.walk')

foldername = 'C:/_git/vcs/_1.data/______test_files3'

for root, dirs, files in os.walk(foldername):
    for rcs_dir in ('.svn', '.git', '.hg', 'build'):
        print('xxxxxx')
    for filename in files:
        #if not (filename.endswith('.c') or filename.endswith('.h')):
        #    continue
        print(filename)
        path = os.path.join(root, filename)
        print(path)


foldername = 'C:/_git/vcs/_1.data/______test_files3'

if os.path.isdir(foldername):
    list = []
    os.walk(foldername, list)
elif os.path.exists(foldername):
    print('xxxxx')


'''
for dirname in dirs:
    os.walk(dirname, visit, prog)
'''


print('----------------------------------------------------------------------')	#70個
print('ls 測試 os.walk')





print('----------------------------------------------------------------------')	#70個
print('ls 測試 glob.glob')

'''

    def glob(self, pattern, exclude = None):
        """Add a list of files to the current component as specified in the
        glob pattern. Individual files can be excluded in the exclude list."""
        files = glob.glob1(self.absolute, pattern)
        for f in files:
            if exclude and f in exclude: continue
            self.add_file(f)
        return files






            files = glob.glob(name)
            list = []
            for file in files:
                list.extend(getFilesForName(file))
            return list



'''




