from bokeh.plotting import figure, show

p = figure(width=800, height=400)
listx = [1,5,7,9,13,16]
listy = [15,50,80,40,70,50]
p.line(listx, listy)
show(p)
