#讀取檔案字典範例

print("將 字典 寫入檔案")
filename = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/sssssss3.txt'

scores=dict()

scores[1] = 30
scores[2] = 50
scores[3] = 80
scores[4] = 90
scores[5] = 100

with open(filename,'w') as fp:
    fp.write(str(scores))
    
print("寫入檔案 : " + filename)



import sys

std_data = dict()
with open(filename, encoding='utf-8') as fp:
    alldata = fp.readlines()
    for item in alldata:
        no, name = item.rstrip('\n').split(',')
        std_data[no] = name
print(std_data)




