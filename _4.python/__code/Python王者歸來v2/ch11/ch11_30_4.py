# ch11_30_4.py
def local_fun():
    var_nonlocal = 22    
    def local_inner():
        global var_global
        nonlocal var_nonlocal        
        var_global = 111
        var_nonlocal = 222
    local_inner()
    print('local_fun輸出 var_global   = ', var_global)
    print('local_fun輸出 var_nonlocal = ', var_nonlocal)
    
var_global = 1
var_nonlocal = 2
print('主程式輸出 var_global   = ', var_global)
print('主程式輸出 var_nonlocal = ', var_nonlocal)
local_fun()
print('主程式輸出 var_global   = ', var_global)
print('主程式輸出 var_nonlocal = ', var_nonlocal)


    






