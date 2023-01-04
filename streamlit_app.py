import folium as fl
from streamlit_folium import st_folium
import streamlit as st
import pandas
def get_pos(lat,lng):
    return lat,lng

m = fl.Map(location=[21.437273,40.512714],zoom_start=10)

#m.add_child(fl.LatLngPopup())
data=123456
map = st_folium(m, height=350, width=700)
try:
  data = map['last_clicked']['lat'],map['last_clicked']['lng']
except:
  print("An exception occurred")

if data is not None:
    st.write(data)
################
import json  
import os 
dictionary = {'type':st.secrets['type'],
              'project_id':st.secrets['project_id'],
              'private_key_id':st.secrets['private_key_id'],
              'private_key':st.secrets['private_key'],
              'client_email':st.secrets['client_email'],
              'client_id':st.secrets['client_id'],
              'auth_uri':st.secrets['auth_uri'],
              'token_uri':st.secrets['token_uri'],
              'auth_provider_x509_cert_url':st.secrets['auth_provider_x509_cert_url'],
              'client_x509_cert_url':st.secrets['client_x509_cert_url']
             }

#https://signup.earthengine.google.com/#!/service_accounts
PathtoKeyFile=os.path.join(os.getcwd(), "key.json")
with open(os.path.join(os.getcwd(), "key.json"), 'w') as outfile:
    json.dump(dictionary, outfile)

import ee
EE_CREDENTIALS = ee.ServiceAccountCredentials(st.secrets['client_email'], PathtoKeyFile)
ee.Initialize(EE_CREDENTIALS)
st.write("____________________________________ Initalised______________________________________________")
################
BldSA=ee.FeatureCollection('projects/sat-io/open-datasets/MSBuildings/Kingdom_of_Saudi_Arabia')
import geemap
import geopandas as gpd
PoI = ee.Geometry.Point(map['last_clicked']['lat'],map['last_clicked']['lng']) # Cast Lat and Long into required class
RoI = PoI.buffer(1e3) # Define a region of interest with a buffer zone of 1000 km around PoI.

filtered = BldSA.filterBounds(RoI)
transparent_df = geemap.ee_to_geopandas(filtered)
st.write(transparent_df)
