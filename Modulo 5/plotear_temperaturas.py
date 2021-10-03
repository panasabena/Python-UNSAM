# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 13:36:11 2021

@author: Alfredo
"""

import random
import matplotlib.pyplot as plt
import numpy as np
def medir_temp(n):
    mediciones=[]
    for i in range(n):
        mediciones.append(random.normalvariate(37.5,0.2))
    plt.hist(mediciones, bins=10, alpha=0.5)
    np.savetxt(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\temperaturas.npy', mediciones)
    return mediciones
# np.loadtxt('new_file.csv')