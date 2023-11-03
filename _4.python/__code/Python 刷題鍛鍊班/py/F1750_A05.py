# F1750 附錄 A-5

def are_brackets_valid(s):
    brackets = {'(': ')', '[': ']', '{': '}'}
    stack = []
 
    for b in s:
        if b in brackets:
            stack.append(brackets[b])
        else:
            if not (stack and b == stack.pop()):
                return False
    return True if not stack else False

print(are_brackets_valid('[()]'))
