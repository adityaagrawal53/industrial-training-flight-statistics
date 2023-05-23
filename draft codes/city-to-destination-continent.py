from math import radians, degrees, sin, cos, asin, acos, sqrt
import pandas as pd


# input: source airport ID (int)
# output: closest_city, furthest_city
# closest_city = float, distance in kilometers
# furthest_city = float, distance in kilometers

def find_continent(source_city):
    airports = pd.read_csv('../static/airports.dat', delimiter=',',
                           names=['id', 'name', 'city', 'country', 'iata',
                                  'icao', 'lat', 'long', 'altitude', 'timezone',
                                  'dst', 'tz', 'type', 'source'])

    continents = pd.read_csv('../Countries-Continents.csv', delimiter=',',
                             names=['continent', 'country'])

    routes = pd.read_csv('../static/routes.dat', delimiter=',',
                         names=['airline', 'id', 'source_airport', 'source_airport_id',
                                'destination_airport', 'destination_airport_id', 'codeshare',
                                'stops', 'equipment'])

    filter1 = airports['city'] == source_city
    source_airports = airports[filter1]

    # total airports counted in each continent
    north_america_sum = 0
    south_america_sum = 0
    europe_sum = 0
    asia_sum = 0
    africa_sum = 0
    oceania_sum = 0
    # loop through the dataframe:

    for index, row in routes.iterrows():
        for index2, row2 in source_airports.iterrows():
            # print("Source airport at this row:", row['source_airport'])

            if row['source_airport'] == row2['iata']:
                print("Found a match!")
                airport_code = row['destination_airport']
                print("Airport code: ", airport_code)
                # filter2 = row2['iata'] == airport_code
                destination_airport = row2[row2['iata'] == airport_code]
                print("Destination airport: ", destination_airport)
                for index3, row3 in continents.iterrows():
                    if row3['country'] == destination_airport['country']:
                        continent = row3['continent']

                        if continent == "North America":
                            north_america_sum += 1
                        elif continent == 'South America':
                            south_america_sum += 1
                        elif continent == 'Europe':
                            europe_sum += 1
                        elif continent == "Asia":
                            asia_sum += 1
                        elif continent == "Africa":
                            africa_sum += 1
                        elif continent == "Oceania":
                            oceania_sum += 1

    print(north_america_sum)
    print(south_america_sum)
    print(europe_sum)
    print(asia_sum)
    print(africa_sum)
    print(oceania_sum)


find_continent("Berlin")
