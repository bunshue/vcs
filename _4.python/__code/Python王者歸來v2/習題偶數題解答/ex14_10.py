# ex14_10.py
src = input("請輸入來源圖檔 : ")
dst = input("請輸入目的圖檔 : ")

with open(src, 'rb') as file_rd:
    tmp = file_rd.read()
    with open(dst, 'wb') as file_wr:
        file_wr.write(tmp)






