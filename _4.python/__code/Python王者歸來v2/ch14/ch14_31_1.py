# ch14_31_1.py
src = 'hung.jpg'
dst = 'hung1.jpg'
tmp = ''

with open(src, 'rb') as file_rd:
    tmp = file_rd.read()
    with open(dst, 'wb') as file_wr:
        file_wr.write(tmp)






