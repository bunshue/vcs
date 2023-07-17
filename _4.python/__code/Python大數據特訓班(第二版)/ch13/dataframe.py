import pandas as pd

columns = ['姓名', '班級']
data = [['林大和','一年甲班'], ['張小明','一年乙班'], ['林美麗','一年乙班'],
        ['鄭中林','二年甲班'], ['林品朋','二年甲班'], ['陳明朋','二年乙班']]
df = pd.DataFrame(data, columns=columns)
#print(df)

df1 = df[df['班級']=='二年甲班']
#print(df1)
df2 = df[df['姓名'].str.contains('林')]
#print(df2)
df3 = df[(df['姓名'].str.contains('林')) & (df['班級'].str.contains('一年'))]
print(df3)
