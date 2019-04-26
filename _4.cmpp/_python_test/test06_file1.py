#f = open('test05_time.py', 'r', encoding = 'utf8')
f = open('test05_time.py', 'r', encoding = 'UTF-8')

print("檔名: ", f.name)
for line in f.readlines():
    #line = line.strip
    print(line)
f.close






