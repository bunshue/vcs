from bokeh.plotting import figure, show, output_file

output_file("circle1.html")

p = figure(width=800, height=400, title="零用金統計")
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

show(p)
