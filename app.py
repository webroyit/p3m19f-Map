import folium

# create map object
m = folium.Map(location = [40.755571,-73.9465337], zoom_start = 12)

# generate the code for the map 
m.save("index.html")