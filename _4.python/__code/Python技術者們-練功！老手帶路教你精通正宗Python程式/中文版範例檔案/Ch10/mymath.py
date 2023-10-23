"""mymath – 自訂數學模組"""
pi = 3.14159
def area(r):
    """area(r): 傳回半徑r的圓形面積."""
    global pi
    return(pi * r * r)