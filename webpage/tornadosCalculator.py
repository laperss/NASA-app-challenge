import numpy as np
def getTornadoCoords(lon, lat):
    '''Given a latitude and longitude, return a list of where tornados appear'''
    numTornados = 5
    sigma = 7
    longs = np.random.normal(lon, sigma, numTornados)
    lats = np.random.normal(lat, sigma, numTornados)
    return list(zip(longs, lats))

