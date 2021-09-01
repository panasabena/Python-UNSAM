# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 15:00:11 2021

@author: Alfredo
"""

import csv
#%%
ruta_del_archivo=(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\missing.csv')

def costo_camion(ruta_del_archivo):
        
    f = open(ruta_del_archivo,'rt')
    filas = csv.reader(f)
    encabezados = next(filas)
    for n_fila, fila in enumerate(filas,start = 1):
        record = dict(zip(encabezados, fila))
        costo_total=0
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
           