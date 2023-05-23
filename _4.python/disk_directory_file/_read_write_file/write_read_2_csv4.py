
filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/python_ReadWrite_CSV3_eword.csv'

count = 0
with open(filename, 'r', encoding = 'UTF-8-sig') as f:
    for line in f:
        eword,cword = line.rstrip('\n').split(',')
        print(eword,":",cword)

        word={eword:cword}
        print(word)
        count += 1
        if count == 10:
            break

count = 0
with open(filename, 'r', encoding = 'UTF-8-sig') as f:
    for line in f:
        eword,cword = line.rstrip('\n').split(',')
        word={'eword':eword,'cword':cword}
        print(word)
        #word={eword:cword}
        #print(word)
        count += 1
        if count == 10:
            break




