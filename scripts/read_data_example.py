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

# Print data contents
print('\nData content:')
for idx,sds in enumerate(datasets.keys()):
    print( idx,sds )


sds_obj = file.select('Solar_Azimuth') # select sds

data = sds_obj.get() # get sds data

#----------------------------------------------------------------------------------------#
# get attributes

print('\nData attributes:')
pprint.pprint( sds_obj.attributes() )

for key, value in sds_obj.attributes().items():
    print( key, value )
    if key == 'add_offset':
        add_offset = value  
    if key == 'scale_factor':
        scale_factor = value

print('\nScale factors:')        
print( 'add_offset', add_offset, type(add_offset) )
print( 'scale_factor', scale_factor, type(scale_factor) )

data = (data - add_offset) * scale_factor


print('\nScaled data: :')
print( data )
