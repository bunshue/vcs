import pandas as pd
from numpy.random import randint

df1 = pd.DataFrame(randint(5,10,size=(3,4)),columns=["a","b","c","d"])  
df2 = pd.DataFrame(randint(5,10,size=(2,3)),columns=["b","d","a"])  
print(df1)
df1.to_html("ch8-4-4a-01.html")
print("---------------------------")
print(df2)
df2.to_html("ch8-4-4a-02.html")
print("---------------------------")  
df3 = pd.concat([df1,df2])  
print(df3)
df3.to_html("ch8-4-4a-03.html")
print("---------------------------")
df4 = pd.concat([df1,df2], ignore_index=True)
print(df4) 
df4.to_html("ch8-4-4a-04.html") 