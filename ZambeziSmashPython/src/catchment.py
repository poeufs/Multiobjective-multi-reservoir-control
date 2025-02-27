# Catchment class

import numpy as np
import sys,os
sys.path.append(os.path.realpath('..'))



class Catchment:
    """Catchments have a name and inflow (from data file)"""
    def __init__(self, name, model):
        # Explanation placeholder
        self.name = name
        self.model = model

        data_directory = "../data/"
        self.inflow = np.loadtxt(f"{data_directory}Inflow{name}.txt")
    def printing(self):
       print(f'Name is {self.name} and inflow is {self.inflow}')

#TEST
# ITT = Catchment('ITT','model')
# ITT.printing()