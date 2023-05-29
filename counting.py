import geopandas as gpd
import matplotlib                                # Agg is a non-interactive backend that can only write to files
matplotlib.use('agg')                            # Adding this for counting to run more than once
import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd
from shapely.geometry import LineString

#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)

def filter_and_count(source_airport):
       plt.clf()
       
       routes = pd.read_csv("static/database/routes.dat", delimiter=',',
                         names=['airline', 'id', 'source_airport', 'source_airport_id',
                                'destination_airport', 'destination_airport_id', 'codeshare',
                                'stops', 'equitment'])

       #Returns number of occurences of each airline from AER
       routes_filter = routes["source_airport"] == source_airport
       routes2 = routes[routes_filter].groupby(["airline"])["airline"].count().sort_values(ascending=False)

       routes2.plot(kind="bar")

       #Save as image
       plt.savefig('static/images/airport_count.png')

#Example:
#filter_and_count("AER")