
from math import radians, degrees, sin, cos, asin, acos, sqrt

# input: source airport ID (int)
# output: closest_city, furthest_city
# closest_city = float, distance in kilometers
# furthest_city = float, distance in kilometers

def closest_furthest(source, ):

    latitudes = {}
    longitudes = {}

    with open('static/airports.dat','r', encoding="utf-8") as f:
        for line in f:
            word = line.split(",")
            latitudes[int(word[0])] = word[6]
            longitudes[int(word[0])] = word[7]

    source_latitude = float(latitudes[source])
    source_longitude = float(longitudes[source])
    
    closest_city = (1, great_circle(source_longitude, source_latitude, float(longitudes[1]), float(latitudes[1])))
    furthest_city = (1, great_circle(source_longitude, source_latitude, float(longitudes[1]), float(latitudes[1])))

    for i in range(1, 67663):
        try:
            if i == source:
                pass
            else:
                distance = great_circle(source_longitude, source_latitude, float(longitudes[i]), float(latitudes[i]))
                if distance < closest_city[1]:
                    closest_city = (i, distance)
                if distance > furthest_city[1]:
                    furthest_city = (i, distance)
        except KeyError:
            pass
        except ValueError:
            pass
    
    return closest_city, furthest_city


    
def great_circle(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    return 6371 * (acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2)))


if __name__ == '__main__':
    closest_city, furthest_city = closest_furthest(214)
    print("Source city ID: {}".format(214))
    print("Closest city ID: {}, distance {} km".format(closest_city[0], closest_city[1]))
    print("Furthest city ID: {}, distance {} km".format(furthest_city[0], furthest_city[1]))




    
