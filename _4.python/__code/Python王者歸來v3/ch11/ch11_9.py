# ch11_9.py
def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi, ", name, " Good Morning!")
    
ret_value = greeting('Nelson')
print(f"greeting()傳回值 = {ret_value}")
print(f"{ret_value} 的 type  = {type(ret_value)}")



