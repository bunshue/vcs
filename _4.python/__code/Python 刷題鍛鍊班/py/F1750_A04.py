# F1750 附錄 A-4

class Stack():
    def __init__(this):
        this.data = []
 
    def push(this, x):
        this.data.append(x)
 
    def pop(this):
        if this.data:
            return this.data.pop()
 
    def top(this):
        return this.data[-1]
 
    def min_num(this):
        return min(this.data)

    def max_num(this):
        return max(this.data)

stack = Stack()
stack.push(3)
stack.push(2)
stack.push(8)
stack.push(6)
stack.push(5)
print(stack.pop())
print(stack.top())
print(stack.min_num())
print(stack.max_num())
