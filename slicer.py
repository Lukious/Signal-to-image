"""
Created on Thu Jul 18 17:16:43 2019

@author: lukious
"""

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

filename = input("Input file name:")
raw_data = pd.read_csv("./"+filename+".csv")
data = pd.DataFrame(raw_data,columns=["f_ml","f_v1","ml","v1"])


data.plot()