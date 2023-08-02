import os, codecs, encodings

_debug = 0

def listcodecs(dir):
    names = []
    for filename in os.listdir(dir):
        if filename[-3:] != '.py':
            continue
        name = filename[:-3]
        # Check whether we've found a true codec
        try:
            codecs.lookup(name)
        except LookupError:
            # Codec not found
            continue
        except Exception as reason:
            # Probably an error from importing the codec; still it's
            # a valid code name
            if _debug:
                print('* problem importing codec %r: %s' % \
                      (name, reason))
        names.append(name)
    return names


print()
print(encodings)
print(encodings.__path__)
print(encodings.__path__[0])
print()
names = listcodecs(encodings.__path__[0])
names.sort()
print('all_codecs = [')
for name in names:
    print('    %r,' % name)
print(']')


