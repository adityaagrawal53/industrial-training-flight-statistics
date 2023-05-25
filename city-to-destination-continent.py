from math import radians, degrees, sin, cos, asin, acos, sqrt
import pandas as pd


# input: source airport ID (int)
# output: closest_city, furthest_city
# closest_city = float, distance in kilometers
# furthest_city = float, distance in kilometers

def find_continent(source_city):
    airports = pd.read_csv('static/database/airports.dat', delimiter=',',
                           names=['id', 'name', 'city', 'country', 'iata',
                                  'icao', 'lat', 'long', 'altitude', 'timezone',
                                  'dst', 'tz', 'type', 'source'])

    ccs = pd.read_csv('static/database/Countries-Continents.csv', delimiter=',',
                             names=['continent', 'country'])

    routes = pd.read_csv('static/database/routes.dat', delimiter=',',
                         names=['airline', 'id', 'source_airport', 'source_airport_id',
                                'destination_airport', 'destination_airport_id', 'codeshare',
                                'stops', 'equipment'])

    # all the airports in the source city
    source_airports = airports[airports['city'] == source_city]

    # total airports counted in each continent
    north_america_sum = 0
    south_america_sum = 0
    europe_sum = 0
    asia_sum = 0
    africa_sum = 0
    oceania_sum = 0
    # loop through the dataframe:

    for _, route in routes.iterrows():
        for _, source_airport in source_airports.iterrows():
            # route to source airport
            if route['source_airport'] == source_airport['iata']:                
                d_ap = airports[airports['iata']==route['destination_airport']].squeeze() # destination in this route as a series in aps                
                d_continent = ccs[ccs['country']==d_ap['country']]['continent'].squeeze()                
                if isinstance(d_continent, str):
                    print(d_continent)
                    if d_continent == "North America":
                        north_america_sum += 1
                    elif d_continent == 'South America':
                        south_america_sum += 1
                    elif d_continent == 'Europe':
                        europe_sum += 1
                    elif d_continent == "Asia":
                        asia_sum += 1
                    elif d_continent == "Africa":
                        africa_sum += 1
                    elif d_continent == "Oceania":
                        oceania_sum += 1                    

    print(north_america_sum)
    print(south_america_sum)
    print(europe_sum)
    print(asia_sum)
    print(africa_sum)
    print(oceania_sum)


find_continent("Madrid")
