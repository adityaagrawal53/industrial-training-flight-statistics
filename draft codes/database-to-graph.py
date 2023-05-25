import geopandas as gpd
import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd
from shapely.geometry import LineString


# import cartopy.crs as ccrs

def funk(d):
    # read airports
    airports = pd.read_csv("../static/airports.dat", delimiter=',',
                           names=['id', 'name', 'city', 'country', 'iata',
                                  'icao', 'lat', 'long', 'altitude', 'timezone',
                                  'dst', 'tz', 'type', 'source'])

    print(airports)

#     inp = input("Enter the name of a country: ")
    inp = d["place"]
#     index = airports.index(inp)
    airport_filter = airports["country"] == inp
    airports2 = airports[airport_filter]

    img = plt.imread('openflights/data/map-2048.png')

    fig, ax = plt.subplots()
    ax.imshow(img)
    fig.set_size_inches(12,6)

    ax.scatter(airports['long'], airports['lat'], s=1.2, alpha=1, edgecolors='none')
    ax.scatter(airports2['long'], airports2['lat'], s=0.5, alpha=1, edgecolors='none')

    ax.axis('off')

    fig.savefig('static/images/airports_map.png')

    plt.show()

    # read routes

    routes = pd.read_csv("../static/routes.dat", delimiter=',',
                         names=['airline', 'id', 'source_airport', 'source_airport_id',
                                'destination_airport', 'destination_airport_id', 'codeshare',
                                'stops', 'equitment'])

    print(routes)

    # manipulate the data to be DataFrames instead of Linestrings.
    source_airports = airports[['name', 'iata', 'icao', 'lat', 'long']]
    destination_airports = source_airports.copy()
    source_airports.columns = [str(col) + '_source' for col in source_airports.columns]
    destination_airports.columns = [str(col) + '_destination' for col in destination_airports.columns]

    routes = routes[['source_airport', 'destination_airport']]
    routes = pd.merge(routes, source_airports, left_on='source_airport', right_on='iata_source')
    routes = pd.merge(routes, destination_airports, left_on='destination_airport', right_on='iata_destination')

    print(routes.columns)

    geometry = [LineString([[routes.iloc[i]['long_source'], routes.iloc[i]['lat_source']],
                            [routes.iloc[i]['long_destination'], routes.iloc[i]['lat_destination']]]) for i in
                range(routes.shape[0])]
    routes = gpd.GeoDataFrame(routes, geometry=geometry, crs='EPSG:4326')
    print(routes)

    # Data validation:
    fig = plt.figure(facecolor='black')
    ax = plt.axes()

    fig.set_size_inches(7, 3.5)
    ax.patch.set_facecolor('black')

    routes.plot(ax=ax, color='white', linewidth=0.1)

    plt.setp(ax.spines.values(), color='white')
    plt.setp([ax.get_xticklines(), ax.get_yticklines()], color='black')

    # Add on top the filtered data:
    source_airports2 = airports2[['name', 'iata', 'icao', 'lat', 'long']]
    destination_airports2 = source_airports2.copy()
    source_airports2.columns = [str(col) + '_source' for col in source_airports2.columns]
    destination_airports2.columns = [str(col) + '_destination' for col in destination_airports2.columns]

    routes2 = routes[['source_airport', 'destination_airport']]
    routes2 = pd.merge(routes2, source_airports2, left_on='source_airport', right_on='iata_source')
    routes2 = pd.merge(routes2, destination_airports2, left_on='destination_airport', right_on='iata_destination')

    print(routes.columns)

    geometry2 = [LineString([[routes2.iloc[i]['long_source'], routes2.iloc[i]['lat_source']],
                             [routes2.iloc[i]['long_destination'], routes2.iloc[i]['lat_destination']]]) for i in
                 range(routes2.shape[0])]
    routes2 = gpd.GeoDataFrame(routes2, geometry=geometry2, crs='EPSG:4326')
    print(routes2)

    routes2.plot(ax=ax, color='green', linewidth=0.5)

    plt.setp(ax.spines.values(), color='black')
    plt.setp([ax.get_xticklines(), ax.get_yticklines()], color='black')

    fig.savefig('static/images/routes_map.png')



dictionary = {"place": "Japan"}

funk(dictionary)
