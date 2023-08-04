import os

def walk_python_files(paths, is_python=looks_like_python, exclude_dirs=None):
        if os.path.isfile(path):
            if is_python(path):
                yield path
        elif os.path.isdir(path):
            print("    it is a directory")
            for dirpath, dirnames, filenames in os.walk(path):
                for exclude in exclude_dirs:
                    if exclude in dirnames:
                        dirnames.remove(exclude)
                for filename in filenames:
                    fullpath = os.path.join(dirpath, filename)
                    print("testing: %s" % fullpath)
                    if is_python(fullpath):
                        yield fullpath
        else:
            print("    unknown type")


if __name__ == "__main__":
    # Two simple examples/tests
    for fullpath in walk_python_files(['.']):
        print(fullpath)
    print("----------")
    for fullpath in walk_python_files(['.'], is_python=can_be_compiled):
        print(fullpath)


