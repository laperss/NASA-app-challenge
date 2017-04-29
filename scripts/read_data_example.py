#!/usr/bin/env python
# This is an example of how the pyhdf package can be used to access MODIS data

from pyhdf.SD import SD, SDC
import numpy as np
import pprint

file_name = '../assets/example_data/MYD05_L2.A2017109.0000.006.NRT.hdf'

file = SD(file_name, SDC.READ)

print('Data size: ')
print( file.info() )


datasets = file.datasets()


def scaled_data(sds_obj):
    data = sds_obj.get()
    offset = sds_obj.attributes()['add_offset']
    factor = sds_obj.attributes()['scale_factor']
    scaled_data = (data - offset)*factor
    return scaled_data


# Print data contents
print('\nData content:')
for key in datasets.keys():
    print('\n' + key)
    sds_obj = file.select(key)
    data = scaled_data(sds_obj)
    print(data)


