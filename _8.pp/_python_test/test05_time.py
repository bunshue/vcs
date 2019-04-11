import time

start = time.time()

ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970: ", ticks)


time1 = time.gmtime(28800)
time2 = time.gmtime()

print(time1)
print(time2)



time3 = time.localtime(1234)
time4 = time.localtime()

print(time3)
print(time4)


time5 = time.asctime()

print(time5)


time6 = time.ctime()
time7 = time.ctime(time.time())

print(time6)
print(time7)

localtime = time.strftime("%Y/%m/%d %A %H:%M:%S", time.localtime(time.time()))
print("現在是: ", localtime)


stop = time.time()

diff = stop - start

print("使用時間 " + str(diff) + " 秒")







