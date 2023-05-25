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

    airport_code = ""
    destination_airport = ""

    print("Now computing destination airports, this might take a while...")
    for _, route in routes.iterrows():

        for _, source_airport in source_airports.iterrows():
            # print("Source airport at this route:", route['source_airport'])

            if route['source_airport'] == source_airport['iata']:
                # print("Found matching source airports!")
                airport_code = route['destination_airport']
                # print("Airport code: ", airport_code)

                for _, airport in airports.iterrows():
                    # print("Comparison between destination and airport name: ", airport_code, airport['iata'])
                    # filter2 = airport['iata'] == airport_code
                    # filter2 = airport['iata'].__contains__(airport_code)
                    if airport_code == airport['iata']:
                        destination_airport = airport
                        # print("Destination airport: ", destination_airport)
                        for _, continent in continents.iterrows():
                            if continent['country'] == destination_airport['country']:
                                continent = continent['continent']

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
                        break

    print("Number of destination airports in each continent: ")
    print("North America: ", north_america_sum)
    print("South America: ", south_america_sum)
    print("Europe: ", europe_sum)
    print("Asia: ", asia_sum)
    print("Africa: ", africa_sum)
    print("Oceania: ", oceania_sum)


find_continent("Madrid")
