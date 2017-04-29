# Retrieve correctly scaled data
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

# Print description of data if it exists
def print_description(sds_obj):
    if 'description' in sds_obj.attributes():
        string = sds_obj.attributes()['description']
        print(string)

