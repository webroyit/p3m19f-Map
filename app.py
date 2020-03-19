import folium

# create map object
m = folium.Map(location = [40.755571,-73.9465337], zoom_start = 12)

# create markers
folium.Marker([40.8448089,-73.9106434],
                popup = "<strong>Location One</strong>").add_to(m)

# generate the code for the map on index.html
m.save("index.html")