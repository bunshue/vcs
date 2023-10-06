# 7-1-1 在 dict 查不到鍵時傳回預設值

name_for_userid = {
    382: '愛麗絲',
    950: '鮑勃',
    590: '呆伯特',
    }

def greeting(userid):
    return '哈嘍, {}!'.format(
        name_for_userid.get(userid, '訪客')
        )

print(greeting(590))

print(greeting(490))

#print(name_for_userid[490])