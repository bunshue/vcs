# ch6_18.py
strN = " DeepStone "
strL = strN.lstrip( )       # 刪除字串左邊多餘空白
strR = strN.rstrip( )       # 刪除字串右邊多餘空白
strB = strN.lstrip( )       # 先刪除字串左邊多餘空白
strB = strB.rstrip( )       # 再刪除字串右邊多餘空白
strO = strN.strip( )        # 一次刪除頭尾端多餘空白
print("/%s/" % strN)
print("/%s/" % strL)
print("/%s/" % strR)
print("/%s/" % strB)
print("/%s/" % strO)


    
