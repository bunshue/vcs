# ch12_9_6.py
class Counter():
    counter = 0                             # 類別屬性,可由類別本身調用
    def __init__(self):
        Counter.counter += 1                # 更新指標
    @classmethod
    def show_counter(cls):                  # 類別方法,可由類別本身調用
        print("class method")
        print("counter = ", cls.counter)    # 也可使用Counter.counter調用
        print("counter = ", Counter.counter)
        
one = Counter()
two = Counter()
three = Counter()
Counter.show_counter()












        
        
