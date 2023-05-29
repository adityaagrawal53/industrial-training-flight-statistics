# Industrial Training Group 2


# Instruction on how to start the server:
1. Clone the repository
2. Open command line (terminal).
Using command line:
3. type "python --version" to check if you have python yet
4. install flask by typing "pip install flask" (python server package)
4. cd to the directory you cloned the repository
5. type "python -m app" to start the localhost server. You can access the web app on http://127.0.0.1:5000
To use Ngrok:
6. start ngrok.exe
7. type "ngrok http 5000"
You will be able to reach your localhost on internet using the link Ngrok gives you

# introduction

The goal of this project was to make a website that takes a user input and outputs graphs and data about flight route data, airlines, destination continents, closest and furthest airport. Mainly Python and HTML was used in this project. Python was used to handle the data and backend, and HTML to outline the website appearance and frontend.


**In an nutshell the repository does the following:**

1. ngrok.exe starts a local host server that can be accessed with an IPv4 adddress
2. html files in the templates folder handle the visual appearance of the URL website
3. static folder stores all the databases and png files made by the python files
4. pycache folder has all the cache information
3. each python file gets a source airport as an input and outputs a desired string, picture or a graph.
4. app.py combines the listing and routing of different files and html domain names by using flask app routing.

The airports.dat and routes.dat databases are from an open source database, OpenFlights that is linked in the beginning of the README file.

# links

Link for the flight map GitHub repository: https://github.com/zhangwengame/Python-Flight-Map

Link for the OpenFlights website: https://openflights.org/data.html#airport

Link for the OpenFlights Github: https://github.com/jpatokal/openflights

Link for the OpenFlights Github (data): https://github.com/jpatokal/openflights/tree/master/data

# app.py
The file combines the listing and routing of different files and html domain names.
It imports the following files to output the desired pictures / strings made by those files to the website.

- aps_listing_and_routing.py
    - to output images of all the **routes** from a source city
- closest_furthest_cities.py
    - to print out the **closest and furthest** city from a source airport
- aps_per_continent_by_src.py
    - to output a graph of how many **destinations** a given source airport has to different continents
- counting.py
    - to output all the **airlines** that depart from the given input source airport.


It also uses flask to make a micronetwork.


# aps_listing_and_routing

This file defines a function that reads in two databases (airports.dat and routes.dat) as pandas dataframes, and then filters their contents based on user input. The user inputs the name of a city, and the function then filters the airports database to only contain airports in the given city, and the routes database to only contain routes in which the source airports are located in the given city.

The function then outputs two images: one contains a map of all the airports in the database in blue with the airports in the given city appearing in red, and the other image contains a world map with route lines from the source city in red.  The files are named airports_map.png and routes_map.png, and are sent to the website via an HTML POST request from app.py.


# closest_furthest_cities.py

The python file determines the closest and furthest airport to the given airport.

The input is the source airport's unique OpenFlights ID.

The output:


Source ID: (ID)
Closest city: (ID), distance (distance) kilometeres.
Furthest city: (ID), distance (distance) kilometeres.


The code determines the closest and furthest airport to the given source airport by first taking the first airport from the database, taking its longitude and latitude, calculating the distance between that and the source airport and making that distance as the base closest and furthest airport. After that the code goes line by line through the database (has about 6500 airports) and comparares each airport's distance to the base closest and furthest airport. The distance is calculated using great circle method that is precise enough for this application.


# aps_per_continent_by_src.py

A python file that outputs how many destinations a given source airport has to different continents.

The input is the source airport's city.

The output is a png picture that has a bar graph of all the continents and the number of occurances of each continent. 

The code reads data from airport.dat, routes.dat and Countries-Continents.csv.
It determines all the destinations from the source code, determies all the continents for each of those destinations (by determining the country from the airport.dat and finding the continent pair from Countries-Continents.csv) and sums up all the occurances of each continent into a designated variable.

Pandas extension: helps to read databases in a convenient way.
MatPlotLib extension: used to plot the graph


# counting.py

A python file that outputs all the airlines that depart from the given input source airport.

The input is the source airport's IATA code. 

The output is a bar graph that has all the airlines that depart from the source airport. The more departures a specific airline has, the higher the bar in the graph.


Pandas extension: helps to read databases in a convenient way.
MatPlotLib extension: used to plot the graph



# mapping.py
This file outputs all the destination airports for an input source city using CartoPy Python package.




# the syntax of the databases
**Use the airport database for the longitude, altitude and continent information!
Example:**



**507**,"London Heathrow Airport","London","United Kingdom","LHR","EGLL",**51.4706**,**-0.461941**,83,0,"E",**"Europe/London"**,"airport","OurAirports"

Use the following:

Index 0: Airport ID

Index 6: Latitude

Index 7: Longitude

Index 11: Timezone. Can be used to determine the continent 





**Use the route data database for the route information, aircraft type and stop over number! Example:**

BA,1355,SIN,**3316**,LHR,**507**,,**0**,**744**
Use the following:

Index 3: departure airport ID

Index 5: arrival airport ID

Index 7: number of stopovers

Index 8: aircraft type











***

