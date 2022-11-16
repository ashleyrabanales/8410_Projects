
import plotly
import plotly.express as px
import pandas as pd

df = pd.read_json("locations.json")
df.head()

fig = px.scatter_mapbox(df,
                        lat = "lat",
                        lon = "lng",
                        hover_name = "name",
                        zoom = 3,
                        width = 100,
                        height = 400)
fig.update_layout(mapbox_style = "open-street-map")
fig.update_layout(margin={"r":0, "t":0, "l":0, "b":0})
fig.show()

