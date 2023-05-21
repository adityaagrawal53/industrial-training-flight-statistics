import csv
import geopandas as gpd
import pandas as pd
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

#Credits: https://scitools.org.uk/cartopy/docs/v0.15/matplotlib/intro.html

ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()                                          #Add the map

ny_lon, ny_lat = -75, 43                                #Longitude and latitude of 2 cities
delhi_lon, delhi_lat = 77.23, 28.61                     #TODO: Get coordinates of airports to plot

plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],      #Plot coordinates of airports
         color='blue', linewidth=2, marker='o',
         transform=ccrs.Geodetic(),
         )

plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
         color='gray', linestyle='--',
         transform=ccrs.PlateCarree(),
         )

plt.text(ny_lon, ny_lat, 'New York',                    #Plot route
         horizontalalignment='center',
         transform=ccrs.Geodetic())

plt.text(delhi_lon + 3, delhi_lat - 12, 'Delhi',        #Name of airport
         horizontalalignment='left',
         transform=ccrs.Geodetic())

plt.show()                                              #Display plot