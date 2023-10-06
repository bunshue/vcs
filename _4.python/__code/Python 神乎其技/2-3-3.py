# 2-3-3 巢狀 with 與資源管理器 - 撰寫 API 介面的漂亮排版功能

class Indenter:
    
    def __init__(self):
        self.level = 0
    
    def __enter__(self):
        self.level += 1
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1
        
    def print(self, text):
        print('    ' * self.level + text)


with Indenter() as indent:
    indent.print('嗨!')
    with indent:
        indent.print('哈嘍')
        with indent:
            indent.print('你好')
    indent.print('嘿啊')