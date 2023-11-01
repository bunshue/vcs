with open("phrase.txt","r") as file1:
    txt = file1.readlines()#一次讀取所有行
    for line in txt: #以for廻圈讀取
        print(line, end = '')
