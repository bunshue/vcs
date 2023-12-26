# ch11_10.py
def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi, ", name, " Good Morning!")
    return      # Python自動回傳 None
ret_value = greeting('Nelson')
print(f"greeting()傳回值 = {ret_value}")
print(f"{ret_value} 的 type  = {type(ret_value)}")



