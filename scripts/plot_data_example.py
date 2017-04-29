#!/usr/bin/env python
# This is an example of how the pyhdf package can be used to plot MODIS data
# Based on code found in http://hdfeos.org/examples/code/pyhdf/AIRS.py

import os
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
from pyhdf.SD import SD, SDC


file_name = '../assets/example_data/MYD05_L2.A2017109.0000.006.NRT.hdf'
file = SD(file_name, SDC.READ)
print(file.datasets().keys())

def scaled_data(sds_obj):
    data = sds_obj.get()
    if 'add_offset' in sds_obj.attributes():
        offset = sds_obj.attributes()['add_offset']
    else:
        offset = 0.0
    if 'scale_factor' in sds_obj.attributes():        
        factor = sds_obj.attributes()['scale_factor']
    else:
        factor = 1.0
    scaled_data = (data - offset)*factor
    return scaled_data

# Read dataset.
DATAFIELD_NAME='Water_Vapor_Infrared'
#DATAFIELD_NAME = 'Cloud_Mask_QA'
#DATAFIELD_NAME = 'Quality_Assurance_Near_Infrared'

data = scaled_data(file.select(DATAFIELD_NAME))[:,:]
lat = file.select('Latitude')[:,:]
lon = file.select('Longitude')[:,:]


m = Basemap(projection='cyl', resolution='l', llcrnrlat=-90, urcrnrlat = 90, llcrnrlon=-180, urcrnrlon=180)
m.drawcoastlines(linewidth=0.5)
m.drawparallels(np.arange(-90., 120., 30.), labels=[1, 0, 0, 0])
m.drawmeridians(np.arange(-180., 181., 45.), labels=[0, 0, 0, 1])
x, y = m(lon, lat)
m.pcolormesh(x, y, data)
cb = m.colorbar()
cb.set_label('Unit:%')
plt.title('Test data')
fig = plt.gcf()
plt.show()
