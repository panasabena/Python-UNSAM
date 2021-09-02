# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 15:00:11 2021

@author: Alfredo
"""

nombre_archivo=('../Data/camion.csv')
nombre_archivo=(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\missing.csv')

#%%
import csv

def costo_camion(nombre_archivo):
    camion=[]
    f = open(nombre_archivo,'rt')
    filas = csv.reader(f)
    encabezados = next(filas)
    costo_total=0
    for n_fila, fila in enumerate(filas,start = 1):
        record = dict(zip(encabezados, fila))
        camion.append(record)
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            costo_total += ncajones * precio
            
            if fila != '':
                #print(zip(fila,encabezado))
                #print (fila)
                print(record) # imprime el código en forma de diccionario
                # o probar tambien con:
                ## imprime el codigo en forma de lista
                #print(fila)
                    
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar {fila}')
    return costo_total
    
#costo_camion(nombre_archivo)
