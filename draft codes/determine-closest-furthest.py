
from math import radians, degrees, sin, cos, asin, acos, sqrt

# example data, random data from airports.dat file

# sample_data:
# 1,"Goroka Airport","Goroka","Papua New Guinea","GKA","AYGA",-6.081689834590001,145.391998291,5282,10,"U","Pacific/Port_Moresby","airport","OurAirports"
# 702,"Feringe Airport","Ljungby","Sweden",\N,"ESMG",56.9502983093,13.921699523900001,538,1,"E","Europe/Stockholm","airport","OurAirports"
# 1906,"Florida Airport","Florida","Cuba",\N,"MUFL",21.49970054626465,-78.20279693603516,197,-5,"U","America/Havana","airport","OurAirports"

# input: dictionary, where the key is the airport ID and the value is a list where first index is the latitude and second is the longitude
# 212,"Boufarik Airport","Boufarik","Algeria",\N,"DAAK",36.545799,2.87611,335,1,"N","Africa/Algiers","airport","OurAirports"


city = [212, [36.545799, 2.87611]]
sample_data = {1: [-6.081689834590001, 145.391998291], 702: [56.9502983093, 13.921699523900001], 1906: [21.49970054626465, -78.20279693603516]}

def closest_furthest(source, data):
    # source city coordinates
    source_ID = city[0]
    source_coordinates = city[1]
    source_latitude = source_coordinates[0]
    source_longitude = source_coordinates[1]
    #geopy_obj_source = (source_latitude, source_longitude)

    closest_city = (1, great_circle(source_longitude, source_latitude, sample_data[1][1], sample_data[1][0]))
    furthest_city = (1, great_circle(source_longitude, source_latitude, sample_data[1][1], sample_data[1][0]))

    i = 2

    for i in sample_data:
        dest_ID = i
        dest_coordinates = sample_data[i]
        dest_latitude = dest_coordinates[0]
        dest_longitude = dest_coordinates[1]
        #geopy_obj_dest = (dest_latitude, dest_longitude)

        # distance between two points
        distance = great_circle(source_longitude, source_latitude, dest_longitude, dest_latitude)

        if distance < closest_city[1]:
            closest_city = (dest_ID, distance)
        if distance > furthest_city[1]:
            furthest_city = (dest_ID, distance)
    
    return [closest_city, furthest_city]

    
def great_circle(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    return 6371 * (acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2)))


if __name__ == '__main__':
    closest_city, furthest_city = closest_furthest(city, sample_data)
    print("Source city ID: {}".format(city[0]))
    print("Closest city ID: {}, distance {} km".format(closest_city[0], closest_city[1]))
    print("Furthest city ID: {}, distance {} km".format(furthest_city[0], furthest_city[1]))




    
