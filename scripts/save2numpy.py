#!/usr/bin/env python
# This is an example of how the pyhdf package can be used to access MODIS data

from pyhdf.SD import SD, SDC
import matplotlib.pyplot as plt
import numpy as np
import pdb
from glob import glob

DAT_DIR = '../assets/example_data'
files = sorted(glob(DAT_DIR+'/*E3*'))
keys = ['Atmospheric_Water_Vapor_QA_Mean_Mean', 'Aerosol_Optical_Depth_Average_Ocean_QA_Mean_Mean', 'Aerosol_Optical_Depth_Land_QA_Mean_Mean']

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

def print_description(sds_obj):
    if 'description' in sds_obj.attributes():
        string = sds_obj.attributes()['description']
        print(string)

for path in files:
    file = SD(path, SDC.READ)
    print('\n* ' + path)

    # Water vapor
    sds_obj = file.select(keys[0])
    print(sds_obj.attributes())
    print_description(sds_obj)
    data = scaled_data(sds_obj)
    np.save(path[:-4] + '_Vapor.npy', data)
#    plt.imshow(np. where(data < -2, -2, data), cmap='afmhot', interpolation='nearest')
#    plt.show()

    # Ocean AoD
    sds_obj = file.select(keys[1])
    print_description(sds_obj)
    data = scaled_data(sds_obj)[0:3,:,:]

    # Land AoD
    sds_obj = file.select(keys[2])
    print_description(sds_obj)
    land = scaled_data(sds_obj)

    data = np.where(data < 0, land, data)
    np.save(path[:-4] + '_AoD.npy', data)
#    plt.imshow(np.where(np.sum(data, axis=0) < -2, -2, np.sum(data, axis=0)), cmap='afmhot', interpolation='nearest')
#    plt.show()
