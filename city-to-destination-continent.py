from math import radians, degrees, sin, cos, asin, acos, sqrt
import pandas as pd


# input: source airport ID (int)
# output: closest_city, furthest_city
# closest_city = float, distance in kilometers
# furthest_city = float, distance in kilometers

def find_continent(source_city):
    aps = pd.read_csv('static/database/airports.dat', delimiter=',',
                           names=['id', 'name', 'city', 'country', 'iata',
                                  'icao', 'lat', 'long', 'altitude', 'timezone',
                                  'dst', 'tz', 'type', 'source'])

    ccs = pd.read_csv('static/database/Countries-Continents.csv', delimiter=',',
                             names=['continent', 'country'])

    routes = pd.read_csv('static/database/routes.dat', delimiter=',',
                         names=['airline', 'id', 'source_airport', 'source_airport_id',
                                'destination_airport', 'destination_airport_id', 'codeshare',
                                'stops', 'equipment'])

    # vars to count total airports counted in each continent
    north_america_sum = 0
    south_america_sum = 0
    europe_sum = 0
    asia_sum = 0
    africa_sum = 0
    oceania_sum = 0

    # all the airports in the source city
    saps = aps[aps['city'] == source_city]        

    # loop through all source:
    for _, sap in saps.iterrows():

        # all the routes from this source airport (sap)
        rs_from_sap = routes[routes['source_airport']==sap['iata']]

        # loop through all routes from this source airport (sap)
        for _, route in rs_from_sap.iterrows():                    
            dap = aps[aps['iata']==route['destination_airport']].squeeze() # destination in this route as a series in aps                
            d_continent = ccs[ccs['country']==dap['country']]['continent'].squeeze()                
            if isinstance(d_continent, str):
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
