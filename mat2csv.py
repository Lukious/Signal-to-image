import scipy.io
import numpy as np
import pandas as pd

filename = input("Input .mat file name (only file name no '.mat'):")
data = scipy.io.loadmat(filename+".mat")

f_ml =  data.get("f_ml")
f_v1 =  data.get("f_v1")
ml =  data.get("ml")
v1 =  data.get("v1")



pan_f_ml = pd.DataFrame(f_ml)
pan_f_v1 = pd.DataFrame(f_v1)
pan_ml = pd.DataFrame(ml)
pan_v1 = pd.DataFrame(v1)

pan_needs = pd.DataFrame()

pan_needs = pd.concat([pan_f_ml, pan_f_v1,pan_ml,pan_v1], axis=1)
pan_needs.columns = ['f_ml','f_v1','ml','v1']

pan_needs.to_csv(filename+"_data.csv",mode = 'w')