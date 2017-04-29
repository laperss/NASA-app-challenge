#!/usr/bin/env python
# This is an example of how the pyhdf package can be used to access MODIS data
from pyhdf.SD import SD, SDC
import numpy as np
from hdf_functions import scaled_data, print_description

file_name = '../assets/example_data/MYD05_L2.A2017109.0000.006.NRT.hdf'

file = SD(file_name, SDC.READ)

print('Data size: ' + str(file.info()[0]) + ', ' + str(file.info()[1]))
datasets = file.datasets()

# Print data contents
print('\nData content:')
for key in datasets.keys():
    print('\n* ' + key)
    sds_obj = file.select(key)
    print_description(sds_obj)
    data = scaled_data(sds_obj)
    print(data)



