import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])

map = folium.Map(location=[ 35.92,  -86.86], zoom_start=9, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt,ln], popup="Marker", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")