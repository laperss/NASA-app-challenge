import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as sm
import scipy.stats  as stats
import xgboost as xgb


datapath_aod = "../data_local/MOD08_E3.A2017105.006.2017118135856_AoD.npy"
datapath_vap = "../data_local/MOD08_E3.A2017105.006.2017118135856_Vapor.npy"

print("Loading data from: " + datapath_aod)
aod =  np.load(datapath_aod)
vap =  np.load(datapath_vap)
#plt.figure(1)
#plt.imshow(vap, cmap='afmhot', interpolation='nearest')
#plt.draw()

print(aod.shape)

ols_df  = pd.DataFrame({"vap" : vap.ravel(), "A" : aod[0,:,:].ravel()
                        , "B" : aod[1,:,:].ravel(),"C" : aod[2,:,:].ravel() })

dtrain = xgb.DMatrix(ols_df["A","B","C"])


result = sm.ols(formula="vap  ~ A +1 ", data=ols_df).fit()
vap = 1
print(result.params)
print(ols_df.describe())
#print(dir(ols_df))
#print(dir(result))

pred_datapath_aod =  "../data_local/MYD08_E3.A2017105.006.2017118135357_AoD.npy"
pred_datapath_vap = "../data_local/MYD08_E3.A2017105.006.2017118135357_Vapor.npy"

print("Loading data from: " + pred_datapath_aod)
pred_aod =  np.load(pred_datapath_aod)
pred_vap =  np.load(pred_datapath_vap)


print(pred_vap.shape)
print(pred_vap.size)
pred_df = pd.DataFrame({"vap" : pred_vap.ravel(),"A" : pred_aod[0,:,:].ravel()})

predictions = result.predict(pred_df)

pred_im = predictions.reshape(pred_vap.shape)

plt.figure(1)
plt.imshow(pred_vap, cmap='afmhot', interpolation='nearest')
plt.draw()

plt.figure(2)
plt.imshow(pred_im, cmap='afmhot', interpolation='nearest')
plt.draw()


pred_df = pred_df[ np.logical_and( pred_df.A < 2, np.logical_and( pred_df.A > -1,pred_df.vap > -1)) ]
#pred_df = pred_df.sample(frac=0.05)
print(stats.pearsonr(pred_df['vap'], pred_df['A']))
print(pred_df.corr())
plt.figure(3)
plt.scatter(pred_df["A"],pred_df["vap"],s=0.5)
plt.xlabel("AoD")
plt.ylabel("Vapor")
plt.draw()
plt.show()