class human():
    def __init__(self, name=None):
        if name:
            self.name = name
        else:
            self.name = '???'

    def talk(self, msg):
        print(f'{self.name}: {msg}')

class Taiwan(human):
    def __init__(self, name, age=None):
        super().__init__(name)   # 繼承 human 的 name
        if age:
            self.age = age
        else:
            self.age = '???'


a = human('oxxo')
b = human('tom')
c = human()     # 沒有輸入就採用預設值
print(a.name)   # oxxo
print(b.name)   # tom

a.talk('hello')      # oxxo: hello
b.talk('ya')         # tom: ya
c.talk('okok!!!!!')  # ???: okok!!!!!

c = Taiwan('qq', 18) 
print(c.name, c.age) # qq 18
