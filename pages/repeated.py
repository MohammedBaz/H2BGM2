import folium as fl
from streamlit_folium import st_folium
import streamlit as st
import pandas
import geemap
import geopandas as gpd
from matplotlib import pyplot as plt
from EEBkGr import EEAuth
import mpld3
import streamlit.components.v1 as components
import osmnx as ox
import ee
import plotly.express as px

col1, col2 = st.columns(2)

EEAuth()
BldSA=ee.FeatureCollection('projects/sat-io/open-datasets/MSBuildings/Kingdom_of_Saudi_Arabia')



def GetBldFtPrint(RoI):
  filtered = BldSA.filterBounds(RoI)
  transparent_df = geemap.ee_to_geopandas(filtered)
  fig = plt.figure() 
  transparent_df.plot() 
  fig_html = mpld3.fig_to_html(fig)
  with col2:
    st.write("التوزيع العمراني")
    components.html(fig_html, height=350)
    
  if len(transparent_df)>0:
    st.write(len(transparent_df)," عدد المباني داخل نطاق 1000 متر مربع متمركز حل النقطة التي تم اختيارها")
    st.write(transparent_df['geometry'].area.sum()*1000000,"  المساحات الكلية للمباني")
    st.write(transparent_df['geometry'].area.sum()/1000000,"نسبة الاراضي البيضاء")
    st.write(transparent_df['geometry'].area.mean(),"متوسط مساحات المباني ")
    st.write(transparent_df['geometry'].area.sum()*1000000,"  نسبة المباني غير منتظمة الاضلاع")
    st.write(transparent_df['geometry'].area.sum()/1000000,"اقل مسافة بين مبنين")
    G = ox.graph_from_polygon(RoI, network_type='all')
    st.write(G)
    fig, ax = plt.subplots()
    ox.plot_graph(G)  
    
  else:
    st.write("لا يوجد مباني داخل نطاق 1000 متر مربع متمركز حل النقطة التي تم اختيارها")
    
  #fig_html = mpld3.fig_to_html(fig)
  #components.html(fig_html, height=600)
################
#tile = fl.TileLayer(
#        tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
#        attr = 'Esri',
#        name = 'Esri Satellite',
#        overlay = True,
#        #control = True
#       ).add_to(m)



with col1:
  st.write("الرجاء الضغط علي الخريطه للحصول علي الخصائص العمرانية")
  m = fl.Map(location=[21.437273,40.512714],zoom_start=10)
  m.add_child(fl.LatLngPopup())
  map = st_folium(m, height=350, width=350)
  
try:
  PoI = ee.Geometry.Point(map['last_clicked']['lng'],map['last_clicked']['lat']) # Cast Lat and Long into required class
  RoI = PoI.buffer(1e3) # Define a region of interest with a buffer zone of 1000 km around PoI.
  GetBldFtPrint(RoI)
except:
  print("An exception occurred")
