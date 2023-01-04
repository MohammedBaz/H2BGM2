import streamlit as st
from streamlit_folium import folium_static
import folium
m = folium.Map()
m.add_child(folium.LatLngPopup())
folium_static(m)
