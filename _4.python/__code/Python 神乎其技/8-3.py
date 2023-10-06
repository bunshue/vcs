# 8-3 揭開 bytecode 的神秘面紗 (以 dis 模組檢視)

import dis

def greet(name):
    return '你好呀, ' + name + '!'

print(greet('吉多‧范羅蘇姆'))

print('')

print(dis.dis(greet))