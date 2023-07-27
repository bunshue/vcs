import os

srcdir = os.path.abspath("../..")
print('srcdir', srcdir)

lines = open('patchlevel.h').readlines()

major = minor = micro = level = serial = None

levels = {
    'PY_RELEASE_LEVEL_ALPHA':0xA,
    'PY_RELEASE_LEVEL_BETA': 0xB,
    'PY_RELEASE_LEVEL_GAMMA':0xC,
    'PY_RELEASE_LEVEL_FINAL':0xF
    }
for l in lines:
    if not l.startswith("#define"):
        continue
    l = l.split()
    if len(l) != 3:
        continue
    _, name, value = l
    if name == 'PY_MAJOR_VERSION': major = value
    if name == 'PY_MINOR_VERSION': minor = value
    if name == 'PY_MICRO_VERSION': micro = value
    if name == 'PY_RELEASE_LEVEL': level = levels[value]
    if name == 'PY_RELEASE_SERIAL': serial = value

short_version = major+"."+minor
print('short_version', short_version)

# See PC/make_versioninfo.c
FIELD3 = 1000*int(micro) + 10*level + int(serial)
current_version = "%s.%d" % (short_version, FIELD3)
print('current_version', current_version)

docfile = micro
if level < 0xf:
    if level == 0xC:
        docfile += "rc%s" % (serial,)
    else:
        docfile += '%x%s' % (level, serial)
docfile = 'python%s%s%s.chm' % (major, minor, docfile)
    
# Merge CRT into MSI file. This requires the database to be closed.
mod_dir = os.path.join(os.environ["ProgramFiles"], "Common Files", "Merge Modules")
print('mod_dir', mod_dir)


