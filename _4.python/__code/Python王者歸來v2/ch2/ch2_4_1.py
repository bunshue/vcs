# ch2_4_1.py
a = b = c = 10
x = a + b + c + 12
print(x)
# 續行方法1     # PEP 8風格
y = a \
    + b \
    + c \
    + 12
print(y)
# 續行方法2     # PEP 8風格
z = ( a         # 此處可以加上註解  
      + b 
      + c 
      + 12 )
print(z)

