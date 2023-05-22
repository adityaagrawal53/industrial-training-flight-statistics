from math import radians, degrees, sin, cos, asin, acos, sqrt
import pandas as pd

# input: source airport ID (int)
# output: closest_city, furthest_city
# closest_city = float, distance in kilometers
# furthest_city = float, distance in kilometers

def find_continent(source_city, route_id):

    airports = pd.read_csv("static/airports.dat", delimiter=',',
                           names=['id', 'name', 'city', 'country', 'iata',
                                  'icao', 'lat', 'long', 'altitude', 'timezone',
                                  'dst', 'tz', 'type', 'source'])
    continents = pd.read_csv("Countries-Continents.csv", delimiter=',',
                             names = ['continent', 'country'])

    routes = pd.read_csv("static/routes.dat", delimiter=',',
                         names=['airline', 'id', 'source_airport', 'source_airport_id',
                                'destination_airport', 'destination_airport_id', 'codeshare',
                                'stops', 'equipment'])

    filter = airports["city"] == source_city

    airports2 = airports[filter]
    country_of_city = airports2["country"][0]



    continent_filter =continents["country"] = country_of_city
    res = continents[continent_filter]

    print("Destination continent:" + res)

#city = "Berlin"
#find_continent(city)