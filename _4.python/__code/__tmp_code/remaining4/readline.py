file1=open("phrase.txt ","r")
line= file1.readline()
while line != '':
    print(line,end='')
    line= file1.readline()
file1.close()
