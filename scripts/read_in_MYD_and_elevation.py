import numpy as np
import pandas as pd

AoD1 = np.load('../data_local/numpy/MYD08_E3.A2017073.006.2017086201041_AoD.npy')
vap1 = np.load('../data_local/numpy/MYD08_E3.A2017073.006.2017086201041_Vapor.npy')
elevation_data = np.loadtxt('../assets/elevation.txt')


ols_df = pd.DataFrame({"vap" : vap1.ravel(), "blue" : AoD1[0,:,:].ravel()
                        , "green" : AoD1[1,:,:].ravel(),"red" : AoD1[2,:,:].ravel() })
ols_df['elevation']  = elevation_data.ravel()
ols_df['long'], ols_df['lat'] = np.dstack(np.meshgrid(np.arange(-180,180), np.arange(89,-91,-1))).reshape(-1,2).T

ols_df = ols_df[ols_df['blue']>-5]
ols_df = ols_df[ols_df['green']>-5]
ols_df = ols_df[ols_df['red']>-5]
ols_df = ols_df[ols_df['vap']>-5]
ols_df = ols_df[['long','lat','blue','green','red','elevation','vap']]


print ols_df.sample(40)
