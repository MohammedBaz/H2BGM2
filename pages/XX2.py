import streamlit as st
import  ee
import pandas


def GetInformtionFromGoogleEarth(ListofBands,StartDate,EndDate,Latitude,Longitude):
  ImageCollectionName='COPERNICUS/S2_HARMONIZED'
  PoI = ee.Geometry.Point(Longitude, Latitude)
  ImageCollection=ee.ImageCollection(ImageCollectionName)
  FilteredImageCollections = ImageCollection.filterDate(StartDate, EndDate).filterMetadata('CLOUDY_PIXEL_PERCENTAGE',"less_than", 35)
  ImageCollectionName1='GOOGLE/DYNAMICWORLD/V1'
  ImageCollection1=ee.ImageCollection(ImageCollectionName1)
  FilteredImageCollections1 = ImageCollection1.filterMetadata('system:index','equals',FInstance.get('system:index').getInfo())
  resultsdf=pandas.DataFrame(FilteredImageCollections1) #Cast the results getten from the above to dataframe
  headers = resultsdf.iloc[0] # set the header of dataframe to the first line of the results
  resultsdf = pandas.DataFrame(resultsdf.values[1:], columns=headers) # assign the results to the dataframe and use headers as columns names
  resultsdf = resultsdf.dropna() # drops all rows with no data 
  for band in ListofBands: # Convert the data to numeric values
        resultsdf[band] = pandas.to_numeric(resultsdf[band], errors='coerce')
  resultsdf['datetime'] = pandas.to_datetime(resultsdf['time'], unit='ms') # Convert the time field into a datetime.
  #resultsdf = resultsdf[['time','datetime',  *ListofBands]]
  return resultsdf

StartDate='2020-10-19'
EndDate='2021-10-1'
Latitude=21.0807514
Longitude= 40.2975893

ImageCollectionName='COPERNICUS/S2_HARMONIZED'
probabilityBands = [
  'water', 'trees', 'grass', 'flooded_vegetation', 'crops', 'shrub_and_scrub',
  'built', 'bare', 'snow_and_ice'
]
results=GetInformtionFromGoogleEarth(probabilityBands,StartDate,EndDate,Latitude,Longitude)
st.write(results)
