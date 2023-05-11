from bokeh.plotting import figure, show, output_file
from bs4 import BeautifulSoup as bs
import requests

output_file("personbokeh.html")

year = []
person = []
url = "http://www.daxi-hro.tycg.gov.tw/home.jsp?id=25&parentpath=0,21,22"
content = requests.get(url).text
parse = bs(content, "html.parser")
data1 = parse.find("tbody")
rows = data1.find_all("tr")
for row in rows:
    cols = row.find_all("td")
    if(len(cols) > 0):
        if cols[1].text!="─":
            year.append((cols[0].text[:-1]))
            person.append(cols[1].text)

p = figure(width=800, height=400, title="桃園市大溪區歷年戶數")
p.title.text_font_size = "20pt"
p.xaxis.axis_label = "年度"
p.yaxis.axis_label = "戶數"
p.line(year, person, line_width=2)
show(p)
