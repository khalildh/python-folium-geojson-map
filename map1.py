import folium
import pandas


map1 = folium.Map(location=[40, -75], zoom_start=6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

# volcanoes = pandas.read_csv("Volcanoes_USA.txt")
# for row in range(volcanoes.shape[0]):
#     coordinates = (volcanoes.iloc[row].LAT, volcanoes.iloc[row].LON)
#     fg.add_child(folium.Marker(location=coordinates, popup=str(coordinates), icon=folium.Icon(color='green')))
#
#
# map1.add_child(fg)
# map1.save("Map1.html")

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 2000:
        return 'orange'
    else:
        return 'red'


data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

for lt, ln, el in zip(lat, lon, elev):
    val = str(el) + " m"
    popupVar = folium.Popup(val, parse_html=True)
    #fg.add_child(folium.Marker(location=(lt, ln), popup=popupVar, icon=folium.Icon(color=color_producer(el))))
    fgv.add_child(folium.features.CircleMarker(
        location=[lt, ln], radius=6, popup=popupVar, color='grey',
        fill_color=color_producer(el), fill_opacity=0.7, fill=True))


fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map1.add_child(fgv)
map1.add_child(fgp)
map1.add_child(folium.LayerControl())
map1.save("index.html")
