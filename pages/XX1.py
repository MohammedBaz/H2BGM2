import ee
import geemap

start_date = '2021-01-01'
end_date = '2022-01-01'
PoI = ee.Geometry.Point([21.437273,40.512714])
region = PoI.buffer(1e3)

# Create a Sentinel-2 image composite
image = geemap.dynamic_world_s2(region, start_date, end_date)
vis_params = {'bands': ['B4', 'B3', 'B2'], 'min': 0, 'max': 3000}
landcover = geemap.dynamic_world(region, start_date, end_date, return_type='hillshade')
st.write(landcover)
