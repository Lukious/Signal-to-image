# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:36:45 2019

@author: lukious
"""

from PIL import Image, ImageDraw
from numpy import genfromtxt
import os 

path = "./nF/"
settedname = "pngF"
file_list = os.listdir(path)
file_list_csv = [file for file in file_list if file.endswith(".csv")]
save_number = 0

for i in range(len(file_list_csv)):
    _filename = file_list_csv[i]
    g = open(path+_filename,'r')
    temp = genfromtxt(g, delimiter = ',')
    im = Image.fromarray(temp).convert('RGB')
    pix = im.load()
    rows, cols = im.size
    for x in range(cols):
        for y in range(rows):
            pix[x,y] = (int(temp[y,x] // 256 // 256 % 256),int(temp[y,x] // 256  % 256),int(temp[y,x] % 256))
    im.save("./"+str(settedname)+"/"+str(settedname) +str(save_number)+ '.png')
    save_number = save_number + 1
    del im