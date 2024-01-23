#定義函式
def funTest(*number):
    outcome = 1
    for item in number:
        outcome *= item
    return outcome

#呼叫函式
print('1個引數:', funTest(7))
print('2個引數:', funTest(12, 3))
print('4個引數:', funTest(3, 5, 9, 14))
