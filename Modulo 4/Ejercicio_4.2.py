# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 01:51:11 2021

@author: Alfredo
"""


import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion = []
    #registro = {} #Si queda el registro acá arriba, por cada 
    # iteración de la lista, el registro se sobre escribe y la
    # lista vuelve a guardar el registro con la nueva iteración
    # Entonces lo que hay que hacer es meter el registro dentro 
    # del bucle for para que se limpie el registro con cada 
    # iteración y guarde un elemento nuevo en el objeto camion.
    with open(nombre_archivo,"rt") as f:
        
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            # Al poner el diccionario registro acá adentro, se
            # limpia con cada iteración de las filas.
            registro = {}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\Modulo 4\camion.csv')
pprint(camion)
