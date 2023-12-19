"""
读写二进制文件
"""
import base64

with open('mm.jpg', 'rb') as f:
    data = f.read()
    # print(type(data))
    # print(data)
    print('字节数:', len(data))
    # 将图片处理成BASE-64编码
    print(base64.b64encode(data))

with open('girl.jpg', 'wb') as f:
    f.write(data)
print('写入完成!')
