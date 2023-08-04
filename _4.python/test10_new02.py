print('字串轉拜列')
string = 'lion'
data = repr(string).encode('utf-8') + b'\0'
print(type(data))
print(data)

        
