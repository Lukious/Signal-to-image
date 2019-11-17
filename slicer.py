"""
Created on Thu Jul 18 17:16:43 2019

@author: lukious
"""

import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
from scipy import signal
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sb

save_number = 0

filename = input("Input ecg file name:")
ecg_filename = filename
filename = input("Input peak file name:")
peak_filename = filename
#ecg_filename = "208_data"
#peak_filename = "208_peak"
ecg_raw_data = pd.read_csv("./"+ecg_filename+".csv")
ecg_peak_data = pd.read_csv("./"+peak_filename+".csv")
data = pd.DataFrame(ecg_raw_data,columns=["f_ml","f_v1","ml","v1"])
ecg_use_data = pd.DataFrame(data,columns=["f_ml"])
peak_use_data = pd.DataFrame(ecg_peak_data,columns=["Sample"])
peak_type_data = pd.DataFrame(ecg_peak_data,columns=["Type"])


#test_for_save = ecg_use_data.ix[peak_use_data.iloc[0][0]:peak_use_data.iloc[1][0]]

#cut by peak and interpolation to 784 (for 28*28 img)
for i in range(peak_use_data.shape[0]-1):
    #print(peak_use_data.iloc[i][0])
    for_save = ecg_use_data.ix[peak_use_data.iloc[i][0]:peak_use_data.iloc[i+1][0]]
    for_save = signal.resample(for_save, 784)
    for_save=pd.DataFrame(for_save)
    if peak_type_data.iloc[i][0] == "+":
        for_save.to_csv("./+/_"+str(save_number)+"'s data.csv",mode = 'w', header=False, index=False)
        save_number = save_number + 1
    elif peak_type_data.iloc[i][0] == "F":
        for_save.to_csv("./F/_"+str(save_number)+"'s data.csv",mode = 'w', header=False, index=False)
        save_number = save_number + 1
    elif peak_type_data.iloc[i][0] == "N":
        for_save.to_csv("./N/_"+str(save_number)+"'s data.csv",mode = 'w', header=False, index=False)
        save_number = save_number + 1
    elif peak_type_data.iloc[i][0] == "S":
        for_save.to_csv("./S/_"+str(save_number)+"'s data.csv",mode = 'w', header=False, index=False)
        save_number = save_number + 1
    elif peak_type_data.iloc[i][0] == "V":
        for_save.to_csv("./V/_"+str(save_number)+"'s data.csv",mode = 'w', header=False, index=False)
        save_number = save_number + 1
    elif peak_type_data.iloc[i][0] == "Q":
        for_save.to_csv("./Q/_"+str(save_number)+"'s data.csv",mode = 'w', header=False, index=False)
        save_number = save_number + 1
    elif peak_type_data.iloc[i][0] == "~":
        for_save.to_csv("./~/_"+str(save_number)+"'s data.csv",mode = 'w', header=False, index=False)
        save_number = save_number + 1
    else :
        print("Undecided : "+ str(i))
        save_number = save_number + 1



#From here is normalizatino to 0-255
save_number = 0

for i in range(peak_use_data.shape[0]-1):
    #print(peak_use_data.iloc[i][0])
    for_save = ecg_use_data.ix[peak_use_data.iloc[i][0]:peak_use_data.iloc[i+1][0]]
    for_save = signal.resample(for_save, 784)
    scaler = MinMaxScaler(feature_range=(0, 255))
    scaler.fit(for_save)
    for_save = scaler.transform(for_save)
    for_save=pd.DataFrame(for_save)
    if peak_type_data.iloc[i][0] == "+":
        for_save.to_csv("./n+/_"+str(save_number)+"'s data.csv",mode = 'w', header=False, index=False)
        save_number = save_number + 1
    elif peak_type_data.iloc[i][0] == "F":
        for_save.to_csv("./nF/_"+str(save_number)+"'s data.csv",mode = 'w', header=False, index=False)
        save_number = save_number + 1
    elif peak_type_data.iloc[i][0] == "N":
        for_save.to_csv("./nN/_"+str(save_number)+"'s data.csv",mode = 'w', header=False, index=False)
        save_number = save_number + 1
    elif peak_type_data.iloc[i][0] == "S":
        for_save.to_csv("./nS/_"+str(save_number)+"'s data.csv",mode = 'w', header=False, index=False)
        save_number = save_number + 1
    elif peak_type_data.iloc[i][0] == "V":
        for_save.to_csv("./nV/_"+str(save_number)+"'s data.csv",mode = 'w', header=False, index=False)
        save_number = save_number + 1
    elif peak_type_data.iloc[i][0] == "Q":
        for_save.to_csv("./nQ/_"+str(save_number)+"'s data.csv",mode = 'w', header=False, index=False)
        save_number = save_number + 1
    elif peak_type_data.iloc[i][0] == "~":
        for_save.to_csv("./n~/_"+str(save_number)+"'s data.csv",mode = 'w', header=False, index=False)
        save_number = save_number + 1
    else :
        print("Undecided : "+ str(i))
        save_number = save_number + 1



#From here is normalizatino to 0-255
save_number = 0

for i in range(peak_use_data.shape[0]-1):
    #print(peak_use_data.iloc[i][0])
    for_save = ecg_use_data.ix[peak_use_data.iloc[i][0]:peak_use_data.iloc[i+1][0]]
    for_save = signal.resample(for_save, 784)
    scaler = MinMaxScaler(feature_range=(0, 255))
    scaler.fit(for_save)
    for_save = scaler.transform(for_save)
    for_save = np.reshape(for_save, (28, 28))
    dmap = sb.heatmap(for_save)
    for_save=pd.DataFrame(for_save)
    if peak_type_data.iloc[i][0] == "+":
        for_save.to_csv("./n+/_"+str(save_number)+"'s data.csv",mode = 'w', header=False, index=False)
        plt.savefig("./img+/_"+str(save_number)+"'s data.png")
        save_number = save_number + 1
    elif peak_type_data.iloc[i][0] == "F":
        for_save.to_csv("./nF/_"+str(save_number)+"'s data.csv",mode = 'w', header=False, index=False)
        plt.savefig("./imgF/_"+str(save_number)+"'s data.png")
        save_number = save_number + 1
    elif peak_type_data.iloc[i][0] == "N":
        for_save.to_csv("./nN/_"+str(save_number)+"'s data.csv",mode = 'w', header=False, index=False)
        plt.savefig("./imgN/_"+str(save_number)+"'s data.png")
        save_number = save_number + 1
    elif peak_type_data.iloc[i][0] == "S":
        for_save.to_csv("./nS/_"+str(save_number)+"'s data.csv",mode = 'w', header=False, index=False)
        plt.savefig("./imgS/_"+str(save_number)+"'s data.png")
        save_number = save_number + 1
    elif peak_type_data.iloc[i][0] == "V":
        for_save.to_csv("./nV/_"+str(save_number)+"'s data.csv",mode = 'w', header=False, index=False)
        plt.savefig("./imgV/_"+str(save_number)+"'s data.png")
        save_number = save_number + 1
    elif peak_type_data.iloc[i][0] == "Q":
        for_save.to_csv("./nQ/_"+str(save_number)+"'s data.csv",mode = 'w', header=False, index=False)
        plt.savefig("./imgQ/_"+str(save_number)+"'s data.png")
        save_number = save_number + 1
    elif peak_type_data.iloc[i][0] == "~":
        for_save.to_csv("./n~/_"+str(save_number)+"'s data.csv",mode = 'w', header=False, index=False)
        plt.savefig("./img~/_"+str(save_number)+"'s data.png")
        save_number = save_number + 1
    else :
        print("Undecided : "+ str(i))
        save_number = save_number + 1
        
    plt.show()
