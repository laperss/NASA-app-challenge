#!/usr/bin/env python
# This is an example of how the pyhdf package can be used to access MODIS data

from pyhdf.SD import SD, SDC
import matplotlib.pyplot as plt
import numpy as np
import pdb
from glob import glob
import os.path

#DAT_DIR = '../assets/example_data'
DAT_DIR = '/mnt/stockholm'
files = sorted(glob(DAT_DIR+'/*.A2017*'))
keys = ['Atmospheric_Water_Vapor_QA_Mean_Mean', 'Aerosol_Optical_Depth_Average_Ocean_QA_Mean_Mean', 'Aerosol_Optical_Depth_Land_QA_Mean_Mean','Cloud_Optical_Thickness_Combined_Log_Mean_Mean', 'Pressure_Level']

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

def list_datasets(fileobj):
    for key in fileobj.datasets().keys():
        if "Aerosol" in key:
            print(key)


if __name__ == "__main__":
    # Create output folder
    infolder = os.path.split(files[0])[0]
    outfolder = os.path.join(infolder,"numpy")
    for path in files:

        #pdb.set_trace()
        fileobj = SD(path, SDC.READ)
        print('\n* ' + path)

        filename = os.path.split(path)[1]
        basefile_out = os.path.join(outfolder, filename)

        list_datasets(fileobj)


        # Water vapor
        sds_obj = fileobj.select(keys[0])
        print(sds_obj.attributes())
        print_description(sds_obj)
        data = scaled_data(sds_obj)
        np.save(basefile_out[:-4] + '_Vapor.npy', data)
    #    plt.imshow(np. where(data < -2, -2, data), cmap='afmhot', interpolation='nearest')
    #    plt.show()

        # Ocean AoD
        sds_obj = fileobj.select(keys[1])
        print_description(sds_obj)
        data = scaled_data(sds_obj)[0:3,:,:]

        # Land AoD
        sds_obj = fileobj.select(keys[2])
        print_description(sds_obj)
        land = scaled_data(sds_obj)

        data = np.where(data < 0, land, data)
        np.save(basefile_out[:-4] + '_AoD.npy', data)
    #    plt.imshow(np.where(np.sum(data, axis=0) < -2, -2, np.sum(data, axis=0)), cmap='afmhot', interpolation='nearest')
    #    plt.show()

    # Cloud 
        sds_obj = fileobj.select(keys[3])
        print_description(sds_obj)
        data = scaled_data(sds_obj)
        np.save(basefile_out[:-4] + '_Cloud.npy', data)

    # Pressure
        sds_obj = fileobj.select(keys[4])
        print_description(sds_obj)
        data = scaled_data(sds_obj)
        np.save(basefile_out[:-4] + '_Pressure.npy', data)
