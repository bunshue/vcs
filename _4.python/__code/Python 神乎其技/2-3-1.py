# 2-3-1 在 with 敘述使用自訂資源管理器類別

with open('hello.txt', 'w') as f:
    f.write('Hello, World!')


class ManagedFile:
    
    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file
    
    def __exit__(self, exe_type, exe_value, traceback):
        if self.file:
            self.file.close()


with ManagedFile('hello2.txt') as f:
    f.write('Hello, World!')