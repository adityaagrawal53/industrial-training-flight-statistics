# Industrial Training Group 6

Link for the flight map GitHub repository: https://github.com/zhangwengame/Python-Flight-Map

Link for the OpenFlights website: https://openflights.org/data.html#airport

Link for the OpenFlights Github: https://github.com/jpatokal/openflights

Link for the OpenFlights Github (data): https://github.com/jpatokal/openflights/tree/master/data


# Determine-closest-furthest.py

The python code determines the closest and furthest airport to the given airport.

The input is the source airport's unique OpenFlights ID.

The output:


Source ID: (ID)
Closest city: (ID), distance (distance) kilometeres.
Furthest city: (ID), distance (distance) kilometeres.

The code determines the closest and furthest airport to the given source airport by first taking the first airport from the database, taking its longitude and latitude, calculating the distance between that and the source airport and making that distance as the base closest and furthest airport. After that the code goes line by line through the database (has about 6500 airports) and comparares each airport's distance to the base closest and furthest airport. The distance is calculated using great circle method that is precise enough for this application.

# Mapping.py
# Database-to-graph.py

# Counting.py

A python code that outputs all the airlines that depart from the given input source airport.

The input is the source airport's IATA code. 

The output is a bar graph that has all the airlines that depart from the source airport. The more departures a specific airline has, the higher the bar in the graph.


Pandas extension: helps to read databases in a convenient way.
MatPlotLib extension: used to plot the graph


# City-to-destination.py

A python code that outputs how many destinations a given source airport has to different continents.

The input is the source airport's IATA code.

The output:


Number of destination airports in each continent: 
North America: (int)
South America: (int)
Europe: (int)
Asia: (int)
Africa: (int)
Oceania: (int)

The code read data from airport.dat, routes.dat and Countries-Continents.csv.
It determines all the destinations from the source code, determies all the continents for each of those destinations (by determining the country from the airport.dat and finding the continent pair from Countries-Continents.csv) and sums up all the occurances of each continent into a designated variable.

Pandas extension: helps to read databases in a convenient way.


# The syntax
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









***

