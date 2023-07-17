class MyException(RuntimeError):
    def __init__(self, arg):
        self.args = arg

def CheckSpeed(speed): #檢查速度
    if speed < 70:
        raise Exception("速度太慢了!") # 拋出 Exception 型別例外
    if speed > 110:
        raise Exception("已經超速了!") # 拋出 Exception 型別例外
    else:
        raise MyException("快樂駕駛，平安返家!") # 拋出 MyException 型別例外 
        
def convertTuple(tup):  # tuple 轉換為字串
    str =  ''.join(tup) 
    return str        
 
for speed in (60,100,150):      
    try:
        CheckSpeed(speed)    #檢查速度
    except MyException as e: #接收 MyException 的例外
        err= convertTuple(e.args) # tuple 轉換為串字
        print("目前時速：{}，{}" .format(speed,err))    
    except Exception as e:   #接收 Exception 的例外
        print("現在速度：{}，{}" .format(speed,e))   