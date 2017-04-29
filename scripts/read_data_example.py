#!/usr/bin/env python
# This is an example of how the pyhdf package can be used to access MODIS data

from pyhdf.SD import SD, SDC
import numpy as np

file_name = '../assets/example_data/MYD05_L2.A2017109.0000.006.NRT.hdf'

file = SD(file_name, SDC.READ)

print('Data size: ')
print( file.info() )


datasets = file.datasets()


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


# Print data contents
print('\nData content:')
for key in datasets.keys():
    print('\n* ' + key)
    sds_obj = file.select(key)
    print_description(sds_obj)
    data = scaled_data(sds_obj)
    print(data)



