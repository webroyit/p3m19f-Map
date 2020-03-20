import folium

# create map object
m = folium.Map(location = [40.755571,-73.9465337], zoom_start = 12)

# global tooltip
tooltip = "Click to see more"

# create custom marker icon
logoIcon = folium.features.CustomIcon("logo.png", icon_size = [50, 50])

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

# folium.Icon(color, icon) to change the color and icon
folium.Marker([40.7609969,-73.9504689],
                popup = "<strong>Location Four</strong>",
                tooltip = tooltip,
                icon = folium.Icon(color = "red", icon = "leaf")).add_to(m)

# folium.Icon(color) to change the color of the icon
folium.Marker([40.7183356,-73.9549321],
                popup = "<strong>Location Five</strong>",
                tooltip = tooltip,
                icon = logoIcon).add_to(m)

# circle marker
folium.CircleMarker(
    location = [40.7451322,-73.8502186],
    radius = 50,
    popup = "Lucky Zone",
    fill = True,
    fill_color = "#f5f542"
).add_to(m)

# generate the code for the map on index.html
m.save("index.html")