# ch2_10.py
import inspect

# 輸出內建函數名
builtin_functions = [name for name, obj in inspect.getmembers(__builtins__) if inspect.isbuiltin(obj)]
for function_name in builtin_functions:
    print(function_name)


