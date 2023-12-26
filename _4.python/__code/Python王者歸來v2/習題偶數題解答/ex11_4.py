# ex11_4.py
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

op1 = int(input("請輸入第1個數字 = "))
op2 = int(input("請輸入第2個數字 = "))
oper = input("請輸入運算子(+,-,*,/) : ")

if oper == "+":
    print("計算結果 = ", add(op1,op2))
elif oper == "-":
    print("計算結果 = ", sub(op1,op2))
elif oper == "*":
    print("計算結果 = ", mul(op1,op2))
elif oper == "/":
    print("計算結果 = ", div(op1,op2))
else:
    print("運算公式輸入錯誤")




