# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 15:29:22 2021

@author: Alfredo
"""


## fileparse ejercicio 6.6
import csv

def parse_csv(nombre_archivo):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open (nombre_archivo) as f:
        rows = csv.reader(f)
        # Headers lee los encabezados
        headers = next(rows)
        registros = []
        
        for row in rows:
            if not row: # saltea las filas sin datos
                continue
            registro = dict(zip(headers,row))
            registros.append(registro)
    return registros
camion=parse_csv(r'C:\Users\Alfredo\Bitácoras\Python UNSAM\ejercicios_python\Data\camion.csv')
print(camion)
#%%
