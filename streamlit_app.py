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
def GetInformtionFromGoogleEarth(ImageCollectionName,ListofBands,Resultion,StartDate,EndDate,Latitude,Longitude):
  PoI = ee.Geometry.Point(Longitude, Latitude) # Cast Lat and Long into required class
  ImageCollection=ee.ImageCollection(ImageCollectionName) # get the image collecton from google earthengine
  FilteredImageCollections = ImageCollection.select(ListofBands).filterDate(StartDate, EndDate) # apply filter(s):time and/or bands
  results=FilteredImageCollections.getRegion(PoI, Resultion).getInfo() # get the time series of the required bands
  resultsdf=pandas.DataFrame(results) #Cast the results getten from the above to dataframe
  headers = resultsdf.iloc[0] # set the header of dataframe to the first line of the results
  resultsdf = pandas.DataFrame(resultsdf.values[1:], columns=headers) # assign the results to the dataframe and use headers as columns names
  resultsdf = resultsdf.dropna() # drops all rows with no data 
  for band in ListofBands: # Convert the data to numeric values
        resultsdf[band] = pandas.to_numeric(resultsdf[band], errors='coerce')
  resultsdf['datetime'] = pandas.to_datetime(resultsdf['time'], unit='ms') # Convert the time field into a datetime.
  resultsdf = resultsdf[['time','datetime',  *ListofBands]]
  return resultsdf



ImageCollectionName='MODIS/006/MOD13A2'
ListofBands=['NDVI', 'EVI']
Resultion=1000
StartDate='2020-10-19'
EndDate='2022-10-1'
Latitude=21.0807514
Longitude= 40.2975893

results=GetInformtionFromGoogleEarth("NASA/NEX-DCP30",["pr"],4638.3,StartDate,EndDate,Latitude,Longitude)

st.write(results)
