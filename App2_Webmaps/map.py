import folium
import pandas


# reading volcano data as csv
data = pandas.read_csv("Volcanoes_USA.txt")


#color producer function for feature group Volcanoes

def color_producer(elevation):
    if elevation < 1000 :
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


# data for volcanoes

lat = list(data["LAT"])
lon = list(data["LON"])
elev =  list(data["ELEV"])


map = folium.Map(location = [38.58, -99.09], zoom_start = 6, tiles = "Mapbox Bright") #base map



#feature groups to control each Layer

fg1 = folium.FeatureGroup(name = "Volcanoes")
fg2 = folium.FeatureGroup(name = "Polpulation")

# Adding volcanoes markers

for lt , lg , el in zip(lat,lon,elev) :  # for all individual volcanoes zipping data together
    # fg.add_child(folium.Marker(location = [lt,lg], popup = str(el) + " m", icon = folium.Icon(color_producer(el))))
    fg1.add_child(folium.CircleMarker(location = [lt,lg], radius = 6, popup = str(el) + " m",
     fill_color = color_producer(el), color = "grey", fill = True, fill_opacity = 0.7 ))



d_f = open("world.json", "r", encoding = "utf-8-sig")

fg2.add_child(folium.GeoJson(d_f.read(), style_function = lambda x : {'fillColor':'green'
if x['properties']['POP2005']<10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# Adding feature groups to base map
map.add_child(fg1)
map.add_child(fg2)

# Addding layer controls to base Map
map.add_child(folium.LayerControl())

# Saving the Map
map.save("Map1.html")
