# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 23:56:09 2021

@author: Alfredo
"""

import random
import matplotlib.pyplot as plt
for i in range(6):
    print(f'{random.normalvariate(37.5,0.2):.2f}', end= ', ')
    
## La funcion normal tiene muchos usos, uno de ellos es
## modelar errores experimentales, es decir la diferencia
## entre el valor medido de una magnitud física y el valor
## real de dicha magnitud.
#%%
def medir_temp(n):
    mediciones=[]
    for i in range(n):
        mediciones.append(random.normalvariate(37.5,0.2))
    plt.hist(mediciones, bins=10, alpha=0.5)
    return mediciones
#%%
def resumen_temp(mediciones):
    n=len(mediciones)
    ## esta parte de como calcular la mediana,
    ## la saqué de geeks for geeks
    if n % 2 == 0:
        median1 = mediciones[n//2]
        median2 = mediciones[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = mediciones[n//2]
    promedio=sum(mediciones)/len(mediciones)
    resumen=(max(mediciones),min(mediciones), promedio, median)
    return resumen

