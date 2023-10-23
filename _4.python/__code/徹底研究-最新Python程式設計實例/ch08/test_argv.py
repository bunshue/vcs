import sys

print("sys.argv:{}".format(sys.argv))
print("文件名稱{}".format(sys.argv[0]))
length = len(sys.argv)
 
if len(sys.argv) < 2:
    sys.exit(0)

for i in range(1,length):
     n1 = sys.argv[i]
     print( "第{}個引數是{}".format(i,n1))
