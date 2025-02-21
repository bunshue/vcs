import sys

print("------------------------------------------------------------")  # 60個

import bokeh.plotting
#from bokeh.sampledata.us_counties import data as counties
#from bokeh.plotting import figure, output_file, show

p = bokeh.plotting.figure(width=800, height=400)

p.circle([1, 2, 3], [4, 5, 6], size=100, color="orange", alpha=0.5)

bokeh.plotting.output_file("tmp_circle1.html")

#bokeh.plotting.show(p)

print("------------------------------------------------------------")  # 60個

#line 1
bokeh.plotting.output_file("tmp_line1.html")

p = bokeh.plotting.figure(width=800, height=400)
listx = [1,5,7,9,13,16]
listy = [15,50,80,40,70,50]
p.line(listx, listy)

#bokeh.plotting.show(p)

print("------------------------------------------------------------")  # 60個

#line 2

bokeh.plotting.output_file("tmp_line2.html")

p = bokeh.plotting.figure(width=800, height=400)
listx = [1,5,7,9,13,16]
listy = [15,50,80,40,70,50]
p.line(listx, listy)

#bokeh.plotting.show(p)

print("------------------------------------------------------------")  # 60個

#line 3

bokeh.plotting.output_file("tmp_line3.html")

p = bokeh.plotting.figure(width=800, height=400, title="零用金統計")
p.title.text_color = "green"
p.title.text_font_size = "18pt"
p.xaxis.axis_label = "年齡"
p.xaxis.axis_label_text_color = "violet"
p.yaxis.axis_label = "零用金"
p.yaxis.axis_label_text_color = "violet"
dashs = [12, 4]
listx1 = [1,5,7,9,13,16]
listy1 = [15,50,80,40,70,50]
#p.line(listx1, listy1, line_width=4, line_color="red", line_alpha=0.3, line_dash=dashs, legend = "男性")
p.line(listx1, listy1, line_width=4, line_color="red", line_alpha=0.3, line_dash=dashs)
listx2 = [2,6,8,11,14,16]
listy2 = [10,40,30,50,80,60]
#p.line(listx2, listy2, line_width=4, legend = "女性")
p.line(listx2, listy2, line_width=4)

#bokeh.plotting.show(p)

print("------------------------------------------------------------")  # 60個

#circle

bokeh.plotting.output_file("tmp_circle2.html")

p = bokeh.plotting.figure(width=800, height=400, title="零用金統計")
p.title.text_font_size = "18pt"
p.xaxis.axis_label = "X 軸"
p.yaxis.axis_label = "y 軸"
listx = [1,5,7,9,13,16]
listy = [15,50,80,40,70,50]
sizes=[10,20,30,30,20,10]
colors=["red","blue","green","pink","violet","gray"]
#sizes=25  #所有點相同大小
#colors="red"  #所有點相同顏色
p.circle(listx, listy, size=sizes, color=colors, alpha=0.5)

#bokeh.plotting.show(p)

print("------------------------------------------------------------")  # 60個

bokeh.plotting.output_file("tmp_personbokeh.html")

year =  [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]
person1 = [41500, 41958, 41915, 42773, 43136, 43458, 43642, 43828, 44012, 44011, 44204, 44228, 44928, 45684, 46430, 46801, 47084, 47267, 47506, 47408, 47304, 47333, 47305, 47861, 48060, 48156, 48298, 48532, 48618, 48226, 47821]
person2 = [37045, 37397, 36796, 38220, 38510, 38661, 38801, 39097, 39336, 39620, 40061, 40269, 41142, 41907, 42935, 43592, 44062, 44608, 44575, 44571, 44587, 44628, 44582, 45482, 46042, 46295, 46587, 47018, 47046, 46644, 46492]

print('year')
print(year)
print('person1')
print(person1)
print('person2')
print(person2)

p = bokeh.plotting.figure(width = 800, height = 400, title = "桃園市大溪區歷年人口數")
p.title.text_font_size = "20pt"
p.xaxis.axis_label = "年度"
p.yaxis.axis_label = "人口數"
p.line(year, person1, line_width = 2)
p.line(year, person2, line_width = 2)

#bokeh.plotting.show(p)

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



# 資料放在 C:\Users\070601\.bokeh\data
import bokeh.sampledata
#bokeh.sampledata.download()




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



