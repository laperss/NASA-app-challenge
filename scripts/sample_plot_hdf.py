
from pyhdf.SD import SD, SDC
import numpy as np
import pprint
import os
import matplotlib.pyplot as plt

from mpl_toolkits.basemap import Basemap

file_name = '../assets/example_data/MYD05_L2.A2017109.0000.006.NRT.hdf'
file = SD(file_name, SDC.READ)

print ('Available data')
print (file.datasets().keys())

sds_latitude_data = file.select('Latitude')
latitude = sds_latitude_data[:,:]
sds_longitude_data = file.select('Longitude')
longitude = sds_longitude_data[:,:]

water_vapor_infrared_data = file.select('Water_Vapor_Infrared')
raw_data = water_vapor_infrared_data[:,:]

m = Basemap(projection='cyl', resolution='l', llcrnrlat=-90, urcrnrlat = 90, llcrnrlon=-180, urcrnrlon = 180)
m.drawcoastlines(linewidth=0.5)
m.drawparallels(np.arange(-90., 120., 30.), labels=[1, 0, 0, 0])
m.drawmeridians(np.arange(-180., 181., 45.), labels=[0, 0, 0, 1])
x, y = m(longitude, latitude)
m.pcolormesh(x, y, raw_data)
print ('123')
plt.show()