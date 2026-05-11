from machine import Timer

count = 0

def msg(t):
    global count
    count = count + 1
    print("計數: ", count)
    
t = Timer(0)
t.init(period=1000, mode=Timer.PERIODIC, callback=msg)
