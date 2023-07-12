from bokeh.plotting import figure, show, output_file

output_file("personbokeh.html")

year =  [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]
person1 = [41500, 41958, 41915, 42773, 43136, 43458, 43642, 43828, 44012, 44011, 44204, 44228, 44928, 45684, 46430, 46801, 47084, 47267, 47506, 47408, 47304, 47333, 47305, 47861, 48060, 48156, 48298, 48532, 48618, 48226, 47821]
person2 = [37045, 37397, 36796, 38220, 38510, 38661, 38801, 39097, 39336, 39620, 40061, 40269, 41142, 41907, 42935, 43592, 44062, 44608, 44575, 44571, 44587, 44628, 44582, 45482, 46042, 46295, 46587, 47018, 47046, 46644, 46492]

print('year')
print(year)
print('person1')
print(person1)
print('person2')
print(person2)

p = figure(width = 800, height = 400, title = "桃園市大溪區歷年人口數")
p.title.text_font_size = "20pt"
p.xaxis.axis_label = "年度"
p.yaxis.axis_label = "人口數"
p.line(year, person1, line_width = 2)
p.line(year, person2, line_width = 2)

show(p)
