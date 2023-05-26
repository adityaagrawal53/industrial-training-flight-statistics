# Industrial Training Group 6

Link for the flight map GitHub repository: https://github.com/zhangwengame/Python-Flight-Map

Link for the OpenFlights website: https://openflights.org/data.html#airport

Link for the OpenFlights Github: https://github.com/jpatokal/openflights

Link for the OpenFlights Github (data): https://github.com/jpatokal/openflights/tree/master/data


# Determine-closest-furthest

The python code determines the closest and furthest airport to the given airport.
The input is the source airport's unique OpenFlights ID.
The output is the following string:

Source ID: (ID)
Closest city: (ID), distance (distance) kilometeres.
Furthest city: (ID), distance (distance) kilometeres.

The code determines the closest and furthest airport to the given source airport by first taking the first airport from the database, taking its longitude and latitude, calculating the distance between that and the source airport and making that distance as the base closest and furthest airport. After that the code goes line by line through the database (has about 6500 airports) and comparares each airport's distance to the base closest and furthest airport. The distance is calculated using great circle method that is precise enough for this application.



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

