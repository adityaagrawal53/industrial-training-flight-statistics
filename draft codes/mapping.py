import csv
import geopandas as gpd
import pandas as pd
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from shapely.geometry import LineString

def filter_and_map(d):
       # Flight data:
       airports = pd.read_csv("static/database/airports.dat", delimiter=',',
                           names=['id', 'name', 'city', 'country', 'iata',
                                  'icao', 'lat', 'long', 'altitude', 'timezone',
                                  'dst', 'tz', 'type', 'source'])

       routes = pd.read_csv("static/database/routes.dat", delimiter=',',
                         names=['airline', 'id', 'source_airport', 'source_airport_id',
                                'destination_airport', 'destination_airport_id', 'codeshare',
                                'stops', 'equitment'])

       routes_filter = routes["source_airport"] == d
       routes = routes[routes_filter]

       # For getting source and destination airports
       source_airports = airports[['name', 'iata', 'icao', 'lat', 'long']]
       destination_airports = source_airports.copy()
       source_airports.columns = [str(col) + '_source' for col in source_airports.columns]
       destination_airports.columns = [str(col) + '_destination' for col in destination_airports.columns]

       routes = routes[['source_airport', 'destination_airport']]
       routes = pd.merge(routes, source_airports, left_on='source_airport', right_on='iata_source')
       routes = pd.merge(routes, destination_airports, left_on='destination_airport', right_on='iata_destination')

       # For plotting flight path over map
       fig = plt.figure(facecolor='black')
       ax = plt.axes(projection=ccrs.Robinson())
       ax.stock_img()
       fig.set_size_inches(7, 3.5)

       # Takes a list of latitude and longitude pairs and creates a line that joins those points
       geometry = [LineString([[routes.iloc[i]['long_source'], routes.iloc[i]['lat_source']], [routes.iloc[i]['long_destination'], routes.iloc[i]['lat_destination']]]) for i in range(routes.shape[0])]
       routes = gpd.GeoDataFrame(routes, geometry=geometry, crs='EPSG:4326')

       routes.plot(ax=ax, transform=ccrs.Geodetic(), color='red', linewidth=0.5, alpha=1)

       plt.setp(ax.spines.values(), color='black')
       plt.setp([ax.get_xticklines(), ax.get_yticklines()], color='black')
       ax.set_ylim(-7000000, 8800000)

       plt.show()

# Example:
#filter_and_map("MSQ")