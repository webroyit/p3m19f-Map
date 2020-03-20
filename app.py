import folium

# create map object
m = folium.Map(location = [40.755571,-73.9465337], zoom_start = 12)

# global tooltip
tooltip = "Click to see more"

# create markers
# tooltip for display message when hover
# popup to display a popup
folium.Marker([40.8448089,-73.9106434],
                popup = "<strong>Location One</strong>",
                tooltip = tooltip).add_to(m)

# folium.Icon(icon) to change icon
folium.Marker([40.7292637,-74.0263432],
                popup = "<strong>Location Two</strong>",
                tooltip = tooltip,
                icon = folium.Icon(icon = "cloud")).add_to(m)

# folium.Icon(color) to change the color of the icon
folium.Marker([40.7804975,-73.9391392],
                popup = "<strong>Location Three</strong>",
                tooltip = tooltip,
                icon = folium.Icon(color = "green")).add_to(m)

# generate the code for the map on index.html
m.save("index.html")