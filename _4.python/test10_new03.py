
print('字典的用法')
plats = {
    'Linux': 'platform_linux_distribution',
    'Mac': 'platform_mac_ver',
    'Windows': 'platform_win32_ver',
}

print(type(plats))
print(plats)

for name, func in plats.items():
    plat = '%s %r' % (name, func)
    print(plat)



