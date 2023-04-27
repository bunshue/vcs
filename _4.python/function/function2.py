print("自定義函數, 寫在程式裡面")

def area(radius):
	result = radius * radius * 3.14
	return result

def washingMachine():
	print('注水')
	print('輕柔清洗')
	print('洗淨洗劑')
	print('脫水')
	print('烘乾')

washingMachine()

def washingMachine(mode):
	print('注水')
	if (mode == 'soft'):
		print('輕柔清洗')
	elif (mode == 'hard'):
		print('強力清洗')
	else:
		print('一般清洗')


mode = 'soft'
if (mode == 'soft'):
	print('輕柔清洗')
elif (mode == 'hard'):
	print('強力清洗')
else:
	print('一般清洗')



print("自定義函數, 無參數")
def mycnt1():
    for i in range(10, 20, 5):
        print(i)

mycnt1()

print("自定義函數, 有參數")
def mycnt2(n):
    for i in range(10, n, 5):
        print(i)

mycnt2(30)

print("自定義函數, 有參數，有預設值")
def mycnt3(n = 20):
    for i in range(10, n, 5):
        print(i)

mycnt3()
mycnt3(30)

print("自定義函數, 多個參數")

def mycnt4(n1 = 10, n2 = 20):
    for i in range(n1, n2, 5):
        print(i)

mycnt4()
mycnt4(5)
mycnt4(5, 15)

print("函數返回值")

def mysum(n1, n2):
    "函數的說明"
    return n1 + n2

print(mysum(10, 20))




def f(x):
    return x**2

f(10)



def add(x,y):
    return x+y

z = add(1234,5678)
print(z)



#撰寫接受任意數目引數的函式
def avg(first, *rest):
    return (first + sum(rest)) / (1+len(rest))

a = avg(1,2)
b = avg(1,2,3,4)

print("average 1", a, "\n")
print("average 2", b, "\n")

def japanese(month):
    month_name = {
        1:"睦月", 2:"如月", 3:"彌生", 4:"卯月", 5:"皐月", 6:"水無月",
        7:"文月", 8:"葉月", 9:"長月", 10:"神無月", 11:"霜月", 12:"師走"
    }
    try:
        response = month_name[month]
    except:
        response = '請輸入月份數字。'

    return response

print(japanese(5))




def add2number(a, b):
    global d
    c = a + b
    d = a + b
    print("在函數中，(c={}, d={})".format(c,d))
    return c

c = 10
d = 99
print("呼叫函數前，(c={}, d={})".format(c,d))
print("{} + {} = {}".format(2, 2, add2number(2, 2)))
print("函數呼叫後，(c={}, d={})".format(c,d))



def add(n1,n2):
    return n1+n2
    
def sub(n1,n2):
    return n1-n2

print(add(5,2))  # 7
print(sub(5,2))  # 3





def ctof(c):  #攝氏轉華氏
    f = c * 1.8 + 32
    return f

inputc = float(input("請輸入攝氏溫度："))
print("華氏溫度為：%5.1f 度" % ctof(inputc))





  



