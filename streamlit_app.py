import folium as fl
from streamlit_folium import st_folium
import streamlit as st
import pandas
import json  
import os 
import geemap
import geopandas as gpd
import ee
from matplotlib import pyplot as plt
from EEBkGr import EEAuth
EEAuth()

BldSA=ee.FeatureCollection('projects/sat-io/open-datasets/MSBuildings/Kingdom_of_Saudi_Arabia')


def GetBldFtPrint(RoI):
  filtered = BldSA.filterBounds(RoI)
  #st.write(filtered)
  transparent_df = geemap.ee_to_geopandas(filtered)
  #st.write((len(transparent_df)))
  fig, ax = plt.subplots()
  transparent_df.plot(ax=ax)
  st.pyplot(fig)
################
def get_pos(lat,lng):
    return lat,lng

m = fl.Map(location=[21.437273,40.512714],zoom_start=10, TileLayer='Stamen.Terrain')

m.add_child(fl.LatLngPopup())
data=123456
map = st_folium(m, height=350, width=700)
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



