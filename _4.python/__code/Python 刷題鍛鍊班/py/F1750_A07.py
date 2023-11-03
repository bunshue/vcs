# F1750 附錄 A-7

def find_common_prefix(strs):
    prefix = []
    for c in zip(*strs):
        if len(set(c)) == 1:
            prefix.append(c[0])
        else:
             break
    return ''.join(prefix)

print(find_common_prefix(['expensive', 'export', 'experience']))
