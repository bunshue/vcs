import pandas as pd

writer = pd.ExcelWriter('test.xlsx')
print(type(writer))

# 建立數據一
df1 = pd.DataFrame({"name":["david","tom","chiou"],
                    "id":[123,456,789] })
df1.to_excel(writer,sheet_name='sheet1',index=False)

# 建立數據二
df2 = pd.DataFrame({"電話":["0912-112233","0987-556677"],
                    "地址":["台北市","埔里鎮"] })
df2.to_excel(writer,sheet_name='工作表二')

# 儲存至 Excel文件中
writer.save()