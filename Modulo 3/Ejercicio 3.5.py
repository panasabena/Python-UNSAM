# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 00:12:15 2021

@author: Alfredo
"""


import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    
    #registro={} cambio de lugar esta variable
    with open(nombre_archivo,"rt") as f:
        camion=[]
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            # pongo la variable registro dentro del for
            # y le doy formato de diccionario aca mismo con
            # sus respectivas columnas
            registro = {'Nombre':fila[0],
                        'Cajones': int(fila[1]),
                        'Precio': float(fila[2])
                        }
            #registro[encabezado[0]] = str(fila[0])
            #registro[encabezado[1]] = int(fila[1])
            #registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion
#%%
camion = leer_camion('../Data/camion.csv')
pprint(camion)
#%%
lista_de_tuplas = [(1,2),(3,4),(5,6),(7,8),(9,10)]
for x,y in lista_de_tuplas:
    print(x,y)
#%%
lista_1=[1,2,3,4,5,6,7,8,9]
lista_2=[8,5,2,3,4]
## Vemos que se detiene en el ultimo numero de la lista_2
## Que es la lista mas chica, 
for i in zip(lista_1,lista_2):
    print(i)
 #%%
for i in range(0,10,2):
    print(i)
    











