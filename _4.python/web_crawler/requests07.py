#各國GDP資料

# 讀入csv 文字檔
import pandas as pd
csv_file = "https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.csv"
gdp = pd.read_csv(csv_file)
print('------------------------------------------------')
print(type(gdp))
print('------------------------------------------------')
print(gdp.head())
print('------------------------------------------------')



# 讀入excel 試算表
xlsx_file = "https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.xlsx"
gapminder = pd.read_excel(xlsx_file)
print('------------------------------------------------')
print(type(gapminder))
print('------------------------------------------------')
print(gapminder.head())
print('------------------------------------------------')

print('用list 標註變數名稱從DataFrame選出country 與continent 欄位：')
print(gapminder[['country', 'continent']])

print('------------------------------------------------')
print('選一個變數且沒有以list 標註，選出欄位資料，型別為Series')
country = gapminder['country']
print(type(country))
print('------------------------------------------------')
print('聚合函數計算sum，計算2007 年全球人口總數：')
aa = gapminder[gapminder['year'] == 2007][['pop']].sum()
print(aa)
print('------------------------------------------------')
print('計算2007 年全球的平均壽命、平均財富：')
bb = gapminder[gapminder['year'] == 2007][['lifeExp', 'gdpPercap']].mean()
print(bb)
print('------------------------------------------------')
print('groupby群組計算2007 年各洲人口總數：')
cc = gapminder[gapminder['year'] == 2007].groupby(by = 'continent')['pop'].sum()
print(cc)

print('------------------------------------------------')


