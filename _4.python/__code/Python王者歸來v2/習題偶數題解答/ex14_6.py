# ex14_6.py

str1 = 'Python入門邁向高手之路'
str2 = '作者:洪錦魁'
str3 = '深石數位科技'
str4 = 'DeepStone Corporation'
str5 = 'Deep Learning'

dst1 = 'ex14_6_1.txt'
dst2 = 'ex14_6_2.txt'
dst3 = 'ex14_6_3.txt'

dstStr = str1+'\n'+str2+'\n'+str3+'\n'+str4+'\n'+str5
with open(dst1, 'w') as dst_Obj:    # 開啟檔案mode=w
    dst_Obj.write(dstStr)           # 將str1輸出到檔案

with open(dst2, 'w') as dst_Obj:    # 開啟檔案mode=w
    dst_Obj.write(str1)             # 將str1輸出到檔案
    dst_Obj.write(str2)             # 將str2輸出到檔案
    dst_Obj.write(str3)             # 將str3輸出到檔案
    dst_Obj.write(str4)             # 將str4輸出到檔案
    dst_Obj.write(str5)             # 將str5輸出到檔案

with open(dst3, 'w') as dst_Obj:    # 開啟檔案mode=w
    dst_Obj.write(str1+'  ')        # 將str1輸出到檔案
    dst_Obj.write(str2+'  ')        # 將str2輸出到檔案
    dst_Obj.write(str3+'  ')        # 將str3輸出到檔案
    dst_Obj.write(str4+'  ')        # 將str4輸出到檔案
    dst_Obj.write(str5+'  ')        # 將str5輸出到檔案




    
