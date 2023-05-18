import geopandas as gpd
import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd
from shapely.geometry import LineString

#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)

airports = pd.read_csv("static/airports.dat", delimiter=',',
                           names=['id', 'name', 'city', 'country', 'iata',
                                  'icao', 'lat', 'long', 'altitude', 'timezone',
                                  'dst', 'tz', 'type', 'source'])

routes = pd.read_csv("static/routes.dat", delimiter=',',
                         names=['airline', 'id', 'source_airport', 'source_airport_id',
                                'destination_airport', 'destination_airport_id', 'codeshare',
                                'stops', 'equitment'])

airport_filter = airports["country"] == "Finland"
airports2 = airports[airport_filter]

#Returns number of occurences of each airline from AER
routes_filter = routes["source_airport"] == "AER"
routes2 = routes[routes_filter].groupby(["airline"])["airline"].count().sort_values(ascending=False)

print(routes2)

routes2.plot(kind="bar")
plt.show()