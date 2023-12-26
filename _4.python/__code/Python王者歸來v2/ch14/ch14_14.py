# ch14_14.py
import glob

print("方法1:列出\\Python\\ch14工作目錄的所有檔案")
for file in glob.glob('D:\\Python\\ch14\*.*'):
    print(file)
    
print("方法2:列出目前工作目錄的特定檔案")
for file in glob.glob('ch14_1*.py'):
    print(file)
    
print("方法3:列出目前工作目錄的特定檔案")
for file in glob.glob('ch14_2*.*'):
    print(file)




      




