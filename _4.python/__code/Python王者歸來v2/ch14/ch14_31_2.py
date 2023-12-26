# ch14_31_2.py
dst = 'bdata'
bytedata = bytes(range(0,256))
with open(dst, 'wb') as file_dst:
    file_dst.write(bytedata)








