# 7-1-2 在 dict 查不到鍵時傳回預設值、並將預設值加入 dict

name_for_userid = {
    382: '愛麗絲',
    950: '鮑勃',
    590: '呆伯特',
    }

def greeting(userid):
    return '哈嘍, {}!'.format(
        name_for_userid.setdefault(userid, '訪客')
        )

print(greeting(590))

print(greeting(490))

print(name_for_userid)