import os.path as path
 
p = "D:\PythonChatGPT\ch11"
f = "ch11-2-2.py"
print(p, f)
r = path.join(p, f)
print("os.path.join(p,f) =", r)
