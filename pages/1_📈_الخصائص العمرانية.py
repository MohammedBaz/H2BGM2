import folium as fl
from streamlit_folium import st_folium
import streamlit as st
import pandas
import geemap
import geopandas as gpd
import ee
from matplotlib import pyplot as plt
from EEBkGr import EEAuth
import mpld3
import streamlit.components.v1 as components

col1, col2 = st.columns(2)

EEAuth()
BldSA=ee.FeatureCollection('projects/sat-io/open-datasets/MSBuildings/Kingdom_of_Saudi_Arabia')
st.write("الرجاء الضغط علي الخريطه لتوليد الخصائص العمرانية")
def GetBldFtPrint(RoI):
  filtered = BldSA.filterBounds(RoI)
  #st.write(filtered)
  transparent_df = geemap.ee_to_geopandas(filtered)
  #st.write((len(transparent_df)))
  fig, ax = plt.subplots()
  #fig=plt.figure()
  transparent_df.plot(ax=ax)
  transparent_df.plot()
  with col2:
    st.header("الرجاء الضغط علي الخريطه للحصول علي الخصائص العمرانية")
    st.pyplot(fig)
  
  #fig_html = mpld3.fig_to_html(fig)
  #components.html(fig_html, height=600)
################
def get_pos(lat,lng):
    return lat,lng

m = fl.Map(location=[21.437273,40.512714],zoom_start=10)

#tile = fl.TileLayer(
#        tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
#        attr = 'Esri',
#        name = 'Esri Satellite',
#        overlay = True,
#        #control = True
#       ).add_to(m)

m.add_child(fl.LatLngPopup())
data=123456

with col1:
  st.header("التوزيع العمراني")
  map = st_folium(m, height=350, width=350)
try:
  data = map['last_clicked']['lat'],map['last_clicked']['lng']
  PoI = ee.Geometry.Point(map['last_clicked']['lng'],map['last_clicked']['lat']) # Cast Lat and Long into required class
  #st.write(PoI)
  RoI = PoI.buffer(1e3) # Define a region of interest with a buffer zone of 1000 km around PoI.
  GetBldFtPrint(RoI)
except:
  print("An exception occurred")

if data is not None:
    st.write(data)
################

################
