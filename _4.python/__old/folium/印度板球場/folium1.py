import folium
import pandas as pd

data = pd.read_csv("stadium.csv", encoding="cp1252")
latitude = list(data['LAT'])
longitude = list(data['LON'])
name = list(data["NAME"])
capacity = list(data["capacity"])
website = list(data["website"])
picture = list(data['picture'])
f = folium.FeatureGroup("my map")

f.add_child(folium.GeoJson(data=(open("D:/_git/vcs/_big_files/india_states.json",'r',encoding='utf-8-sig').read())))
for lt, ln, nm, cp, ws, pic in zip(latitude, longitude, name, capacity, website, picture):
    f.add_child(folium.Marker(location=[lt, ln], popup="<b>name   : </b>"+nm+ "<br> <b>capacity  : </b>"+str(cp)+"<br><b>wikipidea link: </b><a href="+ws+">click here</a>"+"<br> <img src="+pic+" height=142 width=290>",icon=folium.Icon(color="green")))

map = folium.Map(location=[21.1458,79.0082],zoom_start=5)
map.add_child(f)
map.save('tmp_map.html')

print('製作完成')
