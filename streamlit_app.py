import folium as fl
from streamlit_folium import st_folium
import streamlit as st

def get_pos(lat,lng):
    return lat,lng

m = fl.Map(location=[21.437273,40.512714],zoom_start=10)

#m.add_child(fl.LatLngPopup())

map = st_folium(m, height=350, width=700)


data=12345
data = get_pos(map['last_clicked']['lat'],map['last_clicked']['lng'])

if data is not None:
    st.write(data)
    fl.CircleMarker(
    location=[21.437273,40.512714],
    radius=50,
    popup="Laurelhurst Park",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",).add_to(m)
