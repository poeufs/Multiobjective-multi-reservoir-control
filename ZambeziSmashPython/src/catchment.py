# Catchement class

import numpy as np
import sys,os
sys.path.append(os.path.realpath('..'))



class Catchment:
   print("Catchment class")
   def __init__(self, name, model):
        # Explanation placeholder
        self.name = name
        self.model = model

        data_directory = "../data/"
        self.inflow = np.loadtxt('zambezi_inflows86_05.txt') #zambezi_inflows86_05 #self.inflow = np.loadtxt(f"{data_directory}Inflow{name}.txt")