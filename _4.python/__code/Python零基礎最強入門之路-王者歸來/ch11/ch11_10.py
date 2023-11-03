# ch11_10.py
def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi, ", name, " Good Morning!")
    return                      # Python將自動回傳None
ret_value = greeting('Nelson')
print("greeting( )傳回值 = ", ret_value)
print(ret_value, " 的 type  = ", type(ret_value))



