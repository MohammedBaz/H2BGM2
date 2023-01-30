import streamlit as st
import  ee
import pandas

def GetInformtionFromGoogleEarth(ListofBands,StartDate,EndDate,Latitude,Longitude):
  ImageCollectionName='COPERNICUS/S2_HARMONIZED'
  PoI = ee.Geometry.Point(Longitude, Latitude)
  ImageCollection=ee.ImageCollection(ImageCollectionName)
  FilteredImageCollections = ImageCollection.filterDate(StartDate, EndDate).filterMetadata('CLOUDY_PIXEL_PERCENTAGE',"less_than", 35)
  FInstance=FilteredImageCollections.first()
  
  ImageCollectionName1='GOOGLE/DYNAMICWORLD/V1'
  ImageCollection1=ee.ImageCollection(ImageCollectionName1)
  FilteredImageCollections1 = ImageCollection1.filterMetadata('system:index','equals',FInstance.get('system:index').getInfo())
  return (FilteredImageCollections1)
  
StartDate='2020-10-19'
EndDate='2021-10-1'
Latitude=21.0807514
Longitude= 40.2975893

probabilityBands = [
  'water', 'trees', 'grass', 'flooded_vegetation', 'crops', 'shrub_and_scrub',
  'built', 'bare', 'snow_and_ice'
]
results=GetInformtionFromGoogleEarth(probabilityBands,StartDate,EndDate,Latitude,Longitude)
#st.write(results.count())
#imgListFirst3 = results.toList(3)
#st.write(imgListFirst3.get(4))
#st.write(len(imgListFirst3))
first_image = results.first()
band = first_image.bandNames().get(0)
