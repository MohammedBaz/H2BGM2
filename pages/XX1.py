import ee
import geemap
Map = geemap.Map()
Map.add_basemap('HYBRID')
Map
# Set the region of interest by simply drawing a polygon on the map
region = Map.user_roi
if region is None:
    region = ee.Geometry.BBox(-89.7088, 42.9006, -89.0647, 43.2167)

Map.centerObject(region)
# Set the date range
start_date = '2021-01-01'
end_date = '2022-01-01'
# Create a Sentinel-2 image composite
image = geemap.dynamic_world_s2(region, start_date, end_date)
vis_params = {'bands': ['B4', 'B3', 'B2'], 'min': 0, 'max': 3000}
Map.addLayer(image, vis_params, 'Sentinel-2 image')
# Create Dynamic World land cover composite
landcover = geemap.dynamic_world(region, start_date, end_date, return_type='hillshade')
Map.addLayer(landcover, {}, 'Land Cover')
# Add legend to the map
Map.add_legend(title="Dynamic World Land Cover", builtin_legend='Dynamic_World')
Map
