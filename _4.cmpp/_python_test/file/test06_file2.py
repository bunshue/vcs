filename_r = "TestFileR.txt"

print("一次讀完一檔")
f = open(filename_r, 'r')
line = f.readlines()
print(line),
f.close()

print("一次讀一行")
f = open(filename_r, 'r')
i = 0
while True:
    line = f.readline()
    if len(line) == 0:  #Zero length indicates EOF
        break;
    i = i + 1
    #print(str(i), line),    # Notice comma to avoid automatic newline added by Python
    print(line),
f.close()

print("一次讀一行")
f = open(filename_r, 'r')
for line in f: print(line) #通过迭代器访问
f.close()


print("附加模式寫檔案")
filename_w = "TestFileW.txt"
f = open(filename_w, "a")

data = "123456789\n"
f.write(data)
f.close()


fo = open("TestFileR.txt", "r+")
str = fo.read(10);  #讀10拜
print("Read String is : ", str)
# Close opend file
fo.close()
